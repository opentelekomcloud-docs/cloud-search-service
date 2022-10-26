:original_name: iam_02_0008.html

.. _iam_02_0008:

Making an API Request
=====================

This section describes the structure of a RESTful API request, and uses the API for Obtaining a User Token as an example to describe how to call an API. A token is a user's access credential, which contains the user identity and permission information. The obtained token is used to authenticate the calling of other APIs.

Request URI
-----------

A request URI is in the following format:

**{URI-scheme}://{Endpoint}/{resource-path}?{query-string}**

.. table:: **Table 1** Request URL

   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter     | Description                                                                                                                                                                                                                                                          |
   +===============+======================================================================================================================================================================================================================================================================+
   | URI-scheme    | Protocol used to transmit requests. All APIs use **HTTPS**.                                                                                                                                                                                                          |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Endpoint      | Domain name or IP address of the server running the REST service. The endpoint varies between services in different regions. It can be obtained from :ref:`Endpoints <css_03_0053>`.                                                                                 |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | resource-path | API access path for performing a specified operation. Obtain the value from the URI of the API. For example, the **resource-path** of the API for **obtaining a user token** is **/v3/auth/tokens**.                                                                 |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | query-string  | Query parameter, which is optional. Ensure that a question mark (**?**) is included before a query parameter that is in the format of "**Parameter name=Parameter value**". For example, **limit=10** indicates that a maximum of 10 pieces of data is to be viewed. |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. code-block::

For example, to obtain an IAM token in a region, obtain the endpoint of IAM for this region and the **resource-path** (**/v3/auth/tokens**) in the URI of the API used to obtain a user token. Then, construct the URI as follows:

.. code-block::

   https://<iam-endpoint>/v3/auth/tokens

.. note::

   To simplify the URI display, each API is provided with only a **resource-path** and a request method. This is because the **URI-scheme** value of all APIs is **HTTPS**, and the endpoints in a region are the same. Therefore, the two parts are omitted.

Request Methods
---------------

HTTP-based request methods, which are also called operations or actions, specify the type of operations that you are requesting.

-  **GET**: requests the server to return specified resources.
-  **PUT**: requests the server to update specified resources.
-  **POST**: requests the server to add resources or perform special operations.
-  **DELETE**: requests the server to delete specified resources, for example, an object.
-  **HEAD**: requests a server resource header.
-  **PATCH**: requests the server to update partial content of a specified resource. If the target resource does not exist, PATCH may create a resource.

If **POST** is displayed in the URI of the API for obtaining a user token, the request is as follows:

.. code-block::

   POST https://{iam-endpoint}/v3/auth/tokens

Request Header
--------------

You can also add additional fields to a request, such as the fields required by a specified URI or an HTTP method. For example, add **Content-Type** that defines a request body type to request for the authentication information.

Common request headers are as follows:

-  **Content-Type**: specifies the request body type or format. This field is mandatory and its default value is **application/json**.
-  **X-Auth-Token**: specifies the user token, which is optional. This field is mandatory for token-based authentication. **X-Auth-Token** is the value of **x-subject-token** returned in response to the API used to obtain a user token.

   .. note::

      In addition to supporting authentication using tokens, APIs support authentication using the access key ID (AK)/secret access key (SK), which uses SDKs to sign a request. During the signing, the **Authorization** (signature authentication information) and **X-Sdk-Date** (time when a request is sent) headers are automatically added to the request. For more details, see :ref:`Authentication Using AK/SK <iam_02_0510>`.

The API used to obtain a user token does not require authentication. Therefore, only the **Content-Type** field needs to be added to requests for calling the API. An example of such requests is as follows:

.. code-block:: text

   POST https://{iam-endpoint}/v3/auth/tokens
   Content-Type: application/json

Request Body
------------

A request body conveys information other than the request header and is generally sent in a structured format defined by the request header field **Content-Type**.

The request body varies according to the APIs. Certain APIs do not require the request body, such as the GET and DELETE APIs.

In the case of the API used to obtain a user token, the request parameters and parameter description can be obtained from the API request. The following provides an example request with a body included. Replace *username*, *domainname*, ``********`` (login password), and *xxxxxxxxxxxxxxxxxx* (project ID) with the actual values. To learn how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`.

.. note::

   The **scope** parameter defines the application scope of the token, indicating that the obtained token can access only the resources in the specified project.

.. code-block:: text

   POST https://{iam-endpoint}/v3/auth/tokens
   Content-Type: application/json
   {
       "auth": {
           "identity": {
               "methods": [
                   "password"
               ],
               "password": {
                   "user": {
                       "name": "username",    //Username
                       "password": "********",    //Login password
                       "domain": {
                           "name": "domainname "    //Name of the account to which the user belongs
                       }
                   }
               }
           },
           "scope": {
               "project": {
                   "id": "xxxxxxxxxxxxxxxxxx"    //Project ID
               }
           }
       }
   }

If all data required by a request is available, you can send the request to call an API through `curl <https://curl.haxx.se/>`__, `Postman <https://www.getpostman.com/>`__, or coding. For the API of obtaining a user token, **x-subject-token** in the response header is the desired user token. Then, you can use the token to authenticate the calling of other APIs.
