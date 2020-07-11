.. Wannier Berri documentation master file, created by
   sphinx-quickstart on Tue Jul  7 23:40:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. title:: Wannier Berri

.. image:: imag/logo-WB/WANNIERBERRI-line-redblack.png
    :width: 700px
    :alt: Wannier Berri
    :align: center

|

is a code to calculate different properties by neans of Wannier interpolation. 
It may be considered very much improved version of ``postw90.x`` part of `Wannier90 <https://wannier.org>`_.  

#############
Advantages
#############

    *  **speed** - it may be upto **1000 or more times faster** then ``postw90.x`` : :ref:`comparison  <sec-timing>`

    *  **extensive functionality** -- see :ref:`sec-capabilities`

    *  **felxibility** -- may be used with Wannier functions and TB models

    *  use of  :ref:`symmetries <sec-symmetries>`  to reduce evaluation to symmetry-irreducible **k** points.

    *  :ref:`fast Fourier transform  <sec-FFT>`  

    *  Recursive adaptive :ref:`refinement   <sec-refine>` for enhanced accuracy.

    *  :ref:`Fermi scan <sec-fermiscan>`  and :ref:`minimal distance replica selection  <sec-replica>` have no cost

#############
Please cite
#############

    *   Destraz, Daniel, Lakshmi Das, Stepan S. Tsirkin, Yang Xu, Titus Neupert, J. Chang, A. Schilling, et al. 2020. “Magnetism and
        Anomalous Transport in the Weyl Semimetal Pralge: Possible Route
        to Axial Gauge Fields.” *Npj Quantum Materials* 5 (1): 5.
        `DOI <https://doi.org/10.1038/s41535-019-0207-7>`_.

    *   Stepan S. Tsirkin. "WannierBerri: an advanced python code for interpolation and integration of Berry curvature and related quantities", to be published

#########################################################
`Presentation slides 
#########################################################

.. image:: imag/presentation.png
   :width: 100px
   :target: http://slides.wannier-berri.org


##############
Contact:
##############

    *    Subscribe to `mailing list <https://physik.lists.uzh.ch/sympa/info/wannier-berri>`_.
    *    contact author: `stepan.tsirkin@uzh.ch <mailto:stepan.tsirkin@uzh.ch>`_
    *    GitHub repository: `<https://github.com/stepan-tsirkin/wannier-berri>`_

################################################################################################################
Install  via ``pip``  (`PyPI <https://pypi.org/project/wannierberri>`_):
################################################################################################################
::

   pip3 install wannierberri



.. toctree:: 
   :maxdepth: 3
   :hidden:

   news
   capabilities
   exampleFe
   install
   wannierberri
   methods
   timing
   people
   organizations
   contribute
   software



########################
.. Indices and tables
########################
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
