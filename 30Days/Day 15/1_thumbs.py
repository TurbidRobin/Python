import os

from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail__per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail__per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-half-second")

os.makedirs(thumbnail_dir, exist_ok= True)
os.makedirs(thumbnail__per_frame_dir, exist_ok= True)
os.makedirs(thumbnail__per_half_second_dir, exist_ok= True)

clip = VideoFileClip(source_path)
#print(clip.reader.fps)
#print(clip.reader.nframes)
#print(clip.duration) #seconds


duration = clip.duration
max_duration = int(duration + 1)


for i in range(0, max_duration + 1):
    frame = clip.get_frame(int(i))
   # print(frame)
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
  #  print(f"frame has {i} seconds saved at {new_img_filepath}")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps * 1.0)

for i,frame in enumerate(clip.iter_frames()):
    if i % fps == 0:
        current_ms = int((i / fps) * 1000)
        new_img_filepath = os.path.join(thumbnail__per_frame_dir, f"{current_ms}.jpg")
        #print(f"frame has {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)

for i,frame in enumerate(clip.iter_frames()):
    fphs = int(fps/2.0)
    if i % fphs == 0:
        current_ms = int((i / fps) * 1000)
        new_img_filepath = os.path.join(thumbnail__per_half_second_dir, f"{current_ms}.jpg")
        #print(f"frame has {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)