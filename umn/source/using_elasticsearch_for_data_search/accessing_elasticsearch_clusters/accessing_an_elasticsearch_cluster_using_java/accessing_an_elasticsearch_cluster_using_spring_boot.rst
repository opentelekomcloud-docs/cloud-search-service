:original_name: css_01_0389.html

.. _css_01_0389:

Accessing an Elasticsearch Cluster Using Spring Boot
====================================================

You can access a CSS cluster using Spring Boot. Spring Boot can connect to a cluster in any of the following ways:

-  :ref:`Accessing an HTTP Cluster Through Spring Boot <css_01_0389__en-us_topic_0000001961178861_section197550282614>`: applicable to clusters in non-security mode and clusters in security mode+HTTP
-  :ref:`Using Spring Boot to Access an HTTPS Cluster (Without Using Any Security Certificate) <css_01_0389__en-us_topic_0000001961178861_section1523020817518>`: suitable for clusters in security mode+HTTPS
-  :ref:`Using Spring Boot to Access an HTTPS Cluster (Using a Security Certificate) <css_01_0389__en-us_topic_0000001961178861_section1368184211106>`: suitable for clusters in security mode+HTTPS

.. note::

   For details about how to use Spring Boot, see the official document: https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/

Precautions
-----------

-  You are advised to use the Elasticsearch Rest High Level Client version that matches the Elasticsearch version. For example, use Rest High Level Client 7.10.2 to access an Elasticsearch 7.10.2 cluster.
-  This section uses Spring Boot 2.5.5 as an example to describe how to connect Spring Boot to a cluster. The corresponding Spring Data Elasticsearch version is 4.2.\ *x*.

Prerequisites
-------------

-  The CSS cluster is available.

-  Ensure that the server running Java can communicate with the CSS cluster.

-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Network Configuration <css_01_0381__section855085010198>`.

-  Install JDK 1.8 on the server. You can download JDK 1.8 from: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

-  Create a Spring Boot project.

-  Declare Java dependencies.

   *7.10.2* indicates the version of the Elasticsearch Java client.

   -  Maven mode:

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

.. _css_01_0389__en-us_topic_0000001961178861_section197550282614:

Accessing an HTTP Cluster Through Spring Boot
---------------------------------------------

This scenario applies to clusters in non-security mode or clusters in security mode+HTTP.

Configuration file:

::

   elasticsearch.url=host1:9200,host2:9200
   // You do not need to configure the following two lines for a non-security cluster.
   elasticsearch.username=username
   elasticsearch.password=password

.. table:: **Table 1** Parameter description

   ========= ===================================================
   Parameter Description
   ========= ===================================================
   host      IP address for accessing the Elasticsearch cluster.
   username  Username for accessing the cluster.
   password  Password of the user.
   ========= ===================================================

Code:

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

   @Configuration
   @EnableElasticsearchRepositories(basePackages = "com.xxx.repository")
   @ComponentScan(basePackages = "com.xxx")
   public class Config extends AbstractElasticsearchConfiguration {

       @Value("${elasticsearch.url}")
       public String elasticsearchUrl;

       // You do not need to set the following two parameters for a non-security cluster.
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

.. _css_01_0389__en-us_topic_0000001961178861_section1523020817518:

Using Spring Boot to Access an HTTPS Cluster (Without Using Any Security Certificate)
-------------------------------------------------------------------------------------

You can connect to a cluster in Security mode + HTTPS without using any security certificate.

Configuration file:

::

   elasticsearch.url=host1:9200,host2:9200
   elasticsearch.username=username
   elasticsearch.password=password

.. table:: **Table 2** Parameter description

   ========= ===================================================
   Parameter Description
   ========= ===================================================
   host      IP address for accessing the Elasticsearch cluster.
   username  Username for accessing the cluster.
   password  Password of the user.
   ========= ===================================================

Code:

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
   @EnableElasticsearchRepositories(basePackages = "com.xxx.repository")
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

.. _css_01_0389__en-us_topic_0000001961178861_section1368184211106:

Using Spring Boot to Access an HTTPS Cluster (Using a Security Certificate)
---------------------------------------------------------------------------

You can use a security certificate to connect to a cluster in security mode + HTTPS.

#. Obtain the security certificate **CloudSearchService.cer**.

   a. Log in to the CSS management console.
   b. In the navigation pane, choose **Clusters**. The cluster list is displayed.
   c. Click the name of a cluster to go to the cluster details page.
   d. On the **Configuration** page, click **Download Certificate** next to **HTTPS Access**.

#. Convert the security certificate **CloudSearchService.cer**. Upload the downloaded security certificate to the client and use keytool to convert the .cer certificate into a .jks certificate that can be read by Java.

   -  In Linux, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

   -  In Windows, run the following command to convert the certificate:

      .. code-block::

         keytool -import -alias newname -keystore .\truststore.jks -file .\CloudSearchService.cer

   In the preceding command, *newname* indicates the user-defined certificate name.

   After this command is executed, you will be prompted to set the certificate password and confirm the password. Securely store the password. It will be used for accessing the cluster.

#. **application.properties** configuration file:

   ::

      elasticsearch.url=host1:9200,host2:9200
      elasticsearch.username=username
      elasticsearch.password=password

   .. table:: **Table 3** Parameter description

      ========= ===================================================
      Parameter Description
      ========= ===================================================
      host      IP address for accessing the Elasticsearch cluster.
      username  Username for accessing the cluster.
      password  Password of the user.
      ========= ===================================================

#. Code:

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
      @EnableElasticsearchRepositories(basePackages = "com.xxx.repository")
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
                  TrustManager[] tm = {new MyX509TrustManager(cerFilePath, cerPassword)};
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
          public static class NullHostNameVerifier implements HostnameVerifier {
              @Override
              public boolean verify(String arg0, SSLSession arg1) {
                  return true;
              }
          }
      }

   In the preceding command, *cerFilePath* and *cerPassword* indicate the path and password of the .jks certificate, respectively.
