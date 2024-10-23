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

a code to calculate different properties by means of Wannier interpolation: Berry curvature, orbital moment and derived properties.

|NEW| :ref:`WannierBerri World Tour <sec-worldtour>`  is open for applications

#############
Advantages
#############

    * |NEW| Symmetry adapted Wannier functions (R. Sakuma `Phys. Rev. B 87, 235109 (2013) <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.87.235109>`__ )with 

      - spin-orbit coupling
      - time-reversal symmetry
      - magnetic symmetries
      - frozen window
      - compatible with Quantum ESPRESSO, VASP, and Abinit 

      See `documentation <https://docs.wannier-berri.org/en/master/docs/wannierisation.html>`__ 
      and `tutorial <https://tutorial.wannier-berri.org/tutorials/6_wannierisation/wannierise.html>`__  for details

    *  **speed**  - it may be upto **1000 or more times faster** then ``postw90.x`` : :ref:`comparison  <sec-timing>`

    *  **extensive functionality** -- see :ref:`sec-capabilities`

    *  **felxibility** -- may be used with 
         - Wannier functions calculated by 
               +  WannierBerri itself ( `docs <https://docs.wannier-berri.org/en/master/docs/wannierisation.html>`__ )
               +  Wannier90 ( `docs <https://docs.wannier-berri.org/en/master/docs/system.html#id1>`__ )
               +  FPLO ( `docs <https://docs.wannier-berri.org/en/master/docs/system.html#fplo>`__ )
               +  ASE ( `docs <https://docs.wannier-berri.org/en/master/docs/system.html#ase>`__ )
         -  tight-binding models
               + PythTB ( `docs <https://docs.wannier-berri.org/en/master/docs/system.html#pythtb>`__ )
               + TBmodels ( `docs <https://docs.wannier-berri.org/en/master/docs/system.html#tbmodels>`__ )
         - :math:`k\cdot p` `models <https://docs.wannier-berri.org/en/master/docs/system.html#mathbf-k-cdot-mathbf-p-models>`__
         
    *  use of `symmetries <https://docs.wannier-berri.org/en/master/symmetries.html>`__  to reduce evaluation to symmetry-irreducible **k** points and increase precision.

    *  `fast Fourier transform  <https://www.nature.com/articles/s41524-021-00498-5/figures/1>`__  

    *  Recursive adaptive  `refinement   <https://www.nature.com/articles/s41524-021-00498-5/figures/1>`__ for enhanced accuracy.

    *  `Fermi scan <https://www.nature.com/articles/s41524-021-00498-5/figures/4>`__  and
       `minimal distance replica selection  <https://www.nature.com/articles/s41524-021-00498-5/figures/3>`__ have no cost

#############
Please cite
#############

    *   Stepan S. Tsirkin. High performance Wannier interpolation of Berry curvature and related quantities with WannierBerri code. `npj Comput Mater 7, 33 (2021).  <https://www.nature.com/articles/s41524-021-00498-5>`_ (Open Access).

################
Documentation
################

Link to detailed `Documentation <https://docs.wannier-berri.org>`__


################
Tutorials
################

Tutorials in Jupyter notebooks are available on `GitHub  <https://github.com/wannier-berri/WannierBerri-tutorial>`__


##############
Contact:
##############

    *    The **preferred** way of commonication is  the `GitHub repository: <https://github.com/wannier-berri/wannier-berri>`_   via |github-issue| or  |github-discussion|
    *    |github|
    *    Consider subscribing to the `mailing list <https://physik.lists.uzh.ch/sympa/info/wannier-berri>`_ .
         If you do not wish to register on GitHub, questions also may be asked there
         Also updates to the code are announced there.
         Also please search through the mailing list `archive <https://physik.lists.uzh.ch/sympa/arc/wannier-berri>`_
    
.. |twitter-button| raw:: html

   <a href="https://twitter.com/WannierBerri?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @WannierBerri</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. |github|    raw:: html

   <a class="github-button" href="https://github.com/wannier-berri/wannier-berri/subscription" data-icon="octicon-eye" aria-label="Watch wannier-berri/wannier-berri on GitHub">Watch</a>
   <a class="github-button" href="https://github.com/wannier-berri/wannier-berri/archive/master.zip" data-icon="octicon-download" aria-label="Download wannier-berri/wannier-berri on GitHub">Download</a>
   <a class="github-button" href="https://github.com/wannier-berri/wannier-berri/fork" data-icon="octicon-repo-forked" aria-label="Fork wannier-berri/wannier-berri on GitHub">Fork</a>
   <a class="github-button" href="https://github.com/wannier-berri/wannier-berri" data-icon="octicon-star" aria-label="Star wannier-berri/wannier-berri on GitHub">Star</a>
   <a class="github-button" href="https://github.com/wannier-berri" aria-label="Follow @wannier-berri on GitHub">Follow @wannier-berri</a>



.. |github-issue|  raw:: html

   <a class="github-button" href="https://github.com/wannier-berri/wannier-berri/issues" data-icon="octicon-issue-opened" aria-label="Issue wannier-berri/wannier-berri on GitHub">Issue</a>


.. |github-discussion|  raw:: html

   <a class="github-button" href="https://github.com/wannier-berri/wannier-berri/discussions" data-icon="octicon-discussion-opened" aria-label="Issue wannier-berri/wannier-berri on GitHub">Discussion</a>


################################################################################################################
Install  via ``pip``  (`PyPI <https://pypi.org/project/wannierberri>`_):
################################################################################################################
::

   pip3 install wannierberri


#########################
Author
#########################
`Stepan Tsirkin  <https://www.ikerbasque.net/es/stepan-tsirkin>`_,   
Ikerbasque Research Fellow at `Materials Physics Center <https://cfm.ehu.es/team/stepan-tsirkin/>`__, San Sebastian, Spain.


************************
Contributing to the code
************************

``WannierBerri``\ is a free open-source projec, under the GNU public
Licence v2, and everyone is welcome to modify the code to better match
one’s own needs. Contributions that might be useful for general public
are encouraged to be submitted via pull request to the  
`gitHub repository <https://github.com/wannier-berri/wannier-berri>`_.


.. toctree:: 
   :maxdepth: 3
   :hidden:

   worldtour
   capabilities
   Documentation <https://docs.wannier-berri.org>
   Tutorials  <https://tutorial.wannier-berri.org>
   timing
   people
   publications


.. |NEW| image:: imag/NEW.jpg
   :width: 100px
   :alt: NEW!
