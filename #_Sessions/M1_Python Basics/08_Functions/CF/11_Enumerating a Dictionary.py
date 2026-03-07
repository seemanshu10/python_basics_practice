shots = {
    'shot01': 'Approved',
    'shot02': 'Pending',
    'shot03': 'Fix Required'
}

for index, key in enumerate(shots):
    print(index, key)



# ---------- If you want both key and value:
for index, (key, value) in enumerate(shots.items(), start=1):
    print(index, key, value)