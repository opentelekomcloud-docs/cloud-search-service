:original_name: css_01_0124.html

.. _css_01_0124:

Connecting to a Cluster Through the Elasticsearch Java API Client
=================================================================

You can query and manage data in a CSS OpenSearch cluster using the Elasticsearch Java API Client. As the official Java client supported by Elasticsearch 8.x, the Elasticsearch Java API Client encapsulates native Elasticsearch APIs. You only need to construct the required request structure to access an OpenSearch cluster. For details about how to use the Elasticsearch Java API Client, see `Java API Client <https://www.elastic.co/guide/en/elasticsearch/client/java-api-client/8.19/getting-started-java.html>`__.

Although CSS's OpenSearch clusters can be connected using the Elasticsearch Java API Client, some features of the client may still be missing if later client versions are used. To ensure compatibility, confirm that the target API has been implemented and verified in CSS.

Prerequisites
-------------

-  The target OpenSearch cluster is available, the cluster version is 2.19.0 or 3.4.0, and the image version is 2.19.0_25.6.1_xxx or later.
-  The server that runs the Java code can communicate with the target OpenSearch cluster.
-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Obtaining the cluster access address <en-us_topic_0000001992165561__en-us_topic_0000001975823337_section855085010198>`.
-  Java has been installed on the server and the JDK version is 11 or later. Download JDK 11 from `Java Archive Downloads <https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html>`__.

Introducing Dependencies
------------------------

Import Java dependencies on the server that runs the Java code using either of the following ways:

-  Maven:

   Replace 8.19.0 with the actual Java client version.

   .. code-block::

      <dependencies>
       <dependency>
        <groupId>co.elastic.clients</groupId>
        <artifactId>elasticsearch-java</artifactId>
        <version>8.19.0</version>
       </dependency>
       <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>2.17.0</version>
       </dependency>
      </dependencies>

-  Gradle:

   Replace 8.19.0 with the actual Java client version.

   .. code-block::

      dependencies {
          implementation 'co.elastic.clients:elasticsearch-java:8.19.0'
          implementation 'com.fasterxml.jackson.core:jackson-databind:2.17.0'
      }

Accessing a Cluster
-------------------

The sample code varies depending on the security mode settings of the target OpenSearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +-------------------------------------------+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | OpenSearch Cluster Security-Mode Settings | Whether to Load a Security Certificate | Details                                                                                                                                                           |
   +===========================================+========================================+===================================================================================================================================================================+
   | Non-security mode                         | ``-``                                  | :ref:`Connecting to a Non-Security Mode Cluster Using the Elasticsearch Java API Client <en-us_topic_0000002474015994__section194331913152910>`                   |
   +-------------------------------------------+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTP                      | No                                     | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch Java API Client (Without a Certificate) <en-us_topic_0000002474015994__section1313513211296>` |
   |                                           |                                        |                                                                                                                                                                   |
   | Security mode + HTTPS                     |                                        |                                                                                                                                                                   |
   +-------------------------------------------+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                     | Yes                                    | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch Java API Client (With a Certificate) <en-us_topic_0000002474015994__section14782152316147>`   |
   +-------------------------------------------+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002474015994__section194331913152910:

Connecting to a Non-Security Mode Cluster Using the Elasticsearch Java API Client
---------------------------------------------------------------------------------

Use the Elasticsearch Java API Client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import co.elastic.clients.elasticsearch.ElasticsearchClient;
   import co.elastic.clients.elasticsearch.indices.CreateIndexResponse;
   import co.elastic.clients.elasticsearch.indices.DeleteIndexResponse;
   import co.elastic.clients.elasticsearch.indices.GetIndexResponse;
   import co.elastic.clients.json.jackson.JacksonJsonpMapper;
   import co.elastic.clients.transport.ElasticsearchTransport;
   import co.elastic.clients.transport.rest_client.RestClientTransport;

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.conn.ssl.NoopHostnameVerifier;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.elasticsearch.client.RestClient;

   import java.io.File;
   import java.io.FileInputStream;
   import java.io.IOException;
   import java.io.InputStream;
   import java.security.KeyManagementException;
   import java.security.KeyStore;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   public class Main {

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }

       private static ElasticsearchClient create(List<String> host, int port, String protocol, int connectTimeout,
           int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath,
           String certPassword) throws IOException {
           // Create the low-level client
           RestClient restClient = RestClient.builder(constructHttpHosts(host, port, protocol))
               .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                   .setConnectionRequestTimeout(connectionRequestTimeout)
                   .setSocketTimeout(socketTimeout))
               .setHttpClientConfigCallback(httpClientBuilder -> {
                   // enable user authentication
                   if (username != null && password != null) {
                       final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                       credentialsProvider.setCredentials(AuthScope.ANY,
                           new UsernamePasswordCredentials(username, password));
                       httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                   }
                   // set keepalive
                   httpClientBuilder.setKeepAliveStrategy(((httpResponse, httpContext) -> TimeUnit.MINUTES.toMinutes(10)));
                   // enable SSL / TLS
                   SSLContext sc = (certFilePath != null && certPassword != null) ?
                       createContextFromCaCert(certFilePath, certPassword) : createTrustAllCertsContext();

                   SSLIOSessionStrategy sslStrategy = new SSLIOSessionStrategy(sc, new NoopHostnameVerifier());
                   httpClientBuilder.setSSLStrategy(sslStrategy);

                   httpClientBuilder.setMaxConnTotal(500);
                   httpClientBuilder.setMaxConnPerRoute(300);
                   return httpClientBuilder;
               })
               .build();

           // Create the transport with a Jackson mapper
           ElasticsearchTransport transport = new RestClientTransport(restClient, new JacksonJsonpMapper());

           // And create the API client
           return new ElasticsearchClient(transport);
       }

       private static SSLContext createTrustAllCertsContext() {
           try {
               SSLContext sslContext = SSLContext.getInstance("SSL");
               sslContext.init(null, trustAllCerts, new SecureRandom());
               return sslContext;
           } catch (NoSuchAlgorithmException | KeyManagementException e) {
               throw new RuntimeException("Can not create the SSLContext", e);
           }
       }

       private static SSLContext createContextFromCaCert(String certFilePath, String certPassword) {
           try {
               // enable SSL / TLS
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
               SSLContext sc = SSLContext.getInstance("SSL", "SunJSSE");
               //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
               sc.init(null, tm, new SecureRandom());
               return sc;
           } catch (Exception e) {
               throw new RuntimeException(e);
           }
       }

       /**
        * Configure trustAllCerts to ignore the certificate configuration.
        */
       private static TrustManager[] trustAllCerts = new TrustManager[] {
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

       /**
        * Configure certificate authentication
        */
       private static class MyX509TrustManager implements X509TrustManager {
           X509TrustManager sunJSSEX509TrustManager;

           MyX509TrustManager(String certFilePath, String certPassword) throws Exception {
               File file = new File(certFilePath);
               if (!file.isFile()) {
                   throw new Exception("Wrong Certification Path");
               }
               System.out.println("Loading KeyStore " + file + "...");
               InputStream in = new FileInputStream(file);
               KeyStore ks = KeyStore.getInstance("JKS");
               ks.load(in, certPassword.toCharArray());
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
           public void checkClientTrusted(X509Certificate[] chain, String authType) {

           }

           @Override
           public void checkServerTrusted(X509Certificate[] chain, String authType) {

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
           ElasticsearchClient esClient = create(Arrays.asList("{IP address of the target cluster}"), 9200, "http", 1000, 1000, 1000, null, null, null, null);

           CreateIndexResponse indexRequest = esClient.indices()
               .create(createIndexBuilder -> createIndexBuilder.index("test"));
           boolean acknowledged = indexRequest.acknowledged();
           System.out.println("Create index successfully! " + acknowledged);

           GetIndexResponse getIndexResponse = esClient.indices().get(getIndexRequest -> getIndexRequest.index("test"));
           System.out.println("Query index successfully! \n" + getIndexResponse.toString());

           DeleteIndexResponse deleteResponse = esClient.indices()
               .delete(createIndexBuilder -> createIndexBuilder.index("test"));
           System.out.println("Delete index successfully! \n" + deleteResponse.toString());
       }
   }

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000002474015994__section1313513211296:

Connecting to a Security-Mode Cluster Using the Elasticsearch Java API Client (Without a Certificate)
-----------------------------------------------------------------------------------------------------

Use the Elasticsearch Java API Client to connect to a security-mode OpenSearch cluster (HTTP or HTTPS) without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import co.elastic.clients.elasticsearch.ElasticsearchClient;
   import co.elastic.clients.elasticsearch.indices.CreateIndexResponse;
   import co.elastic.clients.elasticsearch.indices.DeleteIndexResponse;
   import co.elastic.clients.elasticsearch.indices.GetIndexResponse;
   import co.elastic.clients.json.jackson.JacksonJsonpMapper;
   import co.elastic.clients.transport.ElasticsearchTransport;
   import co.elastic.clients.transport.rest_client.RestClientTransport;

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.conn.ssl.NoopHostnameVerifier;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.elasticsearch.client.RestClient;

   import java.io.File;
   import java.io.FileInputStream;
   import java.io.IOException;
   import java.io.InputStream;
   import java.security.KeyManagementException;
   import java.security.KeyStore;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   public class Main {

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }

       private static ElasticsearchClient create(List<String> host, int port, String protocol, int connectTimeout,
           int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath,
           String certPassword) throws IOException {
           // Create the low-level client
           RestClient restClient = RestClient.builder(constructHttpHosts(host, port, protocol))
               .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                   .setConnectionRequestTimeout(connectionRequestTimeout)
                   .setSocketTimeout(socketTimeout))
               .setHttpClientConfigCallback(httpClientBuilder -> {
                   // enable user authentication
                   if (username != null && password != null) {
                       final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                       credentialsProvider.setCredentials(AuthScope.ANY,
                           new UsernamePasswordCredentials(username, password));
                       httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                   }
                   // set keepalive
                   httpClientBuilder.setKeepAliveStrategy(((httpResponse, httpContext) -> TimeUnit.MINUTES.toMinutes(10)));
                   // enable SSL / TLS
                   SSLContext sc = (certFilePath != null && certPassword != null) ?
                       createContextFromCaCert(certFilePath, certPassword) : createTrustAllCertsContext();

                   SSLIOSessionStrategy sslStrategy = new SSLIOSessionStrategy(sc, new NoopHostnameVerifier());
                   httpClientBuilder.setSSLStrategy(sslStrategy);

                   httpClientBuilder.setMaxConnTotal(500);
                   httpClientBuilder.setMaxConnPerRoute(300);
                   return httpClientBuilder;
               })
               .build();

           // Create the transport with a Jackson mapper
           ElasticsearchTransport transport = new RestClientTransport(restClient, new JacksonJsonpMapper());

           // And create the API client
           return new ElasticsearchClient(transport);
       }

       private static SSLContext createTrustAllCertsContext() {
           try {
               SSLContext sslContext = SSLContext.getInstance("SSL");
               sslContext.init(null, trustAllCerts, new SecureRandom());
               return sslContext;
           } catch (NoSuchAlgorithmException | KeyManagementException e) {
               throw new RuntimeException("Can not create the SSLContext", e);
           }
       }

       private static SSLContext createContextFromCaCert(String certFilePath, String certPassword) {
           try {
               // enable SSL / TLS
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
               SSLContext sc = SSLContext.getInstance("SSL", "SunJSSE");
               //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
               sc.init(null, tm, new SecureRandom());
               return sc;
           } catch (Exception e) {
               throw new RuntimeException(e);
           }
       }

       /**
        * Configure trustAllCerts to ignore the certificate configuration.
        */
       private static TrustManager[] trustAllCerts = new TrustManager[] {
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

       /**
        * Configure certificate authentication
        */
       private static class MyX509TrustManager implements X509TrustManager {
           X509TrustManager sunJSSEX509TrustManager;

           MyX509TrustManager(String certFilePath, String certPassword) throws Exception {
               File file = new File(certFilePath);
               if (!file.isFile()) {
                   throw new Exception("Wrong Certification Path");
               }
               System.out.println("Loading KeyStore " + file + "...");
               InputStream in = new FileInputStream(file);
               KeyStore ks = KeyStore.getInstance("JKS");
               ks.load(in, certPassword.toCharArray());
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
           public void checkClientTrusted(X509Certificate[] chain, String authType) {

           }

           @Override
           public void checkServerTrusted(X509Certificate[] chain, String authType) {

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
           ElasticsearchClient esClient = create(Arrays.asList("{IP address of the target cluster}"), 9200, "https", 1000, 1000, 1000, "{Username}", "{Password}", null, null);

           CreateIndexResponse indexRequest = esClient.indices()
               .create(createIndexBuilder -> createIndexBuilder.index("test"));
           boolean acknowledged = indexRequest.acknowledged();
           System.out.println("Create index successfully! " + acknowledged);

           GetIndexResponse getIndexResponse = esClient.indices().get(getIndexRequest -> getIndexRequest.index("test"));
           System.out.println("Query index successfully! \n" + getIndexResponse.toString());

           DeleteIndexResponse deleteResponse = esClient.indices()
               .delete(createIndexBuilder -> createIndexBuilder.index("test"));
           System.out.println("Delete index successfully! \n" + deleteResponse.toString());
       }
   }

.. table:: **Table 2** Variables

   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                                |
   +==========================+============================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them using a comma (,). |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                                 |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol, which can be **http** or **https**.                                                   |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                         |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                                 |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                            |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                        |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                      |
   +--------------------------+------------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000002474015994__section14782152316147:

Connecting to a Security-Mode Cluster Using the Elasticsearch Java API Client (With a Certificate)
--------------------------------------------------------------------------------------------------

Use the Elasticsearch Java API Client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000002474015994__section697213217486>`.

