import os

from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.video.fx.all import crop 

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
output_path1 = os.path.join(GIF_DIR, 'sample1.gif')
output_path2 = os.path.join(GIF_DIR, 'cropped-sample2.gif')

os.makedirs(GIF_DIR, exist_ok=True)

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10, 20)
subclip = subclip.resize(width=500)
subclip.write_gif(output_path1, program='ffmpeg') # faster with ffmpeg but can be blury

w, h =clip.size
subclip2 = clip.subclip(10, 20)
cropped_clip = crop(subclip2, width = 320, height=320, x_center=w/2, y_center=h/2) #makes it sqaure

#cropped_clip.write_gif(output_path2, program='ffmpeg')