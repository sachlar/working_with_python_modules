# importing an entire module
# import the module, in our example pizza
# use the function in the module by module_name.function_name(args to pass....) 
# pizza.make_pizza(16, 'pepperoni)

# to import specific functions from a module
from pizza import make_pizza

# to give a function an alias

from pizza import make_pizza as mp # mp being the alias

# to give a module an alias

import pizza as p # p being the alias

# importing all functions in a module

from pizza import *