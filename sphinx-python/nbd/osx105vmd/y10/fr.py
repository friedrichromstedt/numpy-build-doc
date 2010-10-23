"""
Friedrich Romstedt 2010
=======================
"""

def python254():
    """
    -- 10/14/10

    *   Installed Python 2.5.4 from::
            
            Shared/Downloads/2010/python.org/python-2.5.4-macosx.dmg

        from http://www.python.org. /usr/local/bin/ did not contain any pythonic 
        stuff before.  PATH must be extended by the Framework path to use the 
        python.

        Afterwards (``|grep python``)::

            lrwxr-xr-x  1 root  wheel      68 Oct 14 14:25 python -> ../../../Library/Frameworks/Python.framework/Versions/2.5/bin/python
            lrwxr-xr-x  1 root  wheel      75 Oct 14 14:25 python-config -> ../../../Library/Frameworks/Python.framework/Versions/2.5/bin/python-config
            lrwxr-xr-x  1 root  wheel      71 Oct 14 14:25 python2.5 -> ../../../Library/Frameworks/Python.framework/Versions/2.5/bin/python2.5
            lrwxr-xr-x  1 root  wheel      78 Oct 14 14:25 python2.5-config -> ../../../Library/Frameworks/Python.framework/Versions/2.5/bin/python2.5-config
            lrwxr-xr-x  1 root  wheel      69 Oct 14 14:25 pythonw -> ../../../Library/Frameworks/Python.framework/Versions/2.5/bin/pythonw
            lrwxr-xr-x  1 root  wheel      72 Oct 14 14:25 pythonw2.5 -> ../../../Library/Frameworks/Python.framework/Versions/2.5/bin/pythonw2.5

    """
    return '''
        open /Users/Shared/Downloads/2010/python.org/python-2.5.4-macosx.dmg'''

def gfortran423():
    """
    -- 10/14/10

    *   Installing gfortran 4.2.3 from::

            Shared/Downloads/2010/gfortran/gfortran-4.2.3.dmg

        from http://r.research.att.com/tools/ as recommended by the numpy
        build instructions, the file is more precisely 
        http://r.research.att.com/gfortran-4.2.3.dmg.

        Binary distribution package.
    """
    return '''
        open /Users/Shared/Downloads/2010/gfortran/gfortran-4.2.3.dmg'''

