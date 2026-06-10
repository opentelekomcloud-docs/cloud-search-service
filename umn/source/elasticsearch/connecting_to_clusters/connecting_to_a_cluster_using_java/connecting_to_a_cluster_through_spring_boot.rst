:original_name: css_01_0068.html

.. _css_01_0068:

Connecting to a Cluster Through Spring Boot
===========================================

Working directly with Elasticsearch's underlying APIs can increase development complexity, such as additional code maintenance tasks. CSS Elasticsearch clusters support data query and management through Spring Data Elasticsearch (an integrated Elasticsearch component in the Spring Boot ecosystem). This component encapsulates official Elasticsearch Java APIs. Developers can use the Spring repository API or native query DSL to efficiently access clusters without working with underlying APIs. For details about how to use Spring Boot, see `Spring Boot <https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/>`__.

Prerequisites
-------------

-  The target Elasticsearch cluster is available.

-  The server that runs the Java code can communicate with the Elasticsearch cluster.

-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Obtaining the Cluster Access Address <en-us_topic_0000001975823337__section855085010198>`.

-  Java has been installed on the server and the JDK version is 1.8 or later. Download JDK 1.8 from `Java Downloads <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__.

-  The Spring Boot version has been confirmed. To ensure better compatibility, use a Java client that has the same version as the target Elasticsearch cluster.

   In this document, Spring Boot 2.5.5 is used as an example. The corresponding Spring Data Elasticsearch version is 4.2.x, and the target Elasticsearch cluster version is 7.10.2.

Preparations
------------

#. Check that the Spring Boot version you're using meets the compatibility requirements. For details, see the `official compatibility list <https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/versions.html>`__.

   In this document, Spring Boot 2.5.5 is used as an example. The corresponding Spring Data Elasticsearch version is 4.2.x, and the target Elasticsearch cluster version is 7.10.2.

#. Create a Spring Boot project.

#. Declare Java dependencies. Declare the Apache version in Maven mode.

   .. code-block::

      <parent>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-parent</artifactId>
          <version>2.5.5</version>
      </parent>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-web</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-elasticsearch</artifactId>
          </dependency>
          <dependency>
              <groupId>org.elasticsearch.client</groupId>
              <artifactId>elasticsearch-rest-high-level-client</artifactId>
              <version>7.10.2</version>
          </dependency>
      </dependencies>

Connecting to a Cluster
-----------------------

The sample code varies depending on the security mode settings of the target Elasticsearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------------------------------+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch Cluster Security-Mode Settings | Whether to Load a Security Certificate | Details                                                                                                                                                                  |
   +==============================================+========================================+==========================================================================================================================================================================+
   | Non-security mode                            | ``-``                                  | :ref:`Connecting to a Cluster That Uses HTTP Through Spring Boot <en-us_topic_0000002504464273__en-us_topic_0000001961178861_section197550282614>`                       |
   |                                              |                                        |                                                                                                                                                                          |
   | Security mode + HTTP                         |                                        |                                                                                                                                                                          |
   +----------------------------------------------+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                        | No                                     | :ref:`Connecting to a Cluster That Uses HTTPS via Spring Boot (Without a Certificate) <en-us_topic_0000002504464273__en-us_topic_0000001961178861_section1523020817518>` |
   +----------------------------------------------+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                        | Yes                                    | :ref:`Connecting to a Cluster That Uses HTTPS via Spring Boot (With a Certificate) <en-us_topic_0000002504464273__en-us_topic_0000001961178861_section1368184211106>`    |
   +----------------------------------------------+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002504464273__en-us_topic_0000001961178861_section197550282614:

Connecting to a Cluster That Uses HTTP Through Spring Boot
----------------------------------------------------------

The following are steps for using Spring Boot to connect to a non-security mode Elasticsearch cluster; or a security-mode Elasticsearch cluster that uses HTTP instead of HTTPS.

#. Configure the **application.properties** file.

   ::

      elasticsearch.url=host1:9200,host2:9200
      // You do not need to configure the following two lines for a non-security cluster.
      elasticsearch.username=username
      elasticsearch.password=password

   .. table:: **Table 2** Configuration parameters

      ========= ===================================
      Parameter Description
      ========= ===================================
      host      Address for accessing the cluster.
      username  Username for accessing the cluster.
      password  Password of the user.
      ========= ===================================

#. Configure the client code.

   ::

      package com.xxx.configuration;

      import org.elasticsearch.client.RestHighLevelClient;
      import org.springframework.beans.factory.annotation.Value;
      import org.springframework.context.annotation.Bean;
      import org.springframework.context.annotation.ComponentScan;
      import org.springframework.context.annotation.Configuration;
      import org.springframework.data.elasticsearch.client.ClientConfiguration;
      import org.springframework.data.elasticsearch.client.RestClients;
      import org.springframework.data.elasticsearch.config.AbstractElasticsearchConfiguration;
      import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;

      @Configuration
      // com.xxx.repository is the repository directory, which is defined by extends org.springframework.data.elasticsearch.repository.ElasticsearchRepository.
      @EnableElasticsearchRepositories(basePackages = "com.xxx.repository")
      // com.xxx indicates the project directory, for example, com.company.project.
      @ComponentScan(basePackages = "com.xxx")
      public class Config extends AbstractElasticsearchConfiguration {

          @Value("${elasticsearch.url}")
          public String elasticsearchUrl;

          // There is no need to set the following two parameters for a non-security cluster.
          @Value("${elasticsearch.username}")
          public String elasticsearchUsername;

          @Value("${elasticsearch.password}")
          public String elasticsearchPassword;

          @Override
          @Bean
          public RestHighLevelClient elasticsearchClient() {
              final ClientConfiguration clientConfiguration = ClientConfiguration.builder()
                  .connectedTo(StringHostParse(elasticsearchUrl))
                  // For a non-security cluster, there is no need to configure withBasicAuth.
                  .withBasicAuth(elasticsearchUsername, elasticsearchPassword)
                  .build();

              return RestClients.create(clientConfiguration).rest();
          }

          private String[] StringHostParse(String hostAndPorts) {
              return hostAndPorts.split(",");
          }
      }

#. If Spring Boot starts properly, the cluster is connected.

.. _en-us_topic_0000002504464273__en-us_topic_0000001961178861_section1523020817518:

Connecting to a Cluster That Uses HTTPS via Spring Boot (Without a Certificate)
-------------------------------------------------------------------------------

The following are steps for using Spring Boot to connect to a security-mode + HTTPS Elasticsearch cluster without loading a security certificate.

#. Configure the **application.properties** file.

   ::

      elasticsearch.url=host1:9200,host2:9200
      elasticsearch.username=username
      elasticsearch.password=password

   .. table:: **Table 3** Configuration parameters

      ========= ===================================
      Parameter Description
      ========= ===================================
      host      Address for accessing the cluster.
      username  Username for accessing the cluster.
      password  Password of the user.
      ========= ===================================

#. Configure the client code.

   ::

      package com.xxx.configuration;
      import org.elasticsearch.client.RestHighLevelClient;
      import org.springframework.beans.factory.annotation.Value;
      import org.springframework.context.annotation.Bean;
      import org.springframework.context.annotation.ComponentScan;
      import org.springframework.context.annotation.Configuration;
      import org.springframework.data.elasticsearch.client.ClientConfiguration;
      import org.springframework.data.elasticsearch.client.RestClients;
      import org.springframework.data.elasticsearch.config.AbstractElasticsearchConfiguration;
      import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;
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
      @Configuration
      // com.xxx.repository is the repository directory, which is defined by extends org.springframework.data.elasticsearch.repository.ElasticsearchRepository.
      @EnableElasticsearchRepositories(basePackages = "com.xxx.repository")
      // com.xxx indicates the project directory, for example, com.company.project.
      @ComponentScan(basePackages = "com.xxx")
      public class Config extends AbstractElasticsearchConfiguration {
          @Value("${elasticsearch.url}")
          public String elasticsearchUrl;
          @Value("${elasticsearch.username}")
          public String elasticsearchUsername;
          @Value("${elasticsearch.password}")
          public String elasticsearchPassword;
          @Override
          @Bean
          public RestHighLevelClient elasticsearchClient() {
              SSLContext sc = null;
              try {
                  sc = SSLContext.getInstance("SSL");
                  sc.init(null, trustAllCerts, new SecureRandom());
              } catch (KeyManagementException | NoSuchAlgorithmException e) {
                  e.printStackTrace();
              }
              final ClientConfiguration clientConfiguration = ClientConfiguration.builder()
                  .connectedTo(StringHostParse(elasticsearchUrl))
                  .usingSsl(sc, new NullHostNameVerifier())
                  .withBasicAuth(elasticsearchUsername, elasticsearchPassword)
                  .build();
              return RestClients.create(clientConfiguration).rest();
          }
          private String[] StringHostParse(String hostAndPorts) {
              return hostAndPorts.split(",");
          }
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
          public static class NullHostNameVerifier implements HostnameVerifier {
              @Override
              public boolean verify(String arg0, SSLSession arg1) {
                  return true;
              }
          }
      }

