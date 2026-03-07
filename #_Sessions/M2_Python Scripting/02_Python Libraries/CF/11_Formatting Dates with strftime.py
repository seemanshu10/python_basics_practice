import datetime

date_obj = datetime.date.today()
# print(date_obj)




formatted_date = date_obj.strftime("%d/%y/%m")
# print(formatted_date) 
# Output: 18/07/25




formatted = date_obj.strftime("%Y-%m-%d")
print(formatted)
# Output: 2025-07-18

