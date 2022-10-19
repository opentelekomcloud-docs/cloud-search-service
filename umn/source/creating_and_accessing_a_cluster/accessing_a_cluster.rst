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

   .. _css_01_0012__fig129821943205913:

   .. figure:: /_static/images/en-us_image_0000001286436598.png
      :alt: **Figure 1** Command output


      **Figure 1** Command output

.. _css_01_0012__section1619554519273:

Accessing a Cluster Using Java API in Non-security Mode
-------------------------------------------------------

For clusters in the non-security mode, you are advised to use use RestHighLevelClient.

-  Create a client using the default method of the RestHighLevelClient class.

   +-----------------------------------+---------------------------------------------------------------+
   | ::                                | ::                                                            |
   |                                   |                                                               |
   |    1                              |    RestHighLevelClient client = new RestHighLevelClient(      |
   |    2                              |            RestClient.builder(                                |
   |    3                              |                    new HttpHost("localhost", 9200, "http"))); |
   +-----------------------------------+---------------------------------------------------------------+

.. _css_01_0012__section0445155723816:

Accessing a Cluster Using the Java API in Security Mode with Elasticsearch
--------------------------------------------------------------------------

After enabling the security mode function for Elasticsearch 7.1.1 and later versions, accessing a cluster requires the use of HTTPS and the username and password for authentication.

You need to use clusters 7.1.1 and later versions as well as related APIs if you use the Java API to access a cluster, because the TransportClient class in the earlier version cannot access a cluster using the username and password.

Two access modes are available: Create a client using either the TransportClient or RestHighLevelClient class. RestHighLevelClient is recommended.

-  **Create a client using the TransportClient class.**

   Run the following commands on the client to generate the keystore and truststore files. The certificate (**CloudSearchService.cer**) downloaded from the cluster management page is used.

   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | ::                                | ::                                                                                              |
   |                                   |                                                                                                 |
   |    1                              |    keytool -genkeypair -alias certificatekey -keyalg RSA -keystore transport-keystore.jks       |
   |    2                              |    keytool -import -alias certificatekey -file CloudSearchService.cer  -keystore truststore.jks |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+

   Use the keystore and truststore files to access the cluster, create the TransportClient class using the PreBuiltTransportClient method, and add the settings in the client thread.

   The key code is as follows:

   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | ::                                | ::                                                                                                                                       |
   |                                   |                                                                                                                                          |
   |     1                             |    String userPw = "username:password";                                                                                                  |
   |     2                             |    String path = Paths.get(SecurityTransportClientDemo.class.getClassLoader().getResource(".").toURI()).toString();                      |
   |     3                             |                                                                                                                                          |
   |     4                             |    Settings settings = Settings.builder()                                                                                                |
   |     5                             |                     .put("opendistro_security.ssl.transport.enforce_hostname_verification", false)                                       |
   |     6                             |                     .put("opendistro_security.ssl.transport.keystore_filepath", path + "/transport-keystore.jks")                        |
   |     7                             |                     .put("opendistro_security.ssl.transport.keystore_password", "tscpass")                                               |
   |     8                             |                     .put("opendistro_security.ssl.transport.truststore_filepath", path + "/truststore.jks")                              |
   |     9                             |                     .put("client.transport.ignore_cluster_name", "true")                                                                 |
   |    10                             |                     .put("client.transport.sniff", false).build();                                                                       |
   |    11                             |                                                                                                                                          |
   |    12                             |    TransportClient client = (new PreBuiltTransportClient(settings, new Class[]{OpenDistroSecurityPlugin.class})).addTransportAddress(new |
   |    13                             |                          TransportAddress(InetAddress.getByName(ip), 9300));                                                             |
   |    14                             |                                                                                                                                          |
   |    15                             |    String base64UserPw = Base64.getEncoder().encodeToString(userPw.getBytes("utf-8"));                                                   |
   |    16                             |                   client.threadPool().getThreadContext().putHeader("Authorization", "Basic " + base64UserPw);                            |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

