:original_name: css_01_0387.html

.. _css_01_0387:

Accessing an Elasticsearch Cluster Through the Rest Low Level Client
====================================================================

The high-level client is encapsulated based on the low-level client. If the method calls (such as **.search** and **.bulk**) in the high-level client cannot meet the requirements or has compatibility issues, you can use the low-level client. You can even use **HighLevelClient.getLowLevelClient()** to directly obtain the low-level client. A low-level client allows you to customize the request structure, which is more flexible and supports all the request formats of Elasticsearch, such as GET, POST, DELETE, and HEAD.

This section describes how to use the Rest Low Level Client to access the CSS cluster. The methods are as follows. For each method, you can directly create a REST low-level client, or create a high-level client and then invoke getLowLevelClient() to obtain a low-level client.

-  :ref:`Connecting to a Non-Security Cluster Through the Rest Low Level Client <css_01_0387__en-us_topic_0000001934179694_section11903524419>`: suitable for clusters using non-security mode
-  :ref:`Connecting to a Security Cluster Through Rest Low Level Client (Without Security Certificates) <css_01_0387__en-us_topic_0000001934179694_section115491950202410>`: suitable for clusters in security mode+HTTP, and for clusters in security mode+HTTPS (without using certificates)
-  :ref:`Connecting to a Security Cluster Through Rest Low Level Client (With Security Certificates) <css_01_0387__en-us_topic_0000001934179694_section1684712173252>`: suitable for clusters in security mode+HTTPS

Precautions
-----------

You are advised to use the Rest Low Level Client version that matches the Elasticsearch version. For example, use Rest Low Level Client 7.6.2 to access the Elasticsearch 7.6.2 cluster.

Prerequisites
-------------

-  The CSS cluster is available.

-  Ensure that the server running Java can communicate with the CSS cluster.

