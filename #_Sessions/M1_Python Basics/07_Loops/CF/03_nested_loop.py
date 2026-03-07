# Nested For Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end='\t')
    print()

# Output
# 1 x 1 = 1    1 x 2 = 2    1 x 3 = 3    
# 2 x 1 = 2    2 x 2 = 4    2 x 3 = 6    
# 3 x 1 = 3    3 x 2 = 6    3 x 3 = 9    


# Nested While Loop
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print("X", end=' ') 
        j += 1
    print()
    i += 1 

# Output
# X X 
# X X 



