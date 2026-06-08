from datetime import datetime
import os
# now is current datetime 
log_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

print(log_time)

print(os.path.dirname(os.path.abspath(__file__)))