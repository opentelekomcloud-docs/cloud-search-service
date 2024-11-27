:original_name: css_03_0079.html

.. _css_03_0079:

Authentication
==============

You can use either of the following authentication methods when calling APIs:

-  AK/SK-based authentication: Requests are encrypted using AK/SK pairs.
-  Token authentication: Requests are authenticated using a token.

AK/SK-based Authentication
--------------------------

An AK/SK is used to verify the identity of a request sender. In AK/SK-based authentication, a signature needs to be obtained and then added to the request header.

.. note::

   AK: access key ID, which is a unique identifier used in conjunction with a secret access key to sign requests cryptographically.

   SK: secret access key used in conjunction with an AK to sign requests cryptographically. It identifies a request sender and prevents the request from being modified.

The following uses a demo project to show how to sign a request and use an HTTP client to send an HTTPS request.

Download the demo from https://github.com/api-gate-way/SdkDemo.

If you do not need the demo project, directly download the API Gateway signing SDK at

Obtain the API Gateway signing SDK from the enterprise administrator.

Decompress the downloaded demo package to obtain a JAR file and reference the obtained JAR files as dependencies, as highlighted in the following figure.

|image1|

#. Generate an AK/SK pair. (If an AK/SK file has already been created, skip this step and locate the downloaded AK/SK file. Generally, the file name will be **credentials.csv**.)

   a. Log in to the console.
   b. Hover over the username and select **My Credentials** from the drop-down list.
   c. In the navigation pane, click **Access Keys**.
   d. Click **Create Access Key**. The **Create Access Key** dialog box is displayed.
   e. Enter your login password.
   f. Enter the verification code sent to your email or mobile phone.

      .. note::

         For users created in IAM, if no email address or phone number was specified during the user creation, only a login password is required.

   g. Click **OK** to download the AK/SK.

      .. note::

         Anyone who possesses your access keys can decrypt your login information. Therefore, keep your access keys secure.

#. Decompress the demo project.

#. .. _css_03_0079__li19564155663214:

   Import the demo project to Eclipse.


   .. figure:: /_static/images/en-us_image_0000002083397786.png
      :alt: **Figure 1** Selecting Existing Projects into Workspace

      **Figure 1** Selecting Existing Projects into Workspace


   .. figure:: /_static/images/en-us_image_0000002119077481.png
      :alt: **Figure 2** Selecting the demo project

      **Figure 2** Selecting the demo project


   .. figure:: /_static/images/en-us_image_0000002083557722.png
      :alt: **Figure 3** Structure of the demo project

      **Figure 3** Structure of the demo project

