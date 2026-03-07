#---------------- Converting int to float ----------------
count = 45
count_f = float(count)

print("Int to float:", count_f)               # 45.0



#---------------- Converting float to int ----------------
pi = 3.14159
pi_int = int(pi)

print("Float to int:", pi_int)                # 3



#---------------- Converting number to string -----------
score = 99
msg = "Your score is " + str(score)

print(msg)                                    # "Your score is 99"



#---------------- Converting string to number -----------
height_str = "180"
height = int(height_str)

print("Height in cm:", height)                # 180



#---------------- Boolean conversion ----------------------
print(bool(0))        # False
print(bool(-3))       # True
print(bool([]))       # False (empty list)
print(bool([1, 2]))   # True (non-empty list)
