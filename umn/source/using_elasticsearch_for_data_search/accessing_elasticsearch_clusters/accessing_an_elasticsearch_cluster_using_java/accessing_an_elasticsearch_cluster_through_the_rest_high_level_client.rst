:original_name: css_01_0386.html

.. _css_01_0386:

Accessing an Elasticsearch Cluster Through the Rest High Level Client
=====================================================================

Elasticsearch provides SDK (Rest High Level Client) for connecting to a cluster. This client encapsulates Elasticsearch APIs. You only need to construct required structures to access the Elasticsearch cluster. For details about how to use the Rest Client, see the official document at https://www.elastic.co/guide/en/elasticsearch/client/java-rest/current/java-rest-high.html.

This section describes how to use the Rest High Level Client to access the CSS cluster. The Rest High Level Client can be connected to the cluster in any of the following ways:

-  :ref:`Connecting to a Non-Security Mode Cluster Through the Rest High Level Client <css_01_0386__en-us_topic_0000001961178813_section197550282614>`: suitable for clusters using non-security mode
-  :ref:`Connecting to a Security Cluster Through Rest High Level Client (Without Security Certificates) <css_01_0386__en-us_topic_0000001961178813_section1523020817518>`: suitable for clusters in security mode+HTTP, and for clusters in security mode+HTTPS (without using certificates)
-  :ref:`Connecting to a Security Cluster Through Rest High Level Client (With Security Certificates) <css_01_0386__en-us_topic_0000001961178813_section1368184211106>`: suitable for clusters in security mode+HTTPS

Constraints
-----------

You are advised to use the Rest High Level Client version that matches the Elasticsearch version. For example, use Rest High Level Client 7.6.2 to access an Elasticsearch 7.6.2 cluster. If your Java Rest High Level Client version is later than the Elasticsearch cluster and incompatible with a few requests, you can use **RestHighLevelClient.getLowLevelClient()** to obtain Low Level Client and customize the Elasticsearch request content.

Prerequisites
-------------

-  There are available CSS clusters.

-  You have a server running Java that can communicate with the CSS cluster.

