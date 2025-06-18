:original_name: css_01_0413.html

.. _css_01_0413:

Configuring a Dedicated Load Balancer for an Elasticsearch Cluster
==================================================================

CSS integrates shared load balancers, through which you can enable access to a cluster from the public network as well as through the VPC Endpoint service. Dedicated load balancers provide higher performance and more diverse features than shared load balancers. This topic describes how to configure a dedicated load balancer for a cluster.

Scenarios
---------

Advantages of connecting to a cluster through a dedicated load balancer:

-  A non-security cluster can also use the capabilities of the Elastic Load Balance (ELB) service.
-  You can use custom certificates for HTTPS two-way authentication.
-  Seven-layer traffic monitoring and alarm configuration are supported, allowing you to keep close track of the cluster status.

There are eight different ELB service forms for clusters in different security modes to connect to a dedicated load balancer. :ref:`Table 1 <css_01_0413__en-us_topic_0000001463358273_table4446327845>` describes the ELB capabilities for different cluster configurations. :ref:`Table 2 <css_01_0413__en-us_topic_0000001463358273_table1537163912019>` describes the configurations for different ELB service forms.

.. _css_01_0413__en-us_topic_0000001463358273_table4446327845:

.. table:: **Table 1** ELB capabilities for different clusters

   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security Mode         | Service Form Provided by ELB for External Systems | ELB Load Balancing | ELB Traffic Monitoring | ELB Two-way Authentication |
   +=======================+===================================================+====================+========================+============================+
   | Non-security          | No authentication                                 | Yes                | Yes                    | No                         |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication                            | Yes                | Yes                    | Yes                        |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication                            |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTP  | Password authentication                           | Yes                | Yes                    | No                         |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication + Password authentication  | Yes                | Yes                    | Yes                        |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTPS | One-way authentication + Password authentication  | Yes                | Yes                    | Yes                        |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+

.. _css_01_0413__en-us_topic_0000001463358273_table1537163912019:

.. table:: **Table 2** Configurations for different ELB service forms depending on the cluster

   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   | Security Mode         | Service Form Provided by ELB for External Systems | ELB Listener      | ELB Listener  | ELB Listener           | Backend Server Group | Backend Server Group | Backend Server Group          |
   +=======================+===================================================+===================+===============+========================+======================+======================+===============================+
   |                       |                                                   | Frontend Protocol | Frontend Port | SSL Authentication     | Backend Protocol     | Health Check Port    | Health Check Path             |
   +-----------------------+---------------------------------------------------+-------------------+---------------+------------------------+----------------------+----------------------+-------------------------------+
   | Non-security          | No authentication                                 | HTTP              | 9200          | No authentication      | HTTP                 | 9200                 | /                             |
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

To connect a CSS cluster to a dedicated load balancer, perform the following steps:

#. If the ELB listener uses HTTPS, prepare a signature certificate and upload it to the ELB console: :ref:`Preparing and Uploading a Self-Signed Certificate <css_01_0413__section7363183565716>`
#. Create a dedicated load balancer on the ELB console: :ref:`Creating a Dedicated Load Balancer <css_01_0413__en-us_topic_0000001463438465_section7323118163219>`
#. Enable load balancing for the cluster: :ref:`Connecting a Cluster to a Load Balancer <css_01_0413__section1566363619613>`
#. Connect to the cluster through an instance of a dedicated load balancer: :ref:`Accessing a Cluster Using cURL Commands <css_01_0413__en-us_topic_0000001463438465_section6525113933311>`

See also: :ref:`Sample Code for ESSecuredClientWithCerDemo <css_01_0413__en-us_topic_0000001412998750_section1146765293619>`, :ref:`Sample Code for SecuredHttpClientConfigCallback <css_01_0413__en-us_topic_0000001412998750_section177951919193614>`, and :ref:`pom.xml Sample Code <css_01_0413__en-us_topic_0000001412998750_section5394175153518>`.

Constraints
-----------

-  You are not advised to connect a load balancer that has been associated with a public IP address to a non-security mode cluster. Access from the public network using such a load balancer may cause security risks because a non-security mode cluster can be accessed using HTTP without security authentication.
-  HTTPS-enabled security-mode clusters do not support HTTP-based frontend authentication. If the frontend uses HTTP, disable security mode for the clusters first. For details, see :ref:`Changing the Security Mode of an Elasticsearch Cluster <css_01_0158>`. Before changing the security mode, disable load balancing first. After the security mode is changed, enable load balancing again.

.. _css_01_0413__section7363183565716:

Preparing and Uploading a Self-Signed Certificate
-------------------------------------------------

If the ELB listener uses HTTPS, prepare a self-signed certificate by referring to the steps in this section and upload it to the ELB console as a server certificate or CA certificate.

.. note::

   You are advised to use a certificate purchased in Cloud Certificate Manager (CCM) or issued by a trusted authority.

#. Log in to a Linux client where the OpenSSL tool and JDK are installed.

#. Run the following commands to create a self-signed certificate:

   ::

      mkdir ca
      mkdir server
      mkdir client

      #Use OpenSSL to create a CA certificate.
      cd ca
      #Create the OpenSSL configuration file ca_cert.conf for the CA certificate.
      cat >ca_cert.conf <<EOF
      [ req ]
      distinguished_name     = req_distinguished_name
      prompt                 = no

      [ req_distinguished_name ]
       O                      = ELB
      EOF
      #Create private key file ca.key for the CA certificate.
      openssl genrsa -out ca.key 2048
      #Create the CSR file ca.csr for the CA certificate.
      openssl req -out ca.csr -key ca.key -new -config ./ca_cert.conf
      #Create a self-signed CA certificate ca.crt.
      openssl x509 -req -in ca.csr -out ca.crt -sha1 -days 5000 -signkey ca.key
      #Convert the CA certificate format to p12.
      openssl pkcs12 -export -clcerts -in ca.crt -inkey ca.key -out ca.p12
      #Convert the CA certificate format to JKS.
      keytool -importkeystore -srckeystore ca.p12 -srcstoretype PKCS12 -deststoretype JKS -destkeystore ca.jks


      #Use the CA certificate to issue a server certificate.
      cd ../server
      #Create the OpenSSL configuration file server_cert.conf for the server certificate. Change the CN field to the domain name or IP address of the server as required.
      cat >server_cert.conf <<EOF
      [ req ]
      distinguished_name     = req_distinguished_name
      prompt                 = no

      [ req_distinguished_name ]
       O                      = ELB
       CN                     = 127.0.0.1
      EOF
      #Create the private key file server.key for the server certificate.
      openssl genrsa -out server.key 2048
      #Create the CSR request file server.csr for the server certificate.
      openssl req -out server.csr -key server.key -new -config ./server_cert.conf
      #Use the CA certificate to issue the server certificate server.crt.
      openssl x509 -req -in server.csr -out server.crt -sha1 -CAcreateserial -days 5000 -CA ../ca/ca.crt -CAkey ../ca/ca.key
      #Convert the server certificate format to p12.
      openssl pkcs12 -export -clcerts -in server.crt -inkey server.key -out server.p12
      #Convert the service certificate format to JKS.
      keytool -importkeystore -srckeystore server.p12 -srcstoretype PKCS12 -deststoretype JKS -destkeystore server.jks


      #Use the CA certificate to issue a client certificate.
      cd ../client
      #Create the OpenSSL configuration file client_cert.conf for the client certificate. Change the CN field to the domain name or IP address of the server as required.
      cat >client_cert.conf <<EOF
      [ req ]
      distinguished_name     = req_distinguished_name
      prompt                 = no

      [ req_distinguished_name ]
      O                      = ELB
      CN                     = 127.0.0.1
      EOF
      #Create private key client.key for the client certificate.
      openssl genrsa -out client.key 2048
      #Create the CSR file client.csr for the client certificate.
      openssl req -out client.csr -key client.key -new -config ./client_cert.conf
      #Use the CA certificate to issue the client certificate client.crt.
      openssl x509 -req -in client.csr -out client.crt -sha1 -CAcreateserial -days 5000 -CA ../ca/ca.crt -CAkey ../ca/ca.key
      #Convert the client certificate to a p12 file that can be identified by the browser.
      openssl pkcs12 -export -clcerts -in client.crt -inkey client.key -out client.p12
      #Convert the client certificate format to JKS.
      keytool -importkeystore -srckeystore client.p12 -srcstoretype PKCS12 -deststoretype JKS -destkeystore client.jks

