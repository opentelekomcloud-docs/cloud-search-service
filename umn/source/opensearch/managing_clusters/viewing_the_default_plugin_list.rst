:original_name: en-us_topic_0000001591616594.html

.. _en-us_topic_0000001591616594:

Viewing the Default Plugin List
===============================

CSS clusters have default plug-ins. You can view the default plugin information on the console or Kibana.

Viewing Plugins on the Console
------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters**. Click the target cluster name and go to the **Cluster Information** page of the cluster.
#. Click the **Plugins** tab.
#. On the **Default** tab page, view default plugins supported by the current version.

Viewing Plugins on the Kibana
-----------------------------

#. Log in to the CSS management console.

#. In the navigation pane, choose **Clusters**. Locate the target cluster and click **Access Kibana** in the **Operation** column to log in to OpenSearch Dashboard.

#. Go to **Dev Tools** and run the following command to view the cluster plugin information:

   .. code-block:: text

      GET _cat/plugins?v

   The following is an example of the response body:

   .. code-block::

      name                 component                            version
      css-3657-ess-esn-1-1 analysis-dynamic-synonym             1.3.6
      css-3657-ess-esn-1-1 analysis-icu                         1.3.6
      css-3657-ess-esn-1-1 analysis-ik                          1.3.6
      css-3657-ess-esn-1-1 analysis-kuromoji                    1.3.6
      css-3657-ess-esn-1-1 analysis-logtxt                      1.0.0
      css-3657-ess-esn-1-1 analysis-nori                        1.3.6
      css-3657-ess-esn-1-1 analysis-pinyin                      1.3.6
      css-3657-ess-esn-1-1 analysis-stconvert                   1.3.6
      css-3657-ess-esn-1-1 hpack                                2.0.0
      css-3657-ess-esn-1-1 ingest-attachment                    1.3.6
      css-3657-ess-esn-1-1 obs-store-plugin                     1.3.6
      css-3657-ess-esn-1-1 opensearch-alerting                  1.3.6.0
      css-3657-ess-esn-1-1 opensearch-anomaly-detection         1.3.6.0
      css-3657-ess-esn-1-1 opensearch-asynchronous-search       1.3.6.0
      css-3657-ess-esn-1-1 opensearch-cross-cluster-replication 1.3.6.0
      css-3657-ess-esn-1-1 opensearch-index-management          1.3.6.0
      css-3657-ess-esn-1-1 opensearch-job-scheduler             1.3.6.0
      css-3657-ess-esn-1-1 opensearch-knn                       1.3.6.0
      css-3657-ess-esn-1-1 opensearch-ml                        1.3.6.0
      css-3657-ess-esn-1-1 opensearch-observability             1.3.6.0
      css-3657-ess-esn-1-1 opensearch-performance-analyzer      1.3.6.0
      css-3657-ess-esn-1-1 opensearch-reports-scheduler         1.3.6.0
      css-3657-ess-esn-1-1 opensearch-security                  1.3.6.0
      css-3657-ess-esn-1-1 opensearch-sql                       1.3.6.0
      css-3657-ess-esn-1-1 repository-obs                       1.3.6

   **name** indicates the cluster node name, **component** indicates the plugin name, and **version** indicates the plugin version.
