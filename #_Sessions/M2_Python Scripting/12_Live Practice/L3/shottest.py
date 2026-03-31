from datetime import datetime

# now is current datetime 
log_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

print(log_time)