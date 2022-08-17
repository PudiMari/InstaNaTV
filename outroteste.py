from moviepy.editor import *
from vinheta import credits1

# Load video
video = VideoFileClip("video-teste/teste.mp4")

# Video lenght
duration = video.duration

# Video size
w, h = video.size

# Text for video
txt = (TextClip('data.txt', fontsize=50, font='Amiri-regular',
                color='white').set_duration(duration))

# Transparent text background
txt_col = txt.on_color(size=(video.w + txt.w, txt.h - 10),
                       color=(0, 0, 0), pos=(6, 'center'), col_opacity=0.8)

# Animate text
txt_mov = credits1('data.txt', w)

# Overlay text on video
result = CompositeVideoClip([video, txt_mov])
result = result.set_duration(video.duration)
# Render video
result.write_videofile("test.mp4")