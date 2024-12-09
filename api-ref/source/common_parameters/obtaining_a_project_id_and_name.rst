:original_name: css_03_0071.html

.. _css_03_0071:

Obtaining a Project ID and Name
===============================

A project ID or project name is required in some API requests. You need to obtain the project ID and name before calling an API.

Obtaining a Project ID and Name from the Console
------------------------------------------------

#. Log in to the console.
#. In the upper right corner of the page, click the username and choose **My Credentials** from the drop-down list. The **My Credentials** page is displayed.
#. In the project list, view the **Project ID** and **Project Name**.

Obtaining a Project ID by Calling an API
----------------------------------------

The API for obtaining a project ID is **GET https://**\ *{iam-endpoint}*\ **/v3/projects**. *{iam-endpoint}* indicates the endpoint of IAM, which can be obtained from :ref:`Endpoints <css_03_0053>`.

The following is an example response. For example, if CSS is deployed in region **xxx**, the value of **name** in the response body is **xxx**. The value of **id** in **projects** is the project ID.

.. code-block::

   {
       "projects": [
           {
               "domain_id": "65382450e8f64ac0870cd180d14exxxx",
               "is_domain": false,
               "parent_id": "65382450e8f64ac0870cd180d14exxxx",
               "name": "xxx",    //Project name, the name of the deployment zone.
               "description": "",
               "links": {
                   "next": null,
                   "previous": null,
                   "self": "https://www.example.com/v3/projects/a4a5d4098fb4474fa22cd05f897dxxxx"
               },
               "id": "a4a5d4098fb4474fa22cd05f897dxxxx",    //Project ID
               "enabled": true
           }
       ],
       "links": {
           "next": null,
           "previous": null,
           "self": "https://www.example.com/v3/projects"
       }
   }