#. Upload the self-signed certificate. For details, see `Configuring the Server Certificate and Private Key <https://docs.otc.t-systems.com/elastic-load-balancing/umn/advanced_features_of_http_https_listeners/mutual_authentication.html#configuring-the-server-certificate-and-private-key>`__.

.. _css_01_0413__en-us_topic_0000001463438465_section7323118163219:

Creating a Dedicated Load Balancer
----------------------------------

#. Log in to the ELB management console.

#. Create a dedicated load balancer. For details, see `Creating a Dedicated Load Balancer <https://docs.otc.t-systems.com/elastic-load-balancing/umn/load_balancer/creating_a_dedicated_load_balancer.html>`__. :ref:`Table 3 <css_01_0413__en-us_topic_0000001463438465_table937081413137>` describes the parameters required for connecting a CSS cluster with a dedicated load balancer.

   .. _css_01_0413__en-us_topic_0000001463438465_table937081413137:

   .. table:: **Table 3** Parameters for connecting a CSS cluster with a dedicated load balancer

      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | Parameter             | Description                                                                                                                                                                                                                                                                      | Example                                 |
      +=======================+==================================================================================================================================================================================================================================================================================+=========================================+
      | Type                  | Load balancer type. Select **Dedicated**.                                                                                                                                                                                                                                        | Dedicated                               |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | Billing Mode          | Billing mode of the dedicated load balancer.                                                                                                                                                                                                                                     | Pay-per-use                             |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | Region                | Region where the CSS cluster is located.                                                                                                                                                                                                                                         | ``-``                                   |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | IP as Backend Servers | A CSS cluster can be connected only after the cross-VPC backend is enabled.                                                                                                                                                                                                      | Enabled                                 |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | Network Type          | Type of the network used by the load balancer to provide services to external systems.                                                                                                                                                                                           | Private IPv4 network                    |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       | CSS supports **Private IPv4 network** and **IPv6 network**.                                                                                                                                                                                                                      |                                         |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       | -  When **IPv6 network** is selected, **Private IP Address** and **IPv6 address** are displayed under **Load balancing instance** after CSS is connected to the load balancer. **EIP** is displayed only when the dedicated load balancer is associated with a shared bandwidth. |                                         |
      |                       | -  When **Private IPv4 network** is selected, **Private IP Address** and **EIP** are displayed under **Load balancing instance** after CSS is connected to the load balancer.                                                                                                    |                                         |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       | .. note::                                                                                                                                                                                                                                                                        |                                         |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       |    CSS supports IPv6 networks only in the CN East 2 region. In other regions, only private IPv4 networks are supported.                                                                                                                                                          |                                         |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | VPC                   | VPC where the load balancer works. This parameter is mandatory no matter which network type is selected.                                                                                                                                                                         | ``-``                                   |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       | Select the VPC of the CSS cluster.                                                                                                                                                                                                                                               |                                         |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | Subnet                | Subnet where the load balancer is to be created. This parameter is mandatory no matter which network type is selected.                                                                                                                                                           | ``-``                                   |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       | Select the subnet of the CSS cluster.                                                                                                                                                                                                                                            |                                         |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
      | Specifications        | You are advised to select **Application load balancing (HTTP/HTTPS)**, which provides better functionality and performance.                                                                                                                                                      | Application load balancing (HTTP/HTTPS) |
      |                       |                                                                                                                                                                                                                                                                                  |                                         |
      |                       |                                                                                                                                                                                                                                                                                  | **Small I**                             |
      +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+

.. _css_01_0413__section1566363619613:

Connecting a Cluster to a Load Balancer
---------------------------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, select the cluster you want to connect to the load balancer and click the cluster name. The cluster information page is displayed.

#. In the navigation pane, choose **Load Balancing**. Toggle on **Load Balancing** and configure basic load balancing information.

   .. table:: **Table 4** Configuring load balancing

      +---------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter     | Description                                                                                                                                                                               |
      +===============+===========================================================================================================================================================================================+
      | Load Balancer | Select a dedicated load balancer created earlier. A CSS cluster is a managed resource. The selected load balancer becomes available only after **IP as Backend Servers** is enabled.      |
      +---------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Agency        | Select an IAM agency to authorize CSS to access and use ELB resources using the current account. The selected agency must include the **ELB Administrator** or **ELB FullAccess** policy. |
      +---------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


   .. figure:: /_static/images/en-us_image_0000001951397478.png
      :alt: **Figure 1** Enabling load balancing

      **Figure 1** Enabling load balancing

