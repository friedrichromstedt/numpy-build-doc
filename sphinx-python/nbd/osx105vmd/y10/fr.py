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
    -- 10/15/10

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
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

    *   Testing numpy.

        This gives some errors.
    """
    return '''
        cd ..
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee numpy-host/Logs/10-10-15/test.2.log'''

def numpy141_py25():
    """
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

    *   Testing numpy.
            
        Lotsa errors.
    """
    return '''
        cd ..
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee numpy-host/Logs/10-10-15/test.3.log'''

def numpy150rc1_py25_2nd():
    """
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

    **Deprecated**

    *   Compiling matplotlib.

        Failed because /Developer libPng.dylib doesn't contain PPC arch.
    """
    return '''
        vim setupext.py (section darwin)
        python2.5 setup.py build 2>&1 | tee setup-build.log'''

def libpng144_2nd():
    """
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

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
    -- 10/15/10 approx.

    *   In numpy-deployment.

        Some problem with numpydoc prolly missing (docutils problem).
    """
    return '''
        git checkout 1.5.0rc1
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.1.log'''

def numpydoc14_py25():
    """
    -- 10/15/10 approx.

    *   Installing numpydoc 1.4 from::

            Shared/Downloads/2010/Numpydoc/numpydoc-0.4.tar.gz

        This did something to docutils.  Promising.
    """
    return '''
        python2.5 setup.py build 2>&1 | tee setup-build.log
        python2.5 setup.py install 2>&1 | tee setup-install.log'''

def dmg_numpy150rc1_py25_2nd():
    """
    -- 10/15/10 approx.

    *   In numpy-deployment.

        Same error persists, in trac known but marked as fixed.
    """
    return '''
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.2.log'''

def dmg_numpy141rc3_py25_1st():
    """
    -- 10/15/10 approx.

    *   Using 1.4.1rc3.

        Even worser (error occurs earlier).
    """
    return '''
        git checkout 1.4.1rc3
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.3.log'''

def dmg_numpy200dev_py25_1st():
    """
    -- 10/15/10 approx.

    *   Using 2.0.0.dev.

        pdflatex not found.
    """
    return '''
        git checkout master
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.4.log'''

def dmg_numpy200dev_py25_2nd():
    """
    -- 10/15/10 approx.

    *   Retrying with extended PATH.

        .4.log accidentally overwirtten :-(

        For some reasons insists on py2.6, monkey-patching DEFAULT.
    """
    return '''
        export PATH=$PATH:/usr/texbin
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.5.log'''

def dmg_numpy200dev_py25_3rd():
    """
    -- 10/15/10 approx.

    *   Wrong documentation.
    """
    return '''
        paver2.5 dmg 2>&1 | tee Logs/10-10-15/paver-dmg.6.log'''

def python27_framework_permissions_1st():
    """
    -- 10/22/10 approx.

    *   Used TinkerTool System 2.4 to set up permissions in::

            /Library/Frameworks/Python.framework/Versions/...

        to "Full Control" for ``group:admin``.

    *   Unfortunately, as we found out on 10/23/10, this breaks nosetests,
        because the ``execute`` permission is set for all files.

        -   bash seens to ignore this.  Test: Files in Shared have undergone
            the same permission process, but do not show up in Tab 
            completion in bash.

        -   But nosetests seems to not ignore it.  At least it's telling
            that the files are ignore because they are executable, and thus
            in effect no numpy test is run.

    *   A fix is provided in 
        :func:`nbd.osx105vmd.y10.fr.python27_framework_permissions_2nd`.
    """
    return '''
        # Used TinkerTool's GUI to make the changes.'''

#
# Initialising git repos in :file:`Versions/2.5`, :file:`Versions/2.6` and
# :file:`Versions/2.7`
#

def python27_framework_git_1st():
    """
    -- 10/22/10

    *   Set up a git repo in::
            
            /Library/Frameworks/Python.framework/Versions/2.7/

    *   We used after some plumbing the following :file:`.gitignore`::
            
            .DS_Store

        for this reasons:

        -   Ignoring :file:`.pyc` and :file:`.pyo` makes them untracked, so
            they will survive branch switching.  When the :file:`.pyc` file
            is more recent than the checked-out :file:`.py` file, this causes
            trouble.

    *   We used this :file:`.gitattributes`::
            
            *.so -text
            *.pyc -text
            *.pyo -text

        to make this file types binary in the repo.

        The repo is *not* planned to be published.
    """
    return '''
        # See the git log'''

def python27_framework_git_2nd():
    """
    -- 10/23/10 13:38

    *   Providing scripts to fix the permission mistake mentioned in 
        :func:`nbd.odx105vmd.y10.fr.python27_framework_git_1st`.

        -   :file:`/Library/Frameworks/Python.framework/Versions/fix_global.sh`
        -   :file:`/Library/Frameworks/Python.framework/Versions/fix2.7.sh`

        The ``global`` file is here for download, just adapt the ``DIR`` 
        variable to your needs:
        :download:`//Library/Frameworks/Python.framework/Versions/fix_global.sh`

    *   I found out that the ``search`` permission on directories translates
        to the not-wanted ``execute`` permission on files once inherited.

        To avoid the wrong permission on newly created files, the inheriting
        permissions on the :file:`2.*` directories should be changed, and once
        the permissions should be propagated.  This is done by the 
        :file:`fix_global.sh` script.

        I fixed the perms on :file:`2.7` manually with::

            chmod -a "group:admin allow execute" .
            chmod -a "group:admin allow search" .

        while in the :file:`2.7` dir.  The ``allow execute`` step is most
        likely not needed.

    *   From ow on, the :file:`fix*.sh` scripts will most likely not be
        necessary anymore, because the :file:`2.*` directories in
        :file:`Versions/` will inherit the correct rights.  The perms have
        been propagated in *all* versions.
    """
    return '''
        /Library/Frameworks/Python.framework/Versions/fix_global.sh'''

# ===== From here to add to the timeline =====

def python25_framework_git_1st():
    """
    -- 10/24/10 06:12

    *   Initialising a git repo in :file:`Versions/2.5`.
        
        -   One branch for normal Python use: ``normal``

        -   One branch where the numpy during installer builds gets
            installed: ``installer``

        -   Empty ``master`` branch, containing only the config files for
            git.

        -   Copying over the config files from the :file:`Versions/2.7/` dir.
        
        -   Adding the files to the ``normal`` branch, and branching the
            ``installer`` branch from that.
    """
    return '''
        git init
        cp ../2.7/.gitignore ../2.7/.gitattributes .
        git add .gitignore .gitattributes
        git commit
        git branch normal
        git checkout normal
        git add *
        git commit
        git branch installer
        git checkout installer
        '''

def python26_framework_git_1st():
    """
    -- 10/24/10 06:30

    *   See :func:`nbd.osx105vmd.y10.fr.python25_framework_git_1st`
    """
    return '''
        => nbd.osx105vmd.y10.fr.python25_framework_git_1st
        '''

def python27_framework_git_3rd():
    """
    -- 10/24/10 06:42

    *   Restructuring the branch structure in Python 2.7:

        -   ``normal`` and ``installer`` branches under ``10.3`` and ``10.5``
            directories

        -   Other feature branches may be added under the ``10.3`` and `10.5``
            directoies when working on the Python installation.
    """
    return '''
        git status
        git checkout master
        git branch -m 10.3 10.3/normal
        git branch -m 10.5 10.5/normal
        git checkout 10.3/normal
        git branch 10.3/installer
        git checkout 10.5/normal
        git branch 10.5/installer
        '''

def python_framework_git_1st():
    """
    10/24/10 07:47

    *   Renaming the branch structure of all Python system repos:

        -   ``normal -> vmd``
        -   ``installer -> numpy``
        -   branching ``fr`` from ``vmd``

        to accomodate with maybe upcoming scipy builds, or whatever the
        future might bring.
    """
    return '''
        git branch  # on branch normal
        git branch -m vmd
        git branch fr
        git branch -m installer numpy
        '''

#
# Setting up status-reporting :file:`sitecustomize.py` files in all Pythons
# 

def python_sitecustomize_1st():
    """
    -- 10/24/10 08:00

    *   Modifying the :file:`lib/pythonx.y/site-packages/sitecustomize.py`
        files such that it prints what family the Python belongs to.

        This will be printed each time the Python starts.

        E.g.::
            
            print "Python 2.5 on branch family python"

            print "Python 2.7 on branch family 10.5/vmd"

        Feature branches in the Python system git repos should:

        -   Not change this file.

        -   Not mix families.  The different Python families should be
            treated as independent installations and no merge should transfer
            installation files from one to the other.
    """
    return '''
        # checkout, edit sitecustomize.py, commit, ...
        '''

#
# Preparing a proper 1.5.1rc1-py2.5-python.org-macosx10.3 release
#

def dmg_151rc1_py25_pythonorg_macosx103_1st():
    """
    -- 10/24/10 10:39

    *   Resetting Vincent's pollution of the 1.5.x branch with commits
        intended for the 1.5.x-py2.7-python.org-macosx10.5 branch.

        They are still in that branch.  Just the 1.5.x branch has been
        resetted.

    *   Branching the 1.5.x-py2.5-python.org-macosx10.3 branch from the
        1.5.x branch.  We did a fetch numpy today, everything was up to date,
        the last commit was in fact 3 days ago.

    *   Checking that the ``numpy`` branch of Python 2.5 is active.

    *   **NOTE**: The following complicates the thingy:
        
        1.  On the 1.5.x-py2.* branch, a checkout and commit of the
            tagged 1.5.x branch, e.g. v1.5.1rc1, would be necessary.

        2.  But when checking out v1.5.1rc1, the HEAD goes detached.  So it's
            impossible then to commit to 1.5.1-py2.*.

        Following a solution:
        
        1.  checkout of e.g. v1.5.1rc1.  HEAD goes detached.

        2.  Starting a new branch, named by the tag, e.g. 
            1.5.1rc1-py2.5-python.org-macosx10.3.

        3.  Committing to this tag the subsequent logs and dmgs.

        So it seems not feasible to have the 1.5.x series dmgs in a single
        branch, except when following the build process like this:

        1.  checkout of e.g. v1.5.1rc1.

        2.  Starting the 1.5.x-py2.5-python.org-macosx10.3 branch (as an
            example).

        3.  Committing on this branch the dmgs.

        4.  Patching the source by merge v1.5.1rc2, or by merge 1.5.x.

        5.  Continuing generating dmgs and committing them.

        But this technique has the conspicuous drawback that once e.g.
        rc1 is finished and the commits went on to rc2, no more commits
        using the rc1 codebase is possible.

        So I favour the "one branch for each release" scheme.
    """
    return '''
        git branch maintenance/1.5.x
        git reset --hard c0bd3f
        git branch maintenance/1.5.x-py2.5-python.org-macosx10.3
        pushd /Library/Frameworks/Python.framework/Versions/2.5
        git status
        # On branch numpy
        popd
        '''

def dmg_151rc1_py25_pythonorg_macosx103_2nd():
    """
    -- 10/24/10 12:11

    *   Deleting the 1.5.x-py2.7-python.org-macosx10.3 branch, while on
        1.5.x.

    *   Checking out v1.5.1rc1, and branching the detached HEAD to
        maintenance/release/1.5.1rc1-py2.5-python.org-macosx10.3.

    *   Decided not to put it under maintenance, but directly under release/.

    *   Python 2.5 is on the ``numpy`` branch.

    *   The steps remaining from the instructions in :file:`pavement.py` are::

            python setupegg.py install
            paver dmg

        This are on our system, since also setupegg.py is equivalent to
        calling setup.py directly (see its content)::

            python2.5 setup.py build 2>&1 | tee release/logs/01.setup-build.log
            # git ...
            python2.5 setup.py install 2>&1 | tee release/logs/02.setup-install.log
            # git ...
            paver2.5 dmg 2>&1 | tee release/logs/02.paver25-dmg.log

    *   Compilation looks good, ``MACOSX_DEPLOYMENT_TARGET=10.3``
        effectively, although not set manually.

    *   We do refrain from adding build/ to the repo.  The steps given should
        suffice for reproduction.  The files built can be inspected from
        the Python 2.5 system commit.

    *   Since :file:`*.log` is in :file:`.gitignore`, renamed to 
        :file:`*.rlog` (Release LOGs).

    *   Install looks good.

    *   Committing the change to system Python in :file:`Versions/2.5`.

        :file:`bin/f2py` has been modified, I don't know why and how.
        Saved a diff.

    *   DMG created successfully.  It's duplicate in 
        :file:`tools/numpy/macosx-installer` and :file:`release/installers`.
        Removing the stuff created for the macosx-installer.

    *   *Only* adding the dmg and the rlogs.  *Not* adding the pdfs 
        generated, they are either not needed for reproduction or included
        in the dmg.

    *   Tests fail partially.
    
    *   Removing dangling directories left from the build process.  
        **Needs-Revision**
    """
    return '''
        git checkout maintenance/1.5.x
        git branch -D 
        git checkout v1.5.1rc1
        git branch maintenance/release/1.5.1rc1-py2.5-python.org-macosx10.3
        git checkout maintenance/release/1.5.1rc1-py2.5-python.org-macosx10.3
        git branch -m release/1.5.1rc1-py2.5-python.org-macosx10.3
        mkdir release
        mkdir release/logs
        python2.5 setup.py build 2>&1 | tee release/logs/01.setup-build.log
        mv release/logs/01.setup-build.log release/logs/01.setup-build.rlog
        git add numpy/version.py release
        git commit -m "Build succeeded"
        python2.5 setup.py install 2>&1 | tee release/logs/02.setup-install.rlog

        pushd /Library/Frameworks/Python.framework/Versions/2.5
        git diff bin/f2py > ~/Development/numpy/release/logs/03.bin-f2py.log
        git add *
        git commit -m "Installed numpy v1.5.1rc1"

        popd
        git add release/logs
        git commit  # Noting the system Python commit.
        paver2.5 -p 2.5 dmg 2>&1 | tee release/logs/04.paver25-p25-dmg.rlog
        paver2.5 dmg -p 2.5 2>&1 | tee release/logs/05.paver25-dmg-p25.rlog

        cd tools/numpy-macosx-installer
        rm -r content numpy-1.5.1rc1-py2.5-python.org-macosx10.3.dmg

        cd ../../
        git add release
        git commit -m "dmg built"

        pushd release/logs 
        python2.5 -c "import numpy; numpy.test()" 2>&1 | tee 06.python25-c-test.rlog
        git add 06.python25-c-test.rlog
        git commit

        popd
        rm -r build_doc doc/source/referece/generated
        '''
