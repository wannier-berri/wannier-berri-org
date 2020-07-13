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

.. autoclass:: wannierberri.__system.System
   :members: set_symmetry

From Wannier functions
----------------------

.. autoclass:: System_w90
   :show-inheritance:


From tight-binding model
------------------------

.. autoclass:: System_tb
   :show-inheritance:


Symmetries
======================

.. automodule:: wannierberri.symmetry
   :members: Rotation,Mirror
   :undoc-members:
   :show-inheritance:
