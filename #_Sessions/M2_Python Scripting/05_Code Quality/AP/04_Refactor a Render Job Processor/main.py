import os
import json

def run(d):
 files=os.listdir(d)
 total=0
 for f in files:
  if ".json" in f:
   p=d+"/"+f
   file=open(p,"r")
   data=json.load(file)
   file.close()

   s=data["frame_start"]
   e=data["frame_end"]
   r=data["render_time_per_frame"]

   fc=e-s+1
   tr=fc*r

   data["frame_count"]=fc
   data["total_render_time"]=tr

   file=open(p,"w")
   json.dump(data,file)
   file.close()

   print("done",f,fc,tr)

   total=total+tr

 print("all",total)

run("jobs")