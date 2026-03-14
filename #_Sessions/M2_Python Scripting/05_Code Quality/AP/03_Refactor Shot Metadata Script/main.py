import os,json

def p(d):
 files=os.listdir(d)
 for f in files:
  if f.endswith(".json"):
   path=d+"/"+f
   file=open(path,"r")
   data=json.load(file)
   file.close()

   s=data["frame_start"]
   e=data["frame_end"]
   t=e-s+1

   data["frame_count"]=t

   file=open(path,"w")
   json.dump(data,file)
   file.close()

   print("done",f,t)

p("shots")