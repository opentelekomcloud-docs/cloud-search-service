:original_name: css_01_0043.html

.. _css_01_0043:

Creating Alarm Rules
====================

You can create the alarm rules for cluster metrics on the Cloud Eye management console. If the monitored metrics meet the specified alarm rule, alarms are reported. In this case, you can learn about cluster exceptions in time and take proper measures.

Procedure
---------

#. Log in to the Cloud Eye console.

#. In the left navigation pane, choose **Alarm Management** > **Alarm Rules**.

#. Click **Create Alarm Rule** in the upper right corner.

#. In the displayed **Create Alarm Rule** page, set parameters as required.

   You can create an alarm rule for a specific metric or use the alarm template to create alarm rules in batches for multiple cloud service instances. In this example, assume that you use the alarm template to create the alarm rule for the CSS cluster.

   a. Configure the name and description of an alarm rule.

      .. table:: **Table 1** Parameter description

         +-------------+------------------------------------------------------------------------------------------------------+---------------+
         | Parameter   | Description                                                                                          | Example Value |
         +=============+======================================================================================================+===============+
         | Name        | Name of the alarm rule. The system automatically generates a name, which you can change if required. | alarm-p8v9    |
         +-------------+------------------------------------------------------------------------------------------------------+---------------+
         | Description | Alarm rule description. This parameter is optional.                                                  | ``-``         |
         +-------------+------------------------------------------------------------------------------------------------------+---------------+

   b. Select a monitored object and set alarm content parameters.

      .. table:: **Table 2** Parameters for configuring alarms

         +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
         | Parameter             | Description                                                                                                                                                                     | Example Value         |
         +=======================+=================================================================================================================================================================================+=======================+
         | Resource Type         | Name of the service for which the alarm rule is configured                                                                                                                      | Cloud Search Service  |
         +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
         | Dimension             | Metric dimension of the alarm rule. Currently, the following dimensions are supported:                                                                                          | CSS clusters          |
         |                       |                                                                                                                                                                                 |                       |
         |                       | -  **CSS Clusters**: Alarm rules are specified by cluster.                                                                                                                      |                       |
         |                       | -  **CSS Clusters - CSS Instances**: Alarm rules are specified by node in a cluster.                                                                                            |                       |
         +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
         | Monitoring Scope      | Resource range to which the alarm rule applies. You can select **Resource groups** or **Specific resources**.                                                                   | Specific resources    |
         |                       |                                                                                                                                                                                 |                       |
         |                       | Note:                                                                                                                                                                           |                       |
         |                       |                                                                                                                                                                                 |                       |
         |                       | -  If you select **Resource groups** and any resource in the group meets the alarm policy, an alarm is triggered.                                                               |                       |
         |                       | -  If you select **Specific resources**, select one or more monitored objects and click |image1| to synchronize the monitored object or objects to the dialog box on the right. |                       |
         +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

   c. Specify **Method**, **Template**, and **Alarm Notification**.

      .. table:: **Table 3** Parameter description

         +-----------------------+---------------------------------------------------------------------------------------------------------------+-----------------------+
         | Parameter             | Description                                                                                                   | Example Value         |
         +=======================+===============================================================================================================+=======================+
         | Method                | Select **Use template** or **Create manually**.                                                               | Create manually       |
         |                       |                                                                                                               |                       |
         |                       | If you set **Monitoring Scope** to **Specific resources**, you can set **Method** to **Use template**.        |                       |
         +-----------------------+---------------------------------------------------------------------------------------------------------------+-----------------------+
         | Template              | Template you want to import                                                                                   | ``-``                 |
         +-----------------------+---------------------------------------------------------------------------------------------------------------+-----------------------+
         | Alarm Notification    | If you enable this function, specify **Validity Period**, **Notification Object**, and **Trigger Condition**. | ``-``                 |
         +-----------------------+---------------------------------------------------------------------------------------------------------------+-----------------------+

   d. Click **Create**.

      After the alarm rule is successfully created, it will be displayed in the alarm rule list

.. |image1| image:: /_static/images/en-us_image_0000001286596290.png
