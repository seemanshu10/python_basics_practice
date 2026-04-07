class RenderJob:
    def __init__(self, job_name, renderer, status):
        self.job_name = job_name
        self.renderer = renderer
        self.status = status
        
    def show_job_info(self):

        print(f"Job Name: {self.job_name}")
        print(f"Renderer: {self.renderer}")
        print(f"Status : {self.status}\n")
        
    def set_frame_range(self, frame_range):
        self.frame_range = frame_range
        print(f"Frame range set to {frame_range} for {self.job_name}\n")
        
    def submit_render(self, artist_name, priority):
        print(f"{self.job_name} submitted by {artist_name} with {priority} priority\n")
        
    def output(self, format = "exr"):
        print(f"{self.job_name} will output in {format} format\n")

    def render_note():
        print("Always check frame range before submitting render jobs.\n")

asset = RenderJob("Shot01_Render", "Arnold", "Pending")

asset.show_job_info()
asset.set_frame_range("1-120")
asset.submit_render("Riya", "High")
asset.output()
asset.output("png")
RenderJob.render_note()

"""
Job Name: Shot01_Render
Renderer: Arnold
Status : Pending

Frame range set to 1-120 for Shot01_Render

Shot01_Render submitted by Riya with High priority

Shot01_Render will output in exr format

Shot01_Render will output in png format

Always check frame range before submitting render jobs.
"""