-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Network Configuration <css_01_0381__section855085010198>`.

-  Install JDK 1.8 on the server. You can download JDK 1.8 from: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

-  Java dependencies have been installed on the server.

   *7.6.2* indicates the version of the Elasticsearch Java client.

   -  Maven mode:

      .. code-block::

         <dependency>
             <groupId>org.elasticsearch.client</groupId>
             <artifactId>elasticsearch-rest-high-level-client</artifactId>
             <version>7.6.2</version>
         </dependency>
         <dependency>
             <groupId>org.elasticsearch</groupId>
             <artifactId>elasticsearch</artifactId>
             <version>7.6.2</version>
         </dependency>

   -  Gradle mode:

      .. code-block::

         compile group: 'org.elasticsearch.client', name: 'elasticsearch-rest-high-level-client', version: '7.6.2'

.. _css_01_0386__en-us_topic_0000001961178813_section197550282614:

Connecting to a Non-Security Mode Cluster Through the Rest High Level Client
----------------------------------------------------------------------------

You can use the Rest High Level Client to connect to a non-security mode cluster and check whether the **test** index exists. The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.elasticsearch.client.RequestOptions;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
   import org.elasticsearch.client.indices.GetIndexRequest;

   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;

   /**
   * Use Rest Hive Level to connect to a non-security cluster.
    */
   public class Main {
       public static void main(String[] args) throws IOException {
           List<String> host = Arrays.asList("x.x.x.x", "x.x.x.x");
           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, 9200, "http"));
           final RestHighLevelClient client = new RestHighLevelClient(builder);
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }
   }

*host* indicates the IP address of the cluster. If there are multiple IP addresses, separate them using commas (,). *test* indicates the index name to be queried.

.. _css_01_0386__en-us_topic_0000001961178813_section1523020817518:

Connecting to a Security Cluster Through Rest High Level Client (Without Security Certificates)
-----------------------------------------------------------------------------------------------

You can connect to a cluster in security mode+HTTP or a cluster in security mode + HTTPS (without using certificates).

The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   import org.elasticsearch.action.admin.cluster.health.ClusterHealthRequest;
   import org.elasticsearch.action.admin.cluster.health.ClusterHealthResponse;
   import org.elasticsearch.client.RequestOptions;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
   import org.elasticsearch.client.indices.GetIndexRequest;
   import org.elasticsearch.common.Nullable;

   import java.io.IOException;
   import java.security.KeyManagementException;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.Objects;

   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.X509TrustManager;

   /**
   * Connect to a security cluster through Rest High Level (without using certificates).
    */
   public class Main {
       /**
   * Create a class for the client. Define the create function.
        */
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password) throws IOException{
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
           SSLContext sc = null;
           try {
               sc = SSLContext.getInstance("SSL");
               sc.init(null, trustAllCerts, new SecureRandom());
           } catch (KeyManagementException | NoSuchAlgorithmException e) {
               e.printStackTrace();
           }
           SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());
           SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,
               credentialsProvider);


           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, port, protocol))
               .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                   .setConnectionRequestTimeout(connectionRequestTimeout)
                   .setSocketTimeout(socketTimeout))
               .setHttpClientConfigCallback(httpClientConfigCallback);
           final RestHighLevelClient client = new RestHighLevelClient(builder);
           logger.info("es rest client build success {} ", client);

           ClusterHealthRequest request = new ClusterHealthRequest();
           ClusterHealthResponse response = client.cluster().health(request, RequestOptions.DEFAULT);
           logger.info("es rest client health response {} ", response);
           return client;
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }

       /**
        * Configure trustAllCerts to ignore the certificate configuration.
        */
       public static TrustManager[] trustAllCerts = new TrustManager[] {
           new X509TrustManager() {
               @Override
               public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
               }

               @Override
               public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
               }

               @Override
               public X509Certificate[] getAcceptedIssuers() {
                   return null;
               }
           }
       };

       private static final Logger logger = LogManager.getLogger(Main.class);

       static class SecuredHttpClientConfigCallback implements RestClientBuilder.HttpClientConfigCallback {
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

       public static class NullHostNameVerifier implements HostnameVerifier {
           @Override
           public boolean verify(String arg0, SSLSession arg1) {
               return true;
           }
       }

       /**
   * The following is an example of the main function. Call the create function to create a client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("x.x.x.x", "x.x.x.x"), 9200, "https", 1000, 1000, 1000,  "username", "password");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
       }
   }

.. table:: **Table 1** Variables

   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                                            |
   +==========================+========================================================================================================================+
   | host                     | IP address for accessing the Elasticsearch cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the Elasticsearch cluster. The default value is **9200**.                                               |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol, which can be **http** or **https**.                                                               |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout period.                                                                                      |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Timeout period of a socket connection request.                                                                         |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Timeout period of a socket request.                                                                                    |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                                    |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                                  |
   +--------------------------+------------------------------------------------------------------------------------------------------------------------+

.. _css_01_0386__en-us_topic_0000001961178813_section1368184211106:

Connecting to a Security Cluster Through Rest High Level Client (With Security Certificates)
--------------------------------------------------------------------------------------------

You can use a security certificate to connect to a cluster in security mode + HTTPS.

#. Obtain the security certificate **CloudSearchService.cer**.

   a. Log in to the CSS management console.
   b. In the navigation pane, choose **Clusters**. The cluster list is displayed.
   c. Click the name of a cluster to go to the cluster details page.
   d. On the **Configuration** page, click **Download Certificate** next to **HTTPS Access**.

#. Convert the security certificate **CloudSearchService.cer**. Upload the downloaded security certificate to the client and use keytool to convert the .cer certificate into a .jks certificate that can be read by Java.

   -  In Linux, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

   -  In Windows, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore .\truststore.jks -file .\CloudSearchService.cer

   In the preceding command, *newname* indicates the user-defined certificate name.

   After this command is executed, you will be prompted to set the certificate password and confirm the password. Securely store the password. It will be used for accessing the cluster.

#. Access the cluster. The sample code is as follows:

   ::

      import org.apache.http.HttpHost;
      import org.apache.http.auth.AuthScope;
      import org.apache.http.auth.UsernamePasswordCredentials;
      import org.apache.http.client.CredentialsProvider;
      import org.apache.http.conn.ssl.NoopHostnameVerifier;
      import org.apache.http.impl.client.BasicCredentialsProvider;
      import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
      import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
      import org.apache.logging.log4j.LogManager;
      import org.apache.logging.log4j.Logger;
      import org.elasticsearch.action.admin.cluster.health.ClusterHealthRequest;
      import org.elasticsearch.action.admin.cluster.health.ClusterHealthResponse;
      import org.elasticsearch.client.RequestOptions;
      import org.elasticsearch.client.RestClient;
      import org.elasticsearch.client.RestClientBuilder;
      import org.elasticsearch.client.RestHighLevelClient;
      import org.elasticsearch.client.indices.GetIndexRequest;
      import org.elasticsearch.common.Nullable;

      import java.io.File;
      import java.io.FileInputStream;
      import java.io.IOException;
      import java.io.InputStream;
      import java.security.KeyStore;
      import java.security.SecureRandom;
      import java.security.cert.CertificateException;
      import java.security.cert.X509Certificate;
      import java.util.Arrays;
      import java.util.List;
      import java.util.Objects;

      import javax.net.ssl.SSLContext;
      import javax.net.ssl.TrustManager;
      import javax.net.ssl.TrustManagerFactory;
      import javax.net.ssl.X509TrustManager;

      /**
      * Use Rest Hive Level to connect to a security cluster (using an HTTPS certificate).
       */
      public class Main {
          public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String cerFilePath,
              String cerPassword) throws IOException {

              final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
              credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
              SSLContext sc = null;
              try {
                  TrustManager[] tm = {new MyX509TrustManager(cerFilePath, cerPassword)};
                  sc = SSLContext.getInstance("SSL", "SunJSSE");
                  //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
                  sc.init(null, tm, new SecureRandom());
              } catch (Exception e) {
                  e.printStackTrace();
              }

              SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NoopHostnameVerifier());
              SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,
                  credentialsProvider);

              RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, port, protocol))
                  .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                      .setConnectionRequestTimeout(connectionRequestTimeout)
                      .setSocketTimeout(socketTimeout))
                  .setHttpClientConfigCallback(httpClientConfigCallback);
              final RestHighLevelClient client = new RestHighLevelClient(builder);
              logger.info("es rest client build success {} ", client);

              ClusterHealthRequest request = new ClusterHealthRequest();
              ClusterHealthResponse response = client.cluster().health(request, RequestOptions.DEFAULT);
              logger.info("es rest client health response {} ", response);
              return client;
          }

          /**
           * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
           */
          public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
              return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
          }

          /**
           * SecuredHttpClientConfigCallback class definition
           */
          static class SecuredHttpClientConfigCallback implements RestClientBuilder.HttpClientConfigCallback {
              @Nullable
              private final CredentialsProvider credentialsProvider;

              private final SSLIOSessionStrategy sslStrategy;

              SecuredHttpClientConfigCallback(final SSLIOSessionStrategy sslStrategy,
                  @Nullable final CredentialsProvider credentialsProvider) {
                  this.sslStrategy = Objects.requireNonNull(sslStrategy);
                  this.credentialsProvider = credentialsProvider;
              }

              @Nullable
              CredentialsProvider getCredentialsProvider() {
                  return credentialsProvider;
              }

              SSLIOSessionStrategy getSSLStrategy() {
                  return sslStrategy;
              }

              @Override
              public HttpAsyncClientBuilder customizeHttpClient(final HttpAsyncClientBuilder httpClientBuilder) {
                  httpClientBuilder.setSSLStrategy(sslStrategy);
                  if (credentialsProvider != null) {
                      httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                  }
                  return httpClientBuilder;
              }
          }

          private static final Logger logger = LogManager.getLogger(Main.class);

          public static class MyX509TrustManager implements X509TrustManager {
              X509TrustManager sunJSSEX509TrustManager;

              MyX509TrustManager(String cerFilePath, String cerPassword) throws Exception {
                  File file = new File(cerFilePath);
                  if (!file.isFile()) {
                      throw new Exception("Wrong Certification Path");
                  }
                  System.out.println("Loading KeyStore " + file + "...");
                  InputStream in = new FileInputStream(file);
                  KeyStore ks = KeyStore.getInstance("JKS");
                  ks.load(in, cerPassword.toCharArray());
                  TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509", "SunJSSE");
                  tmf.init(ks);
                  TrustManager[] tms = tmf.getTrustManagers();
                  for (TrustManager tm : tms) {
                      if (tm instanceof X509TrustManager) {
                          sunJSSEX509TrustManager = (X509TrustManager) tm;
                          return;
                      }
                  }
                  throw new Exception("Couldn't initialize");
              }

              @Override
              public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {

              }

              @Override
              public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {

              }

              @Override
              public X509Certificate[] getAcceptedIssuers() {
                  return new X509Certificate[0];
              }
          }

          /**
      * The following is an example of the main function. Call the create function to create a client and check whether the test index exists.
           */
          public static void main(String[] args) throws IOException {
              RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 1000, 1000, 1000, "username", "password", "cerFilePath", "cerPassword");
              GetIndexRequest indexRequest = new GetIndexRequest("test");
              boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
              System.out.println(exists);
              client.close();
          }
      }

   .. table:: **Table 2** Function parameters

      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | Parameter                | Description                                                                                                            |
      +==========================+========================================================================================================================+
      | host                     | IP address for accessing the Elasticsearch cluster. If there are multiple IP addresses, separate them with commas (,). |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | port                     | Access port of the Elasticsearch cluster. The default value is **9200**.                                               |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | protocol                 | Connection protocol. Set this parameter to **https**.                                                                  |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | connectTimeout           | Socket connection timeout period.                                                                                      |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | connectionRequestTimeout | Timeout period of a socket connection request.                                                                         |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | socketTimeout            | Timeout period of a socket request.                                                                                    |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | username                 | Username for accessing the cluster.                                                                                    |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | password                 | Password of the user.                                                                                                  |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | cerFilePath              | Certificate path.                                                                                                      |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
      | cerPassword              | Certificate password.                                                                                                  |
      +--------------------------+------------------------------------------------------------------------------------------------------------------------+
