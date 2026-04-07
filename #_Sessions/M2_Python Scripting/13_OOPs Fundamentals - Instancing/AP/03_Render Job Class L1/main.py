class RenderJob:

    def show_job_info(self):
    
        self.job_name = "TestRender"
        self.renderer = "Arnold"
        self.status = "Pending"

        print(f"Job Name: {self.job_name}")
        print(f"Renderer: {self.renderer}")
        print(f"Status : {self.status}")
        print()

    def set_frame_range(self, frame_range):
        self.frame_range = frame_range
        print(f"Frame range set to {frame_range}")
        print()

    def submit_render(self, artist_name, priority):
        print(f"Render submitted by {artist_name} with {priority} priority")
        print()

    def output(self, format = "exr"):
        print(f"Render output will be saved as {format} format")

asset = RenderJob()

asset.show_job_info()
asset.set_frame_range("1-120")
asset.submit_render("Riya", "High")
asset.output()
asset.output("png")

"""
Job Name: TestRender
Renderer: Arnold
Status : Pending

Frame range set to 1-120

Render submitted by Riya with High priority

Render output will be saved as exr format
Render output will be saved as png format
"""