"""

Creating a Numbered Shot Status Summary from Nested Review Data


"""


# Sample data input 
review_data = [
    ["SHOT001", "Animation", "Smooth movement", "Approved"],
    ["SHOT002", "Lighting", "Add rim light to character ", "Needs Fixes"],
    ["SHOT003", "Compositing", "Final glow pass ", "Pending"],
    ["SHOT004", " FX", "Add sparks in explosion", "Approved"],
]

# loop through data starting from 1 

for index,shot in enumerate(review_data,start=1):
    # unpack each shot data 
    shot_id , department ,notes , status = shot

    # prepare the status 
    if status == "Approved":
        label = "Approved"
    elif status in ["Needs Fixes", "Pending"]:
        label = "Action Required"
    else:
        label = status  

    # print the forma t

    print(f"{index} | {shot_id} | {department} | {notes} | {status} - {label}")

"""
1 | SHOT001 | Animation | Smooth movement | Approved - Approved
2 | SHOT002 | Lighting | Add rim light to character  | Needs Fixes - Action Required
3 | SHOT003 | Compositing | Final glow pass  | Pending - Action Required
4 | SHOT004 |  FX | Add sparks in explosion | Approved - Approved

"""