:original_name: css_01_0012.html

.. _css_01_0012:

Accessing a Cluster
===================

After a cluster is created, you can access the cluster to use Elasticsearch and perform operations, such as, defining index data, importing data, and searching for data. For more information about Elasticsearch, see the `Elasticsearch Reference <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`__. You can use any of the following methods to access a cluster:

-  :ref:`Accessing a Cluster Using Kibana on the Management Console <css_01_0012__section9848115695612>`
-  :ref:`Accessing a Cluster by Calling Elasticsearch APIs on the ECS That Is Located in the Same VPC as the Cluster <css_01_0012__section16223134914582>`
-  :ref:`Accessing a Cluster Using Java API in Non-security Mode <css_01_0012__section1619554519273>`
-  :ref:`Accessing a Cluster Using the Java API in Security Mode with Elasticsearch <css_01_0012__section0445155723816>`

.. _css_01_0012__section9848115695612:

Accessing a Cluster Using Kibana on the Management Console
----------------------------------------------------------

#. Log in to the CSS management console.
#. In the left navigation pane, click **Clusters**.
#. On the displayed **Clusters** page, locate the row containing the target cluster and click **Access Kibana** in the **Operation** column.
#. On the Kibana page that is displayed, you can create indices, query indices and documents, and analyze document fields. For details about Kibana, see :ref:`Kibana <css_04_0007>`. For details about how to import data to Elasticsearch, see the following sections:

   -  :ref:`Using Logstash to Import Data to Elasticsearch <css_01_0048>`
   -  :ref:`Using Kibana or APIs to Import Data to Elasticsearch <css_01_0024>`

.. _css_01_0012__section16223134914582:

Accessing a Cluster by Calling Elasticsearch APIs on the ECS That Is Located in the Same VPC as the Cluster
-----------------------------------------------------------------------------------------------------------

The ECS that you use to access the cluster by calling Elasticsearch APIs, must meet the following requirements. For details about how to create and log in to an ECS, see `Logging In to a Linux ECS <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html>`__ or `Logging In to a Windows ECS <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html>`__.

-  Sufficient disk space is allocated for the ECS.

-  The ECS and the cluster must be in the same VPC.

-  The security group of the ECS must be the same as that of the cluster.

   If this requirement is not met, modify the ECS security group or configure the inbound and outbound rules of the ECS security group to allow the ECS security group to be accessed by all security groups of the cluster. For details, see `Configuring Security Group Rules <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030878383.html>`__.

-  Configure security group rule settings of the target CSS cluster. Set **Protocol** to **TCP** and **Port Range** to **9200** or a port range including port **9200** for both the outbound and inbound directions.

To access a cluster by calling Elasticsearch APIs on the ECS that is located in the same VPC as the cluster, perform the following steps:

#. Create and then log in to an ECS that meets the requirements.

#. To access a cluster, use the private network address and port number of one node in the cluster. You can obtain the private network addresses of nodes from the **Private Network Address** column in the cluster list. If there is only one node in the cluster, the private network address and port number of this node are displayed. If there are multiple nodes in the cluster, private network addresses and port numbers of all nodes are displayed.

   Assume that there are two nodes in a cluster. Value **10.62.179.32:9200 10.62.179.33:9200** indicates that the private network addresses of the two nodes are **10.62.179.32** and **10.62.179.33** respectively, and port **9200** is used to access both nodes.

#. Run the cURL command to execute the API or call the API by using a program before accessing the cluster. For details about Elasticsearch operations and APIs, see the `Elasticsearch Reference <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`__.

   For example, run the following cURL command to view the index information in the cluster. In this example, the private access IP address of one node in the cluster is **10.62.179.32** and the port number is **9200**.

   -  If the cluster you access has the communication encryption function enabled, you need to access the cluster using HTTPS and add **-k** to the cURL command.

      If communication encryption is enabled, the CSS server uses a shared self-signed certificate. In this case, the client cannot authenticate the certificate. You are advised to disable certificate verification on the client.

      .. code-block::

         curl -k 'https://10.62.179.32:9200/_cat/indices'

   -  If encryption has not been enabled for the communication with the cluster, run the following command:

      .. code-block::

         curl 'http://10.62.179.32:9200/_cat/indices'

   .. note::

      In the preceding command, the private network address and port number of only one node in the cluster are used. If the node fails, the command will fail to be executed. If the cluster contains multiple nodes, you can replace the private network address and port number of the faulty node with those of any available node in the cluster. If the cluster contains only one node, restore the node and execute the command again.

   If encryption has not been enabled for the communication with the cluster, the command output is similar to that shown in the following figure.


   .. figure:: /_static/images/en-us_image_0000001286436598.png
      :alt: **Figure 1** Command output


      **Figure 1** Command output

.. _css_01_0012__section1619554519273:

