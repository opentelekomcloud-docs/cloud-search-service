:original_name: css_02_0128.html

.. _css_02_0128:

How Do I Convert the Format of a CER Security Certificate in CSS?
=================================================================

The security certificate (**CloudSearchService.cer**) can be downloaded only for security clusters that have enabled HTTPS access. Most software supports certificates in the **.pem** or **.jks** format. You need to convert the format of the CSS security certificate.

-  Run the following command to convert the security certificate from **.cer** to **.pem**:

   .. code-block::

      openssl x509 -inform pem -in CloudSearchService.cer -out newname.pem

-  Run the following command to convert the security certificate from **.cer** to **.jks**:

   .. code-block::

      keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

In the preceding commands, *newname* indicates the user-defined certificate name.

After the command is executed, set the certificate password and confirm the password as prompted. Securely store the password. It will be used for accessing the cluster.
