'''
### 🎯 AP. Creating a Numbered Shot Status Summary from Nested Review Data

#### Task Objective:

* Work with a nested list containing review data for multiple shots.
* Use `enumerate()` with `start=1` to create a cleanly numbered summary.
* Unpack each shot’s data and access individual components.
* Use conditional formatting based on the shot's status (e.g., flagging pending or fix-required shots).


#### 🛠 Instructions:

* Create a list called `review_data`. Each item should be a list containing:
  * Shot ID (string)
  * Department (string)
  * Review note (string)
  * Status (string) — values can include `"Approved"`, `"Pending"`, `"Needs Fixes"`
* Use `enumerate()` to loop over the data, starting the count from 1.
* For each entry:
  * Unpack the values properly inside the loop.
  * Print the index, shot ID, department, and review note.
  * If the status is `"Needs Fixes"` or `"Pending"`, append a label: `⚠️ Action Required`
  * If the status is `"Approved"`, append: `✅ Approved`



#### Sample Output:

```
1. shot_001 | Lighting | Add rim light to character  [Status: Needs Fixes] ⚠️ Action Required
2. shot_002 | Compositing | Final glow pass  [Status: Approved] ✅ Approved
3. shot_003 | FX | Add sparks in explosion  [Status: Pending] ⚠️ Action Required
```

'''

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