Accessing a Cluster Using Java API in Non-security Mode
-------------------------------------------------------

For clusters in the non-security mode, you are advised to use use RestHighLevelClient.

-  Create a client using the default method of the RestHighLevelClient class.

   ::

      RestHighLevelClient client = new RestHighLevelClient(
              RestClient.builder(
                      new HttpHost("localhost", 9200, "http")));

.. _css_01_0012__section0445155723816:

Accessing a Cluster Using the Java API in Security Mode with Elasticsearch
--------------------------------------------------------------------------

After enabling the security mode function for Elasticsearch 7.1.1 and later versions, accessing a cluster requires the use of HTTPS and the username and password for authentication.

You need to use clusters 7.1.1 and later versions as well as related APIs if you use the Java API to access a cluster, because the TransportClient class in the earlier version cannot access a cluster using the username and password.

Two access modes are available: Create a client using either the TransportClient or RestHighLevelClient class. RestHighLevelClient is recommended.

-  **Create a client using the TransportClient class.**

   Run the following commands on the client to generate the keystore and truststore files. The certificate (**CloudSearchService.cer**) downloaded from the cluster management page is used.

   ::

      keytool -genkeypair -alias certificatekey -keyalg RSA -keystore transport-keystore.jks
      keytool -import -alias certificatekey -file CloudSearchService.cer  -keystore truststore.jks

   Use the keystore and truststore files to access the cluster, create the TransportClient class using the PreBuiltTransportClient method, and add the settings in the client thread.

   The key code is as follows:

   ::

      String userPw = "username:password";
      String path = Paths.get(SecurityTransportClientDemo.class.getClassLoader().getResource(".").toURI()).toString();

      Settings settings = Settings.builder()
                       .put("opendistro_security.ssl.transport.enforce_hostname_verification", false)
                       .put("opendistro_security.ssl.transport.keystore_filepath", path + "/transport-keystore.jks")
                       .put("opendistro_security.ssl.transport.keystore_password", "tscpass")
                       .put("opendistro_security.ssl.transport.truststore_filepath", path + "/truststore.jks")
                       .put("client.transport.ignore_cluster_name", "true")
                       .put("client.transport.sniff", false).build();

      TransportClient client = (new PreBuiltTransportClient(settings, new Class[]{OpenDistroSecurityPlugin.class})).addTransportAddress(new
                            TransportAddress(InetAddress.getByName(ip), 9300));

      String base64UserPw = Base64.getEncoder().encodeToString(userPw.getBytes("utf-8"));
                     client.threadPool().getThreadContext().putHeader("Authorization", "Basic " + base64UserPw);

