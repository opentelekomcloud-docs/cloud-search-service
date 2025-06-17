:original_name: css_01_0388.html

.. _css_01_0388:

Accessing an Elasticsearch Cluster Through the Transport Client
===============================================================

You can use Transport Client to access a CSS cluster in non-security mode. For a cluster in security mode, you are advised to use :ref:`Accessing an Elasticsearch Cluster Through the Rest High Level Client <css_01_0386>`.

Precautions
-----------

-  You are advised to use the Transport Client version that matches the Elasticsearch version. For example, use Transport Client 7.6.2 to access an Elasticsearch 7.6.2 cluster.
-  This solution is suitable for clusters that are not using the security mode. Such clusters can only be accessed through private IP addresses.

Prerequisites
-------------

-  The CSS cluster is available.

-  Ensure that the server running Java can communicate with the CSS cluster.

-  Install JDK 1.8 on the server. You can download JDK 1.8 from: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

-  Declare Java dependencies.

   *7.6.2* indicates the version of the Elasticsearch Java client.

   .. code-block::

      <dependency>
          <groupId>org.elasticsearch.client</groupId>
          <artifactId>transport</artifactId>
          <version>7.6.2</version>
      </dependency>
      <dependency>
          <groupId>org.elasticsearch</groupId>
          <artifactId>elasticsearch</artifactId>
          <version>7.6.2</version>
      </dependency>

Accessing a Cluster
-------------------

The following code is an example of using Transport Client to connect to the Elasticsearch cluster and check whether the **test** index exists.

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
           String host1 = "x.x.x.x";
           String host2 = "y.y.y.y";
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
