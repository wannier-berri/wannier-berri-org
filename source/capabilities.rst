
.. _sec-capabilities:

**************
Capabilities 
**************

.. role:: red
.. role:: green

**Note** : This is an incomplete list. Please refer to `Documentation for calculators <https://docs.wannier-berri.org/en/master/docs/calculators.html>`__ for details.


|NEW| Wannierisation
---------------

 WannierBerri can now construct Symmetry adapted Wannier functions (R. Sakuma `Phys. Rev. B 87, 235109 (2013) <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.87.235109>`__ )with 

   - spin-orbit coupling
   - time-reversal symmetry
   - magnetic symmetries
   - frozen window
   - compatible with Quantum ESPRESSO, VASP, and Abinit 

See `documentation <https://docs.wannier-berri.org/en/master/docs/wannierisation.html>`__ 
and `tutorial <https://tutorial.wannier-berri.org/tutorials/6_wannierisation/wannierise.html>`__  for details

|NEW| Automated search for projections
--------------------------------

 Search for suitable projections based on the symmetry indecators of the DFT bands within the frozen window. 
See `documentation <https://docs.wannier-berri.org/en/master/docs/projections_searcher.html>`__ 
and `tutorial <https://tutorial.wannier-berri.org/tutorials/7_find_projections/find_projections.html>`__  for details


Integration
-----------

see `Calculators <https://docs.wannier-berri.org/en/master/docs/calculators.html>`__ for details

The code may be used to evaluate the following quantities, represented
as Brillouin zone integrals.

Static (frequency-independent) quantities
++++++++++++++++++++++++++++++++++++++++++

see `StaticCalculator  <https://docs.wannier-berri.org/en/master/docs/calculators.html#static-dependent-only-on-fermi-level>`__ for details

Dynamic (frequency-dependent) quantities
++++++++++++++++++++++++++++++++++++++++++

see `DynamicCalculator  <https://docs.wannier-berri.org/en/master/docs/calculators.html#dynamic-dependent-on-fermi-level-and-frequency>`__ for details


Tabulating
----------

.. _figFefrmsf:
.. figure:: imag/figures/Fe-berry.pdf.svg

   Fermi surface of bcc iron, colored by the Berry curvature
   :math:`\Omega_z`. Figure produced using `FermiSurfer <https://fermisurfer.osdn.jp/>`_.

``WannerBerri`` can also tabulate certain band-resolved quantities over the
Brillouin zone producing files ``Fe_berry-?.frmsf``, containing the Energies
and Berry curvature of bands ``4-9`` (band counting starts from zero).
The format of the files allows to be directly passed to the
``FermiSurfer`` visualization tool (Kawamura 2019) which can produce a
plot like :numref:`figFefrmsf`. Transformation of files to other
visualization software is straightforward.

Some of the quantites that are available to tabulate are:

-  Berry curvature [Å\ :sup:`2`\]

   .. math:: \Omega^\gamma_n({\bf k})=-\epsilon_{\alpha\beta\gamma}{\rm Im\,}\langle\partial_\alpha u_{n{\bf k}}\vert\partial_\beta u_{n{\bf k}}\rangle;

-  orbital moment of Bloch states [eV·Å\ :sup:`2`\]

   .. math:: m^\gamma_n({\bf k})=\frac{e}{2\hbar}\epsilon_{\alpha\beta\gamma}{\rm Im\,}\langle\partial_\alpha u_{n{\bf k}}\vert H_{\bf k}-E_{n{\bf k}}\vert\partial_\beta u_{n{\bf k}}\rangle;

-  the expectation value of the Pauli operator [ħ]

   .. math:: \mathbf{s}_n({\bf k})=\langle u_{n{\bf k}}\vert\hat{\bf \sigma}\vert u_{n{\bf k}}\rangle;

-  the band gradients [eV·Å] :math:`\nabla_{\bf k}E_{n{\bf k}}`.