#. Click **OK** to enable load balancing.

#. In the **Listener Configuration** area, click |image1| to configure listener information.

   .. table:: **Table 5** Listener configuration

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                  |
      +===================================+==============================================================================================================================================================================================+
      | Frontend Protocol                 | Protocol used by the client and listener to distribute traffic. Select **HTTP** or **HTTPS**.                                                                                                |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select a protocol as required.                                                                                                                                                               |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Frontend Port                     | Port used by the client and listener to distribute traffic.                                                                                                                                  |
      |                                   |                                                                                                                                                                                              |
      |                                   | Set this parameter based on site requirements.                                                                                                                                               |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | SSL Authentication                | Authentication mode for the client to access the server. Set this parameter only when **Frontend Protocol** is set to **HTTPS**.                                                             |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select an authentication mode that suits your needs.                                                                                                                                         |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Server Certificate                | The server certificate is used for SSL handshake. The certificate content and private key must be provided. It is required only when **Frontend Protocol** is set to **HTTPS**.              |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select the server certificate created in :ref:`Preparing and Uploading a Self-Signed Certificate <css_01_0413__section7363183565716>`.                                                       |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | CA Certificate                    | Also called client CA public key certificate. It is used to verify the issuer of a client certificate. It is required only when **SSL Authentication** is set to **Two-way authentication**. |
      |                                   |                                                                                                                                                                                              |
      |                                   | Select the CA certificate created in :ref:`Preparing and Uploading a Self-Signed Certificate <css_01_0413__section7363183565716>`.                                                           |
      |                                   |                                                                                                                                                                                              |
      |                                   | When HTTPS two-way authentication is enabled, an HTTPS connection can be established only when the client can provide the certificate issued by a trusted CA.                                |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


   .. figure:: /_static/images/en-us_image_0000001951401518.png
      :alt: **Figure 2** Listener configuration

      **Figure 2** Listener configuration

#. (Optional) In the Listener Configuration area, click **Settings** next to **Access Control** to go to the **Listeners** page of the load balancer. Click **Configure** in the **Access Control** column to configure the list of IP addresses that are allowed to access the cluster through the load balancer. If this parameter is not set, all IP addresses will be allowed to access the cluster.

#. In the **Health Check** area, you can view the health check result for each node IP address.

   .. table:: **Table 6** Health check result description

      =================== ====================================
      Health Check Result Description
      =================== ====================================
      Normal              The node IP address is connected.
      Abnormal            The node IP address is disconnected.
      =================== ====================================

.. _css_01_0413__en-us_topic_0000001463438465_section6525113933311:

Accessing a Cluster Using cURL Commands
---------------------------------------

#. In the navigation pane on the left, choose **Clusters**.

#. On the **Clusters** page, click the name of the cluster you want to access. The **Cluster Information** page is displayed.

#. In the navigation pane, choose **Load Balancing**. Record the private or public IP address or IPv6 address of the load balancer, as well as the frontend protocol/port of the listener.

   .. note::

      You are not advised to connect a load balancer that has been associated with a public IP address to a non-security mode cluster. Access from the public network using such a load balancer may cause security risks because a non-security mode cluster can be accessed using HTTP without security authentication.

#. Run the following cURL commands on an ECS to check whether the dedicated load balancer can connect to the cluster.

   .. table:: **Table 7** Commands for accessing different types of clusters

      +-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------+
      | Security Mode         | Service Form Provided by ELB for External Systems | cURL Command for Accessing a Cluster                                                         |
      +=======================+===================================================+==============================================================================================+
      | Non-security          | No authentication                                 | .. code-block::                                                                              |
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

   .. table:: **Table 8** Variables

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

.. _css_01_0413__en-us_topic_0000001412998750_section1146765293619:

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

.. _css_01_0413__en-us_topic_0000001412998750_section177951919193614:

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

.. _css_01_0413__en-us_topic_0000001412998750_section5394175153518:

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

.. |image1| image:: /_static/images/en-us_image_0000001983636885.png
