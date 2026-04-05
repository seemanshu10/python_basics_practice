# -------------- Direct Append
import sys

sys.path.append(r"C:\Users\pralhad\Desktop\dev")




# -------------- Using os.path
import sys
import os

package_path = os.path.abspath("../dev")  

print(package_path)
# Output: C:\Users\pralhad\Desktop\dev


if package_path not in sys.path:
    sys.path.append(package_path)





# -------------- Verify If Package Path is Added
for path in sys.path:
    print(path)
      
  # Output:
#   C:/Users/our_name/tools
#   C:/Python39/Lib
#   C:/Python39/Lib/site-packages
#   C:/Users/our_name/dev   ← ✅ Our custom path