- Spin Berry curvature [ħ·Å\ :sup:`2`\]. Requires an additional parameter ``spin_current_type`` which can be ``"ryoo"`` or ``"qiao"``.

   .. math::

      \Omega^{{\rm spin};\,\gamma}_{\alpha\beta, n}({\bf k}) = -2 {\rm Im} \sum_{\substack{l \\ \varepsilon_{l{\bf k}} \neq \varepsilon_{n{\bf k}}}}
      \frac{\langle\psi_{n{\bf k}}\vert \frac{1}{2} \{ s^{\gamma}, v_\alpha \} \vert\psi_{l{\bf k}}\rangle
      \langle\psi_{l{\bf k}}\vert v_\beta\vert\psi_{n{\bf k}}\rangle}
      {(\varepsilon_{n{\bf k}}-\varepsilon_{l{\bf k}})^2}.

- k-space derivatives of the above quantities (following the `paper <https://arxiv.org/abs/2303.10129>`__)

see `full list here <https://docs.wannier-berri.org/en/master/docs/calculators.html#tabulating>`__

Evaluation of additional matrix elements 
-----------------------------------------

In order to produce the matrix elements that are not evaluated by a particular *ab initio* code, the following interfaces
have been developed:

mmn2uHu 
++++++++++++++++++

see `documentation <https://docs.wannier-berri.org/en/master/docs/mmn2uHu.html>`__ for more details


The |mmn2uHu| module evaluates the (``.uHu`` file) containing the matrix elements needed for orbital moment calculations

.. math::

    C_{mn}^{\mathbf{b}_1,\mathbf{b}_2}({\bf q})=\langle u_{m{\bf q}+\mathbf{b}_1}\vert\hat{H}_{\bf q}\vert u_{n{\bf q}+\mathbf{b}_2}\rangle.

on the basis of the ``.mmn`` and ``.eig`` files by means of the sum-over-states formula

.. math::

    C_{mn}^{\mathbf{b}_1,\mathbf{b}_2}({\bf q})\approx\sum_l^{l_{\rm max}}  \left(M_{lm}^{\mathbf{b}_1}({\bf q})\right)^* E_{l{\bf q}}   M_{ln}^{\mathbf{b}_2}({\bf q}).

and the (``.sHu`` and ``.sIu`` file) containing the matrix elements needed for Ryoo's spin current calculations(`Ryoo, Park, and Souza 2019 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.99.235113>`_)
on the basis of the ``.mmn``, ``.spn`` and ``.eig`` files by means of the sum-over-states formula

.. math::

    \langle u_{m{\bf q}}\vert\hat{s}\hat{H}_{\bf q}\vert u_{n{\bf q}+\mathbf{b}}\rangle \approx \sum_l^{l_{\rm max}}  \left(s_{lm}({\bf q})\right)^* E_{l{\bf q}}   M_{ln}^{\mathbf{b}}({\bf q}).
.. math::

    \langle u_{m{\bf q}}\vert\hat{s}\vert u_{n{\bf q}+\mathbf{b}}\rangle \approx \sum_l^{l_{\rm max}}  \left(s_{lm}({\bf q})\right)^*   M_{ln}^{\mathbf{b}}({\bf q}).  


vaspspn 
+++++++

see `documentation <file://///wsl.localhost/Ubuntu-24.04/home/stepan/github/wannier-berri-org/docs/html/capabilities.html#vaspspn>`__ for more details

The |vaspspn| computes the spin matrix

.. math:: s_{mn}({\bf q})=\langle u_{m{\bf q}}\vert\hat{\sigma}\vert u_{n{\bf q}}\rangle

based on the normalized pseudo-wavefunction read from the ``WAVECAR`` file written by 
`VASP <https://www.vasp.at/>`_




The |mmn2uHu| and |vaspspn| modules were initially developed and
used in (`Tsirkin, Puente, and Souza 2018 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.97.035158>`_) as separate scripts. 

.. include:: shortcuts.rst


