:original_name: css_01_0182.html

.. _css_01_0182:

Configuring a Dedicated Load Balancer for an OpenSearch Cluster
===============================================================

CSS integrates shared load balancers, through which you can enable access to a cluster from the public network as well as through the VPC Endpoint service. Dedicated load balancers provide higher performance and more diverse features than shared load balancers. This topic describes how to configure a dedicated load balancer for a cluster.

Scenarios
---------

Advantages of connecting to a cluster through a dedicated load balancer:

-  A non-security cluster can also utilize the capabilities of the Elastic Load Balance (ELB) service.
-  You can use custom certificates for HTTPS two-way authentication.
-  Seven-layer traffic monitoring and alarm configuration are supported, allowing you to keep close track of the cluster status.

There are eight different ELB service forms for clusters in different security modes to connect to a dedicated load balancer. :ref:`Table 1 <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001463358273_table4446327845>` describes the ELB capabilities for different cluster configurations. :ref:`Table 2 <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001463358273_table1537163912019>` describes the configurations for different ELB service forms.

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001463358273_table4446327845:

.. table:: **Table 1** ELB capabilities for different clusters

   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security Mode         | Service Form Provided by ELB for External Systems | ELB Load Balancing | ELB Traffic Monitoring | ELB Two-way Authentication |
   +=======================+===================================================+====================+========================+============================+
   | Non-security mode     | No authentication                                 | Supported          | Supported              | Not supported              |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication                            | Supported          | Supported              | Supported                  |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication                            |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTP  | Password authentication                           | Supported          | Supported              | Not supported              |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication + Password authentication  | Supported          | Supported              | Supported                  |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTPS | One-way authentication + Password authentication  | Supported          | Supported              | Supported                  |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001463358273_table1537163912019:

.. table:: **Table 2** Configurations for different ELB service forms depending on the cluster

   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   | Security Mode         | Service Form Provided by ELB for External Systems | ELB Listener      | ELB Listener  | ELB Listener           | Backend Server Group | Backend Server Group | Backend Server Group          |
   +=======================+===================================================+===================+===============+========================+======================+======================+===============================+
   |                       |                                                   | Frontend Protocol | Frontend Port | SSL Authentication     | Backend Protocol     | Health Check Port    | Health Check Path             |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   | Non-security mode     | No authentication                                 | HTTP              | 9200          | No authentication      | HTTP                 | 9200                 | /                             |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   |                       | One-way authentication                            | HTTPS             | 9200          | One-way authentication | HTTP                 | 9200                 |                               |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   |                       | Two-way authentication                            | HTTPS             | 9200          | Two-way authentication | HTTP                 | 9200                 |                               |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   | Security mode + HTTP  | Password authentication                           | HTTP              | 9200          | No authentication      | HTTP                 | 9200                 | /_opendistro/_security/health |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   |                       | One-way authentication + Password authentication  | HTTPS             | 9200          | One-way authentication | HTTP                 | 9200                 |                               |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   |                       | Two-way authentication + Password authentication  | HTTPS             | 9200          | Two-way authentication | HTTP                 | 9200                 |                               |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   | Security mode + HTTPS | One-way authentication + Password authentication  | HTTPS             | 9200          | One-way authentication | HTTPS                | 9200                 |                               |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   |                       | Two-way authentication + Password authentication  | HTTPS             | 9200          | Two-way authentication | HTTPS                | 9200                 |                               |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+

Constraints
-----------

-  You are not advised to connect a load balancer that has been associated with a public IP address to a non-security mode cluster. Allowing public network access through such a load balancer may cause security risks because a non-security mode cluster can be accessed using HTTP without security authentication.
-  HTTPS-enabled security-mode clusters do not support HTTP-based frontend authentication. If the frontend uses HTTP, disable security mode for your cluster first. For details, see :ref:`Changing the Security Mode of an OpenSearch Cluster <css_01_0310>`. Before changing the security mode, disable load balancing first. After the security mode is changed, enable load balancing again.

Prerequisites
-------------

-  A dedicated load balancer has been created. For details, see `Creating a Dedicated Load Balancer <https://docs.otc.t-systems.com/elastic-load-balancing/umn/load_balancer/creating_a_dedicated_load_balancer.html>`__. This load balancer must meet the following requirements:

   -  Its VPC is the same as that of the CSS cluster. The network between the two are connected.
   -  **IP as a Backend** is enabled. This is necessary to connect a dedicated load balancer to a CSS cluster.
   -  Determine whether to configure an EIP based on service needs. A public IP address is displayed for the load balancer connecting the CSS cluster only if an EIP is configured. This will enable public network access to the cluster through this load balancer.

-  If the ELB listener uses HTTPS, upload a server certificate or CA certificate to the ELB console. For details, see `Configuring the Server Certificate and Private Key <https://docs.otc.t-systems.com/elastic-load-balancing/umn/advanced_features_of_http_https_listeners/mutual_authentication.html#configuring-the-server-certificate-and-private-key>`__.

   -  If one-way authentication is used, upload a server certificate.
   -  If two-way authentication is used, upload a server certificate and a CA certificate.

Connecting a Cluster to a Load Balancer
---------------------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Cluster Access** tab, and then click the **Load Balancing** tab. On the **OpenSearch** tab, toggle on **Load Balancing**. In the displayed dialog box, set the parameters.

   .. table:: **Table 3** Configuring load balancing

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                                                                                                   |
      +===================================+===============================================================================================================================================================================================================================================================================================================================================================+
      | Load Balancer                     | Select the dedicated load balancer you have created earlier.                                                                                                                                                                                                                                                                                                  |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   | To create a dedicated load balancer, see `Creating a Dedicated Load Balancer <https://docs.otc.t-systems.com/elastic-load-balancing/umn/load_balancer/creating_a_dedicated_load_balancer.html>`__.                                                                                                                                                            |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Agency                            | To configure a load balancer, you must have the permission to access ELB resources. By configuring an IAM agency, you can authorize CSS to access its ELB resources through an associated account.                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   | -  If you are configuring an agency for the first time, click **Automatically Create IAM Agency** to create **css-elb-agency**.                                                                                                                                                                                                                               |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   | -  If there is an IAM agency automatically created earlier, you can click **One-click authorization** to have the permissions associated with the **ELB Administrator** role or the **ELB FullAccess** system policy deleted automatically, and have the following custom policies added automatically instead to implement more refined permissions control. |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   |       "elb:loadbalancers:list",                                                                                                                                                                                                                                                                                                                               |
      |                                   |       "elb:loadbalancers:get",                                                                                                                                                                                                                                                                                                                                |
      |                                   |       "elb:certificates:list",                                                                                                                                                                                                                                                                                                                                |
      |                                   |       "elb:healthmonitors:*",                                                                                                                                                                                                                                                                                                                                 |
      |                                   |       "elb:members:*",                                                                                                                                                                                                                                                                                                                                        |
      |                                   |       "elb:pools:*",                                                                                                                                                                                                                                                                                                                                          |
      |                                   |       "elb:listeners:*"                                                                                                                                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   | -  To use **Automatically Create IAM Agency** and **One-click authorization**, the following minimum permissions are required:                                                                                                                                                                                                                                |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   |       "iam:agencies:listAgencies",                                                                                                                                                                                                                                                                                                                            |
      |                                   |       "iam:roles:listRoles",                                                                                                                                                                                                                                                                                                                                  |
      |                                   |       "iam:agencies:getAgency",                                                                                                                                                                                                                                                                                                                               |
      |                                   |       "iam:agencies:createAgency",                                                                                                                                                                                                                                                                                                                            |
      |                                   |       "iam:permissions:listRolesForAgency",                                                                                                                                                                                                                                                                                                                   |
      |                                   |       "iam:permissions:grantRoleToAgency",                                                                                                                                                                                                                                                                                                                    |
      |                                   |       "iam:permissions:listRolesForAgencyOnProject",                                                                                                                                                                                                                                                                                                          |
      |                                   |       "iam:permissions:revokeRoleFromAgency",                                                                                                                                                                                                                                                                                                                 |
      |                                   |       "iam:roles:createRole"                                                                                                                                                                                                                                                                                                                                  |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   | -  To use an IAM agency, the following minimum permissions are required:                                                                                                                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                                                                                                                               |
      |                                   |       "iam:agencies:listAgencies",                                                                                                                                                                                                                                                                                                                            |
      |                                   |       "iam:agencies:getAgency",                                                                                                                                                                                                                                                                                                                               |
      |                                   |       "iam:permissions:listRolesForAgencyOnProject",                                                                                                                                                                                                                                                                                                          |
      |                                   |       "iam:permissions:listRolesForAgency"                                                                                                                                                                                                                                                                                                                    |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to enable load balancing.

   Load balancer information is displayed.

#. In the **Listener** area, click |image1| to configure listener information.

   .. table:: **Table 4** Listener configuration

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                  |
      +===================================+==============================================================================================================================================================================================+
      | Frontend Protocol                 | Protocol used by the client and listener to distribute traffic.                                                                                                                              |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select **HTTP** or **HTTPS**.                                                                                                                                                                |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select this protocol based on your connectivity needs.                                                                                                                                       |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Frontend Port                     | Port used by the client and listener to distribute traffic.                                                                                                                                  |
      |                                   |                                                                                                                                                                                              |
      |                                   | Set this parameter based on site requirements.                                                                                                                                               |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | SSL Authentication                | Client authentication mode. Set this parameter only when **Frontend Protocol** is set to **HTTPS**.                                                                                          |
      |                                   |                                                                                                                                                                                              |
      |                                   | Both one-way and two-way authentication are supported.                                                                                                                                       |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select an authentication mode that suits your needs.                                                                                                                                         |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Server Certificate                | The server certificate is used for SSL handshake. The certificate content and private key must be provided. It is required only when **Frontend Protocol** is set to **HTTPS**.              |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select the server certificate created on ELB.                                                                                                                                                |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | CA Certificate                    | Also called client CA public key certificate. It is used to verify the issuer of a client certificate. It is required only when **SSL Authentication** is set to **Two-way authentication**. |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select the CA certificate created on ELB.                                                                                                                                                    |
      |                                   |                                                                                                                                                                                              |
      |                                   | When HTTPS two-way authentication is enabled, an HTTPS connection can be established only when the client can provide the certificate issued by a trusted CA.                                |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


   .. figure:: /_static/images/en-us_image_0000002416194325.png
      :alt: **Figure 1** Configuring a listener

      **Figure 1** Configuring a listener

