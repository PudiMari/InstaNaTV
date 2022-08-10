# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
# getting subclip as video is large
# adding margin to the video
clip1 = VideoFileClip("bordadolistico/2021-05-08_15-51-38_UTC.mp4").subclip(0, 12).margin(10)

# getting clip2 by mirroring over x axis
clip2 = VideoFileClip("video-teste/teste.mkv").subclip(0, 12).margin(10).without_audio()

# clips list
clips = [[clip1, clip2]]

# stacking clips
final = clips_array(clips)

# showing final clip
final.ipython_display(width=480)
