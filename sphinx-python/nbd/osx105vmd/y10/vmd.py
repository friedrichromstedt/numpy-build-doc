"""
Vincent Davis 2010
=======================
"""

def python27_105():
    """
    -- 10/22/10

    *   Installed python-2.7-macosx10.5 from::
            
            Shared/Downloads/2010/python.org/python-2.7-macosx10.5.dmg
    """
    return '''
        open /Users/Shared/Downloads/2010/python.org/python-2.7-macosx10.5.dmg'''

def cython013_py27_105():
    """
    -- 10/22/10
    
    *   Installing Cython 0.13 from::
            
            Shared/Downloads/2010/Cython/Cython-0.13.tar.gz

        from http://www.cython.org/release/Cython-0.13.tar.gz into python2.7::
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/Cython-0.13/setup-build.log` 
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/Cython-0.13/setup-install.log`

    """
    return '''
        python2.7 setup.py build 2>&1 | tee setup-build.log
        python2.7 setup.py install 2>&1 | tee setup-install.log'''
        
        
def paver103_py27_105():
    """
    -- 10/22/10

    *   Installing Paver 1.03 from::

            Shared/Downloads/2010/Paver/Paver-1.0.3.tar.gz
            Rename paver to paver2.7 in /Library/Frameworks/Python.framework/Versions/2.7/bin/paver

        from http://pypi.python.org/pypi/Paver, http://pypi.python.org/pypi/Paver, 
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/Paver-1.0.3/setup-build.log` 
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/Paver-1.0.3/setup-install.log`
    """
    return '''
        python2.7 setup.py build 2>&1 | tee setup-build.log
        python2.7 setup.py install 2>&1 | tee setup-install.log
        git mv bin/paver bin/paver2.7'''
        
def setuptools06c11_py27_105():
    """
    -- 10/22/10
    
    *   Installing Setuptools 0.6c11 from::

            Shared/Downloads/2010/Setuptools/setuptools-0.6c11-py2.7.egg

        from http://pypi.python.org/pypi/setuptools, 
        http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11-py2.7.

    """
    return ''' sh setuptools-0.6c11-py2.7.egg'''
    
def bdist_mpkg044_py27_105():
    """
    -- 10/22/10
    
    *   Installing bdist_mpkg 0.4.4 from::

            Shared/Downloads/2010/bdist_mpkg/bdist_mpkg-0.4.4.tar.gz

        from http://pypi.python.org/pypi/bdist_mpkg/,
        http://pypi.python.org/packages/source/b/bdist_mpkg/bdist_mpkg-0.4.4.tar.gz.
            
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/bdist_mpkg-0.4.4/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/bdist_mpkg-0.4.4/setup-install.log`
    """
    return '''
        python2.7 setup.py build 2>&1 | tee setup-build.log
        python2.7 setup.py install 2>&1 | tee setup-install.log'''
        
def virtualenv151_py27_105():
    """
    -- 10/22/10

    *   Installing virtualenv 1.5.1 from::

            Shared/Downloads/2010/Virtualenv/virtualenv-1.5.1.tar.gz

        from http://pypi.python.org/pypi/virtualenv,
        http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.5.1.tar.gz.

        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/virtualenv-1.5.1/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/virtualenv-1.5.1/setup-install.log`
    """
    return '''
        python2.7 setup.py build 2>&1 | tee setup-build.log
        python2.7 setup.py install 2>&1 | tee setup-install.log'''
        
def sphinx104_py27_105():
    """
    -- 10/22/10

    *   Installing Sphinx 1.0.4 from::

            Shared/Downloads/2010/Sphinx/Sphinx-1.0.4.tar.gz

        from http://pypi.python.org/pypi/Sphinx, 
        http://pypi.python.org/packages/source/S/Sphinx/Sphinx-1.0.4.tar.gz.

        Installed additionally:

        -   docutils 0.7
        -   Jinja 2.5.2
        -   Pygments 1.3.1

        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/Sphinx-1.0.4/setup-build.log`
        :download:`//Users/Shared/Builds/2010/python2.7/python-2.7-macosx10.5/Sphinx-1.0.4/setup-install.log`
    """
    return '''
        python2.7 setup.py build 2>&1 | tee setup-build.log
        python2.7 setup.py install 2>&1 | tee setup-install.log'''
        
def sphinx104_py27_105_docs():
    """
    10/22/10

    *   Building the local Sphinx docs.

    """
    return '''
        cd doc
        sphinx-build . _build/html'''
    
def nose0113_py27_105():
    """
    -- 10/22/10

    *   Installing nose 0.11.3 from::
        
            Shared/Downloads/2010/Nose/nose-0.11.3.tar.gz
    """
    return '''
        python2.7 setup.py build 2>&1 | tee setup-build.log
        python2.7 setup.py install 2>&1 | tee setup-install.log'''
        
def numpy15x_py27_105():
    """
    *   We want numpy v1.5.x
    last commit
    105osxpython:numpy Vincent$ git log
    commit c0bd3dfe43e3ec554f30521a86a3ef9fe3e98273
    Author: Pauli Virtanen <pav@iki.fi>
    Date:   Wed Oct 20 21:24:28 2010 +0200
    """
    return '''
        git checkout maintenance/1.5.x-py2.7-python.org-maxosx10.5
        rm -r build
        python2.7 setup.py build 2>&1 | tee Logs/10-10-22/setup-build.2.log
        python2.7 setup.py install 2>&1 | tee Logs/10-10-22/setup-install.2.log'''
        
def matplotlib_v1_0_maint_py27_105():
    """
    -- 10/23/10
    Downloaded the maintenace release of matplotlib v1
    need to modify line 66
    # Original 'darwin' : [],
    to
    'darwin' : ['/usr/local'],
    """
    return '''
       
        python2.7 setup.py build 2>&1 | tee Logs/10-10-22/setup-build.2.log
        python2.7 setup.py install 2>&1 | tee Logs/10-10-22/setup-install.2.log'''
