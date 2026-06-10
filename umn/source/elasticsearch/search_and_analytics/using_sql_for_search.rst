:original_name: css_01_0061.html

.. _css_01_0061:

Using SQL for Search
====================

For developers and data analysts who are familiar with relational databases like MySQL, the native, JSON-based Elasticsearch query DSL may present a steep learning curve. In particular, constructing complex aggregation queries can be an error-prone process. To address this challenge, CSS Elasticsearch clusters integrate the Open Distro for Elasticsearch SQL plugin. This plugin enables users to query, aggregate, and analyze data in Elasticsearch using standard SQL syntax. It also supports interconnection with popular BI tools like Tableau through a JDBC driver, enabling a seamless data exploration experience.

How the Feature Works
---------------------

Open Distro for Elasticsearch SQL is essentially a translator between SQL and Elasticsearch DSL. It works as follows:

#. Parsing: It receives and validates SQL queries submitted by users.
#. Translation: It converts SQL queries into native Elasticsearch DSL queries.
#. Execution: It sends DSL queries to the cluster for execution.
#. Return: It returns the results in JSON or CSV.

For more information, see `SQL Functions <https://opendistro.github.io/for-elasticsearch-docs/docs/sql/functions/>`__.

Constraints
-----------

Only Elasticsearch 6.5.4 or later supports Open Distro for Elasticsearch SQL.

SQL Query Guide
---------------

-  **Method 1: Running SQL Queries in Kibana (Recommended)**

   Use this method for development, debugging, and ad-hoc queries.

   -  Perform a basic query.

      For example, run the following command to search the my-index index for documents where the age field exceeds 20, returning up to 10 results:

      .. code-block:: text

         POST _opendistro/_sql
         {
           "query": "SELECT * FROM my-index WHERE age > 20 LIMIT 10"
         }

   -  Export data in CSV. To export data to an Excel document for analysis, specify **format=csv**.

      For example, run the following command to retrieve 10 documents from the my-index index based on the name and age fields and return the results in CSV format:

      .. code-block:: text

         POST _opendistro/_sql?format=csv
         {
           "query": "SELECT name, age FROM my-index LIMIT 10"
         }

   -  Convert SQL to DSL. To learn how to write DSL queries or analyze the performance of SQL queries, use the **\_explain** API to check the translated DSL queries.

      For example, run the following command to convert a SQL query into the equivalent DSL query:

      .. code-block:: text

         POST _opendistro/_sql/_explain
         {
           "query": "SELECT * FROM my-index WHERE age > 20"
         }

-  **Method 2: Running SQL Queries via cURL Commands on a Server**

   Use this method when you need to incorporate Elasticsearch queries into automated scripts or scheduled tasks.

   For example, run the following command to retrieve 10 records from the **my-index** index. The following is an example of the code used in a security-mode cluster that uses HTTP:

   .. code-block::

      curl -XPOST http://<cluster IP address>:9200/_opendistro/_sql \
        -u <username>:<password> -k \
        -H 'Content-Type: application/json' \
        -d '{"query": "SELECT * FROM my-index LIMIT 10"}'

Supported SQL Syntax
--------------------

Open Distro for Elasticsearch SQL supports the following SQL syntax elements: statements, conditions, aggregations, the include and exclude fields, common functions, joins, and SHOW statements.

-  Statements

   .. table:: **Table 1** Statements

      ========= =======================================================
      Statement Example
      ========= =======================================================
      Select    SELECT \* FROM my-index
      Delete    DELETE FROM my-index WHERE \_id=1
      Where     SELECT \* FROM my-index WHERE ['field']='value'
      Order by  SELECT \* FROM my-index ORDER BY \_id asc
      Group by  SELECT \* FROM my-index GROUP BY range(age, 20,30,39)
      Limit     SELECT \* FROM my-index LIMIT 50 (default is 200)
      Union     SELECT \* FROM my-index1 UNION SELECT \* FROM my-index2
      Minus     SELECT \* FROM my-index1 MINUS SELECT \* FROM my-index2
      ========= =======================================================

   .. caution::

      Large UNION and MINUS queries can cause high resource consumption, potentially leading to degrading cluster performance or even service interruptions. To mitigate this risk, you are advised to optimize the query structure or split large queries into smaller batches.

-  Conditions

   .. table:: **Table 2** Conditions

      ============== =========================================================
      Condition      Example
      ============== =========================================================
      Like           SELECT \* FROM my-index WHERE name LIKE 'j%'
      And            SELECT \* FROM my-index WHERE name LIKE 'j%' AND age > 21
      Or             SELECT \* FROM my-index WHERE name LIKE 'j%' OR age > 21
      Count distinct SELECT count(distinct age) FROM my-index
      In             SELECT \* FROM my-index WHERE name IN ('Bob', 'David')
      Not            SELECT \* FROM my-index WHERE name NOT IN ('Bob')
      Between        SELECT \* FROM my-index WHERE age BETWEEN 20 AND 30
      Aliases        SELECT avg(age) AS Average_Age FROM my-index
      Date           SELECT \* FROM my-index WHERE birthday='1990-11-15'
      Null           SELECT \* FROM my-index WHERE name IS NULL
      ============== =========================================================

-  Aggregations

   .. table:: **Table 3** Aggregations

      =========== ============================================
      Aggregation Example
      =========== ============================================
      avg()       SELECT avg(age) FROM my-index
      count()     SELECT count(age) FROM my-index
      max()       SELECT max(age) AS Highest_Age FROM my-index
      min()       SELECT min(age) AS Lowest_Age FROM my-index
      sum()       SELECT sum(age) AS Age_Sum FROM my-index
      =========== ============================================

-  Include and exclude fields

   .. table:: **Table 4** Include and exclude fields

      ========= ==================================================
      Pattern   Example
      ========= ==================================================
      include() SELECT include('a*'), exclude('age') FROM my-index
      exclude() SELECT exclude('``*name``') FROM my-index
      ========= ==================================================

-  Functions

   .. caution::

      You must enable fielddata in the document mapping for most string functions to work properly.

   .. table:: **Table 5** Functions

      =========== ============================================================
      Function    Example
      =========== ============================================================
      floor       SELECT floor(number) AS Rounded_Down FROM my-index
      trim        SELECT trim(name) FROM my-index
      log         SELECT log(number) FROM my-index
      log10       SELECT log10(number) FROM my-index
      substring   SELECT substring(name, 2,5) FROM my-index
      round       SELECT round(number) FROM my-index
      sqrt        SELECT sqrt(number) FROM my-index
      concat_ws   SELECT concat_ws(' ', age, height) AS combined FROM my-index
      /           SELECT number / 100 FROM my-index
      %           SELECT number % 100 FROM my-index
      date_format SELECT date_format(date, 'Y') FROM my-index
      =========== ============================================================

-  Joins

   .. caution::

      Supported join types: INNER JOIN, LEFT JOIN, and CROSS JOIN.

      Hard limits:

      -  Only two tables (indexes) can be joined.

      -  An alias must be specified for each table, for example, **FROM people p JOIN index b**.

      -  The ON condition supports only AND combinations, not OR or nested conditions.

      -  GROUP BY or ORDER BY cannot be used in a JOIN query.

      -  LIMIT and OFFSET cannot be used together. A negative example: **LIMIT 25 OFFSET 25**

      -  Fields from multiple indexes cannot be combined in the WHERE clause.

         A positive example:

         .. code-block::

            WHERE (a.type1 > 3 OR a.type1 < 0) AND (b.type2 > 4 OR b.type2 < -1)

         A negative example:

         .. code-block::

            WHERE (a.type1 > 3 OR b.type2 < 0) AND (a.type1 > 4 OR b.type2 < -1)

   .. table:: **Table 6** Joins

      +-----------------+-----------------------------------------------------------------------------------------------------------------------------+
      | Join            | Example                                                                                                                     |
      +=================+=============================================================================================================================+
      | Inner join      | SELECT s.firstname, s.lastname, s.gender, sc.name FROM student s JOIN school sc ON sc.name = s.school_name WHERE s.age > 20 |
      +-----------------+-----------------------------------------------------------------------------------------------------------------------------+
      | Left outer join | SELECT s.firstname, s.lastname, s.gender, sc.name FROM student s LEFT JOIN school sc ON sc.name = s.school_name             |
      +-----------------+-----------------------------------------------------------------------------------------------------------------------------+
      | Cross join      | SELECT s.firstname, s.lastname, s.gender, sc.name FROM student s CROSS JOIN school sc                                       |
      +-----------------+-----------------------------------------------------------------------------------------------------------------------------+

-  Show

   Show commands display indexes and mappings that match an index pattern. You can use **\*** or **%** for wildcards.

   .. table:: **Table 7** Show

      ================ ========================
      Show             Example
      ================ ========================
      Show tables like SHOW TABLES LIKE logs-\*
      ================ ========================

BI Integration via JDBC Driver
------------------------------

If you are using Tableau, Power BI, or a self-managed Java application, you can connect to a CSS cluster using the JDBC driver.

Download the JDBC driver from the `GitHub repository <https://github.com/opendistro-for-elasticsearch/sql-jdbc>`__.
