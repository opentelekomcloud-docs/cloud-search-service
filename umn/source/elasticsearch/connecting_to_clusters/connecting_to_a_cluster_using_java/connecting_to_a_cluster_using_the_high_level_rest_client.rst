:original_name: css_01_0065.html

.. _css_01_0065:

Connecting to a Cluster Using the High Level REST Client
========================================================

Working directly with Elasticsearch's diverse APIs can be complex and inefficient. CSS simplifies this by providing a High Level REST Client, offering a more efficient way for querying and managing your data. The High Level REST Client encapsulates Elasticsearch APIs. You only need to construct the required request structures to access an Elasticsearch cluster. This simplifies the process of working with Elasticsearch clusters, as well as the development process. For details about how to use the REST Client, see `Java High Level REST Client <https://www.elastic.co/guide/en/elasticsearch/client/java-rest/current/java-rest-high.html>`__.

Prerequisites
-------------

-  The target Elasticsearch cluster is available.

-  The server that runs the Java code can communicate with the Elasticsearch cluster.

-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Obtaining the Cluster Access Address <en-us_topic_0000001975823337__section855085010198>`.

-  Java has been installed on the server and the JDK version is 1.8 or later. Download JDK 1.8 from `Java Downloads <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__.

-  The High Level REST Client version has been confirmed. CSS allows you to connect to an Elasticsearch cluster using a Java client that has a later version. To ensure better compatibility, however, you are advised to use a Java client that has the same version as the target Elasticsearch cluster.

   If your High Level REST Client version is later than the Elasticsearch cluster version and there are incompatibility issues with some requests, you can use **RestHighLevelClient.getLowLevelClient()** to obtain the Low Level REST Client and customize Elasticsearch requests. For details, see :ref:`Connecting to a Cluster Using the Low Level REST Client <css_01_0066>`.

Introducing Dependencies
------------------------

Import Java dependencies on the server that runs the Java code using either of the following ways:

-  Maven:

   Replace 7.10.2 with the actual Java client version.

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

   Replace 7.10.2 with the actual Java client version.

   .. code-block::

      compile group: 'org.elasticsearch.client', name: 'elasticsearch-rest-high-level-client', version: '7.10.2'

Connecting to a Cluster
-----------------------

The sample code varies depending on the security mode settings of the target Elasticsearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch Cluster Security-Mode Settings | Whether to Load a Security Certificate | Details                                                                                                                                                                                 |
   +==============================================+========================================+=========================================================================================================================================================================================+
   | Non-security mode                            | ``-``                                  | :ref:`Connecting to a Non-Security Mode Cluster Using the High Level REST Client <en-us_topic_0000002471624338__en-us_topic_0000001961178813_section197550282614>`                      |
   +----------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTP                         | No                                     | :ref:`Connecting to a Security-Mode Cluster Using the High Level REST Client (Without a Certificate) <en-us_topic_0000002471624338__en-us_topic_0000001961178813_section1523020817518>` |
   |                                              |                                        |                                                                                                                                                                                         |
   | Security mode + HTTPS                        |                                        |                                                                                                                                                                                         |
   +----------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                        | Yes                                    | :ref:`Connecting to a Security-Mode Cluster Using the High Level REST Client (With a Certificate) <en-us_topic_0000002471624338__en-us_topic_0000001961178813_section1368184211106>`    |
   +----------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002471624338__en-us_topic_0000001961178813_section197550282614:

Connecting to a Non-Security Mode Cluster Using the High Level REST Client
--------------------------------------------------------------------------

