:original_name: ShowClusterDetail.html

.. _ShowClusterDetail:

Querying Cluster Details
========================

Function
--------

This API is used to query and display details about a cluster.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be queried                                                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameter

   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                                                | Description                                                                                                                |
   +=======================+=====================================================================================================+============================================================================================================================+
   | datastore             | :ref:`ClusterDetailDatastore <showclusterdetail__response_clusterdetaildatastore>` object           | Search engine type                                                                                                         |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | instances             | Array of :ref:`ClusterDetailInstances <showclusterdetail__response_clusterdetailinstances>` objects | Node object list                                                                                                           |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | publicKibanaResp      | :ref:`publicKibanaRespBody <showclusterdetail__response_publickibanarespbody>` object               | Kibana public network access information                                                                                   |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | elbWhiteList          | :ref:`elbWhiteListResp <showclusterdetail__response_elbwhitelistresp>` object                       | Public network access information                                                                                          |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | updated               | String                                                                                              | Last modification time of a cluster. The format is **ISO8601: CCYY-MM-DDThh:mm:ss**.                                       |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | name                  | String                                                                                              | Cluster name                                                                                                               |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | publicIp              | String                                                                                              | Public IP address                                                                                                          |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | created               | String                                                                                              | Time when a cluster is created. The format is **ISO8601: CCYY-MM-DDThh:mm:ss**.                                            |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | id                    | String                                                                                              | Cluster ID.                                                                                                                |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | status                | String                                                                                              | Cluster status.                                                                                                            |
   |                       |                                                                                                     |                                                                                                                            |
   |                       |                                                                                                     | -  **100**: The operation, such as instance creation, is in progress.                                                      |
   |                       |                                                                                                     | -  **200**: The cluster is available.                                                                                      |
   |                       |                                                                                                     | -  **303**: The cluster is unavailable.                                                                                    |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | endpoint              | String                                                                                              | IP address and port number for accessing VPC                                                                               |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | vpcId                 | String                                                                                              | VPC ID.                                                                                                                    |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | subnetId              | String                                                                                              | Subnet ID.                                                                                                                 |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | securityGroupId       | String                                                                                              | Security group ID                                                                                                          |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | vpcepIp               | String                                                                                              | VPC endpoint IP address                                                                                                    |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | bandwidthSize         | Integer                                                                                             | Public network bandwidth Unit: Mbit/s                                                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | httpsEnable           | Boolean                                                                                             | Communication encryption status.                                                                                           |
   |                       |                                                                                                     |                                                                                                                            |
   |                       |                                                                                                     | -  Value **false** indicates that communication encryption is not enabled.                                                 |
   |                       |                                                                                                     | -  **true**: communication encryption has been enabled.                                                                    |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | diskEncrypted         | Boolean                                                                                             | Indicates whether disks are encrypted.                                                                                     |
   |                       |                                                                                                     |                                                                                                                            |
   |                       |                                                                                                     | -  Value **true** indicates that disks are encrypted.                                                                      |
   |                       |                                                                                                     | -  **false**: disks are not encrypted.                                                                                     |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | authorityEnable       | Boolean                                                                                             | Indicates whether to enable authentication. The value can be **true** or **false**. Authentication is disabled by default. |
   |                       |                                                                                                     |                                                                                                                            |
   |                       |                                                                                                     | -  **true**: authentication is enabled for the cluster.                                                                    |
   |                       |                                                                                                     | -  **false**: authentication is disabled for the cluster.                                                                  |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | backupAvailable       | Boolean                                                                                             | Indicates whether the snapshot function is enabled.                                                                        |
   |                       |                                                                                                     |                                                                                                                            |
   |                       |                                                                                                     | -  **true**: The snapshot function is enabled.                                                                             |
   |                       |                                                                                                     | -  **false**: The snapshot function is disabled.                                                                           |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | actionProgress        | Object                                                                                              | Cluster operation progress, which displays the progress of cluster creation or scale-out in percentage.                    |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | actions               | Array of strings                                                                                    | Current behavior of a cluster. The value can be **REBOOTING**, **GROWING**, **RESTORING**, and **SNAPSHOTTING**.           |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | enterpriseProjectId   | String                                                                                              | ID of the enterprise project to which a cluster belongs.                                                                   |
   |                       |                                                                                                     |                                                                                                                            |
   |                       |                                                                                                     | If the user of the cluster does not enable the enterprise project, the setting of this parameter is not returned.          |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | tags                  | Array of :ref:`ClusterDetailTags <showclusterdetail__response_clusterdetailtags>` objects           | Cluster tag                                                                                                                |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
   | failedReason          | :ref:`ClusterDetailFailedReasons <showclusterdetail__response_clusterdetailfailedreasons>` object   | Failure cause. If the cluster is in the **Available** state, this parameter is not returned.                               |
   +-----------------------+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

