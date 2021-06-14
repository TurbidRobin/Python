import os

from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail__per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail__per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-half-second")
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepath = [os.path.join(thumbnail_dir, fname)for fname in this_dir if fname.endswith("jpg")]

# filepaths = []
# for fname in this_dir:
#     if fname.endswith("jpg"):
#         path = os.path.join(thumbnail_dir, fname)
#         filepaths.append(path)

#print(filepath)
# clip = ImageSequenceClip(filepath, fps=1)
# clip.write_videofile(output_video)

directory = {}

for root, dirs, files in os.walk(thumbnail__per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try: 
           key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key !=None:
            directory[key] = filepath
new_paths = []
for k in sorted(directory.keys()):
    #print(k)
    filepath = directory[k]
    new_paths.append(filepath)
# clip = ImageSequenceClip(new_paths, fps=10)
# clip.write_videofile(output_video)
my_clips= []
for path in list(new_paths):
    frame = ImageClip(path)
    #print(frame.img) numpy array
    my_clips.append(frame.img)

clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_video)
        
     