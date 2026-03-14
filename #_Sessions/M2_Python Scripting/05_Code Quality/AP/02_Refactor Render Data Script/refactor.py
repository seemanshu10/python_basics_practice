# Refactor Render Data Script


def calculate_total_render_time(list_of_render_frames):
    """
    Calculate the total render time from a list of frame render times.

    Args:
        render_frames (list): List of frame render times in seconds.

    Returns:
        int : Total render time in seconds.
    
    """
    total_time_render = 0

    # input validation if list of frames is passed 
    if not isinstance(list_of_render_frames, list):
        raise TypeError("render_frames must be a list")
    
    for frame in list_of_render_frames:
        total_time_render = total_time_render + frame
    return total_time_render

list_of_render_frames = [12,18,20,10]
total_render_time = calculate_total_render_time(list_of_render_frames)
print(f"Total render time: {total_render_time} seconds ")