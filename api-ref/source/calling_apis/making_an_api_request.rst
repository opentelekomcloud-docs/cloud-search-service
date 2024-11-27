:original_name: css_03_0078.html

.. _css_03_0078:

Making an API Request
=====================

This section describes the structure of a RESTful API request, and uses the IAM API for obtain a user token as an example to describe how to call an API.

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
   | Endpoint      | Domain name or IP address of the server running the REST service. The endpoint varies between services in different regions. It can be obtained from :ref:`Endpoints <css_03_0001__section889174472415>`.                                                            |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | resource-path | API access path for performing a specified operation. Obtain the value from the URI of an API. For example, the resource-path of the **API for obtaining a user token** is **/v3/auth/tokens**.                                                                      |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | query-string  | Query parameter, which is optional. Ensure that a question mark (**?**) is included before a query parameter that is in the format of "**Parameter name=Parameter value**". For example, **limit=10** indicates that a maximum of 10 pieces of data is to be viewed. |
   +---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For example, to obtain an IAM token in a region, obtain the endpoint of IAM for this region and the **resource-path** (**/v3/auth/tokens**) in the URI of the API used to obtain a user token. Then, construct the URI as follows:

.. code-block::

   https://<iam-endpoint>/v3/auth/tokens

.. note::

   To simplify the URI display, each API is provided with only a **resource-path** and a request method. The **URI-scheme** of all APIs is HTTPS, and the endpoints of all APIs in the same region are identical.

Request Methods
---------------

HTTP-based request methods, which are also called operations or actions, specify the type of operations that you are requesting.

-  **GET**: requests the server to return specified resources.
-  **PUT**: requests the server to update specified resources.
-  **POST**: requests the server to add resources or perform special operations.
-  **DELETE**: requests the server to delete specified resources, for example, an object.
-  **HEAD**: requests a server resource header.
-  **PATCH**: requests the server to update partial content of a specified resource. If the target resource does not exist, PATCH may create a resource.

For example, in the URI of the API for obtaining a user token, the request method is **POST**. The request is as follows:

.. code-block::

   POST https://{iam-endpoint}/v3/auth/tokens

Request Header
--------------

You can also add additional fields to a request, such as the fields required by a specified URI or an HTTP method. For example, add **Content-Type** that defines a request body type to request for the authentication information.

:ref:`Table 2 <css_03_0078__en-us_topic_0175865505_table181671338175614>` lists common request header fields.

.. _css_03_0078__en-us_topic_0175865505_table181671338175614:

.. table:: **Table 2** Common request headers

   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory                          | Description                                                                                                                                                                                                                                |
   +=======================+====================================+============================================================================================================================================================================================================================================+
   | Content-Type          | Yes                                | Message body type (or format). You are advised to use the default value **application/json**.                                                                                                                                              |
   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | X-Auth-Token          | Mandatory for token authentication | User token. It is the response to the API for obtaining a user token (only this API does not require authentication). After the request is processed, the value of **X-Subject-Token** in the response header (Header) is the token value. |
   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | X-Project-Id          | No                                 | Subproject ID, which is used in multi-project scenarios. The **X-Project-ID** field is mandatory in the request header for accessing resources in a subproject through AK/SK-based authentication.                                         |
   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | X-Sdk-Date            | Mandatory for AK/SK authentication | Request sending time. When AK/SK authentication is enabled, this field is automatically specified when SDK is used to sign the request.                                                                                                    |
   |                       |                                    |                                                                                                                                                                                                                                            |
   |                       |                                    | For details, see :ref:`Authentication <css_03_0079>`.                                                                                                                                                                                      |
   |                       |                                    |                                                                                                                                                                                                                                            |
   |                       |                                    | The format is YYYYMMDD'T'HHMMSS'Z'. The value is the current GMT time of the system.                                                                                                                                                       |
   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Authorization         | Mandatory for AK/SK authentication | Signature authentication information, When AK/SK authentication is enabled, this field is automatically specified when SDK is used to sign the request.                                                                                    |
   |                       |                                    |                                                                                                                                                                                                                                            |
   |                       |                                    | For details, see :ref:`Authentication <css_03_0079>`.                                                                                                                                                                                      |
   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | X-Language            | No                                 | Request language                                                                                                                                                                                                                           |
   +-----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The API used to obtain a user token does not require authentication. Therefore, only the **Content-Type** field needs to be added to requests for calling the API. An example of such requests is as follows:

.. code-block:: text

   POST https://{iam-endpoint}/v3/auth/tokens
   Content-Type: application/json

Request Body
------------

A request body conveys information other than the request header and is generally sent in a structured format defined by the request header field **Content-Type**.

The request body varies between APIs. Some APIs do not require the request body, such as the APIs requested using the **GET** and **DELETE** methods.

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

If all data required for the API request is available, you can send the request to call the API through curl, Postman, or coding. For the API of obtaining a user token, **x-subject-token** in the response header is the desired user token. Then, you can use the token to authenticate the calling of other APIs.
