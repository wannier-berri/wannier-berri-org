Initializing a System
======================

The first step in the ``wannierberri`` calculation is initialising the System.  This is done by means of child classes :class:`~wannierberri.__system.System` described below. 
They all have an important common method :func:`~wannierberri.System.set_symmetry`. 
The system may come either from :ref:`Wanier functions <sec-wan-fun>`  constructed by `Wannier90 <http://wannier90.org>`_, or from ref:`tight binding <sec-tb-models>` models. 

.. autoclass:: wannierberri.System
   :members: set_parameters , set_symmetry
   :undoc-members:
   :show-inheritance:

.. _sec-wan-fun:

From Wannier functions
----------------------

.. autoclass:: wannierberri.System_w90
   :show-inheritance:

.. _sec-tb-models:


From tight-binding models 
----------------------------------

``wannier90_tb.dat`` file
+++++++++++++++++++++++++

.. autoclass:: wannierberri.System_tb
   :show-inheritance:

PythTB
+++++++++

.. autoclass:: wannierberri.System_PythTB
   :show-inheritance:

TBmodels
+++++++++

.. autoclass:: wannierberri.System_TBmodels
   :show-inheritance:
