set -ev
pip install sphinx 
pip install nbsphinx
pip install -U wannierberri

case "$INSTALL_TYPE" in
    dev)
        pip install -e .
        ;;
    dev_sdist)
    #     python setup.py sdist
    #     ls -1 dist/ | xargs -I % pip install dist/%[dev]
    #     ;;
    # dev_bdist_wheel)
    #     python setup.py bdist_wheel
    #     ls -1 dist/ | xargs -I % pip install dist/%[dev]
    #     ;;
esac
