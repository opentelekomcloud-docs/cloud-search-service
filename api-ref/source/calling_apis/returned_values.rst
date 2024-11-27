:original_name: css_03_0080.html

.. _css_03_0080:

Returned Values
===============

After sending a request, you will receive a response containing the status code, response header, and response body.

Status Code
-----------

A status code is a group of digits, ranging from 1xx to 5xx. It indicates the status of a request. For more information, see :ref:`Status Codes <css_03_0075>`.

If status code 201 is returned for the API for obtaining a user token, the request is successful.

Response Header
---------------

A response header corresponds to a request header, for example, **Content-Type**.

:ref:`Figure 1 <css_03_0080__en-us_topic_0175865507_en-us_topic_0170917209_en-us_topic_0168405765_fig4865141011511>` shows the response header for the API of obtaining a user token, where **x-subject-token** is the desired user token. Then, you can use the token to authenticate the calling of other APIs.

.. _css_03_0080__en-us_topic_0175865507_en-us_topic_0170917209_en-us_topic_0168405765_fig4865141011511:

.. figure:: /_static/images/en-us_image_0000002083397766.png
   :alt: **Figure 1** Header of the response to the request for obtaining a user token

   **Figure 1** Header of the response to the request for obtaining a user token

Response Body
-------------

A response body is generally returned in a structured format, corresponding to the **Content-Type** in the response header, and is used to transfer content other than the response header.

The following is part of the response body for the API used to obtain a user token. The following is only part of the response body.

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
