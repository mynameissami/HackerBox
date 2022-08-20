import requests
import os   
import math

def intervals(parts, duration):
    part_duration = math.ceil(duration / parts)
    return [(start, min(start + part_duration - 1, duration - 1)) 
             for start in range(0, duration, part_duration)]
home = os.path.expanduser("~")
if not os.path.exists(home+'/Desktop/temp'):
    os.makedirs(home+'/Desktop/temp')

PATH = home+"/Desktop/temp/tmp.mp4"

example_file_url = "https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1280_10MG.mp4"


req = requests.head(example_file_url)

size = int(req.headers['Content-Length'])

content_section = 10

section_intervals = intervals(content_section,size)


with  open(PATH, "wb") as file:
    for i,(start,end) in enumerate(section_intervals):
        headers = {"Range": "bytes="+str(start)+"-"+str(end)}
        print(headers)
        r = requests.get(example_file_url, headers=headers)
        file.write(r.content)