:original_name: css_01_0037.html

.. _css_01_0037:

Accessing an OpenSearch Cluster Using the Low Level REST Client
===============================================================

You can query and manage data in a CSS OpenSearch cluster using the Low Level REST Client. The Low Level REST Client encapsulates OpenSearch APIs. You only need to construct the required structures to access an OpenSearch cluster. This simplifies the process of working with an OpenSearch cluster. The Low Level REST Client allows you to customize the request structure, which is more flexible and supports all the request formats of OpenSearch, such as GET, POST, DELETE, and HEAD.

You can access an OpenSearch cluster with the Low Level REST Client using either of the following ways: directly creating the Low Level REST Client; or creating the High Level REST Client first and then calling **RestHighLevelClient.getLowLevelClient()** to obtain the Low Level REST Client.

Prerequisites
-------------

-  The target OpenSearch cluster is available.
-  The server that runs the Java code can communicate with the OpenSearch cluster.
-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Network Configuration <en-us_topic_0000001992165561__en-us_topic_0000001975823337_section855085010198>`.
-  Java has been installed on the server and the JDK version is 11 or later. Download JDK 11 from `Java Archive Downloads <https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html>`__.

Introducing Dependencies
------------------------

Introduce the required Java dependencies on the server where you run Java code.

CSS allows you to use the Elasticsearch 7.10 Java client to connect to OpenSearch clusters. To ensure better compatibility, however, you are advised to use an OpenSearch Java client that has the same version as the target OpenSearch cluster.

Select a reference example based on the Java client you use.

-  Scenario 1 (recommended): Use the OpenSearch Java client to access the OpenSearch cluster and introduce the Apache version using Maven.

   Replace 1.3.6 with the actual Java client version.

   .. code-block::

      <dependency>
          <groupId>org.opensearch.client</groupId>
          <artifactId>opensearch-rest-high-level-client</artifactId>
          <version>1.3.6</version>
      </dependency>

-  Scenario 2: Use the Elasticsearch 7.10.2 Java client to access the OpenSearch cluster and introduce the Apache version using Maven.

   .. code-block::

      <dependency>
          <groupId>org.elasticsearch.client</groupId>
          <artifactId>elasticsearch-rest-client</artifactId>
          <version>7.10.2</version>
      </dependency>
      <dependency>
          <groupId>org.elasticsearch</groupId>
          <artifactId>elasticsearch</artifactId>
          <version>7.10.2</version>
      </dependency>

Accessing a Cluster
-------------------

The sample code varies depending on the Java client and the security mode settings of the target OpenSearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Java Client          | How Low Level REST Client Is Created                                                                          | OpenSearch Cluster Security-Mode Settings | Security Certificate | Details                                                                                                                                                                  |
   +======================+===============================================================================================================+===========================================+======================+==========================================================================================================================================================================+
   | OpenSearch           | Directly create the Low Level REST Client                                                                     | Non-security mode                         | ``-``                | :ref:`Connecting to a Non-Security Mode Cluster Using the OpenSearch Low Level REST Client <en-us_topic_0000001992165569__section4687369363>`                            |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTP                      | No                   | :ref:`Connecting to a Security-Mode Cluster Using the OpenSearch Low Level REST Client (Without a Certificate) <en-us_topic_0000001992165569__section2602143193915>`     |
   |                      |                                                                                                               |                                           |                      |                                                                                                                                                                          |
   |                      |                                                                                                               | Security mode + HTTPS                     |                      |                                                                                                                                                                          |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTPS                     | Yes                  | :ref:`Connecting to a Security-Mode Cluster Using the OpenSearch Low Level REST Client (With a Certificate) <en-us_topic_0000001992165569__section1912544916395>`        |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      | Create the High Level REST Client first and then call getLowLevelClient() to obtain the Low Level REST Client | Non-security mode                         | ``-``                | :ref:`Connecting to a Non-Security Mode Cluster Using the OpenSearch High Level REST Client <en-us_topic_0000001992165569__section111701281216>`                         |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTP                      | No                   | :ref:`Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (Without a Certificate) <en-us_topic_0000001992165569__section138179151553>`     |
   |                      |                                                                                                               |                                           |                      |                                                                                                                                                                          |
   |                      |                                                                                                               | Security mode + HTTPS                     |                      |                                                                                                                                                                          |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTPS                     | Yes                  | :ref:`Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (With a Certificate) <en-us_topic_0000001992165569__section14343162220160>`      |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch 7.10.2 | Directly create the Low Level REST Client                                                                     | Non-security mode                         | ``-``                | :ref:`Connecting to a Non-Security Mode Cluster Using the Elasticsearch Low Level REST Client <en-us_topic_0000001992165569__section215365104713>`                       |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTP                      | No                   | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch Low Level REST Client (Without a Certificate) <en-us_topic_0000001992165569__section361711128499>`   |
   |                      |                                                                                                               |                                           |                      |                                                                                                                                                                          |
   |                      |                                                                                                               | Security mode + HTTPS                     |                      |                                                                                                                                                                          |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTPS                     | Yes                  | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch Low Level REST Client (With a Certificate) <en-us_topic_0000001992165569__section16431305115>`       |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      | Create the High Level REST Client first and then call getLowLevelClient() to obtain the Low Level REST Client | Non-security mode                         | ``-``                | :ref:`Connecting to a Non-Security Mode Cluster Using the Elasticsearch High Level REST Client <en-us_topic_0000001992165569__section17497851185216>`                    |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTP                      | No                   | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (Without a Certificate) <en-us_topic_0000001992165569__section1988811319545>` |
   |                      |                                                                                                               |                                           |                      |                                                                                                                                                                          |
   |                      |                                                                                                               | Security mode + HTTPS                     |                      |                                                                                                                                                                          |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                      |                                                                                                               | Security mode + HTTPS                     | Yes                  | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (With a Certificate) <en-us_topic_0000001992165569__section129618451566>`     |
   +----------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001992165569__section4687369363:

Connecting to a Non-Security Mode Cluster Using the OpenSearch Low Level REST Client
------------------------------------------------------------------------------------

Use the OpenSearch Low Level REST Client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.opensearch.client.Request;
   import org.opensearch.client.Response;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;

   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;
   public class RestLowLevelClientExample {
       public static void main(String[] args) throws IOException {
       List<String> host = Arrays.asList("{Cluster access address}");
           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, 9200, "http"));
           /**
            *Create the Low Level Rest Client.
            */
           RestClient lowLevelClient = builder.build();
           /**
            * Check whether the test index exists. If the index exists, 200 is returned. If the index does not exist, 404 is returned.
            */
           Request request = new Request("HEAD", "/test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }
   }

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section2602143193915:

Connecting to a Security-Mode Cluster Using the OpenSearch Low Level REST Client (Without a Certificate)
--------------------------------------------------------------------------------------------------------

Use the OpenSearch Low Level REST Client to connect to a security-mode OpenSearch cluster (HTTP or HTTPS) without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.apache.http.HttpResponse;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.impl.client.DefaultConnectionKeepAliveStrategy;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.apache.http.protocol.HttpContext;
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   import org.opensearch.client.Request;
   import org.opensearch.client.Response;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.common.Nullable;
   import java.io.IOException;
   import java.security.KeyManagementException;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.Objects;
   import java.util.concurrent.TimeUnit;
   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManager;import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {
       /**
        * Create a class for the client. Define the create function.
        */
       public static RestClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout,  String username, String password) throws IOException {
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
           final RestClient client = builder.build();
           logger.info("opensearch rest client build success {} ", client);
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

       /**
   * The CustomConnectionKeepAliveStrategy function is used to set the connection keepalive during when there are a large number of short connections or when there are not many data requests.
        */
       public static class CustomConnectionKeepAliveStrategy extends DefaultConnectionKeepAliveStrategy {
           public static final CustomConnectionKeepAliveStrategy INSTANCE = new CustomConnectionKeepAliveStrategy();

           private CustomConnectionKeepAliveStrategy() {
               super();
           }

           /**
            * Maximum keepalive time (in minutes)
            * The default value is 10 minutes. You can set it based on the number of TCP connections in TIME_WAIT state. If there are too many TCP connections, you can increase this value.
            */
           private final long MAX_KEEP_ALIVE_MINUTES = 10;

           @Override
           public long getKeepAliveDuration(HttpResponse response, HttpContext context) {
               long keepAliveDuration = super.getKeepAliveDuration(response, context);
               // <0 indicates that the keepalive period is unlimited.
               // Change the period from unlimited to a default period.
               if (keepAliveDuration < 0) {
                   return TimeUnit.MINUTES.toMillis(MAX_KEEP_ALIVE_MINUTES);
               }
               return keepAliveDuration;
           }
       }

       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

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
        * The following is an example of the main function. Call the create function to create a Low Level REST Client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestClient lowLevelClient = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "http", 30000, 30000, 30000, "username", "password");
           Request request = new Request("HEAD", "/test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 2** Variables

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol, which can be **http** or **https**.                                                 |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section1912544916395:

Connecting to a Security-Mode Cluster Using the OpenSearch Low Level REST Client (With a Certificate)
-----------------------------------------------------------------------------------------------------

Use the OpenSearch Low Level REST Client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000001992165569__section697213217486>`.

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
   import org.opensearch.client.Request;
   import org.opensearch.client.Response;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.common.Nullable;

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

   import javax.net.ssl.SSLContext;import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {

       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath, String certPassword) throws IOException {
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
           SSLContext sc = null;
           try {
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
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
           final RestClient client = builder.build();
           logger.info("opensearch rest client build success {} ", client);
           return client;
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);}

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
           }}

       public static class MyX509TrustManager implements X509TrustManager {
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
        * The following is an example of the main function. Call the create function to create a Low Level REST Client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestClient lowLevelClient = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 30000, 30000, 30000, "username", "password", "certFilePath", "certPassword");
           Request request = new Request("HEAD", "test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 3** Function parameters

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol. Set this parameter to **https**.                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certFilePath             | Path for storing the security certificate.                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certPassword             | Password of the security certificate.                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section111701281216:

Connecting to a Non-Security Mode Cluster Using the OpenSearch High Level REST Client
-------------------------------------------------------------------------------------

Use the OpenSearch High Level REST Client to obtain the Low Level REST Client by calling **getLowLevelClient()**, use the low-level client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.opensearch.client.Request;
   import org.opensearch.client.Response;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.client.RestHighLevelClient;

   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;
   public class RestLowLevelClientExample {

       public static void main(String[] args) throws IOException {
       List<String> host = Arrays.asList("{Cluster access address}");
           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, 9200, "http"));
           final RestHighLevelClient restHighLevelClient = new RestHighLevelClient(builder);
           /**
            * Create a high-level client and then call getLowLevelClient() to obtain a low-level client. The code differs from the client creation code only in the following line:
            */
           final RestClient lowLevelClient = restHighLevelClient.getLowLevelClient();
           /**
            * Check whether the test index exists. If the index exists, 200 is returned. If the index does not exist, 404 is returned.
            */
           Request request = new Request("HEAD", "/test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }
   }

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section138179151553:

Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (Without a Certificate)
---------------------------------------------------------------------------------------------------------

Use the OpenSearch High Level REST Client to obtain the Low Level REST Client by calling **getLowLevelClient()**, use the low-level client to connect to a security-mode OpenSearch cluster that uses HTTP or HTTPS without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.apache.http.HttpResponse;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.impl.client.DefaultConnectionKeepAliveStrategy;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.apache.http.protocol.HttpContext;
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   import org.opensearch.client.Request;
   import org.opensearch.client.Response;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.client.RestHighLevelClient;
   import org.opensearch.common.Nullable;

   import java.io.IOException;
   import java.security.KeyManagementException;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.Objects;
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManager;import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout,  String username, String password) throws IOException {

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
           logger.info("opensearch rest client build success {} ", client);
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

       /**
   * The CustomConnectionKeepAliveStrategy function is used to set the connection keepalive during when there are a large number of short connections or when there are not many data requests.
        */
       public static class CustomConnectionKeepAliveStrategy extends DefaultConnectionKeepAliveStrategy {
           public static final CustomConnectionKeepAliveStrategy INSTANCE = new CustomConnectionKeepAliveStrategy();

           private CustomConnectionKeepAliveStrategy() {
               super();
           }

           /**
            * Maximum keepalive time (in minutes)
            * The default value is 10 minutes. You can set it based on the number of TCP connections in TIME_WAIT state. If there are too many TCP connections, you can increase this value.
            */
           private final long MAX_KEEP_ALIVE_MINUTES = 10;

           @Override
           public long getKeepAliveDuration(HttpResponse response, HttpContext context) {
               long keepAliveDuration = super.getKeepAliveDuration(response, context);
               // <0 indicates an unlimited keepalive period.
               // Change the period from unlimited to a default period.
               if (keepAliveDuration < 0) {
                   return TimeUnit.MINUTES.toMillis(MAX_KEEP_ALIVE_MINUTES);
               }
               return keepAliveDuration;
           }
       }

       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

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
   * The following is an example of the main function. Call the create function to create the high-level client, then call the getLowLevelClient() function to obtain the low-level client, and query whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "http", 30000, 30000, 30000, "username", "password");
           RestClient lowLevelClient = client.getLowLevelClient();
           Request request = new Request("HEAD", "test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 4** Variables

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol, which can be **http** or **https**.                                                 |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section14343162220160:

Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (With a Certificate)
------------------------------------------------------------------------------------------------------

Use the OpenSearch High Level REST Client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000001992165569__section697213217486>`.

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
   import org.opensearch.action.admin.cluster.health.ClusterHealthRequest;
   import org.opensearch.action.admin.cluster.health.ClusterHealthResponse;
   import org.opensearch.client.Request;
   import org.opensearch.client.RequestOptions;
   import org.opensearch.client.Response;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.client.RestHighLevelClient;
   import org.opensearch.common.Nullable;
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

   public class RestLowLevelClientExample {
       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath, String certPassword) throws IOException {
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
           SSLContext sc = null;
           try {
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
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
           logger.info("opensearch rest client build success {} ", client);

           ClusterHealthRequest request = new ClusterHealthRequest();
           ClusterHealthResponse response = client.cluster().health(request, RequestOptions.DEFAULT);
           logger.info("opensearch rest client health response {} ", response);
           return client;
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);}

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
           }}

       public static class MyX509TrustManager implements X509TrustManager {
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
   * The following is an example of the main function. Call the create function to create the high-level client, then call the getLowLevelClient() function to obtain the low-level client, and query whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 30000, 30000, 30000, "username", "password", "certFilePath", "certPassword");
           RestClient lowLevelClient = client.getLowLevelClient();
           Request request = new Request("HEAD", "test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 5** Function parameters

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol. Set this parameter to **https**.                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certFilePath             | Path for storing the security certificate.                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certPassword             | Password of the security certificate.                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section215365104713:

Connecting to a Non-Security Mode Cluster Using the Elasticsearch Low Level REST Client
---------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 Low Level REST Client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;

   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;
   public class RestLowLevelClientExample {
       public static void main(String[] args) throws IOException {
       List<String> host = Arrays.asList("{Cluster access address}");
           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, 9200, "http"));
           /**
            *Create the Low Level Rest Client.
            */
           RestClient lowLevelClient = builder.build();
           /**
            * Check whether the test index exists. If the index exists, 200 is returned. If the index does not exist, 404 is returned.
            */
           Request request = new Request("HEAD", "/test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }
   }

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section361711128499:

Connecting to a Security-Mode Cluster Using the Elasticsearch Low Level REST Client (Without a Certificate)
-----------------------------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 Low Level REST Client to connect to a security-mode OpenSearch cluster (HTTP or HTTPS) without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.apache.http.HttpResponse;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.impl.client.DefaultConnectionKeepAliveStrategy;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.apache.http.protocol.HttpContext;
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
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
   import java.util.concurrent.TimeUnit;
   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManager;import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {
       /**
        * Create a class for the client. Define the create function.
        */
       public static RestClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout,  String username, String password) throws IOException {
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
           final RestClient client = builder.build();
           logger.info("es rest client build success {} ", client);
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

       /**
   * The CustomConnectionKeepAliveStrategy function is used to set the connection keepalive during when there are a large number of short connections or when there are not many data requests.
        */
       public static class CustomConnectionKeepAliveStrategy extends DefaultConnectionKeepAliveStrategy {
           public static final CustomConnectionKeepAliveStrategy INSTANCE = new CustomConnectionKeepAliveStrategy();

           private CustomConnectionKeepAliveStrategy() {
               super();
           }

           /**
            * Maximum keepalive time (in minutes)
            * The default value is 10 minutes. You can set it based on the number of TCP connections in TIME_WAIT state. If there are too many TCP connections, you can increase this value.
            */
           private final long MAX_KEEP_ALIVE_MINUTES = 10;

           @Override
           public long getKeepAliveDuration(HttpResponse response, HttpContext context) {
               long keepAliveDuration = super.getKeepAliveDuration(response, context);
               // <0 indicates an unlimited keepalive period.
               // Change the period from unlimited to a default period.
               if (keepAliveDuration < 0) {
                   return TimeUnit.MINUTES.toMillis(MAX_KEEP_ALIVE_MINUTES);
               }
               return keepAliveDuration;
           }
       }

       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

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
        * The following is an example of the main function. Call the create function to create a Low Level REST Client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestClient lowLevelClient = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "http", 30000, 30000, 30000, "username", "password");
           Request request = new Request("HEAD", "/test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 6** Variables

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol, which can be **http** or **https**.                                                 |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section16431305115:

Connecting to a Security-Mode Cluster Using the Elasticsearch Low Level REST Client (With a Certificate)
--------------------------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 Low Level REST Client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000001992165569__section697213217486>`.

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
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
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

   import javax.net.ssl.SSLContext;import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {

       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath, String certPassword) throws IOException {
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
           SSLContext sc = null;
           try {
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
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
           final RestClient client = builder.build();
           logger.info("es rest client build success {} ", client);
           return client;
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);}

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
           }}

       public static class MyX509TrustManager implements X509TrustManager {
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
        * The following is an example of the main function. Call the create function to create a Low Level REST Client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestClient lowLevelClient = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 30000, 30000, 30000, "username", "password", "certFilePath", "certPassword");
           Request request = new Request("HEAD", "test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 7** Function parameters

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol. Set this parameter to **https**.                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certFilePath             | Path for storing the security certificate.                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certPassword             | Password of the security certificate.                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section17497851185216:

Connecting to a Non-Security Mode Cluster Using the Elasticsearch High Level REST Client
----------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 High Level REST Client obtain the Low Level REST Client by calling **getLowLevelClient()**, use the low-level client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;

   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;
   public class RestLowLevelClientExample {

       public static void main(String[] args) throws IOException {
       List<String> host = Arrays.asList("{Cluster access address}");
           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, 9200, "http"));
           final RestHighLevelClient restHighLevelClient = new RestHighLevelClient(builder);
           /**
            * Create a high-level client and then call getLowLevelClient() to obtain a low-level client. The code differs from the client creation code only in the following line:
            */
           final RestClient lowLevelClient = restHighLevelClient.getLowLevelClient();
           /**
            * Check whether the test index exists. If the index exists, 200 is returned. If the index does not exist, 404 is returned.
            */
           Request request = new Request("HEAD", "/test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }

       /**
        * Use the constructHttpHosts function to convert the node IP address list of the host cluster.
        */
       public static HttpHost[] constructHttpHosts(List<String> host, int port, String protocol) {
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);
       }
   }

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section1988811319545:

Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (Without a Certificate)
------------------------------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 High Level REST Client to obtain the Low Level REST Client by calling **getLowLevelClient()**, use the low-level client to connect to a security-mode OpenSearch cluster that uses HTTP or HTTPS without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.apache.http.HttpResponse;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.impl.client.DefaultConnectionKeepAliveStrategy;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.apache.http.protocol.HttpContext;
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
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
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManager;import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout,  String username, String password) throws IOException {

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

       /**
   * The CustomConnectionKeepAliveStrategy function is used to set the connection keepalive during when there are a large number of short connections or when there are not many data requests.
        */
       public static class CustomConnectionKeepAliveStrategy extends DefaultConnectionKeepAliveStrategy {
           public static final CustomConnectionKeepAliveStrategy INSTANCE = new CustomConnectionKeepAliveStrategy();

           private CustomConnectionKeepAliveStrategy() {
               super();
           }

           /**
            * Maximum keepalive time (in minutes)
            * The default value is 10 minutes. You can set it based on the number of TCP connections in TIME_WAIT state. If there are too many TCP connections, you can increase this value.
            */
           private final long MAX_KEEP_ALIVE_MINUTES = 10;

           @Override
           public long getKeepAliveDuration(HttpResponse response, HttpContext context) {
               long keepAliveDuration = super.getKeepAliveDuration(response, context);
               // <0 indicates an unlimited keepalive period.
               // Change the period from unlimited to a default period.
               if (keepAliveDuration < 0) {
                   return TimeUnit.MINUTES.toMillis(MAX_KEEP_ALIVE_MINUTES);
               }
               return keepAliveDuration;
           }
       }

       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

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
   * The following is an example of the main function. Call the create function to create the high-level client, then call the getLowLevelClient() function to obtain the low-level client, and query whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "http", 30000, 30000, 30000, "username", "password");
           RestClient lowLevelClient = client.getLowLevelClient();
           Request request = new Request("HEAD", "test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 8** Variables

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol, which can be **http** or **https**.                                                 |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section129618451566:

Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (With a Certificate)
---------------------------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 High Level REST Client to obtain the Low Level REST Client by calling **getLowLevelClient()**, use the low-level client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000001992165569__section697213217486>`.

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
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.RequestOptions;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
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

   import javax.net.ssl.SSLContext;import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   public class RestLowLevelClientExample {
       private static final Logger logger = LogManager.getLogger(RestLowLevelClientExample.class);

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath, String certPassword) throws IOException {
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
           SSLContext sc = null;
           try {
               TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
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
           return host.stream().map(p -> new HttpHost(p, port, protocol)).toArray(HttpHost[]::new);}

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
           }}

       public static class MyX509TrustManager implements X509TrustManager {
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
   * The following is an example of the main function. Call the create function to create the high-level client, then call the getLowLevelClient() function to obtain the low-level client, and query whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 30000, 30000, 30000, "username", "password", "certFilePath", "certPassword");
           RestClient lowLevelClient = client.getLowLevelClient();
           Request request = new Request("HEAD", "test");
           Response response = lowLevelClient.performRequest(request);
           System.out.println(response.getStatusLine().getStatusCode());
           lowLevelClient.close();
       }
   }

.. table:: **Table 9** Function parameters

   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter                | Description                                                                                              |
   +==========================+==========================================================================================================+
   | host                     | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | port                     | Access port of the cluster. The default value is **9200**.                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | protocol                 | Connection protocol. Set this parameter to **https**.                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectTimeout           | Socket connection timeout (in ms).                                                                       |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | connectionRequestTimeout | Socket connection request timeout (in ms).                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | socketTimeout            | Socket request timeout (in ms).                                                                          |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | username                 | Username for accessing the cluster.                                                                      |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | password                 | Password of the user.                                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certFilePath             | Path for storing the security certificate.                                                               |
   +--------------------------+----------------------------------------------------------------------------------------------------------+
   | certPassword             | Password of the security certificate.                                                                    |
   +--------------------------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **200** (the index exists) or **404** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165569__section697213217486:

Obtaining and Uploading a Security Certificate
----------------------------------------------

To access a security-mode OpenSearch cluster that uses HTTPS, a security certificate must be loaded. Perform the following steps to obtain the security certificate and upload it to the client:

#. Obtain the security certificate **CloudSearchService.cer**.

   a. Log in to the CSS management console.
   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.
   c. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
   d. Click the **Overview** tab. In the **Configuration** area, click **Download Certificate** next to **HTTPS Access**.

#. Convert the security certificate **CloudSearchService.cer**. Upload the downloaded security certificate to the client and use keytool to convert the **.cer** certificate into a **.jks** certificate that can be read by Java.

   -  In Linux, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

   -  In Windows, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore .\truststore.jks -file .\CloudSearchService.cer

   In the preceding command, *newname* indicates the user-defined certificate name.

   After this command is executed, you will be prompted to set the certificate password and confirm the password. Securely store the password. It will be used for accessing the cluster.