def cython013_py25():
    """
    -- 10/14/10
    
    *   Installing Cython 0.13 from::
            
            Shared/Downloads/2010/Cython/Cython-0.13.tar.gz

        from http://www.cython.org/release/Cython-0.13.tar.gz into python2.5::

            Python 2.5.4 (r254:67917, Dec 23 2008, 14:57:27) 
            [GCC 4.0.1 (Apple Computer, Inc. build 5363)] on darwin

        Logfiles got somehow lost.  **Needs-Revision**
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def paver103_py25():
    """
    -- 10/14/10

    *   Installing Paver 1.03 from::

            Shared/Downloads/2010/Paver/Paver-1.0.3.tar.gz

        from http://pypi.python.org/pypi/Paver, http://pypi.python.org/pypi/Paver, 
        :download:`//Users/Shared/Builds/2010/python2.5/Paver/Paver-1.0.3/setup-build.log` 
        :download:`//Users/Shared/Builds/2010/python2.5/Paver/Paver-1.0.3/setup-install.log`
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def setuptools06c11_py25():
    """
    -- 10/14/10
    
    *   Installing Setuptools 0.6c11 from::

            Shared/Downloads/2010/Setuptools/setuptools-0.6c11.tar.gz

        from http://pypi.python.org/pypi/setuptools, 
        http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz.

        :download:`//Users/Shared/Builds/2010/python2.5/Setuptools/setuptools-0.6c11/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.5/Setuptools/setuptools-0.6c11/setup-install.log`
    """
    return '''python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def bdist_mpkg044_py25():
    """
    -- 10/14/10
    
    *   Installing bdist_mpkg 0.4.4 from::

            Shared/Downloads/2010/bdist_mpkg/bdist_mpkg-0.4.4.tar.gz

        from http://pypi.python.org/pypi/bdist_mpkg/,
        http://pypi.python.org/packages/source/b/bdist_mpkg/bdist_mpkg-0.4.4.tar.gz.
            
        :download:`//Users/Shared/Builds/2010/python2.5/bdist_mpkg/bdist_mpkg-0.4.4/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.5/bdist_mpkg/bdist_mpkg-0.4.4/setup-install.log`
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def cython013_py25_test():
    """
    -- 10/14/10

    *   Testing Cython 0.13.

        One failure, looks like a Cython bug, and needs additional testing
        once numpy is compiled.  **Needs-revision**

        Log files are lost together with the directory for unknown reason.
        **Needs-revision**
    """
    return '''
        python2.5 runtests.py 2>&1 | tee runtests.log'''

def paver_py25_rename():
    """
    -- 10/14/10

    *   Renamed::

            /Library/Frameworks/Python.framework/Version/2.5/bin/paver

        to ``paver2.5`` for future other pavers for other Pythons.
    """
    return ''

def virtualenv151_py25():
    """
    -- 10/14/10

    *   Installing virtualenv 1.5.1 from::

            Shared/Downloads/2010/Virtualenv/virtualenv-1.5.1.tar.gz

        from http://pypi.python.org/pypi/virtualenv,
        http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.5.1.tar.gz.

        :download:`//Users/Shared/Builds/2010/python2.5/Virtualenv/virtualenv-1.5.1/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.5/Virtualenv/virtualenv-1.5.1/setup-install.log`
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def numpy200dev_py25_aborted():
    """
    -- 10/15/10

    *   Compiling numpy with python2.5::

        :download:`//Users/Shared/GitHub/project-numpy/owner-numpy/numpy-host/Logs/10-10-15/setup-build.log`

        Aborted because I decided not to compile numpy-2.0.0.dev.
    """
    # python2.5 setup.py build 2>&1 | tee Logs/10-10-15/setup-build.log
    # rm -r build
    return ''

def sphinx104_py25():
    """
    -- 10/15/10

    *   Installing Sphinx 1.0.4 from::

            Shared/Downloads/2010/Sphinx/Sphinx-1.0.4.tar.gz

        from http://pypi.python.org/pypi/Sphinx, 
        http://pypi.python.org/packages/source/S/Sphinx/Sphinx-1.0.4.tar.gz.

        Installed additionally:

        -   docutils 0.7
        -   Jinja 2.5.2
        -   Pygments 1.3.1

        :download:`//Users/Shared/Builds/2010/python2.5/Sphinx/Sphinx-1.0.4/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.5/Sphinx/Sphinx-1.0.4/setup-install.log`
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def sphinx104_py25_docs():
    """
    10/15/10

    *   Building the local Sphinx docs.

        The docs are here: http://vincentdavis.info/Shared/Builds/2010/python2.5/Sphinx/Sphinx-1.0.4/doc/_build/html/
    """
    return '''
        cd doc
        sphinx-build . _build/html'''

def numpy200dev_py25_matplotlib():
    """
    -- 10/15/10

    *   Using a different numpy directory than those for the binary build.

        Needs nose for testing.
    """
    return '''
        cp -r numpy-deployment numpy-host
        cd numpy-host
        python2.5 setup.py build 2>&1 | tee Logs/10-10-15/setup-build.log ^C
        rm -r build
        python2.5 setup.py build 2>&1 | tee Logs/10-10-15/setup-build.log
        python2.5 setup.py install 2>&1 | tee Logs/10-10-15/setup-install.log
        cd ..
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee Logs/10-10-15/test.log'''

def nose0113_py25():
    """
    -- 10/15/10

    *   Installing nose 0.11.3 from::
        
            Shared/Downloads/2010/Nose/nose-0.11.3.tar.gz
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def nose_py25_test():
    """
    -- 10/15/10

    *   Testing nose as installed.

        Did not run any tests.
    """
    return '''
        python2.5 selftest.py 2>&1 | tee selftest.log'''

def numpy200dev_py25_test():
    """
    -- 10/15/10

    *   Testing numpy as installed.

        This gives one Fail, and is using numpy 2.0.0.dev
    """
    return '''
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee numpy-host/Logs/10-10-15/test.log'''

def numpy150rc1_py25():
    """
    *   We want numpy v1.5.0rc1.
    """
    return '''
        cd numpy-host
        git checkout v1.5.0rc1
        rm -r build
        python2.5 setup.py build 2>&1 | tee Logs/10-10-15/setup-build.2.log
        python2.5 setup.py install 2>&1 | tee Logs/10-10-15/setup-install.2.log'''

def numpy150rc1_py25_test():
    """
    *   Testing numpy.

        This gives some errors.
    """
    return '''
        cd ..
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee numpy-host/Logs/10-10-15/test.2.log'''

def numpy141_py25():
    """
    *   Reverting to numpy v1.4.1::
    """
    return '''
        cd numpy-host
        git checkout v1.4.1
        rm -r build
        python2.5 setup.py build 2>&1 | tee Logs/10-10-15/setup-build.3.log
        python2.5 setup.py install 2>&1 | tee Logs/10-10-15/setup-install.3.log'''

def numpy141_py25_test():
    """
    *   Testing numpy.
            
        Lotsa errors.
    """
    return '''
        cd ..
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee numpy-host/Logs/10-10-15/test.3.log'''

def numpy150rc1_py25_2nd():
    """
    *   Actaully numpy v1.5.0rc1 *should* work (since current dev is 2.0.0), so 
        reverting to that.

        Not testing this version again.
    """
    return '''
        cd numpy-host
        git checkout v1.5.0rc1
        rm -r build
        python2.5 setup.py build 2>&1 | tee Logs/10-10-15/setup-build.4.log
        python2.5 setup.py install 2>&1 | tee Logs/10-10-15/setup-install.4.log'''

def freetype243():
    """
    *   Installing Freetype2 from::

            Shared/Downloads/2010/Freetype2/freetyp-2.4.3.tar.bz2
    """
    return '''
        export CFLAGS="-arch i386 -arch x86_64 -arch ppc"
        ./configure --enable-biarch-config 2>&1 | tee configure.log
        make 2>&1 | tee make.log
        sudo make install 2>&1 | tee make-install.log'''

def libpng144_1st():
    """
    **Deprecated**

    *   Installing libpng 1.4.4 from::

            Shared/Downloads/2010/libpng/libpng-1.4.4.tar.gz
    """
    return '''
        CFLAGS exported as before
        ./configure 2>&1 | tee configure.log
        make 2>&1 | tee make.log

        unset CFLAGS
        ./configure 2>&1 | tee configure.2.log
        make 2>&1 | tee make.2.log
        sudo make install 2>&1 | tee make-install.log'''

def matplotlib_py25_1st():
    """
    **Deprecated**

    *   Compiling matplotlib.

        Failed because /Developer libPng.dylib doesn't contain PPC arch.
    """
    return '''
        vim setupext.py (section darwin)
        python2.5 setup.py build 2>&1 | tee setup-build.log'''

def libpng144_2nd():
    """
    **Deprecated**

    *   Trying to fat compile libpng 1.2.44.

        Didn't work.
    """
    return '''
        export CFLAGS="-arch i386 -arch x86_64 -arch ppc"
        ./configure 2>&1 | tee configure.log
        make 2>&1 | tee make.log'''

def libpng144_3rd():
    """
    *   Trying libpng 1.4.4 again.

        SUCCESS!
        
        :download:`//Users/Shared/Builds/2010/libpng/libpng-1.4.4/configure.1.log`
        :download:`//Users/Shared/Builds/2010/libpng/libpng-1.4.4/make.1.log`
        :download:`//Users/Shared/Builds/2010/libpng/libpng-1.4.4/make-install.1.log`
    """
    return '''
        ./configure --disable-dependency-tracking 2>&1 | tee configure.2.log
        mv configure.2.log configure.3.log
        make 2>&1 | tee make.3.log

        cd ..
        mv libpng-1.4.4 libpng-1.4.4.old1
        tar xzf libpng-1.4.4.tar.gz
        cd libpng-1.4.4
        ./configure --disable-dependency-tracking 2>&1 | tee configure.1.log
        make 2>&1 | tee make.1.log
        sudo make install 2>&1 | tee make-install.1.log'''

def matplotlib_py25_2nd():
    """
    *   Retrying matplotlib compilation.

        YOH

        :download:`//Users/Shared/GitHub/project-matplotlib/owner-astraw/matplotlib/Logs/10-10-14/setup-build.2.log`
        :download:`//Users/Shared/GitHub/project-matplotlib/owner-astraw/matplotlib/Logs/10-10-14/setup-install.log`
    """
    return '''
        unset CFLAGS
        python2.5 setup.py build 2>&1 | tee setup-build.2.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def dmg_numpy150rc1_py25_1st():
    """
    *   In numpy-deployment.

        Some problem with numpydoc prolly missing (docutils problem).
    """
    return '''
        git checkout 1.5.0rc1
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.1.log'''

def numpydoc14_py25():
    """
    *   Installing numpydoc 1.4 from::

            Shared/Downloads/2010/Numpydoc/numpydoc-0.4.tar.gz

        This did something to docutils.  Promising.
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def dmg_numpy150rc1_py25_2nd():
    """
    *   In numpy-deployment.

        Same error persists, in trac known but marked as fixed.
    """
    return '''
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.2.log'''

def dmg_numpy141rc3_py25_1st():
    """
    *   Using 1.4.1rc3.

        Even worser (error occurs earlier).
    """
    return '''
        git checkout 1.4.1rc3
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.3.log'''

def dmg_numpy200dev_py25_1st():
    """
    *   Using 2.0.0.dev.

        pdflatex not found.
    """
    return '''
        git checkout master
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.4.log'''

def dmg_numpy200dev_py25_2nd():
    """
    *   Retrying with extended PATH.

        .4.log accidentally overwirtten :-(

        For some reasons insists on py2.6, monkey-patching DEFAULT.
    """
    return '''
        export PATH=$PATH:/usr/texbin
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.5.log'''

def dmg_numpy200dev_py25_3rd():
    """
    *   Wrong documentation.
    """
    return '''
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.6.log'''
