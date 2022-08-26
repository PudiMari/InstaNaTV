from os import walk
from moviepy.editor import *

files = []
files_list = []
path = './teste'

for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break

tamanho = len(files)

for i in range(tamanho):
    files_list.append(os.path.join(path, files[i]))
    
fps = 24
clips = [ImageClip(m).set_duration(4) for m in files_list]

print(clips)
    
concat_clip = concatenate_videoclips(clips, method='compose')

concat_clip.write_videofile('clips.mp4', fps=fps)