:original_name: css_01_0129.html

.. _css_01_0129:

Client Code Sample for Vector Search (Python)
=============================================

Elasticsearch provides standard REST APIs and clients developed using Java and Python.

This section provides a sample of Python code for creating vector indexes, and importing and querying vector data. It shows how to use the client to implement vector search.

Prerequisites
-------------

The Python dependency package has been installed on the client. If it is not installed, run the following commands to install it:

.. code-block::

   # Set the actual cluster version. 7.6 is used in this example.
   pip install elasticsearch==7.6

Sample Code
-----------

.. code-block::

   from elasticsearch import Elasticsearch
   from elasticsearch import helpers

   # Create the Elasticsearch client.
   def get_client(hosts: list, user: str = None, password: str = None):
       if user and password:
           return Elasticsearch(hosts, http_auth=(user, password), verify_certs=False, ssl_show_warn=False)
       else:
           return Elasticsearch(hosts)

   # Create an index table.
   def create(client: Elasticsearch, index: str):
       # Index mapping information
       index_mapping = {
           "settings": {
               "index": {
                   "vector": "true",  # Enable the vector feature.
                   "number_of_shards": 1,  # Set the number of index shards as needed.
                   "number_of_replicas": 0,  # Set the number of index replicas as needed.
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
   def write(client: Elasticsearch, index: str, vecs: list, bulk_size=500):
       for i in range(0, len(vecs), bulk_size):
           actions = [
               {
                   "_index": index,
                   "my_vector": vec,
                   # Other fields can be added if necessary.
               }
               for vec in vecs[i: i+bulk_size]
           ]
           success, errors = helpers.bulk(client, actions, request_timeout=3600)
           if errors:
               print("write bulk failed with errors: ", errors)  # Handle the error as needed.
           else:
               print("write bulk {} docs success".format(success))
       client.indices.refresh(index=index, request_timeout=3600)

   # Query a vector index.
   def search(client: Elasticsearch, index: str, query: list, size: int):
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
   def delete(client: Elasticsearch, index: str):
       res = client.indices.delete(index=index)
       print("delete index result: ", res)

   if __name__ == '__main__':
       # For a non-security cluster, run the following:
       es_client = get_client(hosts=['http://x.x.x.x:9200'])

       # For a security cluster with HTTPS enabled, run the following:
       # es_client = get_client(hosts=['https://x.x.x.x:9200', 'https://x.x.x.x:9200'], user='xxxxx', password='xxxxx')

       # For a security cluster with HTTPS disabled, run the following:
       # es_client = get_client(hosts=['http://x.x.x.x:9200', 'http://x.x.x.x:9200'], user='xxxxx', password='xxxxx')

       # Test the index name.
       index_name = "my_index"

       # Create an index.
       create(es_client, index=index_name)

       # Write data.
       data = [[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
       write(es_client, index=index_name, vecs=data)

       # Query an index.
       query_vector = [1.0, 1.0]
       search(es_client, index=index_name, query=query_vector, size=3)

       # Delete an index.
       delete(es_client, index=index_name)