-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Network Configuration <css_01_0381__section855085010198>`.

-  Install JDK 1.8 on the server. You can download JDK 1.8 from: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

-  Declare the Apache version in Maven mode. The following code uses version 7.6.2 as an example.

   *7.6.2* indicates the version of the Elasticsearch Java client.

   .. code-block::

      <dependency>
          <groupId>org.elasticsearch.client</groupId>
          <artifactId>elasticsearch-rest-client</artifactId>
          <version>7.6.2</version>
      </dependency>
      <dependency>
          <groupId>org.elasticsearch</groupId>
          <artifactId>elasticsearch</artifactId>
          <version>7.6.2</version>
      </dependency>

.. _css_01_0387__en-us_topic_0000001934179694_section11903524419:

Connecting to a Non-Security Cluster Through the Rest Low Level Client
----------------------------------------------------------------------

-  **Method 1: Directly create a Rest Low Level Client.**

   ::

      import org.apache.http.HttpHost;
      import org.elasticsearch.client.Request;
      import org.elasticsearch.client.Response;
      import org.elasticsearch.client.RestClient;
      import org.elasticsearch.client.RestClientBuilder;

      import java.io.IOException;
      import java.util.Arrays;
      import java.util.List;

      public class Main {

          public static void main(String[] args) throws IOException {
              List<String> host = Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx");
              RestClientBuilder builder = RestClient.builder(constructHttpHosts(host, 9200, "http"));
              /**
               * Create a Rest Low Level Client.
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

-  **Method 2: Create a high-level client and then call getLowLevelClient() to obtain a low-level client.**

   ::

      import org.apache.http.HttpHost;
      import org.elasticsearch.client.Request;
      import org.elasticsearch.client.Response;
      import org.elasticsearch.client.RestClient;
      import org.elasticsearch.client.RestClientBuilder;
      import org.elasticsearch.client.RestHighLevelClient;

      import java.io.IOException;
      import java.util.Arrays;
      import java.util.List;

      public class Main {

          public static void main(String[] args) throws IOException {
              List<String> host = Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx");
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

*host* indicates the IP address of the cluster. If there are multiple IP addresses, separate them using commas (,). *test* indicates the index name to be queried.

.. _css_01_0387__en-us_topic_0000001934179694_section115491950202410:

Connecting to a Security Cluster Through Rest Low Level Client (Without Security Certificates)
----------------------------------------------------------------------------------------------

-  **Method 1: Directly create a Rest Low Level Client.**

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

      public class Main {

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
      * The CustomConnectionKeepAliveStrategy function is used to set the connection keepalive time when there are a large number of short connections or when the number of data requests is small.
           */
          public static class CustomConnectionKeepAliveStrategy extends DefaultConnectionKeepAliveStrategy {
              public static final CustomConnectionKeepAliveStrategy INSTANCE = new CustomConnectionKeepAliveStrategy();

              private CustomConnectionKeepAliveStrategy() {
                  super();
              }

              /**
               * Maximum keep alive time (minutes)
               * The default value is 10 minutes. You can set it based on the number of TCP connections in TIME_WAIT state. If there are too many TCP connections, you can increase the value.
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
           * The following is an example of the main function. Call the create function to create a Rest Low Level Client and check whether the test index exists.
           */
          public static void main(String[] args) throws IOException {
              RestClient lowLevelClient = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "http", 1000, 1000, 1000, "username", "password");
              Request request = new Request("HEAD", "/test");
              Response response = lowLevelClient.performRequest(request);
              System.out.println(response.getStatusLine().getStatusCode());
              lowLevelClient.close();
          }
      }

-  **Method 2: Create a high-level client and then call getLowLevelClient() to obtain a low-level client.**

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

      import org.elasticsearch.client.RestHighLevelClient;

      public class Main13 {

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
      * The CustomConnectionKeepAliveStrategy function is used to set the connection keepalive time when there are a large number of short connections or when the number of data requests is small.
           */
          public static class CustomConnectionKeepAliveStrategy extends DefaultConnectionKeepAliveStrategy {
              public static final CustomConnectionKeepAliveStrategy INSTANCE = new CustomConnectionKeepAliveStrategy();

              private CustomConnectionKeepAliveStrategy() {
                  super();
              }

              /**
               * Maximum keep alive time (minutes)
               * The default value is 10 minutes. You can set it based on the number of TCP connections in TIME_WAIT state. If there are too many TCP connections, you can increase the value.
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
      * The following is an example of the main function. Call the create function to create a high-level client, call the getLowLevelClient() function to obtain a low-level client, and check whether the test index exists.
           */
          public static void main(String[] args) throws IOException {
              RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "http", 1000, 1000, 1000, "username", "password");
              RestClient lowLevelClient = client.getLowLevelClient();
              Request request = new Request("HEAD", "test");
              Response response = lowLevelClient.performRequest(request);
              System.out.println(response.getStatusLine().getStatusCode());
              lowLevelClient.close();
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

.. _css_01_0387__en-us_topic_0000001934179694_section1684712173252:

Connecting to a Security Cluster Through Rest Low Level Client (With Security Certificates)
-------------------------------------------------------------------------------------------

-  **Method 1: Directly create a Rest Low Level Client.**

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

      public class Main13 {

          private static final Logger logger = LogManager.getLogger(Main.class);

          /**
           * Create a class for the client. Define the create function.
           */
          public static RestClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String cerFilePath, String cerPassword) throws IOException {
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
           * The following is an example of the main function. Call the create function to create a Rest Low Level Client and check whether the test index exists.
           */
          public static void main(String[] args) throws IOException {
              RestClient lowLevelClient = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 1000, 1000, 1000, "username", "password", "cerFilePath", "cerPassword");
              Request request = new Request("HEAD", "test");
              Response response = lowLevelClient.performRequest(request);
              System.out.println(response.getStatusLine().getStatusCode());
              lowLevelClient.close();
          }
      }

-  **Method 2: Create a high-level client and then call getLowLevelClient() to obtain a low-level client.**

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

      public class Main {

          private static final Logger logger = LogManager.getLogger(Main.class);

          /**
           * Create a class for the client. Define the create function.
           */
          public static RestHighLevelClient create(List<String> host, int port, String protocol, int connectTimeout, int connectionRequestTimeout, int socketTimeout, String username, String password, String cerFilePath, String cerPassword) throws IOException {
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
      * The following is an example of the main function. Call the create function to create a high-level client, call the getLowLevelClient() function to obtain a low-level client, and check whether the test index exists.
           */
          public static void main(String[] args) throws IOException {
              RestHighLevelClient client = create(Arrays.asList("xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"), 9200, "https", 1000, 1000, 1000, "username", "password", "cerFilePath", "cerPassword");
              RestClient lowLevelClient = client.getLowLevelClient();
              Request request = new Request("HEAD", "test");
              Response response = lowLevelClient.performRequest(request);
              System.out.println(response.getStatusLine().getStatusCode());
              lowLevelClient.close();
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
