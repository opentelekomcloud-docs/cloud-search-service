:original_name: css_01_0402.html

.. _css_01_0402:

Client Code Sample for Vector Search (Java)
===========================================

Elasticsearch provides standard REST APIs and clients developed using Java and Python.

This section provides a sample of Java code for creating vector indexes, and importing and querying vector data. It shows how to use the client to implement vector search.

Prerequisites
-------------

Add the following Maven dependency based on the actual cluster version. 7.10.2 is used in this example.

.. code-block::

   <dependency>
       <groupId>org.elasticsearch.client</groupId>
       <artifactId>elasticsearch-rest-high-level-client</artifactId>
       <version>7.10.2</version>
   </dependency>

Sample Code
-----------

.. code-block::

   package org.example;

   import org.apache.http.HttpEntity;
   import org.apache.http.HttpHost;
   import org.apache.http.HttpStatus;
   import org.apache.http.auth.AuthScope;
   import org.apache.http.auth.UsernamePasswordCredentials;
   import org.apache.http.client.CredentialsProvider;
   import org.apache.http.conn.ssl.NoopHostnameVerifier;
   import org.apache.http.impl.client.BasicCredentialsProvider;
   import org.apache.http.nio.conn.ssl.SSLIOSessionStrategy;
   import org.elasticsearch.action.admin.indices.delete.DeleteIndexRequest;
   import org.elasticsearch.action.admin.indices.refresh.RefreshRequest;
   import org.elasticsearch.action.bulk.BulkRequest;
   import org.elasticsearch.action.bulk.BulkResponse;
   import org.elasticsearch.action.index.IndexRequest;
   import org.elasticsearch.action.search.SearchResponse;
   import org.elasticsearch.action.support.master.AcknowledgedResponse;
   import org.elasticsearch.client.Request;
   import org.elasticsearch.client.RequestOptions;
   import org.elasticsearch.client.Response;
   import org.elasticsearch.client.RestClient;
   import org.elasticsearch.client.RestClientBuilder;
   import org.elasticsearch.client.RestHighLevelClient;
   import org.elasticsearch.client.indices.CreateIndexRequest;
   import org.elasticsearch.client.indices.CreateIndexResponse;
   import org.elasticsearch.common.settings.Settings;
   import org.elasticsearch.common.xcontent.DeprecationHandler;
   import org.elasticsearch.common.xcontent.NamedXContentRegistry;
   import org.elasticsearch.common.xcontent.XContentParser;
   import org.elasticsearch.common.xcontent.XContentType;

   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManager;
   import javax.net.ssl.X509TrustManager;
   import java.io.IOException;
   import java.security.KeyManagementException;
   import java.security.NoSuchAlgorithmException;
   import java.security.SecureRandom;
   import java.security.cert.X509Certificate;
   import java.util.Arrays;
   import java.util.List;

   public class ClientExample {
       private final RestHighLevelClient client;

       public ClientExample(RestHighLevelClient client) {
           this.client = client;
       }

       //Create a client for accessing non-security clusters.
       public static RestHighLevelClient getClient(List<String> hosts, int port, String scheme) {
           HttpHost[] httpHosts = hosts.stream().map(p -> new HttpHost(p, port, scheme)).toArray(HttpHost[]::new);
           return new RestHighLevelClient(RestClient.builder(httpHosts));
       }

       //Create a client for accessing security clusters.
       public static RestHighLevelClient getClient(List<String> hosts, int port, String scheme, String user, String password) {
           final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
           credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(user, password));
           SSLContext sc = null;
           try {
               sc = SSLContext.getInstance("SSL");
               sc.init(null, trustAllCerts, new SecureRandom());
           } catch (KeyManagementException | NoSuchAlgorithmException e) {
               e.printStackTrace();
           }
           HttpHost[] httpHosts = hosts.stream().map(p -> new HttpHost(p, port, scheme)).toArray(HttpHost[]::new);
           final SSLIOSessionStrategy sessionStrategy = new SSLIOSessionStrategy(sc, NoopHostnameVerifier.INSTANCE);
           RestClientBuilder builder = RestClient.builder(httpHosts).setHttpClientConfigCallback(httpClientBuilder -> {
               httpClientBuilder.disableAuthCaching();
               httpClientBuilder.setSSLStrategy(sessionStrategy);
               return httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
           });
           return new RestHighLevelClient(builder);
       }

       public static TrustManager[] trustAllCerts = new TrustManager[] {
               new X509TrustManager() {
                   @Override
                   public void checkClientTrusted(X509Certificate[] chain, String authType) {
                   }
                   @Override
                   public void checkServerTrusted(X509Certificate[] chain, String authType) {
                   }
                   @Override
                   public X509Certificate[] getAcceptedIssuers() {
                       return null;
                   }
               }
       };

       # Create an index.
       public void create(String index) throws IOException {
           CreateIndexRequest request = new CreateIndexRequest(index);
           request.settings(Settings.builder()
                   .put("index.vector", true) // Enable the vector feature.
                   .put("index.number_of_shards", 1) //Set the number of index shards as needed.
                   .put("index.number_of_replicas", 0) //Set the number of index replicas as needed.
           );
           String mapping =
                   "{\n" +
                   "  \"properties\": {\n" +
                   "    \"my_vector\": {\n" +
                   "      \"type\": \"vector\",\n" +      // Set this field as the vector type.
                   "      \"indexing\": \"true\",\n" +    // Enable index acceleration.
                   "      \"dimension\": \"2\",\n" +      // Vector dimension
                   "      \"metric\": \"euclidean\",\n" + // Similarity metric
                   "      \"algorithm\": \"GRAPH\"\n" +   // Index algorithm
                   "    }\n" +
                   "  }\n" +
                   "}";
           request.mapping(mapping, XContentType.JSON);
           CreateIndexResponse response = client.indices().create(request, RequestOptions.DEFAULT);
           if (response.isAcknowledged()) {
               System.out.println("create " + index + " success");
           }
       }

       // Write data. You are advised to keep the batch size under 500 records.
       public void write(String index, List<float[]> vectors) throws IOException {
           BulkRequest request = new BulkRequest();
           for (float[] vec : vectors) {
               request.add(new IndexRequest(index).source("my_vector", vec));
           }

           BulkResponse response = client.bulk(request, RequestOptions.DEFAULT);
           if (response.hasFailures()) {
               System.out.println(response.buildFailureMessage());
           } else {
               System.out.println("write bulk to " + index + " success");
           }

           // Optional. Elasticsearch will refresh it by default.
           client.indices().refresh(new RefreshRequest(index), RequestOptions.DEFAULT);
       }

       // Query vectors.
       public void search(String index, float[] query, int size) throws IOException {
           String queryFormat =
               "{\n" +
               "  \"size\":%d,\n" +
               "  \"query\": {\n" +
               "    \"vector\": {\n" +
               "      \"my_vector\": {\n" +  // Query the vector field name.
               "        \"vector\": %s,\n" +
               "        \"topk\":%d\n" +
               "      }\n" +
               "    }\n" +
               "  }\n" +
               "}";
           String body = String.format(queryFormat, size, Arrays.toString(query), size);
           Request request = new Request("POST", index + "/_search");
           request.setJsonEntity(body);
           Response response = client.getLowLevelClient().performRequest(request);
           if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
               System.out.println(response.getEntity()); //Handle the error based on service requirements.
               return;
           }
           // Process the normally returned result based on service requirements.
           HttpEntity entity = response.getEntity();
           XContentType xContentType = XContentType.fromMediaTypeOrFormat("application/json");
           XContentParser parser = xContentType.xContent().createParser(NamedXContentRegistry.EMPTY,
                   DeprecationHandler.IGNORE_DEPRECATIONS, entity.getContent());
           SearchResponse searchResponse = SearchResponse.fromXContent(parser);
           System.out.println(searchResponse);
       }

       // Delete an index.
       public void delete(String index) throws IOException {
           DeleteIndexRequest request = new DeleteIndexRequest(index);
           AcknowledgedResponse response = client.indices().delete(request, RequestOptions.DEFAULT);
           if (response.isAcknowledged()) {
               System.out.println("delete " + index + " success");
           }
       }

       public void close() throws IOException {
           client.close();
       }

       public static void main(String[] args) throws IOException {
            // For a non-security cluster, run the following:
            RestHighLevelClient client = getClient(Arrays.asList("x.x.x.x"), 9200, "http");

           /*
            *For a security cluster with HTTPS enabled, run the following:
            *  RestHighLevelClient client = getClient(Arrays.asList("x.x.x.x", "x.x.x.x"), 9200, "https", "user_name", "password");
            *For a security cluster with HTTPS disabled, run the following:
            *  RestHighLevelClient client = getClient(Arrays.asList("x.x.x.x", "x.x.x.x"), 9200, "http", "user_name", "password");
            */

           ClientExample example = new ClientExample(client);
           String indexName = "my_index";

           //Create an index.
           example.create(indexName);

           //Write data.
           List<float[]> data = Arrays.asList(new float[]{1.0f, 1.0f}, new float[]{2.0f, 2.0f}, new float[]{3.0f, 3.0f});
           example.write(indexName, data);

           //Query an index.
           float[] queryVector = new float[]{1.0f, 1.0f};
           example.search(indexName, queryVector, 3);

           //Delete an index.
           example.delete(indexName);

           //Close the client.
           example.close();
       }
   }
