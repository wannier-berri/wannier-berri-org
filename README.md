# wannier-berri.org
Web page of Wannier Berri 

This is a private repository, for maintainers of the wannier-berri.org web page. I (Stepan) will regulary upload the master branch to the hosting server. 

Compling
---------

to generate the html just type "make"  (you need the sphinx installed, and prbably some other extensions)

Autodoc
-------
Automated documentation will be generated for that wannierberri version which will be imported by the ``import wannierberri`` command. If you want to generate html for the local copy of the code, please make a symbolik link in the root of this repository via `ln -s /path/to/wannier-berri/wannierberri .`

Contributing
------------
You all will be given write acess to the repository. Please use it with caution. If you spot a typo, or have some small changes - do not hesitate to correct it in the master branch. However, if you make more extensive changes, first try them on another branch. 

PDF images
----------
html does not support `\*.pdf` figures, but all `\*.pdf` figures in `source/\*/` directories will be automatically converted  to `\*.pdf.svg`.  So in the .rst files please reference the `\*.pdf.svg` files instead of `pdf`s. Please do not add the converted figures to repository. If you add original svg figures, please do NOT name them `\*.pdf.svg` ,  otehwise they may be accidentally removed. To remove all converted figures type ``make clean_fig_svg``.

Privacy
-------
This is intended to be a private repository. Please do not fork it into your public repository, and avoid any other form of publoshing.
