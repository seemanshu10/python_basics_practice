import os

#  ------------ Exploring os.path and os.name -------------
# print(os.path)  
# print(os.name)  
# posix


# ----------- Using  __file__ --------------
# print(__file__)  



# # --------- Using os.path.dirname() -------------
# print(os.path.dirname(__file__))  



# # # --------- Using os.path.abspath() ------------
print(os.path.abspath(__file__))



# # ------------ Combining os.path.dirname() and os.path.abspath() ----------
print(os.path.dirname(os.path.abspath(__file__)))