:original_name: css_01_0061.html

.. _css_01_0061:

Elasticsearch SQL
=================

For Elasticsearch 6.5.4 and later versions, Open Distro for Elasticsearch SQL lets you write queries in SQL rather than in the Elasticsearch query domain-specific language (DSL).

If you are already familiar with SQL and do not want to learn query DSL, this feature is a great option.

Basic Operations
----------------

To use this function, send requests to the **\_opendistro/_sql** URI. You can use a request parameter or the request body (recommended).

.. code-block:: text

   GET https://<host>:<port>/_opendistro/_sql?sql=select * from my-index limit 50

.. code-block:: text

   POST https://<host>:<port>/_opendistro/_sql
   {
     "query": "SELECT * FROM my-index LIMIT 50"
   }

You can run the cURL command:

.. code-block::

   curl -XPOST https://localhost:9200/_opendistro/_sql -u username:password -k -d '{"query": "SELECT * FROM kibana_sample_data_flights LIMIT 10"}' -H 'Content-Type: application/json'

By default, JSON is returned for query. You can also set the format parameter for the data to be returned in CSV format.

.. code-block:: text

   POST _opendistro/_sql?format=csv
   {
     "query": "SELECT * FROM my-index LIMIT 50"
   }

When data is returned in CSV format, each row corresponds to a document and each column corresponds to a field.

Supported Operations
--------------------

Open Distro for Elasticsearch supports the following SQL operations: statements, conditions, aggregations, include and exclude fields, common functions, joins, and show.

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

   .. note::

      As with any complex query, large UNION and MINUS statements can strain or even crash your cluster.

-  Conditions

   .. table:: **Table 2** Conditions

      +----------------+-----------------------------------------------------------------+
      | Condition      | Example                                                         |
      +================+=================================================================+
      | Like           | SELECT \* FROM my-index WHERE name LIKE 'j%'                    |
      +----------------+-----------------------------------------------------------------+
      | And            | SELECT \* FROM my-index WHERE name LIKE 'j%' AND age > 21       |
      +----------------+-----------------------------------------------------------------+
      | Or             | SELECT \* FROM my-index WHERE name LIKE 'j%' OR age > 21        |
      +----------------+-----------------------------------------------------------------+
      | Count distinct | SELECT count(distinct age) FROM my-index                        |
      +----------------+-----------------------------------------------------------------+
      | In             | SELECT \* FROM my-index WHERE name IN ('alejandro', 'carolina') |
      +----------------+-----------------------------------------------------------------+
      | Not            | SELECT \* FROM my-index WHERE name NOT IN ('jane')              |
      +----------------+-----------------------------------------------------------------+
      | Between        | SELECT \* FROM my-index WHERE age BETWEEN 20 AND 30             |
      +----------------+-----------------------------------------------------------------+
      | Aliases        | SELECT avg(age) AS Average_Age FROM my-index                    |
      +----------------+-----------------------------------------------------------------+
      | Date           | SELECT \* FROM my-index WHERE birthday='1990-11-15'             |
      +----------------+-----------------------------------------------------------------+
      | Null           | SELECT \* FROM my-index WHERE name IS NULL                      |
      +----------------+-----------------------------------------------------------------+

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

   .. note::

      You must enable fielddata in the document mapping for most string functions to work properly.

-  Joins

   .. table:: **Table 6** Joins

      +-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
      | Join            | Example                                                                                                                                     |
      +=================+=============================================================================================================================================+
      | Inner join      | SELECT p.firstname, p.lastname, p.gender, dogs.name FROM people p JOIN dogs d ON d.holdersName = p.firstname WHERE p.age > 12 AND d.age > 1 |
      +-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
      | Left outer join | SELECT p.firstname, p.lastname, p.gender, dogs.name FROM people p LEFT JOIN dogs d ON d.holdersName = p.firstname                           |
      +-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
      | Cross join      | SELECT p.firstname, p.lastname, p.gender, dogs.name FROM people p CROSS JOIN dogs d                                                         |
      +-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+

   For details about the constraints and limitations, see :ref:`Joins <css_01_0061__section89917481618>`.

-  Show

   Show commands display indices and mappings that match an index pattern. You can use **\*** or **%** for wildcards.

   .. table:: **Table 7** Show

      ================ ========================
      Show             Example
      ================ ========================
      Show tables like SHOW TABLES LIKE logs-\*
      ================ ========================

.. _css_01_0061__section89917481618:

Joins
-----

Open Distro for Elasticsearch SQL supports inner joins, left outer joins and cross joins. Joins have the following constraints:

-  You can only join two indices.

-  You must use an alias for an index (for example, people p).

-  In an ON clause, you can only use the AND conditions.

-  In a WHERE statement, do not combine trees that contain multiple indices. For example, the following statement will work:

   .. code-block::

      WHERE (a.type1 > 3 OR a.type1 < 0) AND (b.type2 > 4 OR b.type2 < -1)

   The following statement will not work:

   .. code-block::

      WHERE (a.type1 > 3 OR b.type2 < 0) AND (a.type1 > 4 OR b.type2 < -1)

-  You cannot use GROUP BY or ORDER BY to obtain results.

-  LIMIT with OFFSET (for example, LIMIT 25 OFFSET 25) is not supported.

JDBC Driver
-----------

The Java Database Connectivity (JDBC) driver allows you to integrate Open Distro for Elasticsearch with your business intelligence (BI) applications.

For details about how to download and use JAR files, see `GitHub Repositories <https://github.com/opendistro-for-elasticsearch/sql-jdbc>`__.
