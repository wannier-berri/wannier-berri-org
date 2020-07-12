**********************************
Installation and technical remarks
**********************************

To run the ``WannierBerri``\ code only python3 is required, independent of the
operating system. The easy way of installation of the latest stable
version maybe achieved via ``pip``\ (“PyPI Repository,” n.d.):

::

   pip3 install wannierberri

The dependencies are quite basic and will be installed automatically.
Those include ``numpy``\ (Oliphant 2006), ``scipy >= 1.0``\ (Virtanen et
al. 2020), pyFFTW(“PyFFTW,” n.d.) (python wrapper of FFTW(Frigo and
Johnson 2005)), ``lazy_property``, and a few ’cosmetic’ modules
``colorama``, ``termcolor`` and ``pyfiglet`` which are needed for a nice
colorful output in the terminal.

One note should be mentioned about the parallel run. numpy already
includes parallelization over threads. However, if ``WannierBerri``\ is
running with the number of processes equal to the number of physical
cores, obviously extra threading may only slow down the calculation.
Generally I recommend to switch off the threading in numpy by setting
the corresponding environent variable. It can be done inside the python
script by

::

   import os
   os.environ['OPENBLAS_NUM_THREADS'] = '1'

or

::

   os.environ['MKL_NUM_THREADS'] = '1'  

Depending whether numpy is linked with openblas or MKL libraries. Note,
this should be done in the beginning of the script, before importing
numpy for the first time.
