import datetime

# generate a timestamp 
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# file name with timestamp 
file_name = f"report_{timestamp}.txt"
print(f"file name with timestamp : {file_name}")