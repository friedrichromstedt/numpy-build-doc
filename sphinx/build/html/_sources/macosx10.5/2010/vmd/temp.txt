.. index::
    double: python 2.6.6; matplotlib

2010-10-15: Installing matplotlib 1.0 in python 2.6.6
============================================

*   Installing matplotlib from::

changed line 66 
from::
'darwin' : [],
to::
'darwin' : ['/usr/local']

        UPDATE THIS Shared/Downloads/2010/Sphinx/Sphinx-1.0.4.tar.gz

    UPDATE THISfrom http://pypi.python.org/pypi/Sphinx, 
    UPDATE THIShttp://pypi.python.org/packages/source/S/Sphinx/Sphinx-1.0.4.tar.gz
    using::

        py26 setup.py build 2>&1 | tee setup-build.log
        py26 setup.py install 2>&1 | tee setup-install.log

    Installed additionally:

    -   docutils 0.7
    -   Jinja 2.5.2
    -   Pygments 1.3.1

    :download:`//Users/Shared/Builds/2010/python2.6/Sphinx/Sphinx-1.0.4/setup-build.log`
    :download:`//Users/Shared/Builds/2010/python2.6/Sphinx/Sphinx-1.0.4/setup-install.log`
