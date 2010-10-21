"""Actions run in 2010."""

def an_action():
    """
    2010-10-20 FR

    This is an action which can be run.
    """

    print "HI"

def another_action(a, b):
    """
    2010-10-15 FR

    This action takes arguments.
    """

    print a, b

class NeedsRevision:
    an_action = an_action

class NonPythonSetup:
    an_action = an_action

class PythonSetup:
    pass

class Python254:
    another_action = another_action