#. Sign a request.

   The request signing method is integrated in the JAR files imported in :ref:`3 <css_03_0079__li19564155663214>`. The request needs to be signed before it is sent. The signature will then be added as part of the HTTP header to the request.

   The demo code is classified into the following classes to demonstrate how to sign and send an HTTP request:

   -  **AccessService**: abstract class that merges the GET, POST, PUT, and DELETE methods into the **access** method.
   -  **Demo**: execution entry used to simulate the sending of GET, POST, PUT, and DELETE requests.
   -  **AccessServiceImpl**: implements the **access** method, which contains the code required for communication with API Gateway.

   a. (Optional) Add request header fields.

      *Note: For some services, custom request headers, such as X-Project-Id and X-Domain-Id, may need to be added. To add them, modify the AccessServiceImpl.java file.*

      Uncomment the following code snippet in the **AccessServiceImpl.java** file, and replace the variables with the actual sub-project ID and account ID.

      //**TODO**: Add special headers.

      ::

         //request.addHeader("X-Project-Id", "

      **xxxxx**");

      ::

         //request.addHeader("X-Domain-Id", "

      **xxxxx**");

   b. Edit the main() method in the **Demo.java** file and replace the bold text with actual values.

      If you use other methods such as POST, PUT, and DELETE, see the corresponding comment.

      Replace **region**, **serviceName**, **AK/SK**, and **URL**. In the demo, the URL for obtaining the VPC is used. Replace it with the required URL. For details on how to obtain the project ID in the URL, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. For details about the endpoint, see :ref:`Endpoints <css_03_0001__section889174472415>`.

      //**TODO**: Replace region with the name of the region in which the service to be accessed is located.

      ::

      **private** **static** **final** String **region** = "";

      ::



      ::

         //

      **TODO**: Replace **vpc** with the name of the service you want to access. For example, ecs, vpc, iam, and elb.

      ::

      **private** **static** **final** String **serviceName** = "";

      ::



      ::

      **public** **static** **void** main(String[] args) **throws** UnsupportedEncodingException

      ::

         {

      ::

         //

      **TODO**: Replace the AK and SK with those obtained on the **My Credential** page.

      ::

         String ak = "

      **ZIRRKMTWP******1WKNKB**";

      ::

         String sk = "

      **Us0mdMNHk******YrRCnW0ecfzl**";

      ::



      ::

         //

      **TODO**: To specify a project ID (multi-project scenarios), add the X-Project-Id header.

      ::

         //

      **TODO**: To access a global service, such as IAM, DNS, CDN, and TMS, add the X-Domain-Id header to specify an account ID.

      ::

         //

      **TODO**: To add a header, find "Add special headers" in the **AccessServiceImple.java** file.

      ::



      ::

         //

      **TODO**: Test the API

      ::

         String url = "

      **https://{Endpoint}/v1/{project_id}/vpcs**";

      ::

      *get*\ (ak, sk, url);

      ::



      ::

         //

      **TODO**: When creating a VPC, replace *{project_id}* in postUrl with the actual value.

      ::

         //String postUrl = "https://serviceEndpoint/v1/{project_id}/cloudservers";

      ::

         //String postbody ="{\"

      vpc\\": {\\"name\\": \\"vpc\\",\\"cidr\\": \\"192.168.0.0/16\\"}}";

      ::

         //post(ak, sk, postUrl, postbody);

      ::



      ::

         //

      **TODO**: When querying a VPC, replace *{project_id}* in url with the actual value.

      ::

         //String url = "https://serviceEndpoint/v1/{project_id}/vpcs/{vpc_id}";

      ::

         //get(ak, sk, url);

      ::



      ::

         //

      **TODO**: When updating a VPC, replace *{project_id}* and *{vpc_id}* in putUrl with the actual values.

      ::

         //String putUrl = "https://serviceEndpoint/v1/{project_id}/vpcs/{vpc_id}";

      ::

         //String putbody ="{\"vpc\":{\"name\": \"vpc1\",\"cidr\": \"192.168.0.0/16\"}}";

      ::

         //put(ak, sk, putUrl, putbody);

      ::



      ::

         //

      **TODO**: When deleting a VPC, replace *{project_id}* and *{vpc_id}* in deleteUrl with the actual values.

      ::

         //String deleteUrl = "https://serviceEndpoint/v1/{project_id}/vpcs/{vpc_id}";

      ::

         //delete(ak, sk, deleteUrl);

      ::

         }

   c. Compile and run the code to call an API.

      In the **Package Explorer** area on the left, right-click **Demo.java** and choose **Run AS** > **Java Application** from the shortcut menu to run the demo code.

      You can view API calling logs on the console.

Authentication Using Tokens
---------------------------

.. note::

   -  The validity period of a token is 24 hours. When using a token for authentication, cache it to prevent frequently calling the IAM API.
   -  Ensure that the token is valid while you use it. Using a token that will soon expire may cause API calling failures.

A token specifies certain permissions in a computer system. Authentication using a token adds the token to a request as its header during API calling to obtain permissions to operate APIs through IAM.

The API for obtaining a token is **POST https://**\ *{IAM endpoint}*\ **/v3/auth/tokens**. For details about how to obtain IAM endpoints, see :ref:`Endpoints <css_03_0001__section889174472415>`.

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
                           "name": "domainname"    //Name of the account to which the user belongs
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

.. code-block::

   POST https://{endpoint}/v3/auth/projects
   Content-Type: application/json
   X-Auth-Token: ABCDEFJ....

.. |image1| image:: /_static/images/en-us_image_0000002119077517.png
