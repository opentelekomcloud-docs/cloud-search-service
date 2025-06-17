:original_name: css_01_0392.html

.. _css_01_0392:

Accessing an Elasticsearch Cluster Using Go
===========================================

This section describes how to access a CSS cluster using Go.

Preparations
------------

-  The CSS cluster is available.
-  Ensure that the server running Go can communicate with the CSS cluster.
-  Ensure that Go has been installed on the server. You can download Go from the official website: https://go.dev/dl/.

Connecting to a Non-Security Mode Cluster
-----------------------------------------

Connect to a non-security mode cluster. The sample code is as follows:

::

   package main

   import (
       "github.com/elastic/go-elasticsearch/v7"
       "log"
   )

   func main() {
       cfg := elasticsearch.Config{
           Addresses: []string{
               "http://HOST:9200/",
           },
       }

       es, _ := elasticsearch.NewClient(cfg)
       log.Println(es.Info())
   }

In the information above, **HOST** indicates the internal IP address of a cluster node.

Connecting to a Security-Mode Cluster
-------------------------------------

-  Connect to a security-mode cluster with HTTPS disabled. The sample code is as follows:

   ::

      package main

      import (
          "github.com/elastic/go-elasticsearch/v7"
          "log"
      )

      func main() {
          cfg := elasticsearch.Config{
              Addresses: []string{
                  "http://HOST:9200/",
              },
              Username: "USERNAME",
              Password: "PASSWORD",
          }

          es, _ := elasticsearch.NewClient(cfg)
          log.Println(es.Info())
      }

-  Connect to a security cluster that has enabled HTTPS and does not use certificates. The sample code is as follows:

   ::

      package main

      import (
          "crypto/tls"
          "github.com/elastic/go-elasticsearch/v7"
          "log"
          "net/http"
      )

      func main() {
          cfg := elasticsearch.Config{
              Addresses: []string{
                  "https://HOST:9200/",
              },
              Username: "USERNAME",
              Password: "PASSWORD",
              Transport: &http.Transport{
                  TLSClientConfig: &tls.Config{
                      InsecureSkipVerify: true,
                  },
              },
          }

          es, _ := elasticsearch.NewClient(cfg)
          log.Println(es.Info())
      }

-  Connect to a security cluster that has enabled HTTPS and uses certificates. The sample code is as follows:

   ::

      package main

      import (
          "crypto/tls"
          "crypto/x509"
          "flag"
          "github.com/elastic/go-elasticsearch/v7"
          "io/ioutil"
          "log"
          "net"
          "net/http"
          "time"
      )

      func main() {
          insecure := flag.Bool("insecure-ssl", false, "Accept/Ignore all server SSL certificates")
          flag.Parse()

          // Get the SystemCertPool, continue with an empty pool on error
          rootCAs, _ := x509.SystemCertPool()
          if rootCAs == nil {
              rootCAs = x509.NewCertPool()
          }

          // Read in the cert file
          certs, err := ioutil.ReadFile("/tmp/CloudSearchService.cer")
          if err != nil {
              log.Fatalf("Failed to append %q to RootCAs: %v", "xxx", err)
          }

          // Append our cert to the system pool
          if ok := rootCAs.AppendCertsFromPEM(certs); !ok {
              log.Println("No certs appended, using system certs only")
          }

          config := elasticsearch.Config{
              Addresses: []string{
                  "https://HOST:9200/",
              },
              Username: "USERNAME",
              Password: "PASSWORD",
              Transport: &http.Transport{
                  MaxIdleConnsPerHost:   10,
                  ResponseHeaderTimeout: time.Second,
                  DialContext: (&net.Dialer{
                      Timeout:   30 * time.Second,
                      KeepAlive: 30 * time.Second,
                  }).DialContext,
                  TLSClientConfig: &tls.Config{
                      InsecureSkipVerify: *insecure,
                      RootCAs:            rootCAs,
                  },
              },
          }
          es, _ := elasticsearch.NewClient(config)
          log.Println(elasticsearch.Version)
          log.Println(es.Info())
      }

.. table:: **Table 1** Variables

   +-----------+------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                                            |
   +===========+========================================================================================================================+
   | HOST      | IP address for accessing the Elasticsearch cluster. If there are multiple IP addresses, separate them with commas (,). |
   +-----------+------------------------------------------------------------------------------------------------------------------------+
   | USERNAME  | Username for accessing the cluster.                                                                                    |
   +-----------+------------------------------------------------------------------------------------------------------------------------+
   | PASSWORD  | Password of the user.                                                                                                  |
   +-----------+------------------------------------------------------------------------------------------------------------------------+

Running Code
------------

Write the code above to the **EsTest.gc** file based on the cluster type and save the file to an independent directory. Run the following command in that directory to run the code:

.. code-block::

   go env -w GO111MODULE=on
   go env -w GOPROXY=https://goproxy.io,direct
   go env -w GONOSUMDB=*

   go mod init test
   go mod tidy
   go run EsTest.go
