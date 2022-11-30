:py:mod:`bw2analyzer.utils`
===========================

.. py:module:: bw2analyzer.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.utils.contribution_for_all_datasets_one_method
   bw2analyzer.utils.print_recursive_calculation
   bw2analyzer.utils.print_recursive_supply_chain
   bw2analyzer.utils.infinite_alphabet
   bw2analyzer.utils.recursive_calculation_to_object



.. py:function:: contribution_for_all_datasets_one_method(database, method, progress=True)

   Calculate contribution analysis (for technosphere processes) for all inventory datasets in one database for one LCIA method.

   :param \*database*: Name of database
   :type \*database*: str
   :param \*method*: Method tuple
   :type \*method*: tuple

   :returns: NumPy array of relative contributions. Each column sums to one.
             Lookup dictionary, dataset keys to row/column indices


.. py:function:: print_recursive_calculation(activity, lcia_method, amount=1, max_level=3, cutoff=0.01, file_obj=None, tab_character='  ', use_matrix_values=False, _lca_obj=None, _total_score=None, __level=0, __first=True)

   Traverse a supply chain graph, and calculate the LCA scores of each component. Prints the result with the format:

   {tab_character * level }{fraction of total score} ({absolute LCA score for this input} | {amount of input}) {input activity}

   :param activity: ``Activity``. The starting point of the supply chain graph.
   :param lcia_method: tuple. LCIA method to use when traversing supply chain graph.
   :param amount: int. Amount of ``activity`` to assess.
   :param max_level: int. Maximum depth to traverse.
   :param cutoff: float. Fraction of total score to use as cutoff when deciding whether to traverse deeper.
   :param file_obj: File-like object (supports ``.write``), optional. Output will be written to this object if provided.
   :param tab_character: str. Character to use to indicate indentation.
   :param use_matrix_values: bool. Take exchange values from the matrix instead of the exchange instance ``amount``. Useful for Monte Carlo, but can be incorrect if there is more than one exchange from the same pair of nodes.

   Normally internal args:
       _lca_obj: ``LCA``. Can give an instance of the LCA class (e.g. when doing regionalized or Monte Carlo LCA)
       _total_score: float. Needed if specifying ``_lca_obj``.

   Internal args (used during recursion, do not touch);
       __level: int.
       __first: bool.

   :returns: Nothing. Prints to ``sys.stdout`` or ``file_obj``


.. py:function:: print_recursive_supply_chain(activity, amount=1, max_level=2, cutoff=0, file_obj=None, tab_character='  ', __level=0)

   Traverse a supply chain graph, and prints the inputs of each component.

   This function is only for exploration; use ``bw2calc.GraphTraversal`` for a better performing function.

   The results displayed here can also be incorrect if

   :param activity: ``Activity``. The starting point of the supply chain graph.
   :param amount: int. Supply chain inputs will be scaled to this value.
   :param max_level: int. Max depth to search for.
   :param cutoff: float. Inputs with amounts less than ``amount * cutoff`` will not be printed or traversed further.
   :param file_obj: File-like object (supports ``.write``), optional. Output will be written to this object if provided.
   :param tab_character: str. Character to use to indicate indentation.
   :param __level: int. Current level of the calculation. Only used internally, do not touch.

   :returns: Nothing. Prints to ``stdout`` or ``file_obj``


.. py:function:: infinite_alphabet()

   Return generator with values a-z, then aa-az, ba-bz, then aaa-aaz, aba-abz, etc.


.. py:function:: recursive_calculation_to_object(activity, lcia_method, amount=1, max_level=3, cutoff=0.01, as_dataframe=False, root_label='root', use_matrix_values=False, _lca_obj=None, _total_score=None, __result_list=None, __level=0, __label='', __parent=None)

   Traverse a supply chain graph, and calculate the LCA scores of each component. Adds a dictionary to ``result_list`` of the form:

       {
           'label': Label of this branch. Starts with nothing, then A, AA, AB, AAA, AAB, etc.
           'score': Absolute score of this activity
           'fraction': Fraction of total score of this activity
           'amount': Input amount of the reference product of this activity
           'name': Name of this activity
           'key': Activity key
           'root_label': Starting label of root element for recursion.
       }

   :param activity: ``Activity``. The starting point of the supply chain graph.
   :param lcia_method: tuple. LCIA method to use when traversing supply chain graph.
   :param amount: int. Amount of ``activity`` to assess.
   :param max_level: int. Maximum depth to traverse.
   :param cutoff: float. Fraction of total score to use as cutoff when deciding whether to traverse deeper.
   :param as_dataframe: Return results as a list (default) or a pandas ``DataFrame``
   :param use_matrix_values: bool. Take exchange values from the matrix instead of the exchange instance ``amount``. Useful for Monte Carlo, but can be incorrect if there is more than one exchange from the same pair of nodes.

   Internal args (used during recursion, do not touch):
       __result_list: list.
       __level: int.
       __label: str.
       __parent: str.

   :returns: List of dicts


