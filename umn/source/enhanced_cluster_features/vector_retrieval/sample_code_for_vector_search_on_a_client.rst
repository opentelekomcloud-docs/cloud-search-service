:original_name: en-us_topic_0000001528499121.html

.. _en-us_topic_0000001528499121:

Sample Code for Vector Search on a Client
=========================================

Elasticsearch provides standard REST APIs and clients developed using Java, Python, and Go.

Based on the open-source dataset **SIFT1M** (http://corpus-texmex.irisa.fr/) and Python Elasticsearch client, this section provides a code snippet for creating a vector index, importing vector data, and querying vector data on the client.

Prerequisites
-------------

The Python dependency package has been installed on the client. If it is not installed, run the following commands to install it:

.. code-block::

   pip install numpy
   pip install elasticsearch==7.6.0

Sample Code
-----------

::

   import numpy as np
   import time
   import json

   from concurrent.futures import ThreadPoolExecutor, wait
   from elasticsearch import Elasticsearch
   from elasticsearch import helpers

   endpoint = 'http://xxx.xxx.xxx.xxx:9200/'

   # Construct an Elasticsearch client object
   es = Elasticsearch(endpoint)

   # Index mapping information
   index_mapping = '''
   {
     "settings": {
       "index": {
         "vector": "true"
       }
     },
     "mappings": {
       "properties": {
         "my_vector": {
           "type": "vector",
           "dimension": 128,
           "indexing": true,
           "algorithm": "GRAPH",
           "metric": "euclidean"
         }
       }
     }
   }
   '''

   # Create an index.
   def create_index(index_name, mapping):
       res = es.indices.create(index=index_name, ignore=400, body=mapping)
       print(res)

   # Delete an index.
   def delete_index(index_name):
       res = es.indices.delete(index=index_name)
       print(res)


   # Refresh indexes.
   def refresh_index(index_name):
       res = es.indices.refresh(index=index_name)
       print(res)


   # Merge index segments.
   def merge_index(index_name, seg_cnt=1):
       start = time.time()
       es.indices.forcemerge(index=index_name, max_num_segments=seg_cnt, request_timeout=36000)
       print(f" Complete the merge within {time.time() - start} seconds")


   # Load vector data.
   def load_vectors(file_name):
       fv = np.fromfile(file_name, dtype=np.float32)
       dim = fv.view(np.int32)[0]
       vectors = fv.reshape(-1, 1 + dim)[:, 1:]
       return vectors


   # Load the ground_truth data.
   def load_gts(file_name):
       fv = np.fromfile(file_name, dtype=np.int32)
       dim = fv.view(np.int32)[0]
       gts = fv.reshape(-1, 1 + dim)[:, 1:]
       return gts


   def partition(ls, size):
       return [ls[i:i + size] for i in range(0, len(ls), size)]


   # Write vector data.
   def write_index(index_name, vec_file):
       pool = ThreadPoolExecutor(max_workers=8)
       tasks = []

       vectors = load_vectors(vec_file)
       bulk_size = 1000
       partitions = partition(vectors, bulk_size)

       start = time.time()
       start_id = 0
       for vecs in partitions:
           tasks.append(pool.submit(write_bulk, index_name, vecs, start_id))
           start_id += len(vecs)
       wait(tasks)
       print(f" Complete the writing within {time.time() - start} seconds")


   def write_bulk(index_name, vecs, start_id):
       actions = [
           {
               "_index": index_name,
               "my_vector": vecs[j].tolist(),
               "_id": str(j + start_id)
           }
           for j in range(len(vecs))
       ]
       helpers.bulk(es, actions, request_timeout=3600)


   # Query an index.
   def search_index(index_name, query_file, gt_file, k):
       print("Start query! Index name: " + index_name)

       queries = load_vectors(query_file)
       gt = load_gts(gt_file)

       took = 0
       precision = []
       for idx, query in enumerate(queries):
           hits = set()
           query_json = {
                     "size": k,
                     "_source": False,
                     "query": {
                       "vector": {
                         "my_vector": {
                           "vector": query.tolist(),
                           "topk": k
                         }
                       }
                     }
                   }
           res = es.search(index=index_name, body=json.dumps(query_json))

           for hit in res['hits']['hits']:
               hits.add(int(hit['_id']))
           precision.append(len(hits.intersection(set(gt[idx, :k]))) / k)
           took += res['took']

       print("precision: " + str(sum(precision) / len(precision)))
       print(f" Complete the retrieval within {took / 1000:.2f} seconds; average took size is {took / len(queries):.2f} ms")


   if __name__ == "__main__":
       vec_file = r"./data/sift/sift_base.fvecs"
       qry_file = r"./data/sift/sift_query.fvecs"
       gt_file = r"./data/sift/sift_groundtruth.ivecs"

       index = "test"
       create_index(index, index_mapping)
       write_index(index, vec_file)
       merge_index(index)
       refresh_index(index)

       search_index(index, qry_file, gt_file, 10)
