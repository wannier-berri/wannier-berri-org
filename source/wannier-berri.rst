********************
Documentation
********************

.. automodule:: wannierberri

Integrating
===============

.. autofunction:: integrate

Tabulating
===============

.. autofunction:: tabulate

Creating a grid
===============

.. autoclass:: Grid


Initializing a System
======================

The first step in the ``wannierberri`` calculation is initialising the System.  This is done by means of child classes :class:`~wannierberri.__system.System` described below. 
They all have an important common method :func:`~wannierberri.__system.System.set_symmetry`. 
The system may come either from :ref:`Wanier functions <sec-wan-fun>`  constructed by `Wannier90 <http://wannier90.org>`_, or from ref:`tight binding <sec-tb-models>` models. 

.. autoclass:: wannierberri.__system.System
   :members: set_symmetry

.. _sec-wan-fun:

From Wannier functions
----------------------

.. autoclass:: System_w90
   :show-inheritance:

.. _sec-tb-models:


From tight-binding models 
----------------------------------

``wannier90_tb.dat`` file
+++++++++++++++++++++++++

.. autoclass:: System_tb
   :show-inheritance:

PythTB
+++++++++

.. autoclass:: System_PythTB
   :show-inheritance:

TBmodels
+++++++++

.. autoclass:: System_TBmodels
   :show-inheritance:

Symmetries
======================

.. automodule:: wannierberri.symmetry
   :members: Rotation,Mirror
   :undoc-members:
   :show-inheritance:
