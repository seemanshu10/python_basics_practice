# ---------------- Temporarily Setting an Environment Variable

import os

os.environ['SEMANSHU'] = 'Z:\\StudioTools\\CustomPlugin'

print(f"Updated Maya Plugin Path: {os.environ['SEMANSHU']}")

