"""
Create a dictionary named shot_tracker containing nested dictionaries for individual shots.
Store shot-specific details like artist, status, and frame_range.
Modify the nested dictionary for an existing shot by updating values.
Add a new shot to the tracker with the same structure.
Print the updated dictionary.
Safely access a key that doesn’t exist using the get() method.
"""

# creating A shot Tracker 
# Creting a shot tracker nested dict 

shot_tracker = {
    'shot_001': {'artist': 'Alice', 'status': 'In Progress', 'frame_range': (100, 200)},  
    'shot_002': {'artist': 'Bob', 'status': 'Not Started', 'frame_range': (201, 300)},  
    'shot_003': {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)}  
}

new_Shot = {
    'shot_004': {'artist': 'Katie', 'status': 'Complete', 'frame_range': (201, 500)} 
}
print (shot_tracker)
# output : {'shot_001': {'artist': 'Alice', 'status': 'In Progress', 'frame_range': (100, 200)}, 'shot_002': {'artist': 'Bob', 'status': 'Not Started', 'frame_range': (201, 300)}, 'shot_003': {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)}}

shot_tracker["shot_001"]["artist"] = "David"
shot_tracker["shot_001"]["status"] = "Complete"
print (shot_tracker)
# Output : {'shot_001': {'artist': 'David', 'status': 'Complete', 'frame_range': (100, 200)}, 'shot_002': {'artist': 'Bob', 'status': 'Not Started', 'frame_range': (201, 300)}, 'shot_003': {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)}}

# adding the new Shot
shot_tracker.update(new_Shot)
print("Full Shot Tracker:",shot_tracker)
# output :Full Shot Tracker: {'shot_001': {'artist': 'David', 'status': 'Complete', 'frame_range': (100, 200)}, 'shot_002': {'artist': 'Bob', 'status': 'Not Started', 'frame_range': (201, 300)}, 'shot_003': {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)}, 'shot_004': {'artist': 'Katie', 'status': 'Complete', 'frame_range': (201, 500)}}

shot_005 = shot_tracker.get("shot_005","Unassigned")
print("Artist for Shot_005: ",shot_005)
# Output : Artist for Shot_005:  Unassigned