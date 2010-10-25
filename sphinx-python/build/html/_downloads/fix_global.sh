# Problem:
#   Nosetests requires files to be non-executable.  But the "Full Control"
#   ACEs created by TinkerTool include the *execute* flag.
#
# TinkerTool permissions "Full control" on directories:
# +a "group:admin allow list,add_file,search,delete,add_subdirectory,delete_child,readattr,writeattr,readextattr,writeextattr,readsecurity,writesecurity,chown,file_inherit,directory_inherit" 
# on files:
# +a "group:admin allow read,write,execute,delete,append,readattr,writeattr,readextattr,writeextattr,readsecurity,writesecurity,chown"
#
# We don't need the +a "group:admin allow execute", in fact, it's a bug in
# TinkerTool to set this without ability to inhibit it.
#
#
# Thus we need for both:
# +a "group:admin allow delete,readattr,writeattr,readextattr,writeextattr,readsecurity,writesecurity,chown"
#
# For files:
# +a "group:admin allow read,write,append"
#
# And for directories:
# +a "group:admin list,add_file,search,add_subdirectory,delete_child,file_inherit,directory_inherit"
#
# Unfortunately, the *search* permission, meant to apply only to directories,
# applies also to files as the *execute* flag.
#
# => So we leave the *search* permission alone.

DIR=/Library/Frameworks/Python.framework/Versions

# Add a good ACE:
chmod -R +a# 0 "group:admin allow delete,readattr,writeattr,readextattr,writeextattr,readsecurity,writesecurity,chown,read,write,append,list,add_file,add_subdirectory,delete_child,file_inherit,directory_inherit" $DIR/*

# Remove the old ACE if present:
chmod -R -a# 1 $DIR/*
