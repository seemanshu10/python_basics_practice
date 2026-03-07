import my_module 
#import seemanshu.math_utils as a

from seemanshu import math_utils as a # importing from inside a subfolder 
#from seemanshu import math_utils as m1
my_module.greet()
print(my_module.val)

a.add(3,4)
subtract1 = a.sub(4,6)
print(subtract1)


