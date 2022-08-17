from moviepy.editor import *

# Load video
video = VideoFileClip("video-teste/teste.mp4")

# Video lenght
duration = video.duration

# Video size
w, h = video.size

# Load text from txt
f = open('data.txt', 'r')
data = f.read().replace('\n', '')

# Text for video
txt = (TextClip(data, fontsize=50, font='Amiri-regular',
                color='white')
       .set_duration(duration))

# Transparent text background
txt_col = txt.on_color(size=(video.w + txt.w, txt.h - 10),
                       color=(0, 0, 0), pos=(6, 'center'), col_opacity=0.8)

# Animate text
txt_mov = txt_col.set_pos(lambda t: (max(w / w, int(w - 0.5 * w * t)),
                                     max(5.4 * h / 6, int(0 * t))))

# Overlay text on video
result = CompositeVideoClip([video, txt_mov])
# Render video
result.write_videofile("test.mp4")