#. If Spring Boot starts properly, the cluster is connected.

.. _en-us_topic_0000002504464273__en-us_topic_0000001961178861_section1368184211106:

Connecting to a Cluster That Uses HTTPS via Spring Boot (With a Certificate)
----------------------------------------------------------------------------

The following are steps for using Spring Boot to connect to a security-mode + HTTPS Elasticsearch cluster while loading a security certificate.

#. :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000002504464273__section188511124109>`.

#. Configure the **application.properties** file.

   ::

      elasticsearch.url=host1:9200,host2:9200
      elasticsearch.username=username
      elasticsearch.password=password

   .. table:: **Table 4** Configuration parameters

      ========= ===================================
      Parameter Description
      ========= ===================================
      host      Address for accessing the cluster.
      username  Username for accessing the cluster.
      password  Password of the user.
      ========= ===================================

#. Configure the client code.

   .. note::

      -  **com.xxx** indicates the project directory, for example, **com.company.project**.
      -  **com.xxx.repository** is the repository directory, which is defined by **extends org.springframework.data.elasticsearch.repository.ElasticsearchRepository**.

   ::

      package com.xxx.configuration;
      import org.elasticsearch.client.RestHighLevelClient;
      import org.springframework.beans.factory.annotation.Value;
      import org.springframework.context.annotation.Bean;
      import org.springframework.context.annotation.ComponentScan;
      import org.springframework.context.annotation.Configuration;
      import org.springframework.data.elasticsearch.client.ClientConfiguration;
      import org.springframework.data.elasticsearch.client.RestClients;
      import org.springframework.data.elasticsearch.config.AbstractElasticsearchConfiguration;
      import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;
      import java.io.File;
      import java.io.FileInputStream;
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
      @Configuration
      // com.xxx.repository is the repository directory, which is defined by extends org.springframework.data.elasticsearch.repository.ElasticsearchRepository.
      @EnableElasticsearchRepositories(basePackages = "com.xxx.repository")
      // com.xxx indicates the project directory, for example, com.company.project.
      @ComponentScan(basePackages = "com.xxx")
      public class Config extends AbstractElasticsearchConfiguration {
          @Value("${elasticsearch.url}")
          public String elasticsearchUrl;
          @Value("${elasticsearch.username}")
          public String elasticsearchUsername;
          @Value("${elasticsearch.password}")
          public String elasticsearchPassword;
          @Override
          @Bean
          public RestHighLevelClient elasticsearchClient() {
              SSLContext sc = null;
              try {
                  // certFilePath and certPassword are the path and password of the security certificate.
                  TrustManager[] tm = {new MyX509TrustManager(certFilePath, certPassword)};
                  sc = SSLContext.getInstance("SSL", "SunJSSE");
                  sc.init(null, tm, new SecureRandom());
              } catch (Exception e) {
                  e.printStackTrace();
              }
              final ClientConfiguration clientConfiguration = ClientConfiguration.builder()
                  .connectedTo(StringHostParse(elasticsearchUrl))
                  .usingSsl(sc, new NullHostNameVerifier())
                  .withBasicAuth(elasticsearchUsername, elasticsearchPassword)
                  .build();
              return RestClients.create(clientConfiguration).rest();
          }

          private String[] StringHostParse(String hostAndPorts) {
              return hostAndPorts.split(",");
          }

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
          public static class NullHostNameVerifier implements HostnameVerifier {
              @Override
              public boolean verify(String arg0, SSLSession arg1) {
                  return true;
              }
          }
      }

#. If Spring Boot starts properly, the cluster is connected.

.. _en-us_topic_0000002504464273__section188511124109:

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
