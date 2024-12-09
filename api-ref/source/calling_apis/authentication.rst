:original_name: css_03_0139.html

.. _css_03_0139:

Authentication
==============

CSS supports token authentication.

Authentication Using Tokens
---------------------------

.. note::

   The validity period of a token is 24 hours. When using a token for authentication, cache it to prevent frequently calling the IAM API.

A token specifies certain permissions in a computer system. Authentication using a token adds the token to a request as its header during API calling to obtain permissions to operate APIs through IAM.

The API for obtaining a token is **POST https://**\ *{IAM endpoint}*\ **/v3/auth/tokens**. For details about how to obtain IAM endpoints, see :ref:`Endpoints <css_03_0053>`.

.. code-block::

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
                           "name": "domainname"    //Name of the account that the user belongs to
                       }
                   }
               }
           },
           "scope": {
               "project": {
                   "name": "xxxxxxxx"    //Project name
               }
           }
       }
   }

After a token is obtained, the **X-Auth-Token** header field must be added to requests to specify the token when calling other APIs. For example, if the token is **ABCDEFJ....**, **X-Auth-Token: ABCDEFJ....** can be added to a request as follows:

.. code-block:: text

   POST https://{endpoint}/v3/auth/projects
   Content-Type: application/json
   X-Auth-Token: ABCDEFJ....
