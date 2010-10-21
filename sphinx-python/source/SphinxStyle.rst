.. index::
    single: Sphinx Style

Sphinx Coding Style (by Friedrich Romstedt)
===========================================

I explain here my own coding style, in the hope to convince you, so that we
have an uniform coding style.


Paragraphs
----------

Use line breaks, if you want inform yourself about vim's paragraph handling
capability.  For me, ``J``, finding line end, ``i Enter Esc``, ``J``, ... do 
the job too.  Two spaces at line end at least (because of the intermediate 
space that may trail the last non-white char).

Two spaces after full stop.  (vim will recognise sentences, and it *looks
better*).


Sphinx Headings
---------------

Two newlines before the headline string.  Capitalise words accoding to 
well-known typographic rules, i.e., everything except "the", "a", "for",
"in", "but", etc.  Rule of thumb::

    if len(str) <= 3:
        capitalise()

But there are exceptions.