#. (Optional) In the **Listener** area, click **Configure** next to **Access Control** to go to the listener list of the load balancer. Click Configure in the Access Control column of a listener to configure access control for that listener. For more information, see section "What Is Access Control?" in *Elastic Load Balance User Guide*.

   Without access control policies, all IP addresses are allowed to access the CSS cluster through this load balancer, which may create security risks.

#. In the **Health Check** area, you can check the health check result for each node IP address.

   .. table:: **Table 5** Health check result description

      =================== ====================================
      Health Check Result Description
      =================== ====================================
      Normal              The node IP address is connected.
      Abnormal            The node IP address is disconnected.
      =================== ====================================

#. If the cluster no longer needs a dedicated load balancer, disassociate it to release resources.

   Choose **Load Balancing** > **OpenSearch**, toggle off **Load Balancing**. In the displayed dialog box, click **OK**.

   .. caution::

      After the load balancer is disassociated, any listener or backend server group configurations will be permanently deleted.

Accessing a Cluster Through a Load Balancer by Executing cURL Commands
----------------------------------------------------------------------

#. In the left navigation pane on the CSS console, choose **Clusters**.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Cluster Access** tab, and then click the **Load Balancing** tab. On the **OpenSearch** tab, record the private or public IP address or IPv6 address of the load balancer, as well as the frontend protocol/port of the listener.

   .. caution::

      You are not advised to connect a load balancer that has been associated with a public IP address to a non-security mode cluster. Access from the public network using such a load balancer may cause security risks because a non-security mode cluster can be accessed using HTTP without security authentication.

#. Run the following cURL commands on an ECS to check whether the dedicated load balancer can connect to the cluster.

   .. table:: **Table 6** Commands for accessing different types of clusters

      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      | Security Mode         | Service Form Provided by ELB for External Systems | cURL Command for Accessing a Cluster                                                         |
      +=======================+===================================================+==============================================================================================+
      | Non-security mode     | No authentication                                 | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl  http://IP:port                                                                      |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      |                       | One-way authentication                            | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl --cacert ./ca.crt https://IP:port                                                    |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      |                       | Two-way authentication                            | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl --cacert ./ca.crt --cert ./client.crt --key ./client.key https://IP:port             |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      | Security mode + HTTP  | Password authentication                           | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl  http://IP:port -u user:pwd                                                          |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      |                       | One-way authentication + Password authentication  | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl --cacert ./ca.crt https://IP:port -u user:pwd                                        |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      |                       | Two-way authentication + Password authentication  | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl --cacert ./ca.crt --cert ./client.crt --key ./client.key https://IP:port -u user:pwd |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      | Security mode + HTTPS | One-way authentication + Password authentication  | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl --cacert ./ca.crt https://IP:port -u user:pwd                                        |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      |                       | Two-way authentication + Password authentication  | .. code-block::                                                                              |
      |                       |                                                   |                                                                                              |
      |                       |                                                   |    curl --cacert ./ca.crt --cert ./client.crt --key ./client.key https://IP:port -u user:pwd |
      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+

   .. table:: **Table 7** Variables

      +----------+----------------------------------------------------------------------------------------------+
      | Variable | Description                                                                                  |
      +==========+==============================================================================================+
      | IP       | IP address of a load balancer instance.                                                      |
      +----------+----------------------------------------------------------------------------------------------+
      | port     | Frontend protocol and port configured for the listener.                                      |
      +----------+----------------------------------------------------------------------------------------------+
      | user     | Username of the cluster. This parameter is required only for a security-mode cluster.        |
      +----------+----------------------------------------------------------------------------------------------+
      | pwd      | Password of the username above. This parameter is required only for a security-mode cluster. |
      +----------+----------------------------------------------------------------------------------------------+

   If cluster information is returned, the connection is successful.

See also: :ref:`Sample Code for ESSecuredClientWithCerDemo <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section1146765293619>`, :ref:`Sample Code for SecuredHttpClientConfigCallback <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section177951919193614>`, and :ref:`pom.xml Sample Code <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section5394175153518>`.

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section1146765293619:

Sample Code for ESSecuredClientWithCerDemo
------------------------------------------

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
               // Search by using match_all, which is equivalent to {\"query\": {\"match_all\": {}}}.
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

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section177951919193614:

Sample Code for SecuredHttpClientConfigCallback
-----------------------------------------------

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

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section5394175153518:

pom.xml Sample Code
-------------------

::

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

.. |image1| image:: /_static/images/en-us_image_0000002382515146.png
