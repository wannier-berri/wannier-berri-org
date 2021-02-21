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

is a code to calculate different properties by means of Wannier interpolation. 
It may be considered as a strongly improved version of ``postw90.x`` part of `Wannier90 <https://wannier.org>`_.  

#############
Advantages
#############

    *  **speed**  - it may be upto **1000 or more times faster** then ``postw90.x`` : :ref:`comparison  <sec-timing>`

    *  **extensive functionality** -- see :ref:`sec-capabilities`

    *  **felxibility** -- may be used with Wannier functions and tight-binding models

    *  use of  :ref:`symmetries <sec-symmetry>`  to reduce evaluation to symmetry-irreducible **k** points.

    *  :ref:`fast Fourier transform  <sec-FFT>`  

    *  Recursive adaptive :ref:`refinement   <sec-refine>` for enhanced accuracy.

    *  :ref:`Fermi scan <sec-fermisea>`  and :ref:`minimal distance replica selection  <sec-replica>` have no cost

#############
Please cite
#############

    *   Stepan S. Tsirkin. High performance Wannier interpolation of Berry curvature and related quantities with WannierBerri code. `npj Comput Mater 7, 33 (2021).  <https://www.nature.com/articles/s41524-021-00498-5>`_ (Open Access).

    *   Destraz, Daniel, Lakshmi Das, Stepan S. Tsirkin, Yang Xu, Titus Neupert, J. Chang, A. Schilling, et al. 2020. `“Magnetism and
        Anomalous Transport in the Weyl Semimetal PrAlGe: Possible Route
        to Axial Gauge Fields.”` `Npj Quantum Materials 5 (1): 5. <https://doi.org/10.1038/s41535-019-0207-7>`_.


##############
Contact:
##############

    *    Subscribe to `mailing list <https://physik.lists.uzh.ch/sympa/info/wannier-berri>`_ . 
         It is the **preferred** way of communication with the authors and other users, to ask any questions, report bugs, request new features, etc ). 
         Also consider searching through the mailing list `archive <https://physik.lists.uzh.ch/sympa/arc/wannier-berri>`_
    *    | GitHub repository: `<https://github.com/stepan-tsirkin/wannier-berri>`_  
         | |github|
    *    |github-follow|
    *    |twitter-button|
    
.. |twitter-button| raw:: html

   <a href="https://twitter.com/WannierBerri?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @WannierBerri</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. |github|    raw:: html

   <a class="github-button" href="https://github.com/stepan-tsirkin/wannier-berri/subscription" data-icon="octicon-eye" aria-label="Watch stepan-tsirkin/wannier-berri on GitHub">Watch</a>
   <a class="github-button" href="https://github.com/stepan-tsirkin/wannier-berri/issues" data-icon="octicon-issue-opened" aria-label="Issue stepan-tsirkin/wannier-berri on GitHub">Issue</a>
   <a class="github-button" href="https://github.com/stepan-tsirkin/wannier-berri/archive/master.zip" data-icon="octicon-download" aria-label="Download stepan-tsirkin/wannier-berri on GitHub">Download</a>
   <a class="github-button" href="https://github.com/stepan-tsirkin/wannier-berri/fork" data-icon="octicon-repo-forked" aria-label="Fork stepan-tsirkin/wannier-berri on GitHub">Fork</a>
   <a class="github-button" href="https://github.com/stepan-tsirkin/wannier-berri" data-icon="octicon-star" aria-label="Star stepan-tsirkin/wannier-berri on GitHub">Star</a>

.. |github-follow|  raw:: html

   <a class="github-button" href="https://github.com/stepan-tsirkin" aria-label="Follow @stepan-tsirkin on GitHub">Follow @stepan-tsirkin</a>



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
   timing
   exampleFe
   documentation
   methods
   install
   benchmark
   people
   organizations
   contribute
   software
   literature