.. _showclusterdetail__response_clusterdetaildatastore:

.. table:: **Table 3** ClusterDetailDatastore

   +-----------+--------+-----------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                   |
   +===========+========+===============================================================================================+
   | type      | String | Engine type. Currently, only **Elasticsearch** is supported.                                  |
   +-----------+--------+-----------------------------------------------------------------------------------------------+
   | version   | String | CSS cluster engine version. For details, see :ref:`Supported Cluster Versions <css_03_0056>`. |
   +-----------+--------+-----------------------------------------------------------------------------------------------+

.. _showclusterdetail__response_clusterdetailinstances:

.. table:: **Table 4** ClusterDetailInstances

   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | Parameter             | Type                                                                                  | Description                                                           |
   +=======================+=======================================================================================+=======================================================================+
   | status                | String                                                                                | Node status value.                                                    |
   |                       |                                                                                       |                                                                       |
   |                       |                                                                                       | -  **100**: The operation, such as instance creation, is in progress. |
   |                       |                                                                                       | -  **200**: The cluster is available.                                 |
   |                       |                                                                                       | -  **303**: The cluster is unavailable.                               |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | type                  | String                                                                                | Node type                                                             |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | id                    | Integer                                                                               | Instance ID                                                           |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | name                  | String                                                                                | Instance name                                                         |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | specCode              | String                                                                                | Node specifications.                                                  |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | azCode                | String                                                                                | AZ to which a node belongs.                                           |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | ip                    | String                                                                                | Instance IP address                                                   |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
   | volume                | :ref:`ShowClusterVolumeRsp <showclusterdetail__response_showclustervolumersp>` object | Instance disk information                                             |
   +-----------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. _showclusterdetail__response_showclustervolumersp:

.. table:: **Table 5** ShowClusterVolumeRsp

   ========= ======= ==================
   Parameter Type    Description
   ========= ======= ==================
   type      String  Instance disk type
   size      Integer Instance disk size
   ========= ======= ==================

.. _showclusterdetail__response_publickibanarespbody:

.. table:: **Table 6** publicKibanaRespBody

   +------------------+-------------------------------------------------------------------------------------------+------------------------------------------+
   | Parameter        | Type                                                                                      | Description                              |
   +==================+===========================================================================================+==========================================+
   | eipSize          | Integer                                                                                   | Bandwidth. Unit: Mbit/s                  |
   +------------------+-------------------------------------------------------------------------------------------+------------------------------------------+
   | elbWhiteListResp | :ref:`kibanaElbWhiteListResp <showclusterdetail__response_kibanaelbwhitelistresp>` object | Kibana public network access information |
   +------------------+-------------------------------------------------------------------------------------------+------------------------------------------+
   | publicKibanaIp   | String                                                                                    | Kibana access IP address                 |
   +------------------+-------------------------------------------------------------------------------------------+------------------------------------------+

.. _showclusterdetail__response_kibanaelbwhitelistresp:

.. table:: **Table 7** kibanaElbWhiteListResp

   +-----------------------+-----------------------+----------------------------------------------+
   | Parameter             | Type                  | Description                                  |
   +=======================+=======================+==============================================+
   | enableWhiteList       | Boolean               | Indicates whether access control is enabled. |
   |                       |                       |                                              |
   |                       |                       | -  **true**: Access control is enabled.      |
   |                       |                       | -  **false**: Access control is disabled.    |
   +-----------------------+-----------------------+----------------------------------------------+
   | whiteList             | String                | Whitelist for Kibana public network access   |
   +-----------------------+-----------------------+----------------------------------------------+

.. _showclusterdetail__response_elbwhitelistresp:

.. table:: **Table 8** elbWhiteListResp

   +-----------------------+-----------------------+----------------------------------------------------------+
   | Parameter             | Type                  | Description                                              |
   +=======================+=======================+==========================================================+
   | enableWhiteList       | Boolean               | Indicates whether public access control is enabled.      |
   |                       |                       |                                                          |
   |                       |                       | -  **true**: Public network access control is enabled.   |
   |                       |                       | -  **false**: Public network access control is disabled. |
   +-----------------------+-----------------------+----------------------------------------------------------+
   | whiteList             | String                | Whitelist for public network access                      |
   +-----------------------+-----------------------+----------------------------------------------------------+

.. _showclusterdetail__response_clusterdetailtags:

.. table:: **Table 9** ClusterDetailTags

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   key       String Tag key.
   value     String Tag value
   ========= ====== ===========

.. _showclusterdetail__response_clusterdetailfailedreasons:

.. table:: **Table 10** ClusterDetailFailedReasons

   +-----------------------+-----------------------+----------------------------------------------------+
   | Parameter             | Type                  | Description                                        |
   +=======================+=======================+====================================================+
   | errorCode             | String                | Error code.                                        |
   |                       |                       |                                                    |
   |                       |                       | -  **CSS.6000**: failed to create a cluster.       |
   |                       |                       | -  **CSS.6001**: failed to scale out a cluster.    |
   |                       |                       | -  **CSS.6002**: failed to restart a cluster.      |
   |                       |                       | -  **CSS.6004**: failed to create a node.          |
   |                       |                       | -  **CSS.6005**: failed to initialize the service. |
   +-----------------------+-----------------------+----------------------------------------------------+
   | errorMsg              | String                | Detailed error information                         |
   +-----------------------+-----------------------+----------------------------------------------------+

Request Example
---------------

None

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "datastore" : {
       "type" : "elasticsearch",
       "version" : "x.x.x"
     },
     "instances" : [ {
       "status" : "200",
       "type" : "ess",
       "id" : "3c7fe582-a9f6-46fd-9d01-956bed4a8bbc",
       "name" : "ES-xx",
       "specCode" : "css.xlarge.2",
       "azCode" : "xx-xxx-xx",
       "ip" : "192.168.0.x",
       "volume" : {
         "type" : "COMMON",
         "size" : 40
       }
     } ],
     "publicKibanaResp" : {
       "eipSize" : 5,
       "publicKibanaIp" : "100.95.158.x",
       "elbWhiteListResp" : {
         "whiteList" : "11.11.11.11",
         "enableWhiteList" : true
       }
     },
     "updated" : "2018-01-16T08:37:18",
     "name" : "ES-xx",
     "publicIp" : "100.95.149.xx:9200",
     "elbWhiteList" : {
       "whiteList" : "10.10.10.10",
       "enableWhiteList" : true
     },
     "created" : "2018-01-16T08:37:18",
     "id" : "5c77b71c-5b35-4f50-8984-76387e42451a",
     "status" : "200",
     "endpoint" : "192.168.0.x:9200",
     "vpcId" : "07e7ab39-xxx-xxx-xxx-d3f28ea7f051",
     "subnetId" : "025d45f9-xxx-xxx-xxx-e852c6455a5e",
     "securityGroupId" : "0347aabc-xxx-xxx-xxx-6b10a79701e2",
     "vpcepIp" : "192.168.0.203",
     "bandwidthSize" : 0,
     "diskEncrypted" : false,
     "httpsEnable" : true,
     "authorityEnable" : true,
     "backupAvailable" : true,
     "actionProgress" : { },
     "actions" : [ ],
     "enterpriseProjectId" : "3e1c74a0-xxx-xxx-xxx-c6b9e46cf81b",
     "tags" : [ {
       "key" : "k1",
       "value" : "v1"
     } ]
   }

Status Codes
------------

+-----------------------------------+-----------------------------------------+
| Status Code                       | Description                             |
+===================================+=========================================+
| 200                               | The request is processed.               |
+-----------------------------------+-----------------------------------------+
| 400                               | Invalid request.                        |
|                                   |                                         |
|                                   | Modify the request instead of retrying. |
+-----------------------------------+-----------------------------------------+
| 404                               | The requested resource cannot be found. |
|                                   |                                         |
|                                   | Modify the request instead of retrying. |
+-----------------------------------+-----------------------------------------+