Use the High Level REST Client to connect to an Elasticsearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

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
    * Use the High Level REST Client to connect to a non-security mode cluster.
    */
   public class Main {
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

.. _en-us_topic_0000002471624338__en-us_topic_0000001961178813_section1523020817518:

Connecting to a Security-Mode Cluster Using the High Level REST Client (Without a Certificate)
----------------------------------------------------------------------------------------------

Use the High Level REST Client to connect to a security-mode Elasticsearch cluster (HTTP or HTTPS) without loading a security certificate, and query whether the **test** index exists. The sample code is as follows:

::

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.conn.ssl.NoopHostnameVerifier;
   import org.apache.http.impl.client.BasicCredentialsProvider;
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

   import java.io.IOException;
   import java.security.KeyManagementException;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.CertificateException;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.X509TrustManager;

   /**
    * Use the High Level REST Client to connect to a security-mode cluster (without a certificate).
    */
   public class Main {

       private static final Logger logger = LogManager.getLogger(Main.class);

       /**
        * Create a class for the client. Define the create function.
        */
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout,
           int connectionRequestTimeout, int socketTimeout, String username, String password) throws IOException {

           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, port, protocol))
               .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                   .setConnectionRequestTimeout(connectionRequestTimeout)
                   .setSocketTimeout(socketTimeout))
               .setHttpClientConfigCallback(httpClientBuilder -> {
                   // enable user authentication
                   final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                   credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
                   httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                   // set keepalive
                   httpClientBuilder.setKeepAliveStrategy(((httpResponse, httpContext) -> TimeUnit.MINUTES.toMinutes(10)));
                   // enable SSL / TLS
                   SSLContext sc = null;
                   try {
                       sc = SSLContext.getInstance("SSL");
                       sc.init(null, trustAllCerts, new SecureRandom());
                   } catch (KeyManagementException | NoSuchAlgorithmException e) {
                       e.printStackTrace();
                   }
                   SSLIOSessionStrategy sslStrategy = new SSLIOSessionStrategy(sc, new NoopHostnameVerifier());
                   httpClientBuilder.setSSLStrategy(sslStrategy);

                   return httpClientBuilder;
               });
           final RestHighLevelClient client = new RestHighLevelClient(builder);
           logger.info("es rest client build success {} ", client);

           ClusterHealthRequest request = new ClusterHealthRequest();
           ClusterHealthResponse response = client.cluster().health(request, RequestOptions.DEFAULT);
           System.out.println("es rest client health response {} " + response);
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
   * The following is an example of the main function. Call the create function to create a client and check whether the test index exists.
        */
       public static void main(String[] args) throws IOException {
           RestHighLevelClient client = create(Arrays.asList("{host}"), 9200, "https", 1000, 1000, 1000, "username", "password");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
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

.. _en-us_topic_0000002471624338__en-us_topic_0000001961178813_section1368184211106:

Connecting to a Security-Mode Cluster Using the High Level REST Client (With a Certificate)
-------------------------------------------------------------------------------------------

Use the High Level REST Client to connect to a security-mode Elasticsearch cluster that uses HTTPS with a security certificate loaded, and query whether the **test** index exists. The sample code is as follows:

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000002471624338__section188511124109>`.

::

   import org.apache.http.HttpHost;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.conn.ssl.NoopHostnameVerifier;
   import org.apache.http.impl.client.BasicCredentialsProvider;
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
   import java.util.concurrent.TimeUnit;

   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.TrustManagerFactory;
   import javax.net.ssl.X509TrustManager;

   /**
    * Use the Hive Level REST Client to connect to a security-mode cluster (with an HTTPS certificate).
    */
   public class Main {
       public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout,
           int connectionRequestTimeout, int socketTimeout, String username, String password, String certFilePath,
           String certPassword) throws IOException {

           RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, port, protocol))
               .setRequestConfigCallback(requestConfig -> requestConfig.setConnectTimeout(connectTimeout)
                   .setConnectionRequestTimeout(connectionRequestTimeout)
                   .setSocketTimeout(socketTimeout))
               .setHttpClientConfigCallback(httpClientBuilder -> {
                   // enable user authentication
                   final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
                   credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(username, password));
                   httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                   // set keepalive
                   httpClientBuilder.setKeepAliveStrategy(((httpResponse, httpContext) -> TimeUnit.MINUTES.toMinutes(10)));
                   // enable SSL / TLS
                   SSLContext sc = null;
                   try {
                       TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
                       sc = SSLContext.getInstance("SSL", "SunJSSE");
                      //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
                       sc.init(null, tm, new SecureRandom());
                   } catch (Exception e) {
                       e.printStackTrace();
                   }
                   SSLIOSessionStrategy sslStrategy = new SSLIOSessionStrategy(sc, new NoopHostnameVerifier());
                   httpClientBuilder.setSSLStrategy(sslStrategy);

                   return httpClientBuilder;
               });
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

       private static final Logger logger = LogManager.getLogger(Main.class);

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
           RestHighLevelClient client = create(Arrays.asList({host}), 9200, "https", 1000, 1000, 1000, "username", "password", "certFilePath", "certPassword");
           GetIndexRequest indexRequest = new GetIndexRequest("test");
           boolean exists = client.indices().exists(indexRequest, RequestOptions.DEFAULT);
           System.out.println(exists);
           client.close();
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

.. _en-us_topic_0000002471624338__section188511124109:

Obtaining and Uploading a Security Certificate
----------------------------------------------

To access a security-mode Elasticsearch cluster that uses HTTPS, perform the following steps to obtain the security certificate if it is required, and upload it to the client.

#. Obtain the security certificate **CloudSearchService.cer**.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

   d. Click the **Overview** tab. In the **Network Information** area, click **Download Certificate** below **HTTPS Access**.


      .. figure:: /_static/images/en-us_image_0000002412557593.png
         :alt: **Figure 1** Downloading a security certificate

         **Figure 1** Downloading a security certificate

#. Convert the security certificate **CloudSearchService.cer**. Upload the downloaded security certificate to the client and use keytool to convert the **.cer** certificate into a **.jks** certificate that can be read by Java.

   -  In Linux, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

   -  In Windows, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore .\truststore.jks -file .\CloudSearchService.cer

   In the preceding command, *newname* indicates the user-defined certificate name.

   After this command is executed, you will be prompted to set the certificate password and confirm the password. Securely store the password. It will be used for accessing the cluster.
