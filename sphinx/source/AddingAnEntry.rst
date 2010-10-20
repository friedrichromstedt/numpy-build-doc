.. index::
    double: Adding; Log Entry

Adding a Log Entry
==================

1.  Create log entry file::

        <System>/<Year>/<User Abbreviation>/<YYYY>-<MM>-<DD>.<NN>.rst

2.  With title::

        <YYYY>-<MM>-<DD>: <Title>

    -   When installing software, use for stand-alone software::

            <Title> = <Name> <Version>

        and for Python software::

            <Title> = <Name> <Version> in py<x.y>

        
        For py2.7 on Mac OS X, use either "py2.7-10.4" or "py2.7-10.5".
        Capitalise ``<Name>`` if the package's name is not natively 
        un-capitalised.

    -   When making a log entry, use a short description.  Like "numpy 
        2.0.0.dev Test py2.5"

3.  And index for Python installs e.g.::

        .. index::
            single: Python 2.5.4

    and::

        .. index::
            single: gfortran

    for non-Python installs. For Python packages use e.g.::

        .. index::
            double: Sphinx; py2.5.4

    . For Tests, use e.g.::

        .. index::
            triple: Test; Cython; py2.5.4

    . Place the index directive above the title.

4.  Add the action to the *timeline* in::

        <System>/<Year>.rst

    .  If there's a new timeline to be created, use in the <Year>.rst file::

        <Title> = Timeline <System> <Year>

    and open the timeline as a ``.. toctree::`` directive with 
    ``:maxdepth: 2``.  Thank you.

5.  Add the steps of the action in a bullet list.  Tell:

    -   From where in Shared/ you took the installer,

    -   From where the installer came,

    -   What you issued,

    -   Link to the log files as downloads (``:download:`<file>```).  Seems
        you have to use ``//Users/`` with double slash at the beginning 
        (Sphinx bug?).

    You do *not* need to tell:

    -   Where you did the build,

    -   Where the log files are located.

    The build dir is clear from nomenclature and year, and the log files are 
    linked in anyway.

6.  If necessary, add the action to the "Need Revision" section of your 
    system's SystemSetup.rst.  Mark the spot with ``**Needs Revision**``.

7.  Add the action to all sections of your SystemSetup where appropriate.

Finally it looks like this::

    .. index::
        single: gfortran

    2010-10-14: gfortran 4.2.3
    ==========================

    *   Installing gfortran 4.2.3 from::

            Shared/Downloads/2010/gfortran/gfortran-4.2.3.dmg

        from http://r.research.att.com/tools/ as recommended by the numpy
        build instructions, the file is more precisely 
        http://r.research.att.com/gfortran-4.2.3.dmg.

        Binary distribution package.
