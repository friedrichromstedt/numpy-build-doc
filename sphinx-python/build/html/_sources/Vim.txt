Vim Configuration File
======================

I found this .vimrc extremely useful::

    syntax on
    set autoindent
    set tabstop=4
    set shiftwidth=4
    set expandtab

``expandtab`` replaces tabs by spaces.  If you need to change this later
use::

    :%retab

in the file you're editing.  This will convert tabs to spaces or vice versa, 
if you unsetted ``expandtab``.
