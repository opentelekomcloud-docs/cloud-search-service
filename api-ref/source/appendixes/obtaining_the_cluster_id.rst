:original_name: css_03_0101.html

.. _css_03_0101:

Obtaining the Cluster ID
========================

A cluster ID (**cluster_id**) is required for some URLs when an API is called. To obtain the cluster ID, perform the following steps:

Obtaining the Cluster ID by Calling an API
------------------------------------------

You can obtain the cluster ID by calling the Querying the Cluster List API.

The API for obtaining the cluster ID is GET https://{Endpoint}/v1.0/{project_id}/clusters, where {Endpoint} indicates the IAM endpoint, which can be obtained from Regions and Endpoints. For the project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. For API authentication, see :ref:`Authentication <css_03_0079>`.

The following is an example response. The value of **id** under **clusters** is the cluster ID.

.. code-block::

   {
     "totalSize" : 1,
     "clusters" : [ {
       "datastore" : {
         "type" : "elasticsearch",
         "version" : "7.10.2",
         "subVersion" : "7.10.2_24.3.0_0827",
         "isEosCluster" : false,
         "supportSecuritymode" : false
       },
       "instances" : [ {
         "status" : "200",
         "type" : "ess",
         "id" : "{INSTANCE_ID}",
         "name" : "css-8bc5-ess-esn-1-1",
         "specCode" : "ess.spec-4u8g",
         "azCode" : "{AZ_CODE}",
         "volume" : {
           "type" : "ULTRAHIGH",
           "size" : 40,
           "resourceIds" : [ "{RESOURCE_ID}" ]
         },
         "ip" : "192.168.0.122",
         "resourceId" : "{RESOURCE_ID}"
       } ],
       "publicKibanaResp" : {
         "eipSize" : 10,
         "publicKibanaIp" : "100.95.152.28:9200",
         "elbWhiteListResp" : null,
         "bandwidthResourceId" : "18bec13f-5cc1-4631-867f-33505d15be12"
       },
       "elbWhiteList" : {
         "whiteList" : "",
         "enableWhiteList" : false
       },
       "updated" : "2023-10-09T02:07:13",
       "name" : "css-8bc5",
       "publicIp" : "100.85.222.202",
       "created" : "2023-10-09T02:07:13",
       "id" : "{CLUSTER_ID}",
       "status" : "200",
       "endpoint" : "192.168.0.122:9200",
       "vpcId" : "{VPC_ID}",
       "subnetId" : "{SUBNET_ID}",
       "securityGroupId" : "{SECURITY_GROUP_ID}",
       "bandwidthResourceId" : "{BANDWIDTH_RESOURCE_ID}",
       "bandwidthSize" : 3,
       "httpsEnable" : true,
       "authorityEnable" : true,
       "diskEncrypted" : false,
       "backupAvailable" : false,
       "actionProgress" : { },
       "actions" : [ ],
       "enterpriseProjectId" : "0",
       "tags" : [ ],
       "period" : true
     } ]
   }

Obtaining the Cluster ID from the GaussDB(DWS) Console
------------------------------------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, click **Clusters**.

#. In the cluster list, find the target cluster and click the cluster name. The **Cluster Information** page is displayed.

#. Check the cluster ID under cluster information.


   .. figure:: /_static/images/en-us_image_0000002105031992.png
      :alt: **Figure 1** Checking the cluster ID

      **Figure 1** Checking the cluster ID