-  **Create a client using the RestHighLevelClient class.**

   The HttpHost class is used to process HTTP requests. In the HttpHost class, the CredentialsProvider and SSLIOSessionStrategy configuration parameter classes are encapsulated in the customized SecuredHttpClientConfigCallback class to configure request connection parameters.

   SecuredHttpClientConfigCallback: encapsulates all user-defined connection parameters.

   CredentialsProvider: Elasticsearch API, which is used to encapsulate the username and password using the method provided by Elasticsearch.

   SSLIOSessionStrategy: Configure SSL parameters, including the SSL domain name authentication mode and certificate processing mode. The SSLContext class is used to encapsulate related settings.

   You can access a cluster through either of the following modes: ignore certificates and use certificates.

   -  Ignore all certificates and skip certificate authentication.

      Construct the TrustManager. Use the default X509TrustManager. Do not rewrite any method. That is, ignore all related operations.

      Construct the SSLContext. Use TrustManager in the preceding step as the parameter and construct the SSLContext with the default method.

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
      | ::                                | ::                                                                                                                                              |
      |                                   |                                                                                                                                                 |
      |     1                             |    static TrustManager[] trustAllCerts = new TrustManager[] { new X509TrustManager() {                                                          |
      |     2                             |            @Override                                                                                                                            |
      |     3                             |            public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {                               |
      |     4                             |                                                                                                                                                 |
      |     5                             |            }                                                                                                                                    |
      |     6                             |            @Override                                                                                                                            |
      |     7                             |            public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {                               |
      |     8                             |                                                                                                                                                 |
      |     9                             |            }                                                                                                                                    |
      |    10                             |            @Override                                                                                                                            |
      |    11                             |            public X509Certificate[] getAcceptedIssuers() {                                                                                      |
      |    12                             |                return null;                                                                                                                     |
      |    13                             |            }                                                                                                                                    |
      |    14                             |        }};                                                                                                                                      |
      |    15                             |     final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();                                                             |
      |    16                             |            credentialsProvider.setCredentials(AuthScope.ANY,                                                                                    |
      |    17                             |                    new UsernamePasswordCredentials(userName, password));                                                                        |
      |    18                             |            SSLContext sc = null;                                                                                                                |
      |    19                             |            try{                                                                                                                                 |
      |    20                             |                sc = SSLContext.getInstance("SSL");                                                                                              |
      |    21                             |                sc.init(null, trustAllCerts, new SecureRandom());                                                                                |
      |    22                             |            }catch(KeyManagementException e){                                                                                                    |
      |    23                             |                    e.printStackTrace();                                                                                                         |
      |    24                             |            }catch(NoSuchAlgorithmException e){                                                                                                  |
      |    25                             |                    e.printStackTrace();                                                                                                         |
      |    26                             |            }                                                                                                                                    |
      |    27                             |            SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());                                     |
      |    28                             |                                                                                                                                                 |
      |    29                             |            SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,credentialsProvider); |
      |    30                             |                                                                                                                                                 |
      |    31                             |            RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200,                                                    |
      |    32                             |                                    "https")).setHttpClientConfigCallback(httpClientConfigCallback);                                             |
      |    33                             |                                                                                                                                                 |
      |    34                             |            RestHighLevelClient client = new RestHighLevelClient(builder);                                                                       |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

   -  Upload the downloaded certificate (**CloudSearchService.cer**) for accessing the cluster.

      Upload the certificate to the client and use the keytool to convert the certificate into a format that can be read by Java. (The default password of the keytool is **changeit**).

      .. code-block::

         keytool -import -alias custom name -keystore path for exporting the certificate and its new name -file path for uploading the certificate

      Customize the TrustManager class, which is inherited from the X509TrustManager. Read the certificate generated in the preceding step, add it to the trust certificate, and rewrite the three methods of the X509TrustManager interface.

      Construct the SSLContext. Use TrustManager in the preceding step as the parameter and construct the SSLContext with the default method.

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
      | ::                                | ::                                                                                                                                              |
      |                                   |                                                                                                                                                 |
      |     1                             |    public static class MyX509TrustManager implements X509TrustManager {                                                                         |
      |     2                             |                                                                                                                                                 |
      |     3                             |            X509TrustManager sunJSSEX509TrustManager;                                                                                            |
      |     4                             |            MyX509TrustManager() throws Exception {                                                                                              |
      |     5                             |                File file = new File("certification file path");                                                                                 |
      |     6                             |                if (file.isFile() == false) {                                                                                                    |
      |     7                             |                    throw new Exception("Wrong Certification Path");                                                                             |
      |     8                             |                }                                                                                                                                |
      |     9                             |                System.out.println("Loading KeyStore " + file + "...");                                                                          |
      |    10                             |                InputStream in = new FileInputStream(file);                                                                                      |
      |    11                             |                KeyStore ks = KeyStore.getInstance("JKS");                                                                                       |
      |    12                             |                ks.load(in, "changeit".toCharArray());                                                                                           |
      |    13                             |                TrustManagerFactory tmf =                                                                                                        |
      |    14                             |                        TrustManagerFactory.getInstance("SunX509", "SunJSSE");                                                                   |
      |    15                             |                tmf.init(ks);                                                                                                                    |
      |    16                             |                TrustManager tms [] = tmf.getTrustManagers();                                                                                    |
      |    17                             |                for (int i = 0; i < tms.length; i++) {                                                                                           |
      |    18                             |                    if (tms[i] instanceof X509TrustManager) {                                                                                    |
      |    19                             |                        sunJSSEX509TrustManager = (X509TrustManager) tms[i];                                                                     |
      |    20                             |                        return;                                                                                                                  |
      |    21                             |                    }                                                                                                                            |
      |    22                             |                }                                                                                                                                |
      |    23                             |                throw new Exception("Couldn't initialize");                                                                                      |
      |    24                             |            }                                                                                                                                    |
      |    25                             |                                                                                                                                                 |
      |    26                             |    final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();                                                              |
      |    27                             |            credentialsProvider.setCredentials(AuthScope.ANY,                                                                                    |
      |    28                             |                    new UsernamePasswordCredentials(userName, password));                                                                        |
      |    29                             |                                                                                                                                                 |
      |    30                             |            SSLContext sc = null;                                                                                                                |
      |    31                             |            try{                                                                                                                                 |
      |    32                             |                TrustManager[] tm = {new MyX509TrustManager()};                                                                                  |
      |    33                             |                sc = SSLContext.getInstance("SSL", "SunJSSE");                                                                                   |
      |    34                             |                sc.init(null, tm, new SecureRandom());                                                                                           |
      |    35                             |            }catch (Exception e) {                                                                                                               |
      |    36                             |                e.printStackTrace();                                                                                                             |
      |    37                             |            }                                                                                                                                    |
      |    38                             |                                                                                                                                                 |
      |    39                             |            SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());                                     |
      |    40                             |                                                                                                                                                 |
      |    41                             |            SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy,credentialsProvider); |
      |    42                             |            RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200, "https"))                                          |
      |    43                             |                    .setHttpClientConfigCallback(httpClientConfigCallback);                                                                      |
      |    44                             |            RestHighLevelClient client = new RestHighLevelClient(builder);                                                                       |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

   -  Sample code

      When the code is running, transfer three parameters: access address, cluster login username, and password. The request is **GET /_search{"query": {"match_all": {}}}**.

      .. note::

         The access address of a cluster with security mode enabled usually starts with **https**.

      **ESSecuredClient class (Ignore certificates)**

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
      | ::                                | ::                                                                                                                         |
      |                                   |                                                                                                                            |
      |      1                            |    package securitymode;                                                                                                   |
      |      2                            |                                                                                                                            |
      |      3                            |    import org.apache.http.auth.AuthScope;                                                                                  |
      |      4                            |    import org.apache.http.auth.UsernamePasswordCredentials;                                                                |
      |      5                            |    import org.apache.http.client.CredentialsProvider;                                                                      |
      |      6                            |    import org.apache.http.impl.client.BasicCredentialsProvider;                                                            |
      |      7                            |    import org.apache.http.HttpHost;                                                                                        |
      |      8                            |    import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;                                                               |
      |      9                            |    import org.elasticsearch.action.search.SearchRequest;                                                                   |
      |     10                            |    import org.elasticsearch.action.search.SearchResponse;                                                                  |
      |     11                            |    import org.elasticsearch.client.RequestOptions;                                                                         |
      |     12                            |    import org.elasticsearch.client.RestClient;                                                                             |
      |     13                            |    import org.elasticsearch.client.RestClientBuilder;                                                                      |
      |     14                            |    import org.elasticsearch.client.RestHighLevelClient;                                                                    |
      |     15                            |    import org.elasticsearch.index.query.QueryBuilders;                                                                     |
      |     16                            |    import org.elasticsearch.search.SearchHit;                                                                              |
      |     17                            |    import org.elasticsearch.search.SearchHits;                                                                             |
      |     18                            |    import org.elasticsearch.search.builder.SearchSourceBuilder;                                                            |
      |     19                            |                                                                                                                            |
      |     20                            |    import java.io.IOException;                                                                                             |
      |     21                            |    import java.security.KeyManagementException;                                                                            |
      |     22                            |    import java.security.NoSuchAlgorithmException;                                                                          |
      |     23                            |    import java.security.SecureRandom;                                                                                      |
      |     24                            |    import java.security.cert.CertificateException;                                                                         |
      |     25                            |    import java.security.cert.X509Certificate;                                                                              |
      |     26                            |                                                                                                                            |
      |     27                            |    import javax.net.ssl.HostnameVerifier;                                                                                  |
      |     28                            |    import javax.net.ssl.SSLContext;                                                                                        |
      |     29                            |    import javax.net.ssl.SSLSession;                                                                                        |
      |     30                            |    import javax.net.ssl.TrustManager;                                                                                      |
      |     31                            |    import javax.net.ssl.X509TrustManager;                                                                                  |
      |     32                            |                                                                                                                            |
      |     33                            |    public class ESSecuredClientIgnoreCerDemo {                                                                             |
      |     34                            |                                                                                                                            |
      |     35                            |        public static void main(String[] args) {                                                                            |
      |     36                            |            String clusterAddress = args[0];                                                                                |
      |     37                            |            String userName = args[1];                                                                                      |
      |     38                            |            String password = args[2];                                                                                      |
      |     39                            |           // Create a client.                                                                                              |
      |     40                            |            RestHighLevelClient client = initESClient(clusterAddress, userName, password);                                  |
      |     41                            |            try {                                                                                                           |
      |     42                            |             // Search match_all, which is equivalent to {\"query\": {\"match_all\": {}}}.                                  |
      |     43                            |                SearchRequest searchRequest = new SearchRequest();                                                          |
      |     44                            |                SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();                                        |
      |     45                            |                searchSourceBuilder.query(QueryBuilders.matchAllQuery());                                                   |
      |     46                            |                searchRequest.source(searchSourceBuilder);                                                                  |
      |     47                            |                                                                                                                            |
      |     48                            |                SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);                       |
      |     49                            |                System.out.println("query result: " + searchResponse.toString());                                           |
      |     50                            |                SearchHits hits = searchResponse.getHits();                                                                 |
      |     51                            |                for (SearchHit hit : hits) {                                                                                |
      |     52                            |                    System.out.println(hit.getSourceAsString());                                                            |
      |     53                            |                }                                                                                                           |
      |     54                            |                System.out.println("query success");                                                                        |
      |     55                            |                Thread.sleep(2000L);                                                                                        |
      |     56                            |            } catch (InterruptedException | IOException e) {                                                                |
      |     57                            |                e.printStackTrace();                                                                                        |
      |     58                            |            } finally {                                                                                                     |
      |     59                            |                try {                                                                                                       |
      |     60                            |                    client.close();                                                                                         |
      |     61                            |                    System.out.println("close client");                                                                     |
      |     62                            |                } catch (IOException e) {                                                                                   |
      |     63                            |                    e.printStackTrace();                                                                                    |
      |     64                            |                }                                                                                                           |
      |     65                            |            }                                                                                                               |
      |     66                            |        }                                                                                                                   |
      |     67                            |                                                                                                                            |
      |     68                            |        private static RestHighLevelClient initESClient(String clusterAddress, String userName, String password) {          |
      |     69                            |            final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();                                 |
      |     70                            |            credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(userName, password));         |
      |     71                            |            SSLContext sc = null;                                                                                           |
      |     72                            |            try {                                                                                                           |
      |     73                            |                sc = SSLContext.getInstance("SSL");                                                                         |
      |     74                            |                sc.init(null, trustAllCerts, new SecureRandom());                                                           |
      |     75                            |            } catch (KeyManagementException | NoSuchAlgorithmException e) {                                                 |
      |     76                            |                e.printStackTrace();                                                                                        |
      |     77                            |            }                                                                                                               |
      |     78                            |            SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());                |
      |     79                            |            SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy, |
      |     80                            |                credentialsProvider);                                                                                       |
      |     81                            |            RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200, "https"))                     |
      |     82                            |                .setHttpClientConfigCallback(httpClientConfigCallback);                                                     |
      |     83                            |            RestHighLevelClient client = new RestHighLevelClient(builder);                                                  |
      |     84                            |            return client;                                                                                                  |
      |     85                            |        }                                                                                                                   |
      |     86                            |                                                                                                                            |
      |     87                            |        static TrustManager[] trustAllCerts = new TrustManager[] {                                                          |
      |     88                            |            new X509TrustManager() {                                                                                        |
      |     89                            |                @Override                                                                                                   |
      |     90                            |                public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {      |
      |     91                            |                }                                                                                                           |
      |     92                            |                                                                                                                            |
      |     93                            |                @Override                                                                                                   |
      |     94                            |                public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {      |
      |     95                            |                }                                                                                                           |
      |     96                            |                                                                                                                            |
      |     97                            |                @Override                                                                                                   |
      |     98                            |                public X509Certificate[] getAcceptedIssuers() {                                                             |
      |     99                            |                    return null;                                                                                            |
      |    100                            |                }                                                                                                           |
      |    101                            |            }                                                                                                               |
      |    102                            |        };                                                                                                                  |
      |    103                            |                                                                                                                            |
      |    104                            |        public static class NullHostNameVerifier implements HostnameVerifier {                                              |
      |    105                            |            @Override                                                                                                       |
      |    106                            |            public boolean verify(String arg0, SSLSession arg1) {                                                           |
      |    107                            |                return true;                                                                                                |
      |    108                            |            }                                                                                                               |
      |    109                            |        }                                                                                                                   |
      |    110                            |                                                                                                                            |
      |    111                            |    }                                                                                                                       |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+

      **ESSecuredClient class (Uses certificates)**

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
      | ::                                | ::                                                                                                                         |
      |                                   |                                                                                                                            |
      |      1                            |    package securitymode;                                                                                                   |
      |      2                            |                                                                                                                            |
      |      3                            |    import org.apache.http.auth.AuthScope;                                                                                  |
      |      4                            |    import org.apache.http.auth.UsernamePasswordCredentials;                                                                |
      |      5                            |    import org.apache.http.client.CredentialsProvider;                                                                      |
      |      6                            |    import org.apache.http.impl.client.BasicCredentialsProvider;                                                            |
      |      7                            |    import org.apache.http.HttpHost;                                                                                        |
      |      8                            |    import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;                                                               |
      |      9                            |    import org.elasticsearch.action.search.SearchRequest;                                                                   |
      |     10                            |    import org.elasticsearch.action.search.SearchResponse;                                                                  |
      |     11                            |    import org.elasticsearch.client.RequestOptions;                                                                         |
      |     12                            |    import org.elasticsearch.client.RestClient;                                                                             |
      |     13                            |    import org.elasticsearch.client.RestClientBuilder;                                                                      |
      |     14                            |    import org.elasticsearch.client.RestHighLevelClient;                                                                    |
      |     15                            |    import org.elasticsearch.index.query.QueryBuilders;                                                                     |
      |     16                            |    import org.elasticsearch.search.SearchHit;                                                                              |
      |     17                            |    import org.elasticsearch.search.SearchHits;                                                                             |
      |     18                            |    import org.elasticsearch.search.builder.SearchSourceBuilder;                                                            |
      |     19                            |                                                                                                                            |
      |     20                            |    import java.io.File;                                                                                                    |
      |     21                            |    import java.io.FileInputStream;                                                                                         |
      |     22                            |    import java.io.IOException;                                                                                             |
      |     23                            |    import java.io.InputStream;                                                                                             |
      |     24                            |    import java.security.KeyStore;                                                                                          |
      |     25                            |    import java.security.SecureRandom;                                                                                      |
      |     26                            |    import java.security.cert.CertificateException;                                                                         |
      |     27                            |    import java.security.cert.X509Certificate;                                                                              |
      |     28                            |                                                                                                                            |
      |     29                            |    import javax.net.ssl.HostnameVerifier;                                                                                  |
      |     30                            |    import javax.net.ssl.SSLContext;                                                                                        |
      |     31                            |    import javax.net.ssl.SSLSession;                                                                                        |
      |     32                            |    import javax.net.ssl.TrustManager;                                                                                      |
      |     33                            |    import javax.net.ssl.TrustManagerFactory;                                                                               |
      |     34                            |    import javax.net.ssl.X509TrustManager;                                                                                  |
      |     35                            |                                                                                                                            |
      |     36                            |    public class ESSecuredClientWithCerDemo {                                                                               |
      |     37                            |                                                                                                                            |
      |     38                            |        public static void main(String[] args) {                                                                            |
      |     39                            |            String clusterAddress = args[0];                                                                                |
      |     40                            |            String userName = args[1];                                                                                      |
      |     41                            |            String password = args[2];                                                                                      |
      |     42                            |            String cerFilePath = args[3];                                                                                   |
      |     43                            |            String cerPassword = args[4];                                                                                   |
      |     44                            |           // Create a client.                                                                                              |
      |     45                            |            RestHighLevelClient client = initESClient(clusterAddress, userName, password, cerFilePath, cerPassword);        |
      |     46                            |            try {                                                                                                           |
      |     47                            |             // Search match_all, which is equivalent to {\"query\": {\"match_all\": {}}}.                                  |
      |     48                            |                SearchRequest searchRequest = new SearchRequest();                                                          |
      |     49                            |                SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();                                        |
      |     50                            |                searchSourceBuilder.query(QueryBuilders.matchAllQuery());                                                   |
      |     51                            |                searchRequest.source(searchSourceBuilder);                                                                  |
      |     52                            |                                                                                                                            |
      |     53                            |                // query                                                                                                    |
      |     54                            |                SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);                       |
      |     55                            |                System.out.println("query result: " + searchResponse.toString());                                           |
      |     56                            |                SearchHits hits = searchResponse.getHits();                                                                 |
      |     57                            |                for (SearchHit hit : hits) {                                                                                |
      |     58                            |                    System.out.println(hit.getSourceAsString());                                                            |
      |     59                            |                }                                                                                                           |
      |     60                            |                System.out.println("query success");                                                                        |
      |     61                            |                Thread.sleep(2000L);                                                                                        |
      |     62                            |            } catch (InterruptedException | IOException e) {                                                                |
      |     63                            |                e.printStackTrace();                                                                                        |
      |     64                            |            } finally {                                                                                                     |
      |     65                            |                try {                                                                                                       |
      |     66                            |                    client.close();                                                                                         |
      |     67                            |                    System.out.println("close client");                                                                     |
      |     68                            |                } catch (IOException e) {                                                                                   |
      |     69                            |                    e.printStackTrace();                                                                                    |
      |     70                            |                }                                                                                                           |
      |     71                            |            }                                                                                                               |
      |     72                            |        }                                                                                                                   |
      |     73                            |                                                                                                                            |
      |     74                            |        private static RestHighLevelClient initESClient(String clusterAddress, String userName, String password,            |
      |     75                            |            String cerFilePath, String cerPassword) {                                                                       |
      |     76                            |            final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();                                 |
      |     77                            |            credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(userName, password));         |
      |     78                            |            SSLContext sc = null;                                                                                           |
      |     79                            |            try {                                                                                                           |
      |     80                            |                TrustManager[] tm = {new MyX509TrustManager(cerFilePath, cerPassword)};                                     |
      |     81                            |                sc = SSLContext.getInstance("SSL", "SunJSSE");                                                              |
      |     82                            |                //You can also use SSLContext sslContext = SSLContext.getInstance("TLSv1.2");                               |
      |     83                            |                sc.init(null, tm, new SecureRandom());                                                                      |
      |     84                            |            } catch (Exception e) {                                                                                         |
      |     85                            |                e.printStackTrace();                                                                                        |
      |     86                            |            }                                                                                                               |
      |     87                            |                                                                                                                            |
      |     88                            |            SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, new NullHostNameVerifier());                |
      |     89                            |            SecuredHttpClientConfigCallback httpClientConfigCallback = new SecuredHttpClientConfigCallback(sessionStrategy, |
      |     90                            |                credentialsProvider);                                                                                       |
      |     91                            |            RestClientBuilder builder = RestClient.builder(new HttpHost(clusterAddress, 9200, "https"))                     |
      |     92                            |                .setHttpClientConfigCallback(httpClientConfigCallback);                                                     |
      |     93                            |            RestHighLevelClient client = new RestHighLevelClient(builder);                                                  |
      |     94                            |            return client;                                                                                                  |
      |     95                            |        }                                                                                                                   |
      |     96                            |                                                                                                                            |
      |     97                            |        public static class MyX509TrustManager implements X509TrustManager {                                                |
      |     98                            |            X509TrustManager sunJSSEX509TrustManager;                                                                       |
      |     99                            |                                                                                                                            |
      |    100                            |            MyX509TrustManager(String cerFilePath, String cerPassword) throws Exception {                                   |
      |    101                            |                File file = new File(cerFilePath);                                                                          |
      |    102                            |                if (!file.isFile()) {                                                                                       |
      |    103                            |                    throw new Exception("Wrong Certification Path");                                                        |
      |    104                            |                }                                                                                                           |
      |    105                            |                System.out.println("Loading KeyStore " + file + "...");                                                     |
      |    106                            |                InputStream in = new FileInputStream(file);                                                                 |
      |    107                            |                KeyStore ks = KeyStore.getInstance("JKS");                                                                  |
      |    108                            |                ks.load(in, cerPassword.toCharArray());                                                                     |
      |    109                            |                TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509", "SunJSSE");                            |
      |    110                            |                tmf.init(ks);                                                                                               |
      |    111                            |                TrustManager[] tms = tmf.getTrustManagers();                                                                |
      |    112                            |                for (TrustManager tm : tms) {                                                                               |
      |    113                            |                    if (tm instanceof X509TrustManager) {                                                                   |
      |    114                            |                        sunJSSEX509TrustManager = (X509TrustManager) tm;                                                    |
      |    115                            |                        return;                                                                                             |
      |    116                            |                    }                                                                                                       |
      |    117                            |                }                                                                                                           |
      |    118                            |                throw new Exception("Couldn't initialize");                                                                 |
      |    119                            |            }                                                                                                               |
      |    120                            |                                                                                                                            |
      |    121                            |            @Override                                                                                                       |
      |    122                            |            public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {          |
      |    123                            |                                                                                                                            |
      |    124                            |            }                                                                                                               |
      |    125                            |                                                                                                                            |
      |    126                            |            @Override                                                                                                       |
      |    127                            |            public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {          |
      |    128                            |                                                                                                                            |
      |    129                            |            }                                                                                                               |
      |    130                            |                                                                                                                            |
      |    131                            |            @Override                                                                                                       |
      |    132                            |            public X509Certificate[] getAcceptedIssuers() {                                                                 |
      |    133                            |                return new X509Certificate[0];                                                                              |
      |    134                            |            }                                                                                                               |
      |    135                            |        }                                                                                                                   |
      |    136                            |                                                                                                                            |
      |    137                            |        public static class NullHostNameVerifier implements HostnameVerifier {                                              |
      |    138                            |            @Override                                                                                                       |
      |    139                            |            public boolean verify(String arg0, SSLSession arg1) {                                                           |
      |    140                            |                return true;                                                                                                |
      |    141                            |            }                                                                                                               |
      |    142                            |        }                                                                                                                   |
      |    143                            |                                                                                                                            |
      |    144                            |    }                                                                                                                       |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+

      **SecuredHttpClientConfigCallback class**

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
      | ::                                | ::                                                                                                                             |
      |                                   |                                                                                                                                |
      |     1                             |    import org.apache.http.client.CredentialsProvider;                                                                          |
      |     2                             |    import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;                                                              |
      |     3                             |    import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;                                                                   |
      |     4                             |    import org.elasticsearch.client.RestClientBuilder;                                                                          |
      |     5                             |    import org.elasticsearch.common.Nullable;                                                                                   |
      |     6                             |    import java.util.Objects;                                                                                                   |
      |     7                             |    class SecuredHttpClientConfigCallback implements RestClientBuilder.HttpClientConfigCallback {                               |
      |     8                             |        @Nullable                                                                                                               |
      |     9                             |        private final CredentialsProvider credentialsProvider;                                                                  |
      |    10                             |        /**                                                                                                                     |
      |    11                             |         * The {@link SSLIOSessionStrategy} for all requests to enable SSL / TLS encryption.                                    |
      |    12                             |         */                                                                                                                     |
      |    13                             |        private final SSLIOSessionStrategy sslStrategy;                                                                         |
      |    14                             |        /**                                                                                                                     |
      |    15                             |         * Create a new {@link SecuredHttpClientConfigCallback}.                                                                |
      |    16                             |         *                                                                                                                      |
      |    17                             |         * @param credentialsProvider The credential provider, if a username/password have been supplied                        |
      |    18                             |         * @param sslStrategy         The SSL strategy, if SSL / TLS have been supplied                                         |
      |    19                             |         * @throws NullPointerException if {@code sslStrategy} is {@code null}                                                  |
      |    20                             |         */                                                                                                                     |
      |    21                             |        SecuredHttpClientConfigCallback(final SSLIOSessionStrategy sslStrategy,                                                 |
      |    22                             |                                        @Nullable final CredentialsProvider credentialsProvider) {                              |
      |    23                             |            this.sslStrategy = Objects.requireNonNull(sslStrategy);                                                             |
      |    24                             |            this.credentialsProvider = credentialsProvider;                                                                     |
      |    25                             |        }                                                                                                                       |
      |    26                             |        /**                                                                                                                     |
      |    27                             |         * Get the {@link CredentialsProvider} that will be added to the HTTP client.                                           |
      |    28                             |         *                                                                                                                      |
      |    29                             |         * @return Can be {@code null}.                                                                                         |
      |    30                             |         */                                                                                                                     |
      |    31                             |        @Nullable                                                                                                               |
      |    32                             |        CredentialsProvider getCredentialsProvider() {                                                                          |
      |    33                             |            return credentialsProvider;                                                                                         |
      |    34                             |        }                                                                                                                       |
      |    35                             |        /**                                                                                                                     |
      |    36                             |         * Get the {@link SSLIOSessionStrategy} that will be added to the HTTP client.                                          |
      |    37                             |         *                                                                                                                      |
      |    38                             |         * @return Never {@code null}.                                                                                          |
      |    39                             |         */                                                                                                                     |
      |    40                             |        SSLIOSessionStrategy getSSLStrategy() {                                                                                 |
      |    41                             |            return sslStrategy;                                                                                                 |
      |    42                             |        }                                                                                                                       |
      |    43                             |        /**                                                                                                                     |
      |    44                             |         * Sets the {@linkplain HttpAsyncClientBuilder#setDefaultCredentialsProvider(CredentialsProvider) credential provider}, |
      |    45                             |         *                                                                                                                      |
      |    46                             |         * @param httpClientBuilder The client to configure.                                                                    |
      |    47                             |         * @return Always {@code httpClientBuilder}.                                                                            |
      |    48                             |         */                                                                                                                     |
      |    49                             |        @Override                                                                                                               |
      |    50                             |        public HttpAsyncClientBuilder customizeHttpClient(final HttpAsyncClientBuilder httpClientBuilder) {                     |
      |    51                             |            // enable SSL / TLS                                                                                                 |
      |    52                             |            httpClientBuilder.setSSLStrategy(sslStrategy);                                                                      |
      |    53                             |            // enable user authentication                                                                                       |
      |    54                             |            if (credentialsProvider != null) {                                                                                  |
      |    55                             |                httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);                                           |
      |    56                             |            }                                                                                                                   |
      |    57                             |            return httpClientBuilder;                                                                                           |
      |    58                             |        }                                                                                                                       |
      |    59                             |    }                                                                                                                           |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

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