.. code-block::

   import co.elastic.clients.elasticsearch.ElasticsearchClient;
   import co.elastic.clients.elasticsearch.indices.CreateIndexResponse;
   import co.elastic.clients.elasticsearch.indices.DeleteIndexResponse;
   import co.elastic.clients.elasticsearch.indices.GetIndexResponse;
   import co.elastic.clients.json.jackson.JacksonJsonpMapper;
   import co.elastic.clients.transport.ElasticsearchTransport;
   import co.elastic.clients.transport.rest_client.RestClientTransport;

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.conn.ssl.NoopHostnameVerifier;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.elasticsearch.client.RestClient;

   import java.io.File;
   import java.io.FileInputStream;
   import java.io.IOException;
   import java.io.InputStream;
   import java.security.KeyManagementException;
   import java.security.KeyStore;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   public class Main {

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }

       private static ElasticsearchClient create(List<String> host, int port, String protocol, int connectTimeout,
           int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath,
           String certPassword) throws IOException {
           // Create the low-level client
           RestClient restClient = RestClient.builder(constructHttpHosts(host, port, protocol))
               .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                   .setConnectionRequestTimeout(connectionRequestTimeout)
                   .setSocketTimeout(socketTimeout))
               .setHttpClientConfigCallback(httpClientBuilder -> {
                   // enable user authentication
                   if (username != null && password != null) {
                       final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                       credentialsProvider.setCredentials(AuthScope.ANY,
                           new UsernamePasswordCredentials(username, password));
                       httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                   }
                   // set keepalive
                   httpClientBuilder.setKeepAliveStrategy(((httpResponse, httpContext) -> TimeUnit.MINUTES.toMinutes(10)));
                   // enable SSL / TLS
                   SSLContext sc = (certFilePath != null && certPassword != null) ?
                       createContextFromCaCert(certFilePath, certPassword) : createTrustAllCertsContext();

                   SSLIOSessionStrategy sslStrategy = new SSLIOSessionStrategy(sc, new NoopHostnameVerifier());
                   httpClientBuilder.setSSLStrategy(sslStrategy);

                   httpClientBuilder.setMaxConnTotal(500);
                   httpClientBuilder.setMaxConnPerRoute(300);
                   return httpClientBuilder;
               })
               .build();

           // Create the transport with a Jackson mapper
           ElasticsearchTransport transport = new RestClientTransport(restClient, new JacksonJsonpMapper());

           // And create the API client
           return new ElasticsearchClient(transport);
       }

       private static SSLContext createTrustAllCertsContext() {
           try {
               SSLContext sslContext = SSLContext.getInstance("SSL");
               sslContext.init(null, trustAllCerts, new SecureRandom());
               return sslContext;
           } catch (NoSuchAlgorithmException | KeyManagementException e) {
               throw new RuntimeException("Can not create the SSLContext", e);
           }
       }

       private static SSLContext createContextFromCaCert(String certFilePath, String certPassword) {
           try {
               // enable SSL / TLS
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
               SSLContext sc = SSLContext.getInstance("SSL", "SunJSSE");
               //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
               sc.init(null, tm, new SecureRandom());
               return sc;
           } catch (Exception e) {
               throw new RuntimeException(e);
           }
       }

       /**
        * Configure trustAllCerts to ignore the certificate configuration.
        */
       private static TrustManager[] trustAllCerts = new TrustManager[] {
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

       /**
        * Configure certificate authentication
        */
       private static class MyX509TrustManager implements X509TrustManager {
           X509TrustManager sunJSSEX509TrustManager;

           MyX509TrustManager(String certFilePath, String certPassword) throws Exception {
               File file = new File(certFilePath);
               if (!file.isFile()) {
                   throw new Exception("Wrong Certification Path");
               }
               System.out.println("Loading KeyStore " + file + "...");
               InputStream in = new FileInputStream(file);
               KeyStore ks = KeyStore.getInstance("JKS");
               ks.load(in, certPassword.toCharArray());
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
           public void checkClientTrusted(X509Certificate[] chain, String authType) {

           }

           @Override
           public void checkServerTrusted(X509Certificate[] chain, String authType) {

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
           ElasticsearchClient esClient = create(Arrays.asList("{IP address of the target cluster}"), 9200, "https", 1000, 1000, 1000, "{Username}", "{Password}", "{Certificate path}", "{Certificate password}")

           CreateIndexResponse indexRequest = esClient.indices()
               .create(createIndexBuilder -> createIndexBuilder.index("test"));
           boolean acknowledged = indexRequest.acknowledged();
           System.out.println("Create index successfully! " + acknowledged);

           GetIndexResponse getIndexResponse = esClient.indices().get(getIndexRequest -> getIndexRequest.index("test"));
           System.out.println("Query index successfully! \n" + getIndexResponse.toString());

           DeleteIndexResponse deleteResponse = esClient.indices()
               .delete(createIndexBuilder -> createIndexBuilder.index("test"));
           System.out.println("Delete index successfully! \n" + deleteResponse.toString());
       }
   }

.. table:: **Table 3** Function parameters

   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                                |
   +==========================+============================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them using a comma (,). |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                                 |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol. Set this parameter to **https**.                                                      |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                         |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                                 |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                            |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                        |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                      |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | certFilePath             | Path for storing the security certificate.                                                                 |
   +--------------------------+------------------------------------------------------------------------------------------------------------+
   | certPassword             | Password of the security certificate.                                                                      |
   +--------------------------+------------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000002474015994__section697213217486:

Obtaining and Uploading a Security Certificate
----------------------------------------------

To access a security-mode OpenSearch cluster that uses HTTPS, a security certificate must be loaded. Perform the following steps to obtain the security certificate and upload it to the client:

#. Obtain the security certificate **CloudSearchService.cer**.

   a. Log in to the CSS management console.
   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.
   c. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
   d. Click the **Overview** tab. In the **Network Information** area, click **Download Certificate** below **HTTPS Access**.

#. Convert the security certificate **CloudSearchService.cer**. Upload the downloaded security certificate to the client and use keytool to convert the **.cer** certificate into a **.jks** certificate that can be read by Java.

   -  In Linux, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

   -  In Windows, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore .\truststore.jks -file .\CloudSearchService.cer

   In the preceding command, *newname* indicates the user-defined certificate name.

   After this command is executed, you will be prompted to set the certificate password and confirm the password. Securely store the password. It will be used for accessing the cluster.

FAQ: How Do I Increase the Number of Client Connections to Handle High Concurrency?
-----------------------------------------------------------------------------------

When using the Elasticsearch Java API Client, the default maximum number of client connections may become insufficient under high concurrency, leading to request delays or failures.

To address this, you can increase the connection limit by customizing HttpClientConfigCallback during client initialization. This involves injecting an HttpClientBuilder to increase the maximum number of client connections supported, thereby improving the cluster's ability to handle concurrent requests.

Configuration example:

.. code-block::

   // Set the maximum number of total connections to 500. (Set this parameter based on the typical concurrency the cluster handles.)
   httpClientBuilder.setMaxConnTotal(500);
   //Set the maximum number of connections per route to 300. You are advised to set this value to approximately 60% of the total client connection limit.
   httpClientBuilder.setMaxConnPerRoute(300);
