from missing_data import run_missing_data
from fetch_info import run_fetch_info
from check_module import run_check_module
from update_stock import run_update_stock

def main():
    run_fetch_info()
    run_missing_data()
    run_update_stock()
    run_check_module()
    
    print("This is main_app.py. __name__ is ",__name__)

if __name__ == "__main__":
    main()