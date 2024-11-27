:original_name: css_03_0062.html

.. _css_03_0062:

Creating a Pay-per-Use Elasticsearch Cluster
============================================

This section describes how to create a CSS cluster by using APIs. :ref:`Figure 1 <css_03_0062__en-us_topic_0171541475_en-us_topic_0171174235_fig4812113917173>` illustrates the API calling process.

.. _css_03_0062__en-us_topic_0171541475_en-us_topic_0171174235_fig4812113917173:

.. figure:: /_static/images/en-us_image_0000002119117513.png
   :alt: **Figure 1** API calling process

   **Figure 1** API calling process

.. note::

   The token obtained on IAM is valid for only 24 hours. If you want to use one token for authentication, you can cache it to avoid frequent calling.

Involved APIs
-------------

If you use a token for authentication, you must obtain the token and add **X-Auth-Token** to the request header of the API when making an API call.

-  API for obtaining tokens from IAM
-  API for creating CSS clusters

Procedure
---------

#. .. _css_03_0062__en-us_topic_0171541475_en-us_topic_0171174235_li1265543762911:

   Obtain the token. Send **POST https://IAM** **endpoint/v3/auth/tokens**.

   Obtain the token by following instructions in :ref:`Authentication <css_03_0079>`.

   The value of **X-Subject-Token** in the response header is the user token.

#. Add **Content-type** and **X-Auth-Token** to the request header.

   -  **Content-Type**: The request body type or format. Its default value is **application/json**.
   -  **X-Auth-Token**: Enter the user token obtained in :ref:`1 <css_03_0062__en-us_topic_0171541475_en-us_topic_0171174235_li1265543762911>`.

#. Send a cluster creation request and specify the following parameters in the request body:

   .. code-block:: text

      POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters

      {
        "cluster" : {
          "instance" : {
            "flavorRef" : "ess.spec-4u16g",
            "volume" : {
              "volume_type" : "COMMON",
              "size" : 120
            },
            "nics" : {
              "vpcId" : "{VPC ID}",
              "netId" : "{NET ID}",
              "securityGroupId" : "{Security group ID}"
            },
            "availability_zone" : "{AZ CODE}"
          },
          "datastore" : {
            "version" : "{cluster-version}",
            "type" : "elasticsearch"
          },
          "name" : "cluster-name",
          "instanceNum" : 3,
          "backupStrategy" : {
            "period" : "16:00 GMT+08:00",
            "prefix" : "snapshot",
            "keepday" : 7,
            "frequency" : "DAY",
            "bucket" : "css-obs-backup",
            "basePath" : "css_repository/obs-path",
            "agency" : "css_obs_agency"
          },
          "httpsEnable" : true,
          "authorityEnable" : true,
          "adminPwd" : "{password}",
          "enterprise_project_id" : "0",
          "tags" : [ {
            "key" : "k1",
            "value" : "v1"
          }, {
            "key" : "k2",
            "value" : "v2"
          } ]
        }
      }

   Check the response message. The following is an example response:

   .. code-block::

      {
        "cluster": {
          "id": "ef683016-871e-48bc-bf93-74a29d60d214",
          "name": "ES-Test"
        }
      }

   If the request is successful, 200 OK is returned.

   If the request fails, an error code and error information are returned. For details, see section :ref:`Status Codes <css_03_0075>`.
