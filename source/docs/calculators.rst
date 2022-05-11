Calculators
=============

.. autoclass:: wannierberri.calculators.classes.Calculator



.. autoclass:: wannierberri.calculators.classes.StaticCalculator
   :show-inheritance:



.. autoclass:: wannierberri.calculators.classes.DynamicCalculator
   :show-inheritance:


Static (dependent only on Fermi level)
+++++++++++++++++++++++++++++++++++++++

.. automodule:: wannierberri.calculators.static
   :members: DOS, CumDOS, Spin, Morb, AHC, Ohmic_FermiSea, Ohmic_FermiSurf, Hall_classic_FermiSurf,BerryDipole_FermiSea, BerryDipole_FermiSurf, NLAHC_FermiSea, NLAHC_FermiSurf, NLDrude_FermiSea, NLDrude_FermiSurf, NLDrude_Fermider2, Spin_Hall, GME_orb_FermiSea, GME_orb_FermiSurf, GME_spin_FermiSea, GME_spin_FermiSurf
   :undoc-members:
   :show-inheritance:




Dynamic (dependent on Fermi level and frequency)
+++++++++++++++++++++++++++++++++++++++++++++++++

.. automodule:: wannierberri.calculators.dynamic
   :members: 
   :undoc-members:
   :show-inheritance:


Tabulating
+++++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: wannierberri.calculators.classes.TabulatorAll
   :show-inheritance:


.. automodule:: wannierberri.calculators.tabulate
   :members: Energy, BerryCurvature
   :undoc-members:
   :show-inheritance:
