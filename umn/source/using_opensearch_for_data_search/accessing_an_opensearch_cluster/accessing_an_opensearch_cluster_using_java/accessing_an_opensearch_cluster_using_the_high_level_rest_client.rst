:original_name: css_01_0032.html

.. _css_01_0032:

Accessing an OpenSearch Cluster Using the High Level REST Client
================================================================

You can query and manage data in a CSS OpenSearch cluster using the High Level REST Client. The High Level REST Client encapsulates OpenSearch APIs. You only need to construct the required structures to access an OpenSearch cluster. This simplifies the process of working with an OpenSearch cluster. For details about how to use the REST Client, see `Java high-level REST client <https://docs.opensearch.org/latest/clients/java-rest-high-level/>`__.

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

If your High Level REST Client version is later than the OpenSearch cluster version and there are incompatibility issues with some requests, you can use **RestHighLevelClient.getLowLevelClient()** to obtain the Low Level REST Client and customize OpenSearch requests. For details, see :ref:`Accessing an OpenSearch Cluster Using the Low Level REST Client <css_01_0037>`.

Select a reference example based on the Java client you use.

Scenario 1 (recommended): Use the OpenSearch Java client to access an OpenSearch cluster and introduce dependencies.

-  Maven:

   Replace 1.3.6 with the actual Java client version.

   .. code-block::

      <dependency>
          <groupId>org.opensearch.client</groupId>
          <artifactId>opensearch-rest-high-level-client</artifactId>
          <version>1.3.6</version>
      </dependency>

-  Gradle:

   Replace 1.3.6 with the actual Java client version.

   .. code-block::

      compile group: 'org.opensearch.client', name: 'opensearch-rest-high-level-client', version: '1.3.6'

Scenario 2: Use the Elasticsearch 7.10.2 Java client to access an OpenSearch cluster and introduce dependencies.

-  Maven:

   .. code-block::

      <dependency>
          <groupId>org.elasticsearch.client</groupId>
          <artifactId>elasticsearch-rest-high-level-client</artifactId>
          <version>7.10.2</version>
      </dependency>
      <dependency>
          <groupId>org.elasticsearch</groupId>
          <artifactId>elasticsearch</artifactId>
          <version>7.10.2</version>
      </dependency>

-  Gradle:

   .. code-block::

      compile group: 'org.elasticsearch.client', name: 'elasticsearch-rest-high-level-client', version: '7.10.2'

Accessing a Cluster
-------------------

The sample code varies depending on the Java client and the security mode settings of the target OpenSearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Java Client          | OpenSearch Cluster Security-Mode Settings | Security Certificate | Details                                                                                                                                                                                                                         |
   +======================+===========================================+======================+=================================================================================================================================================================================================================================+
   | OpenSearch           | Non-security mode                         | ``-``                | :ref:`Connecting to a Non-Security Mode Cluster Using the OpenSearch High Level REST Client <en-us_topic_0000001992205773__en-us_topic_0000001972375889_en-us_topic_0000001961178813_section197550282614>`                      |
   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | OpenSearch           | Security mode + HTTP                      | No                   | :ref:`Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (Without a Certificate) <en-us_topic_0000001992205773__en-us_topic_0000001972375889_en-us_topic_0000001961178813_section1523020817518>` |
   |                      |                                           |                      |                                                                                                                                                                                                                                 |
   |                      | Security mode + HTTPS                     |                      |                                                                                                                                                                                                                                 |
   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | OpenSearch           | Security mode + HTTPS                     | Yes                  | :ref:`Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (With a Certificate) <en-us_topic_0000001992205773__en-us_topic_0000001972375889_en-us_topic_0000001961178813_section1368184211106>`    |
   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch 7.10.2 | Non-security mode                         | ``-``                | :ref:`Connecting to a Non-Security Mode Cluster Using the Elasticsearch High Level REST Client <en-us_topic_0000001992205773__section343422304117>`                                                                             |
   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch 7.10.2 | Security mode + HTTP                      | No                   | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (Without a Certificate) <en-us_topic_0000001992205773__section181651279516>`                                                         |
   |                      |                                           |                      |                                                                                                                                                                                                                                 |
   |                      | Security mode + HTTPS                     |                      |                                                                                                                                                                                                                                 |
   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch 7.10.2 | Security mode + HTTPS                     | Yes                  | :ref:`Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (With a Certificate) <en-us_topic_0000001992205773__section1375923212719>`                                                           |
   +----------------------+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001992205773__en-us_topic_0000001972375889_en-us_topic_0000001961178813_section197550282614:

Connecting to a Non-Security Mode Cluster Using the OpenSearch High Level REST Client
-------------------------------------------------------------------------------------

Use the OpenSearch High Level REST Client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.opensearch.client.RequestOptions;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.client.RestHighLevelClient;
   import org.opensearch.client.indices.GetIndexRequest;
   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;
   public class RestHighLevelClientExample {
       public static void main(String[] args) throws IOException {
       List<String> host = Arrays.asList("{Cluster access address}");
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

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992205773__en-us_topic_0000001972375889_en-us_topic_0000001961178813_section1523020817518:

Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (Without a Certificate)
---------------------------------------------------------------------------------------------------------

Use the OpenSearch High Level REST Client to connect to a security-mode OpenSearch cluster (HTTP or HTTPS) without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   import org.opensearch.action.admin.cluster.health.ClusterHealthRequest;
   import org.opensearch.action.admin.cluster.health.ClusterHealthResponse;
   import org.opensearch.client.RequestOptions;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.client.RestHighLevelClient;
   import org.opensearch.client.indices.GetIndexRequest;
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
   import javax.net.ssl.HostnameVerifier;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLSession;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.X509TrustManager;
   /**
    *Connect to a security-model cluster using the High Level REST Client (without a certificate).
    */
   public class RestHighLevelClientExample {
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

       private static final Logger logger = LogManager.getLogger(RestHighLevelClientExampleHttpWithSecurityNoCert.class);

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
           RestHighLevelClient client = create(Arrays.asList("{host}"), 9200, "https", 30000, 30000, 30000,  "username", "password");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
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

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992205773__en-us_topic_0000001972375889_en-us_topic_0000001961178813_section1368184211106:

Connecting to a Security-Mode Cluster Using the OpenSearch High Level REST Client (With a Certificate)
------------------------------------------------------------------------------------------------------

Use the OpenSearch High Level REST Client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000001992205773__section697213217486>`.

.. code-block::

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
   import org.opensearch.client.RequestOptions;
   import org.opensearch.client.RestClient;
   import org.opensearch.client.RestClientBuilder;
   import org.opensearch.client.RestHighLevelClient;
   import org.opensearch.client.indices.GetIndexRequest;
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
   /**
    * Use Hive Level REST Client to connect to a security-mode cluster (with an HTTPS certificate).
    */
   public class RestHighLevelClientExample {
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath,
           String certPassword) throws IOException {

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

       private static final Logger logger = LogManager.getLogger(RestHighLevelClient.class);

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
        * The following is an example of the main function. Call the create function to create a client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("{host}"), 9200, "https", 30000, 30000, 30000, "username", "password", "certFilePath", "certPassword");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
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

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992205773__section343422304117:

Connecting to a Non-Security Mode Cluster Using the Elasticsearch High Level REST Client
----------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 High Level REST Client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

   import org.apache.http.HttpHost;
   import org.elasticsearch.client.RequestOptions;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
   import org.elasticsearch.client.indices.GetIndexRequest;
   import java.io.IOException;
   import java.util.Arrays;
   import java.util.List;
   public class RestHighLevelClientExample {
       public static void main(String[] args) throws IOException {
       List<String> host = Arrays.asList("{Cluster access address}");
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

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992205773__section181651279516:

Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (Without a Certificate)
------------------------------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 High Level REST Client to connect to a security-mode OpenSearch cluster (HTTP or HTTPS) without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

.. code-block::

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
    *Connect to a security-model cluster using the High Level REST Client (without a certificate).
    */
   public class RestHighLevelClientExample {
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

       private static final Logger logger = LogManager.getLogger(RestHighLevelClientExampleHttpWithSecurityNoCert.class);

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
           RestHighLevelClient client = create(Arrays.asList("{host}"), 9200, "https", 30000, 30000, 30000,  "username", "password");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
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

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992205773__section1375923212719:

Connecting to a Security-Mode Cluster Using the Elasticsearch High Level REST Client (With a Certificate)
---------------------------------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 High Level REST Client to connect to a security-mode OpenSearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000001992205773__section697213217486>`.

.. code-block::

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
    * Use Hive Level REST Client to connect to a security-mode cluster (with an HTTPS certificate).
    */
   public class RestHighLevelClientExample {
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath,
           String certPassword) throws IOException {

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

       private static final Logger logger = LogManager.getLogger(RestHighLevelClient.class);

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
        * The following is an example of the main function. Call the create function to create a client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("{host}"), 9200, "https", 30000, 30000, 30000, "username", "password", "certFilePath", "certPassword");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
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

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992205773__section697213217486:

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
