:original_name: css_01_0182.html

.. _css_01_0182:

Configuring a Dedicated Load Balancer
=====================================

In big data processing scenarios, load balancers are essential for distributing traffic and improving the availability and performance of OpenSearch clusters. However, default shared load balancers have functional and performance limitations, making them inadequate for complex, high-concurrency data processing. Dedicated load balancers, with their richer features and superior performance, offer a more robust solution. This topic describes how to configure dedicated load balancers for more efficient and secure cluster access.

Overview
--------

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
-  HTTPS-enabled security-mode clusters do not support HTTP-based frontend authentication. If the frontend uses HTTP, disable security mode for your cluster first. For details, see :ref:`Changing the Security Mode <css_01_0310>`. Before changing the security mode, disable load balancing first. After the security mode is changed, enable load balancing again.

Prerequisites
-------------

-  A dedicated load balancer has been created. For details, see `Creating a Dedicated Load Balancer <https://docs.otc.t-systems.com/elastic-load-balancing/umn/load_balancer/creating_a_dedicated_load_balancer.html>`__. This load balancer must meet the following requirements:

   -  Its VPC is the same as that of the CSS cluster. The network between the two is connected.
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

#. In the **Listener** area, click |image1| to configure a listener to ensure proper accessibility of the CSS cluster.

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

#. (Optional) In the **Listener** area, click **Configure** next to **Access Control** to go to the listener list of the load balancer. Click Configure in the Access Control column of a listener to configure access control for that listener. You can specify IP addresses that are allowed to access your cluster for enhanced security. For more information, see section "What Is Access Control?" in *Elastic Load Balance User Guide*.

   .. warning::

      Without access control policies, all IP addresses are allowed to access the CSS cluster through this load balancer, which may create security risks.

#. In the **Health Check** area, you can check the health check results for each node IP address, ensuring that each node in the cluster is functioning properly.

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
      |                       |                                                   |    curl http://IP:port                                                                       |
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
      |                       |                                                   |    curl http://IP:port -u user:pwd                                                           |
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

See also: :ref:`Sample Code for OpenSearchDemo <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section1146765293619>` and :ref:`pom.xml Sample Code <en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section5394175153518>`.

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section1146765293619:

Sample Code for OpenSearchDemo
------------------------------

.. code-block::

   package org.example;

   import java.io.ByteArrayInputStream;
   import java.io.File;
   import java.io.FileInputStream;
   import java.io.IOException;
   import java.io.InputStream;
   import java.net.URI;
   import java.net.http.HttpClient;
   import java.net.http.HttpRequest;
   import java.net.http.HttpResponse;
   import java.nio.charset.StandardCharsets;
   import java.security.KeyStore;
   import java.security.SecureRandom;
   import java.security.cert.CertificateFactory;
   import java.security.cert.X509Certificate;
   import java.util.Base64;

   import javax.net.ssl.KeyManagerFactory;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.SSLHandshakeException;
   import javax.net.ssl.TrustManagerFactory;

   public class OpensearchDemo {
       private static final String TRUSTED_CA_PATH = "path\\ca.pem"; // CA certificate path
       private static final String PKCS12_PATH = "path\\client.p12"; // Client certificate path
       private static final String KEY_PASSWORD = ""; // Client certificate password
       private static final String HOST_NAME = ""; // ELB IP address or domain name
       private static final int PORT = 9200; //ELB port
       private static final String ELB_URL = "https://" + HOST_NAME + ":" + PORT;
       private static final String OS_USER = ""; // OpenSearch username
       private static final String OS_PASS = ""; // OpenSearch user password
       public static void main(String[] args) throws Exception {
           // 1. Create a standard SSLContext.
           SSLContext sslContext = createStrictMtlsSslContext();
           // 2. Inject the SSLContext.
           HttpClient client = HttpClient.newBuilder()
               .sslContext(sslContext)
               .connectTimeout(java.time.Duration.ofSeconds(10))
               .build();
           String authHeader = getBasicAuthHeader(OS_USER, OS_PASS);
           HttpRequest request = HttpRequest.newBuilder()
               .uri(URI.create(ELB_URL + "/_cat/indices?v"))
               .GET()
               .header("Accept", "application/json")
               .header("Authorization", authHeader)
               .build();
           try {
               // Send a request.
               HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
               System.out.println("http statusCode: " + response.statusCode());
               System.out.println("response body:\n" + response.body());
           } catch (SSLHandshakeException e) {
               System.err.println("SSLHandshakeException: " + e.getMessage());
               e.printStackTrace();
           } catch (IOException e) {
               System.err.println("IOException: " + e.getMessage());
               e.printStackTrace();
           }
       }

       /**
        * Create an SSLContext.
        */
       private static SSLContext createStrictMtlsSslContext() throws Exception {
           // --- 1. Prepare a truststore (server authentication)---
           KeyStore trustStore = KeyStore.getInstance("PKCS12");
           trustStore.load(null, null);
           X509Certificate caCert = loadCertificate(TRUSTED_CA_PATH);
           trustStore.setCertificateEntry("ca-root", caCert);
           TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
           tmf.init(trustStore);
           // --- 2. Prepare a keystore (client identity)---
           KeyStore keyStore = KeyStore.getInstance("PKCS12");
           File p12File = new File(PKCS12_PATH);
           try (InputStream is = new FileInputStream(p12File)) {
               keyStore.load(is, KEY_PASSWORD.toCharArray());
           }
           KeyManagerFactory kmf = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
           kmf.init(keyStore, KEY_PASSWORD.toCharArray());
           // --- 3. Initialize the SSLContext (standard mode)---
           SSLContext sslContext = SSLContext.getInstance("TLSv1.3");
           sslContext.init(kmf.getKeyManagers(), tmf.getTrustManagers(), new SecureRandom());
           return sslContext;
       }

       private static X509Certificate loadCertificate(String path) throws Exception {
           try (InputStream is = new FileInputStream(path)) {
               String pem = new String(is.readAllBytes(), StandardCharsets.UTF_8);
               String base64 = pem.replace("-----BEGIN CERTIFICATE-----", "")
                   .replace("-----END CERTIFICATE-----", "")
                   .replaceAll("\\s+", "");
               byte[] der = Base64.getDecoder().decode(base64);
               CertificateFactory cf = CertificateFactory.getInstance("X.509");
               return (X509Certificate) cf.generateCertificate(new ByteArrayInputStream(der));
           }
       }
       private static String getBasicAuthHeader(String user, String pass) {
           String auth = user + ":" + pass;
           String encoded = Base64.getEncoder().encodeToString(auth.getBytes(StandardCharsets.UTF_8));
           return "Basic " + encoded;
       }
   }

.. _en-us_topic_0000001955726518__en-us_topic_0000001938377780_en-us_topic_0000001412998750_section5394175153518:

pom.xml Sample Code
-------------------

.. code-block::

   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>
       <groupId>org.example</groupId>
       <artifactId>opensearch-demo</artifactId>
       <version>1.0</version>

       <properties>
           <maven.compiler.source>17</maven.compiler.source>
           <maven.compiler.target>17</maven.compiler.target>
           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
       </properties>

       <dependencies>
           <dependency>
               <groupId>org.opensearch.client</groupId>
               <artifactId>opensearch-java</artifactId>
               <version>2.19.0</version>
           </dependency>

           <dependency>
               <groupId>org.opensearch.client</groupId>
               <artifactId>opensearch-rest-client</artifactId>
               <version>2.19.0</version>
           </dependency>

           <dependency>
               <groupId>org.apache.httpcomponents.client5</groupId>
               <artifactId>httpclient5</artifactId>
               <version>5.3.1</version>
           </dependency>

           <dependency>
               <groupId>com.fasterxml.jackson.core</groupId>
               <artifactId>jackson-databind</artifactId>
               <version>2.17.0</version>
           </dependency>
       </dependencies>
   </project>

.. |image1| image:: /_static/images/en-us_image_0000002382515146.png
