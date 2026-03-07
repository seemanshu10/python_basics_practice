shots = [
    ['shot01', 'Approved'],
    ['shot02', 'Pending'],
    ['shot03', 'Fix Required']
]

for index, shot in enumerate(shots, start=1):
    print(index, shot)



# -------- Unpacking
for index, (shot_name, status) in enumerate(shots, start=1):
    print(index, shot_name, status)