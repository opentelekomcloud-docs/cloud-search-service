:original_name: css_03_0050.html

.. _css_03_0050:

Downloading a Certificate File
==============================

Function
--------

This API is used to download the HTTPS certificate file of the server.

URI
---

.. code-block:: text

   GET /v1.0/dev/cluster/sslCert

Request
-------

None

Response
--------

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   +=======================+=======================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | certBase64            | String                | This string is obtained after the certificate file is transcoded using Base64. You need to run the following command to parse the string into a certificate file. The generated certificate file is saved in the folder where the command to be executed is located. In the following command, **"$certBase64"** indicates the string returned in the response message. The name of the generated certificate file is ****CloudSearchService.cert****. You can specify another name for the certificate file, but must use **.cert** as the suffix of the name. |
   |                       |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   |                       |                       | **echo -n "$certBase64" \| base64 -d >** **CloudSearchService.cert**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Examples
--------

Example request

.. code-block:: text

   GET /v1.0/dev/cluster/sslCert

Example response

.. code-block::

   {   "certBase64":"MIIDnTCCAoWgAwIBAgIEXXdMtTANBgkqhkiG9w0BAQsFADB/MRAwDgYDVQQGEwdHZXJtYW55MQ0wCwYDVQQIEwROb25lMQ0wCwYDVQQHEwROb25lMRkwFwYDVQQKExBPcGVuVGVsZWtvbUNsb3VkMRUwEwYDVQQLEwxEYXRhQW5hbHlzaXMxGzAZBgNVBAMTEkNsb3VkU2VhcmNoU2VydmljZTAeFw0xODExMTcxODE4NDJaFw0xOTAyMTUxODE4NDJaMH8xEDAOBgNVBAYTB0dlcm1hbnkxDTALBgNVBAgTBE5vbmUxDTALBgNVBAcTBE5vbmUxGTAXBgNVBAoTEE9wZW5UZWxla29tQ2xvdWQxFTATBgNVBAsTDERhdGFBbmFseXNpczEbMBkGA1UEAxMSQ2xvdWRTZWFyY2hTZXJ2aWNlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApHai9+LMoFSlWqI+YodGiFLw597Vuoo7gG3qTCs+szQTn3PTZtbnzy7TNWjn8K41mkBgUY16wtkhH1nu6AmhRLpZA+2fwAz34v/tDOYahPq045bk9S/znJXQeWWeux93I15z7OP/XC68IF2AKl2NXjmm9bAD/DsqaLuJpoE77d71862sD6uRCBQYyZoQaHw+eKuL8/+5PjWvG9mS+Rxp0DcLd1waFkyK4BjB5Ae3og4bAivKo7vQHH79fgnuK0SQnNpxlU8xLIGaKsQ0/yeJrTrlfy3vBQmj949SbCzFjvmXgkbv4I0jcT5Ax1P68tlasUUnCqFTjGTbzeT82CeE6QIDAQABoyEwHzAdBgNVHQ4EFgQUPPZLu9ElUzQgKURRwn8HpzIliEcwDQYJKoZIhvcNAQELBQADggEBAI/e/sGbZ1jB3ao7Car2p7rm1Pg8ro1kSy9o+Jug6XjJpkwITKGkhPYugtGuKgL6oiYkdJhqmfrm/1R7phf1qzBgRoWtR7eCBg4uorNaYvTelAjbIoYGL03D1c5K6e1XwRsdqNWT3TwiHZ5CuiVOsjAtvt3OrvF2YtPUOJpbbvdXlnLKaLHoaklcyyMJ+KmUbkd2XFhzlhwj4eOaloL8XQcAk/urYFFNTymJPnNiEXjLAgGCfE/j8rX26WKvPUGmcuuqBiK7Ob+VfnfpnssDQoBtQsN9eUNxkYkg6eua8U6zR3nSPxXpdn+TZo3HHnUp3x0f1Xev49MHKe/aPMJOTYE="
   }

After obtaining the preceding character string, run the following command to obtain the **CloudSearchService.cert** certificate file:

.. code-block::

   echo -n "MIIDnTCCAoWgAwIBAgIEXXdMtTANBgkqhkiG9w0BAQsFADB/MRAwDgYDVQQGEwdHZXJtYW55MQ0wCwYDVQQIEwROb25lMQ0wCwYDVQQHEwROb25lMRkwFwYDVQQKExBPcGVuVGVsZWtvbUNsb3VkMRUwEwYDVQQLEwxEYXRhQW5hbHlzaXMxGzAZBgNVBAMTEkNsb3VkU2VhcmNoU2VydmljZTAeFw0xODExMTcxODE4NDJaFw0xOTAyMTUxODE4NDJaMH8xEDAOBgNVBAYTB0dlcm1hbnkxDTALBgNVBAgTBE5vbmUxDTALBgNVBAcTBE5vbmUxGTAXBgNVBAoTEE9wZW5UZWxla29tQ2xvdWQxFTATBgNVBAsTDERhdGFBbmFseXNpczEbMBkGA1UEAxMSQ2xvdWRTZWFyY2hTZXJ2aWNlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApHai9+LMoFSlWqI+YodGiFLw597Vuoo7gG3qTCs+szQTn3PTZtbnzy7TNWjn8K41mkBgUY16wtkhH1nu6AmhRLpZA+2fwAz34v/tDOYahPq045bk9S/znJXQeWWeux93I15z7OP/XC68IF2AKl2NXjmm9bAD/DsqaLuJpoE77d71862sD6uRCBQYyZoQaHw+eKuL8/+5PjWvG9mS+Rxp0DcLd1waFkyK4BjB5Ae3og4bAivKo7vQHH79fgnuK0SQnNpxlU8xLIGaKsQ0/yeJrTrlfy3vBQmj949SbCzFjvmXgkbv4I0jcT5Ax1P68tlasUUnCqFTjGTbzeT82CeE6QIDAQABoyEwHzAdBgNVHQ4EFgQUPPZLu9ElUzQgKURRwn8HpzIliEcwDQYJKoZIhvcNAQELBQADggEBAI/e/sGbZ1jB3ao7Car2p7rm1Pg8ro1kSy9o+Jug6XjJpkwITKGkhPYugtGuKgL6oiYkdJhqmfrm/1R7phf1qzBgRoWtR7eCBg4uorNaYvTelAjbIoYGL03D1c5K6e1XwRsdqNWT3TwiHZ5CuiVOsjAtvt3OrvF2YtPUOJpbbvdXlnLKaLHoaklcyyMJ+KmUbkd2XFhzlhwj4eOaloL8XQcAk/urYFFNTymJPnNiEXjLAgGCfE/j8rX26WKvPUGmcuuqBiK7Ob+VfnfpnssDQoBtQsN9eUNxkYkg6eua8U6zR3nSPxXpdn+TZo3HHnUp3x0f1Xev49MHKe/aPMJOTYE=" | base64 -d > CloudSearchService.cert

Status Code
-----------

.. table:: **Table 2** Status code

   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | Status Code           | Code                  | Status Code Description                                         |
   +=======================+=======================+=================================================================+
   | 400                   | BadRequest            | Invalid request.                                                |
   |                       |                       |                                                                 |
   |                       |                       | The client should not repeat the request without modifications. |
   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | 404                   | NotFound              | The requested resource cannot be found.                         |
   |                       |                       |                                                                 |
   |                       |                       | The client should not repeat the request without modifications. |
   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | 200                   | OK                    | The request is processed successfully.                          |
   +-----------------------+-----------------------+-----------------------------------------------------------------+
