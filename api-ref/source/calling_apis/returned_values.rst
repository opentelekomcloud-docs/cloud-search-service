:original_name: iam_02_0511.html

.. _iam_02_0511:

Returned Values
===============

Status Code
-----------

After sending a request, you will receive a response containing the status code, response header, and response body.

A status code is a group of digits, ranging from 1xx to 5xx. It indicates the status of a request. For more information, see :ref:`Status Code <css_03_0075>`.

If status code 201 is returned for the calling of the API for obtaining a user token, the request is successful.

Response Header
---------------

A response header corresponds to a request header, for example, **Content-Type**.

:ref:`Figure 1 <iam_02_0511__en-us_topic_0170917209_en-us_topic_0168405765_fig4865141011511>` shows the response header for the API of obtaining a user token, where **x-subject-token** is the desired user token. Then, you can use the token to authenticate the calling of other APIs.

.. _iam_02_0511__en-us_topic_0170917209_en-us_topic_0168405765_fig4865141011511:

.. figure:: /_static/images/en-us_image_0000001289590960.png
   :alt: **Figure 1** Header of the response to the request for obtaining a user token

   **Figure 1** Header of the response to the request for obtaining a user token

Response Body
-------------

A response body is generally returned in a structured format, corresponding to the **Content-Type** in the response header, and is used to transfer content other than the response header.

The following shows part of the response body for the API of obtaining a user token.

.. code-block::

   {
       "token": {
           "expires_at": "2019-02-13T06:52:13.855000Z",
           "methods": [
               "password"
           ],
           "catalog": [
               {
                   "endpoints": [
                       {
                           "region_id": "xxx",
   ......

If an error occurs during API calling, the system returns an error code and a message to you. The following shows the format of an error response body:

.. code-block::

   {
       "error_msg": "The format of message is error",
       "error_code": "AS.0001"
   }

In the preceding information, **error_code** is an error code, and **error_msg** describes the error.
