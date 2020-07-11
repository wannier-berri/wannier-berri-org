
.. _sec-capabilities:

*********************
Capabilities
*********************


Integrate
----------

The code may be used to evaluate the following quantities, represented
as Brillouin zone integrals:

-  ``’ahc’``:  intrinsic **anomalous Hall conductivity** (Nagaosa et al. 2010):

   .. math:: \sigma_{\alpha\beta}^{\rm AHC}=-\epsilon_{\alpha\beta\gamma}\frac{e^2}{\hbar}\sum_n^{\rm occ}\int[d{\bf k}]\Omega_n^{\gamma}\label{eq:AHE}

-  anomalous **Nernst** conductivity (Xiao et al. 2006)
   :math:`\alpha_{\alpha\beta}` may be obtained from
   :math:`\sigma_{\alpha\beta}(\mu)` evaluated over e dense grid of
   chemical potentials :math:`\mu`

   .. math:: \alpha_{xy}^{\rm ANE}=-\frac{1}{e}\int d\varepsilon \frac{\partial f}{\partial\mu}\sigma_{xy}(\varepsilon)\frac{\varepsilon-\mu}{T} \label{eq:ANE}

-  ``’Morb’``:  **orbital magnetization**

   .. math:: M^\gamma_n({\bf k})=\frac{e}{2\hbar}{\rm Im\,}\epsilon_{\alpha\beta\gamma}\sum_n^{\rm occ}\int[d{\bf k}]\langle\partial_a u_{n{\bf k}}\vert H_{\bf k}+E_{n{\bf k}}-2\mu\vert\partial_b u_{n{\bf k}}\rangle

-  ``’berry_dipole’``:  **Berry curvature dipole** - Fermi-sea formula (preferred)

   .. math:: D_{\alpha\beta}(\mu)=\int[d{\bf k}] \sum_n^{\rm occ} \partial_\alpha\Omega_n^{\beta} \label{eq:dipole}

-  ``’berry_dipole_fsurf’``:  Berry curvature dipole - Fermi surface formula:

   .. math:: D_{\alpha\beta}(\mu)=\sum_n\int[d{\bf k}]\partial_\alpha E_{n{\bf k}}\Omega_n^{\beta}\delta(E_{n{\bf k}}-\mu) \label{eq:dipole-fsurf}

-  ``’tensorK’``:  **gyrotropic magnetoelectric effect (GME)** tensor - Fermi-sea formula (preferred):

   .. math:: K^{\rm orb}_{\alpha\beta}(\mu)=\sum_n\int[d{\bf k}]\partial_\alpha m_n^{\beta}   \label{eq:KME}

-  ``’tensorK_fsurf’``:  gyrotropic magnetoelectric effect (GME) tensor - Fermi-surface formula:

   .. math:: K^{\rm orb}_{\alpha\beta}(\mu)=\sum_n\int[d{\bf k}]\partial_\alpha E_{n{\bf k}}m_n^{\beta}\delta(E_{n{\bf k}}-\mu)  \label{eq:KME-fsurf}


-  ``’conductivity_Ohmic’``:  **ohmic conductivity** within the Boltzmann
   transport theory in constant relaxation time (:math:`\tau`)
   approximation in the Fermi-sea formula (preferred) : 

   .. math:: \sigma_{\alpha\beta}^{\rm Ohm}(\mu)  =\tau\int[d{\bf k}]\sum_n^{E_{n{\bf k}}<\mu} \partial^2_{\alpha\beta} E_{n{\bf k}}


-  ``’conductivity_Ohmic_fsurf’``:  ohmic conductivity within the Boltzmann
   transport theory in constant relaxation time (:math:`\tau`)
   approximation.

   .. math:: \sigma_{\alpha\beta}^{\rm Ohm}(\mu) =\tau\sum_n\int[d{\bf k}]\partial_\alpha E_{n{\bf k}}\partial_\beta E_{n{\bf k}} \delta(E_{n{\bf k}}-\mu) 


-  ``’dos’``:  **density of states** :math:`n(E)`

-  ``’cumdos’``:  **cumulative density of states**

   .. math:: N(E) = \int\limits_{-\infty}^En(\epsilon)d\epsilon

-  'opt_conductivity': Kubo-greenwood formula for optical conductivity
  
   .. math:: \sigma_{\alpha\beta}(\hbar\omega)=\frac{ie^2\hbar}{N_k\Omega_c}
      \sum_{\bf k}\sum_{n,m}
      \frac{f_{m{\bf k}}-f_{n{\bf k}}}
      {\varepsilon_{m{\bf k}}-\varepsilon_{n{\bf k}}}
      \frac{\langle\psi_{n{\bf k}}\vert v_\alpha\vert\psi_{m{\bf k}}\rangle
      \langle\psi_{m{\bf k}}\vert v_\beta\vert\psi_{n{\bf k}}\rangle}
      {\varepsilon_{m{\bf k}}-\varepsilon_{n{\bf k}}-(\hbar\omega+i\eta)}.



Tabulate
----------

Moreover the following quantities can be tabulated over a grid of
:math:`{\bf k}` points to be visualized with some software.

-  ``’berry’``:  Berry curvature

   .. math:: \Omega^\gamma_n({\bf k})=-{\rm Im\,}\epsilon_{\alpha\beta\gamma}\langle\partial_a u_{n{\bf k}}\vert\partial_b u_{n{\bf k}}\rangle

-  ``’morb’``:  orbital moment of Bloch states

   .. math:: m^\gamma_n({\bf k})=\frac{e}{2\hbar}{\rm Im\,}\epsilon_{\alpha\beta\gamma}\langle\partial_a u_{n{\bf k}}\vert H_{\bf k}-E_{n{\bf k}}\vert\partial_b u_{n{\bf k}}\rangle

-  ``’spin’``:  the expectation value of the Pauli operator.:

   .. math:: \mathbf{s}_n({\bf k})=\langle u_{n{\bf k}}\vert\hat{\bf \sigma}\vert u_{n{\bf k}}\rangle

-  ``’V’``:  the band gradients :math:`\nabla_{\bf k}E_{n{\bf k}}`

The result is written in the format ready to be used by the FermiSurfer
package (Kawamura 2019)



