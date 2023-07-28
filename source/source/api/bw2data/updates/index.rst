:py:mod:`bw2data.updates`
=========================

.. py:module:: bw2data.updates


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.updates.Updates




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.updates.UPDATE_ACTIVITYDATASET
   bw2data.updates.UPDATE_EXCHANGEDATASET
   bw2data.updates.UPTODATE_WARNING
   bw2data.updates.hash_re
   bw2data.updates.is_hash


.. py:class:: Updates

   Bases: :py:obj:`object`

   .. py:attribute:: UPDATES

      

   .. py:method:: check_automatic_updates()
      :classmethod:

      Get list of automatic updates to be applied


   .. py:method:: check_status(verbose=True)
      :classmethod:

      Check if updates need to be applied.

      :returns: List of needed updates (strings), if any.


   .. py:method:: database_search_directories_20()
      :classmethod:


   .. py:method:: do_update(key)
      :classmethod:


   .. py:method:: explain(key)
      :classmethod:


   .. py:method:: processed_data_format_change_23()
      :classmethod:


   .. py:method:: reprocess_all_1_0()
      :classmethod:

      1.0: Reprocess all to make sure default 'loc' value inserted when not specified.


   .. py:method:: schema_change_20_compound_keys()
      :classmethod:


   .. py:method:: set_initial_updates()
      :classmethod:



.. py:data:: UPDATE_ACTIVITYDATASET
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        BEGIN;
        DROP INDEX IF EXISTS "activitydataset_key";
        ALTER TABLE ActivityDataset rename to AD_old;
        CREATE TABLE "activitydataset" (
            "id" INTEGER NOT NULL PRIMARY KEY,
            "database" TEXT NOT NULL,
            "code" TEXT NOT NULL,
            "data" BLOB NOT NULL,
            "location" TEXT,
            "name" TEXT,
            "product" TEXT,
            "type" TEXT
        );
        INSERT INTO ActivityDataset ("database", "code", "data", "location", "name", "product", "type")
            SELECT substr(key, 0, instr(key, '⊡')),
                substr("key", instr("key", '⊡') + 1),
                "data",
                "location",
                "name",
                "product",
                "type"
            FROM AD_old;
        CREATE UNIQUE INDEX "activitydataset_key" ON "activitydataset" ("database", "code");
        DROP TABLE AD_old;
        COMMIT;
        """

    .. raw:: html

        </details>

   

.. py:data:: UPDATE_EXCHANGEDATASET
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        BEGIN;
        DROP INDEX IF EXISTS "exchangedataset_database";
        DROP INDEX IF EXISTS "exchangedataset_input";
        DROP INDEX IF EXISTS "exchangedataset_output";
        ALTER TABLE ExchangeDataset rename to ED_old;
        CREATE TABLE "exchangedataset" (
            "id" INTEGER NOT NULL PRIMARY KEY,
            "data" BLOB NOT NULL,
            "input_database" TEXT NOT NULL,
            "input_code" TEXT NOT NULL,
            "output_database" TEXT NOT NULL,
            "output_code" TEXT NOT NULL,
            "type" TEXT NOT NULL
        );
        INSERT INTO ExchangeDataset ("data", "input_database", "input_code", "output_database", "output_code", "type")
            SELECT "data",
                substr("input", 0, instr("input", '⊡')),
                substr("input", instr("input", '⊡') + 1),
                substr("output", 0, instr("output", '⊡')),
                substr("output", instr("output", '⊡') + 1),
                "type"
            FROM ED_old;
        CREATE INDEX "exchangedataset_input" ON "exchangedataset" ("input_database", "input_code");
        CREATE INDEX "exchangedataset_output" ON "exchangedataset" ("output_database", "output_code");
        DROP TABLE ED_old;
        COMMIT;
        """

    .. raw:: html

        </details>

   

.. py:data:: UPTODATE_WARNING
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        
        Your data needs to be updated. Please run the following program on the command line:
        
        	bw2-uptodate
        """

    .. raw:: html

        </details>

   

.. py:data:: hash_re

   

.. py:data:: is_hash

   

