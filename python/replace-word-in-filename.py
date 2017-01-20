# This script replaces a word in a filename in a given directory
# Based on this stackoverflow answer: http://stackoverflow.com/a/9577192

import os

os.chdir('') # Navigates to a specified directory - make sure to use '/'
[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')] # Replaces a specified character or word in the filename with an alternative
print('All files renamed')
