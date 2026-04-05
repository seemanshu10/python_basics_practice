default_render_engine = "Cycles"

def start_render(scene):
    return f"Rendering Scene: {scene} with {default_render_engine}"

def stop_render():
    return "Render Stopped"