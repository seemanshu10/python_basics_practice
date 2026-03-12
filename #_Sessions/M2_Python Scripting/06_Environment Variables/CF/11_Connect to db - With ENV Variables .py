'''
Using CMD set ENV Variable
    set DB_USER=admin
    set DB_PASSWORD=password123
'''

import os

def connect_to_database():
    db_user = os.environ.get('DB_USER')
    print(db_user)
    db_password = os.environ.get('DB_PASSWORD')

    if not db_user or not db_password:
        print("Error: Database credentials are not set in environment variables.")
        return

    print("Connecting to database with:")
    print(f"Username: {db_user}")
    print(f"Password: {'*' * len(db_password)}")  # Masked for security

connect_to_database()
