

import pathlib
import os

print(pathlib.Path('cit_data.txt').parent.absolute())
print(pathlib.Path().absolute())


# using os module

print(os.path.dirname(os.path.abspath('cit_data.txt')))

# current path

print(os.path.abspath(os.getcwd()))

