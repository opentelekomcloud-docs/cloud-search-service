:original_name: en-us_topic_0000001477419788.html

.. _en-us_topic_0000001477419788:

Sample Code for Two-Way Authentication During the Access to a Cluster
=====================================================================

This section provides the sample code for two-way authentication during the access to a cluster from a Java client.

ESSecuredClientWithCerDemo Code
-------------------------------

::

   import org.apache.commons.io.IOUtils;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.HttpHost;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.elasticsearch.action.search.SearchRequest;
   import org.elasticsearch.action.search.SearchResponse;
   import org.elasticsearch.client.RequestOptions;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
   import org.elasticsearch.index.query.QueryBuilders;
   import org.elasticsearch.search.SearchHit;
   import org.elasticsearch.search.SearchHits;
   import org.elasticsearch.search.builder.SearchSourceBuilder;
   import java.io.FileInputStream;
   import java.io.IOException;
   import java.security.KeyStore;
   import java.security.SecureRandom;
   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.KeyManagerFactory;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManagerFactory;
   public class ESSecuredClientWithCerDemo {
       private static final String KEY_STORE_PWD = "";
       private static final String TRUST_KEY_STORE_PWD = "";
       private static final String CA_JKS_PATH = "ca.jks";
       private static final String CLIENT_JKS_PATH = "client.jks";
       private static final String ELB_ADDRESS = "127.0.0.1";
       private static final int ELB_PORT = 9200;
       private static final String CSS_USERNAME = "user";
       private static final String CSS_PWD = "";
       public static void main(String[] args) {
          // Create a client.
           RestHighLevelClient client = initESClient(ELB_ADDRESS, CSS_USERNAME, CSS_PWD);
           try {
            // Search match_all, which is equivalent to {\"query\": {\"match_all\": {}}}.
               SearchRequest searchRequest = new SearchRequest();
               SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
               searchSourceBuilder.query(QueryBuilders.matchAllQuery());
               searchRequest.source(searchSourceBuilder);
               // query
               SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
               System.out.println("query result: " + searchResponse.toString());
               SearchHits hits = searchResponse.getHits();
               for (SearchHit hit : hits) {
                   System.out.println(hit.getSourceAsString());
               }
               System.out.println("query success");
               Thread.sleep(2000L);
           } catch (InterruptedException | IOException e) {
               e.printStackTrace();
           } finally {
               IOUtils.closeQuietly(client);
           }
       }
       private static RestHighLevelClient initESClient(String clusterAddress, String userName, String password) {
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(userName, password));
           SSLContext ctx = null;
           try {
               KeyStore ks = getKeyStore(CLIENT_JKS_PATH, KEY_STORE_PWD, "JKS");
               KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
               kmf.init(ks, KEY_STORE_PWD.toCharArray());
               KeyStore tks = getKeyStore(CA_JKS_PATH, TRUST_KEY_STORE_PWD, "JKS");
               TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
               tmf.init(tks);
               ctx = SSLContext.getInstance("SSL", "SunJSSE");
               ctx.init(kmf.getKeyManagers(), tmf.getTrustManagers(), new SecureRandom());
           } catch (Exception e) {
               e.printStackTrace();
           }
           SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(ctx, new HostnameVerifier() {
               @Override
               public boolean verify(String arg0, SSLSession arg1) {
                   return true;
               }
           });
           SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,
               credentialsProvider);
           RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, ELB_PORT, "https"))
               .setHttpClientConfigCallback(httpClientConfigCallback);
           RestHighLevelClient client = new RestHighLevelClient(builder);
           return client;
       }
       private static KeyStore getKeyStore(String path, String pwd, String type) {
           KeyStore keyStore = null;
           FileInputStream is = null;
           try {
               is = new FileInputStream(path);
               keyStore = KeyStore.getInstance(type);
               keyStore.load(is, pwd.toCharArray());
           } catch (Exception e) {
               e.printStackTrace();
           } finally {
               IOUtils.closeQuietly(is);
           }
           return keyStore;
       }
   }

SecuredHttpClientConfigCallback Code
------------------------------------

::

   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.common.Nullable;
   import java.util.Objects;
   class SecuredHttpClientConfigCallback implements RestClientBuilder.HttpClientConfigCallback {
       @Nullable
       private final CredentialsProvider credentialsProvider;
       /**
        * The {@link SSLIOSessionStrategy} for all requests to enable SSL / TLS encryption.
        */
       private final SSLIOSessionStrategy sslStrategy;
       /**
        * Create a new {@link SecuredHttpClientConfigCallback}.
        *
        * @param credentialsProvider The credential provider, if a username/password have been supplied
        * @param sslStrategy         The SSL strategy, if SSL / TLS have been supplied
        * @throws NullPointerException if {@code sslStrategy} is {@code null}
        */
       SecuredHttpClientConfigCallback(final SSLIOSessionStrategy sslStrategy,
           @Nullable final CredentialsProvider credentialsProvider) {
           this.sslStrategy = Objects.requireNonNull(sslStrategy);
           this.credentialsProvider = credentialsProvider;
       }
       /**
        * Get the {@link CredentialsProvider} that will be added to the HTTP client.
        *
        * @return Can be {@code null}.
        */
       @Nullable
       CredentialsProvider getCredentialsProvider() {
           return credentialsProvider;
       }
       /**
        * Get the {@link SSLIOSessionStrategy} that will be added to the HTTP client.
        *
        * @return Never {@code null}.
        */
       SSLIOSessionStrategy getSSLStrategy() {
           return sslStrategy;
       }
       /**
        * Sets the {@linkplain HttpAsyncClientBuilder#setDefaultCredentialsProvider(CredentialsProvider) credential provider},
        *
        * @param httpClientBuilder The client to configure.
        * @return Always {@code httpClientBuilder}.
        */
       @Override
       public HttpAsyncClientBuilder customizeHttpClient(final HttpAsyncClientBuilder httpClientBuilder) {
           // enable SSL / TLS
           httpClientBuilder.setSSLStrategy(sslStrategy);
           // enable user authentication
           if (credentialsProvider != null) {
               httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
           }
           return httpClientBuilder;
       }
   }

pom.xml Code
------------

.. code-block::

   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>
       <groupId>1</groupId>
       <artifactId>ESClient</artifactId>
       <version>1.0-SNAPSHOT</version>
       <name>ESClient</name>

       <properties>
           <maven.compiler.source>8</maven.compiler.source>
           <maven.compiler.target>8</maven.compiler.target>
           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
           <elasticsearch.version>7.10.2</elasticsearch.version>
       </properties>
       <dependencies>
           <dependency>
               <groupId>org.elasticsearch.client</groupId>
               <artifactId>transport</artifactId>
               <version>${elasticsearch.version}</version>
           </dependency>
           <dependency>
               <groupId>org.elasticsearch</groupId>
               <artifactId>elasticsearch</artifactId>
               <version>${elasticsearch.version}</version>
           </dependency>
           <dependency>
               <groupId>org.elasticsearch.client</groupId>
               <artifactId>elasticsearch-rest-high-level-client</artifactId>
               <version>${elasticsearch.version}</version>
           </dependency>
           <dependency>
               <groupId>commons-io</groupId>
               <artifactId>commons-io</artifactId>
               <version>2.11.0</version>
           </dependency>
       </dependencies>
   </project>
