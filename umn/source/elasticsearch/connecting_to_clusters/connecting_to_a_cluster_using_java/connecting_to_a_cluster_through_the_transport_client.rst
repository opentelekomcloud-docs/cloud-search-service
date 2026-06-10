:original_name: css_01_0067.html

.. _css_01_0067:

Connecting to a Cluster Through the Transport Client
====================================================

When using Elasticsearch for data query and management, many users rely on the Java-based Transport Client that simplifies interaction with Elasticsearch clusters by encapsulating native APIs. You can work with CSS Elasticsearch clusters through the Transport Client, for which you only need to construct the required structures.

.. caution::

   The Transport Client has been marked deprecated in Elasticsearch 7.0. To ensure better compatibility and feature support, you are advised to use the Java High Level REST Client.

Prerequisites
-------------

-  The target Elasticsearch cluster is available and the security mode is disabled for it. (The Transport Client can only be used to access non-security mode clusters.)
-  The server that runs the Java code can communicate with the Elasticsearch cluster.
-  The cluster's private network address has been obtained. For details, see :ref:`Obtaining the Cluster Access Address <en-us_topic_0000001975823337__section855085010198>`. Given that the Transport Client can only be used to access non-security mode clusters, it can only do so through a private network address.
-  Java has been installed on the server and the JDK version is 1.8 or later. Download JDK 1.8 from `Java Downloads <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__.
-  The Transport Client version has been confirmed. To ensure better compatibility, use a Transport Client that has the same version as the target Elasticsearch cluster.

Introducing Dependencies
------------------------

Introduce the required Java dependencies on the server where you run Java code. Declare the Apache version in Maven mode.

Replace 7.10.2 with the actual Java client version.

.. code-block::

   <dependency>
       <groupId>org.elasticsearch.client</groupId>
       <artifactId>transport</artifactId>
       <version>7.10.2</version>
   </dependency>
   <dependency>
       <groupId>org.elasticsearch</groupId>
       <artifactId>elasticsearch</artifactId>
       <version>7.10.2</version>
   </dependency>

Connecting to a Cluster
-----------------------

Use the Transport Client to connect to an Elasticsearch cluster for which the security mode is disabled, and query whether the **test** index exists. The sample code is as follows:

::

   import org.elasticsearch.action.ActionFuture;
   import org.elasticsearch.action.admin.indices.exists.indices.IndicesExistsRequest;
   import org.elasticsearch.action.admin.indices.exists.indices.IndicesExistsResponse;
   import org.elasticsearch.client.transport.TransportClient;
   import org.elasticsearch.common.settings.Settings;
   import org.elasticsearch.common.transport.TransportAddress;
   import org.elasticsearch.transport.client.PreBuiltTransportClient;

   import java.net.InetAddress;
   import java.net.UnknownHostException;
   import java.util.concurrent.ExecutionException;

   public class Main {
       public static void main(String[] args) throws ExecutionException, InterruptedException, UnknownHostException {
           String cluster_name = "xxx";
           String host1 = "xx.xx.xx.xx";
           String host2 = "yy.yy.yy.yy";
           Settings settings = Settings.builder()
               .put("client.transport.sniff",false)
               .put("cluster.name", cluster_name)
               .build();
           TransportClient client = new PreBuiltTransportClient(settings)
               .addTransportAddress(new TransportAddress(InetAddress.getByName(host1), 9300))
               .addTransportAddress(new TransportAddress(InetAddress.getByName(host2), 9300));
           IndicesExistsRequest indicesExistsRequest = new IndicesExistsRequest("test");
           ActionFuture<IndicesExistsResponse> exists = client.admin().indices().exists(indicesExistsRequest);
           System.out.println(exists.get().isExists());
       }
   }

In the information above, *cluster_name* indicates the cluster name, and *host1* and *host2* indicate the IP addresses of the cluster nodes. You can run the **GET \_cat/nodes** command to obtain the IP addresses of the nodes.

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.