-  **Create a client using the RestHighLevelClient class.**

   The HttpHost class is used to process HTTP requests. In the HttpHost class, the CredentialsProvider and SSLIOSessionStrategy configuration parameter classes are encapsulated in the customized SecuredHttpClientConfigCallback class to configure request connection parameters.

   SecuredHttpClientConfigCallback: encapsulates all user-defined connection parameters.

   CredentialsProvider: Elasticsearch API, which is used to encapsulate the username and password using the method provided by Elasticsearch.

   SSLIOSessionStrategy: Configure SSL parameters, including the SSL domain name authentication mode and certificate processing mode. The SSLContext class is used to encapsulate related settings.

   You can access a cluster through either of the following modes: ignore certificates and use certificates.

   -  Ignore all certificates and skip certificate authentication.

      Construct the TrustManager. Use the default X509TrustManager. Do not rewrite any method. That is, ignore all related operations.

      Construct the SSLContext. Use TrustManager in the preceding step as the parameter and construct the SSLContext with the default method.

      ::

         static TrustManager[] trustAllCerts = new TrustManager[] { new X509TrustManager() {
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
             }};
          final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                 credentialsProvider.setCredentials(AuthScope.ANY,
                         new UsernamePasswordCredentials(userName, password));
                 SSLContext sc = null;
                 try{
                     sc = SSLContext.getInstance("SSL");
                     sc.init(null, trustAllCerts, new SecureRandom());
                 }catch(KeyManagementException e){
                         e.printStackTrace();
                 }catch(NoSuchAlgorithmException e){
                         e.printStackTrace();
                 }
                 SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());

                 SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,credentialsProvider);

                 RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200,
                                         "https")).setHttpClientConfigCallback(httpClientConfigCallback);

                 RestHighLevelClient client = new RestHighLevelClient(builder);

   -  Upload the downloaded certificate (**CloudSearchService.cer**) for accessing the cluster.

      Upload the certificate to the client and use the keytool to convert the certificate into a format that can be read by Java. (The default password of the keytool is **changeit**).

      .. code-block::

         keytool -import -alias custom name -keystore path for exporting the certificate and its new name -file path for uploading the certificate

      Customize the TrustManager class, which is inherited from the X509TrustManager. Read the certificate generated in the preceding step, add it to the trust certificate, and rewrite the three methods of the X509TrustManager interface.

      Construct the SSLContext. Use TrustManager in the preceding step as the parameter and construct the SSLContext with the default method.

      ::

         public static class MyX509TrustManager implements X509TrustManager {

                 X509TrustManager sunJSSEX509TrustManager;
                 MyX509TrustManager() throws Exception {
                     File file = new File("certification file path");
                     if (file.isFile() == false) {
                         throw new Exception("Wrong Certification Path");
                     }
                     System.out.println("Loading KeyStore " + file + "...");
                     InputStream in = new FileInputStream(file);
                     KeyStore ks = KeyStore.getInstance("JKS");
                     ks.load(in, "changeit".toCharArray());
                     TrustManagerFactory tmf =
                             TrustManagerFactory.getInstance("SunX509", "SunJSSE");
                     tmf.init(ks);
                     TrustManager tms [] = tmf.getTrustManagers();
                     for (int i = 0; i < tms.length; i++) {
                         if (tms[i] instanceof X509TrustManager) {
                             sunJSSEX509TrustManager = (X509TrustManager) tms[i];
                             return;
                         }
                     }
                     throw new Exception("Couldn't initialize");
                 }

         final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                 credentialsProvider.setCredentials(AuthScope.ANY,
                         new UsernamePasswordCredentials(userName, password));

                 SSLContext sc = null;
                 try{
                     TrustManager[] tm = {new MyX509TrustManager()};
                     sc = SSLContext.getInstance("SSL", "SunJSSE");
                     sc.init(null, tm, new SecureRandom());
                 }catch (Exception e) {
                     e.printStackTrace();
                 }

                 SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());

                 SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,credentialsProvider);
                 RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200, "https"))
                         .setHttpClientConfigCallback(httpClientConfigCallback);
                 RestHighLevelClient client = new RestHighLevelClient(builder);

   -  Sample code

      When the code is running, transfer three parameters: access address, cluster login username, and password. The request is **GET /_search{"query": {"match_all": {}}}**.

      .. note::

         The access address of a cluster with security mode enabled usually starts with **https**.

      **ESSecuredClient class (Ignore certificates)**

      ::

         package securitymode;

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

         import java.io.IOException;
         import java.security.KeyManagementException;
         import java.security.NoSuchAlgorithmException;
         import java.security.SecureRandom;
         import java.security.cert.CertificateException;
         import java.security.cert.X509Certificate;

         import javax.net.ssl.HostnameVerifier;
         import javax.net.ssl.SSLContext;
         import javax.net.ssl.SSLSession;
         import javax.net.ssl.TrustManager;
         import javax.net.ssl.X509TrustManager;

         public class ESSecuredClientIgnoreCerDemo {

             public static void main(String[] args) {
                 String clusterAddress = args[0];
                 String userName = args[1];
                 String password = args[2];
                // Create a client.
                 RestHighLevelClient client = initESClient(clusterAddress, userName, password);
                 try {
                  // Search match_all, which is equivalent to {\"query\": {\"match_all\": {}}}.
                     SearchRequest searchRequest = new SearchRequest();
                     SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
                     searchSourceBuilder.query(QueryBuilders.matchAllQuery());
                     searchRequest.source(searchSourceBuilder);

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
                     try {
                         client.close();
                         System.out.println("close client");
                     } catch (IOException e) {
                         e.printStackTrace();
                     }
                 }
             }

             private static RestHighLevelClient initESClient(String clusterAddress, String userName, String password) {
                 final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                 credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(userName, password));
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
                 RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200, "https"))
                     .setHttpClientConfigCallback(httpClientConfigCallback);
                 RestHighLevelClient client = new RestHighLevelClient(builder);
                 return client;
             }

             static TrustManager[] trustAllCerts = new TrustManager[] {
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

             public static class NullHostNameVerifier implements HostnameVerifier {
                 @Override
                 public boolean verify(String arg0, SSLSession arg1) {
                     return true;
                 }
             }

         }

      **ESSecuredClient class (Uses certificates)**

      ::

         package securitymode;

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

         import java.io.File;
         import java.io.FileInputStream;
         import java.io.IOException;
         import java.io.InputStream;
         import java.security.KeyStore;
         import java.security.SecureRandom;
         import java.security.cert.CertificateException;
         import java.security.cert.X509Certificate;

         import javax.net.ssl.HostnameVerifier;
         import javax.net.ssl.SSLContext;
         import javax.net.ssl.SSLSession;
         import javax.net.ssl.TrustManager;
         import javax.net.ssl.TrustManagerFactory;
         import javax.net.ssl.X509TrustManager;

         public class ESSecuredClientWithCerDemo {

             public static void main(String[] args) {
                 String clusterAddress = args[0];
                 String userName = args[1];
                 String password = args[2];
                 String cerFilePath = args[3];
                 String cerPassword = args[4];
                // Create a client.
                 RestHighLevelClient client = initESClient(clusterAddress, userName, password, cerFilePath, cerPassword);
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
                     try {
                         client.close();
                         System.out.println("close client");
                     } catch (IOException e) {
                         e.printStackTrace();
                     }
                 }
             }

             private static RestHighLevelClient initESClient(String clusterAddress, String userName, String password,
                 String cerFilePath, String cerPassword) {
                 final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                 credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(userName, password));
                 SSLContext sc = null;
                 try {
                     TrustManager[] tm = {new MyX509TrustManager(cerFilePath, cerPassword)};
                     sc = SSLContext.getInstance("SSL", "SunJSSE");
                     //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
                     sc.init(null, tm, new SecureRandom());
                 } catch (Exception e) {
                     e.printStackTrace();
                 }

                 SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());
                 SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,
                     credentialsProvider);
                 RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200, "https"))
                     .setHttpClientConfigCallback(httpClientConfigCallback);
                 RestHighLevelClient client = new RestHighLevelClient(builder);
                 return client;
             }

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

             public static class NullHostNameVerifier implements HostnameVerifier {
                 @Override
                 public boolean verify(String arg0, SSLSession arg1) {
                     return true;
                 }
             }

         }

      **SecuredHttpClientConfigCallback class**

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

      **pom.xml file**

      .. code-block::

         <?xml version="1.0" encoding="UTF-8"?>
         <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
             <modelVersion>4.0.0</modelVersion>
             <groupId>1</groupId>
             <artifactId>ESClient</artifactId>
             <version>1.0-SNAPSHOT</version>
             <name>ESClient</name>
             <!-- FIXME change it to the project's website -->
             <url>http://www.example.com</url>
             <properties>
                 <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
                 <maven.compiler.source>1.7</maven.compiler.source>
                 <maven.compiler.target>1.7</maven.compiler.target>
             </properties>
             <dependencies>
                 <dependency>
                     <groupId>junit</groupId>
                     <artifactId>junit</artifactId>
                     <version>4.11</version>
                     <scope>test</scope>
                 </dependency>
                 <dependency>
                     <groupId>org.elasticsearch.client</groupId>
                     <artifactId>transport</artifactId>
                     <version>6.5.4</version>
                 </dependency>
                 <dependency>
                     <groupId>org.elasticsearch</groupId>
                     <artifactId>elasticsearch</artifactId>
                     <version>6.5.4</version>
                 </dependency>
                 <dependency>
                     <groupId>org.elasticsearch.client</groupId>
                     <artifactId>elasticsearch-rest-high-level-client</artifactId>
                     <version>6.5.4</version>
                 </dependency>
                 <dependency>
                     <groupId>org.apache.logging.log4j</groupId>
                     <artifactId>log4j-api</artifactId>
                     <version>2.7</version>
                 </dependency>
                 <dependency>
                     <groupId>org.apache.logging.log4j</groupId>
                     <artifactId>log4j-core</artifactId>
                     <version>2.7</version>
                 </dependency>
             </dependencies>
             <build>
                 <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
                     <plugins>
                         <!-- clean lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle -->
                         <plugin>
                             <artifactId>maven-clean-plugin</artifactId>
                             <version>3.1.0</version>
                         </plugin>
                         <!-- default lifecycle, jar packaging: see https://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_jar_packaging -->
                         <plugin>
                             <artifactId>maven-resources-plugin</artifactId>
                             <version>3.0.2</version>
                         </plugin>
                         <plugin>
                             <artifactId>maven-compiler-plugin</artifactId>
                             <version>3.8.0</version>
                         </plugin>
                         <plugin>
                             <artifactId>maven-surefire-plugin</artifactId>
                             <version>2.22.1</version>
                         </plugin>
                         <plugin>
                             <artifactId>maven-jar-plugin</artifactId>
                             <version>3.0.2</version>
                         </plugin>
                         <plugin>
                             <artifactId>maven-install-plugin</artifactId>
                             <version>2.5.2</version>
                         </plugin>
                         <plugin>
                             <artifactId>maven-deploy-plugin</artifactId>
                             <version>2.8.2</version>
                         </plugin>
                         <!-- site lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#site_Lifecycle -->
                         <plugin>
                             <artifactId>maven-site-plugin</artifactId>
                             <version>3.7.1</version>
                         </plugin>
                         <plugin>
                             <artifactId>maven-project-info-reports-plugin</artifactId>
                             <version>3.0.0</version>
                         </plugin>
                     </plugins>
                 </pluginManagement>
             </build>
         </project>
