Calculators
=============

.. autoclass:: wannierberri.calculators.Calculator




Static (dependent only on Fermi level)
+++++++++++++++++++++++++++++++++++++++

.. autoclass:: wannierberri.calculators.static.StaticCalculator
   :members: __init__, __call__

In the following `**kwargs` refer to the arguments of :class:`~wannierberri.calculators.static.StaticCalculator`

.. automodule:: wannierberri.calculators.static
   :members: DOS, CumDOS, Spin, Morb, AHC, Ohmic_FermiSea, Ohmic_FermiSurf, Hall_classic_FermiSurf,BerryDipole_FermiSea, BerryDipole_FermiSurf, NLAHC_FermiSea, NLAHC_FermiSurf, NLDrude_FermiSea, NLDrude_FermiSurf, NLDrude_Fermider2, Spin_Hall, GME_orb_FermiSea, GME_orb_FermiSurf, GME_spin_FermiSea, GME_spin_FermiSurf
   :undoc-members:
   :show-inheritance:
   :exclude-members: StaticCalculator




Dynamic (dependent on Fermi level and frequency)
+++++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: wannierberri.calculators.dynamic.DynamicCalculator

.. automodule:: wannierberri.calculators.dynamic
   :members: 
   :undoc-members:
   :show-inheritance:
   :exclude-members: DynamicCalculator

Tabulating
+++++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: wannierberri.calculators.TabulatorAll
   :show-inheritance:

.. autoclass:: wannierberri.calculators.tabulate.Tabulator
   :show-inheritance:


.. automodule:: wannierberri.calculators.tabulate
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: Tabulator
