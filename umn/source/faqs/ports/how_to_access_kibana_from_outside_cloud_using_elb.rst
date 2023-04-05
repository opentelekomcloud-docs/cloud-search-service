:original_name: css_02_0201.html

.. _css_02_0201:

How to access Kibana from outside cloud using ELB?
==================================================

Overview
--------

Currently to access Kibana dashboard of CSS Service, a user has to login to OTC consoleand navigate to Kibana login page.

To make the access convenient a user can utilize the provided python script which willconfigure the Dedicated Loadbalancer of OTC and a user would be able to access Kibanadashboard with a public IP.

ELB Configuration Script
------------------------

Script to Configure ELB to be able to access CSS Kibana Dashboard in https mode. ThisScript will create a Dedicated Loadbalancer with a HTTPS Listener which will be forwardingthe traffic to CSS nodes at 5601 port in order to access Kibana Dashboard.

Download `Script <https://docs.otc.t-systems.com/cloud-search-service/umn/_downloads/048cb558398d6094eec6f4816e5b19c0/script.py>`__

Installing Dependency
---------------------

The script depends on otcextensions library.

If you already have `Python <https://python.org/>`__ with `pip <https://pip.pypa.io/>`__ installed, you can simply run:

.. code-block::

   pip install otcextensions

-  To know more details about using otcextensions library you can check `otcextensions docs <https://python-otcextensions.readthedocs.io/en/latest/install/index.html>`__.

   A file called clouds.yaml holds all necessary configuration parameters. The file can beplaced either in the local directory, below the user home directory in .config/openstack orin the system-wide directory /etc/openstack. You may use a second file secure.yaml in thesame directories to extra protect clear-text password credentials. For more details see thesection configuration in the official documentation.

   Minimal sample **clouds.yaml** file:

   .. code-block::

      clouds:
            otc:
              profile: otc
              auth:
                username: '<USER_NAME>'
                password: '<PASSWORD>'
                project_name: '<eu-de_project>'
                # or project_id: '<123456_PROJECT_ID>'
                user_domain_name: 'OTC00000000001000000xxx'
                # or user_domain_id: '<123456_DOMAIN_ID>'
                auth_url: 'https://iam.eu-de.otc.t-systems.com:443/v3'

   With this configuration you can start using the CLI with openstack --os-cloud otc \*command\* or by export OS_CLOUD=otc; openstack \*command*.

-  **Environment variables**: Authentication using username/password is often used:

   .. code-block::

      export OS_AUTH_URL=<url-to-openstack-identity>
      export OS_PROJECT_NAME=<project-name>
      export OS_USERNAME=<username>
      export OS_PASSWORD=<password>
      export OS_USER_DOMAIN_NAME=<user-domain-name>
      export OS_IDENTITY_API_VERSION=3

In addition to that a regular clouds.yaml configuration file can be used.

More information is available at:

https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html

Pre-Requisites
--------------

The Script requires ID of a CSS Cluster and Certificate ID for creating a HTTPS listener.

-  You can get a CSS Cluster ID by visiting the OTC console -> CSS Dashboard ->Clusters page, and click on your CSS Cluster to get its details.
-  To learn more about Creating and Getting a TLS Certificate, check `ELB User Guide <https://docs.otc.t-systems.com/elastic-load-balancing/umn/certificate/creating,_modifying,_or_deleting_a_certificate.html>`__

Generating a TSL Certificate with openssl command.

.. code-block::

   openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:4096 -keyout private.key -out certificate.crt

.. note::

   When adding the certificate and private key, Certificate Type must be "Server Certificate".

Running The Script
------------------

Once you have **certificate_id** and **cluster_id**, you are ready to run the script.

List ELB Flavors
----------------

.. code-block::

   python3 script.py elb-flavors

This will print the L7 Flavors supported by Dedicated Loadbalancer. To print all types of flavors supported you may add --all argument to the command. But we need only L7 flavor type, that's why --all argument is set as optional.

Configure ELB
-------------

.. code-block::

    python3 script.py elb-configure --cluster-id <cluster_id> --certificate-id <certificate_id>

Argument --certificate-id is optional, if it's not provided then Loadbalancer will be configured with HTTP listener.

**Configure ELB with specific Flavor**

-  By default ELB will be configured with smallest L7 flavor type. But if you want to have some specific flavor of your choice, follow below commands.
-  Only L7 flavor type must be used since we are creating HTTPS listener.

.. code-block::

    # Prints list of Loadbalancer flavor Types
      python3 script.py elb-flavors

    # Run the script
      python3 script.py elb-configure --cluster-id <cluster_id> --certificate-id <certificate_id> --flavor-id <flavor_id>

Delete ELB
----------

.. code-block::

    python3 script.py elb-delete <loadbalancer_name_or_id>

**Delete ELB and Release Public EIP**

.. code-block::

   python3 script.py elb-delete <loadbalancer_id> --release-public-ip

.. note::

   Please use the elb-delete command with caution.

Logging
-------

When you run the script a log file is created with name **debug.log** where you can find details of all the API requests.
