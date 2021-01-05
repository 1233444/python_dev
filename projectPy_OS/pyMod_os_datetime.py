import os
from datetime import datetime

print(os.curdir)

mod_time = os.stat('README.md').st_mtime

print(datetime.fromtimestamp(mod_time))

