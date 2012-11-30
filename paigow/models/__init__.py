# django, when started, calls 'from <app>/models import *' to get all the models.
#
# The default configuration in each application is a file called 'models.py' in
# the app directory, so 'import' will use that.  However, it for importing it
# is also legal to have a directory instead of a file, so 'models/' directory
# instead of 'models.py' will be import.
#
# When a directory is imported, __init__.py is run from that directory; it is
# now the app's responsibility to import all the actualy models (== SQL tables)
# from the various other files in this directory.

from pgtile import PGTile
from pggame import PGGame

# eventually we want to split this out into individual models
from models import *
