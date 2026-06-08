:original_name: css_01_0127.html

.. _css_01_0127:

OpenSearch Vector Search Sample Code (Python)
=============================================

The CSS vector database is fully compatible with the native OpenSearch Python client. With this SDK, you can use Python to easily manage the vector index lifecycle for OpenSearch clusters, from creating vector indexes and importing high-dimensional vectors at high speed, to performing millisecond-level approximate nearest neighbor (ANN) searches. The sample code in this topic is modular and ready to run. In just a few minutes, you can execute the complete workflow from data ingestion to vector search, helping you accelerate your service deployment.

Prerequisites
-------------

The Python dependency package has been installed on the client. If it is not installed, run the following command to install it:

.. code-block::

   # OpenSearch 2.19.0
   pip install opensearch-py==2.8.0

   # OpenSearch 1.3.6
   pip install opensearch-py==1.1.0

Sample Code
-----------

::

   from opensearchpy import OpenSearch

   # Create a client.
   def get_client(hosts: list, user: str = None, password: str = None):
       if user and password:
           return OpenSearch(hosts, http_auth=(user, password), verify_certs=False, ssl_show_warn=False)
       else:
           return OpenSearch(hosts)

   # Create an index table.
   def create(client: OpenSearch, index: str):
       # Index mapping information
       index_mapping = {
           "settings": {
               "index": {
                   "vector": "true",  # Enable the vector feature.
                   "number_of_shards": 1,  # Set the number of index shards as needed.
                   "number_of_replicas": 0  # Set the number of index replicas as needed.
               }
           },
           "mappings": {
               "properties": {
                   "my_vector": {
                       "type": "vector",
                       "dimension": 2,
                       "indexing": True,
                       "algorithm": "GRAPH",
                       "metric": "euclidean"
                   }
                   # Other fields can be added if necessary.
               }
           }
       }
       res = client.indices.create(index=index, body=index_mapping)
       print("create index result: ", res)

   # Write data.
   def write(client: OpenSearch, index: str, vecs: list, bulk_size=500):
       for i in range(0, len(vecs), bulk_size):
           actions = ""
           for vec in vecs[i: i + bulk_size]:
               actions += '{"index": {"_index": "%s"}}\n' % index
               actions += '{"my_vector": %s}\n' % str(vec)
           client.bulk(body=actions, request_timeout=3600)
       client.indices.refresh(index=index, request_timeout=3600)
       print("write index success!")

   # Query a vector index.
   def search(client: OpenSearch, index: str, query: list, size: int):
       # Query statement. Select an appropriate query method.
       query_body = {
           "size": size,
           "query": {
               "vector": {
                   "my_vector": {
                       "vector": query,
                       "topk": size
                   }
               }
           }
       }
       res = client.search(index=index, body=query_body)
       print("search index result: ", res)

   # Delete an index.
   def delete(client: OpenSearch, index: str):
       res = client.indices.delete(index=index)
       print("delete index result: ", res)

   if __name__ == '__main__':
       os_client = get_client(hosts=['http://xx.xx.xx.xx:9200'])

       # For a security-mode cluster that uses HTTPS, run the following:
       # os_client = get_client(hosts=['https://xx.xx.xx.xx:9200', 'https://xx.xx.xx.xx:9200'], user='xxxxx', password='xxxxx')

       # For a security-mode cluster with HTTPS disabled, run the following:
       # os_client = get_client(hosts=['http://xx.xx.xx.xx:9200', 'http://xx.xx.xx.xx:9200'], user='xxxxx', password='xxxxx')

       # Test the index name.
       index_name = "my_index"

       # Create an index.
       create(os_client, index=index_name)

       # Write data.
       data = [[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
       write(os_client, index=index_name, vecs=data)

       # Query an index.
       query_vector = [1.0, 1.0]
       search(os_client, index=index_name, query=query_vector, size=3)

       # Delete an index.
       delete(os_client, index=index_name)
