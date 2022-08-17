from moviepy.editor import *

clip = ImageSequenceClip(['./teste/2020-04-03_01-39-12_UTC_1.jpg',
                          './teste/2020-04-03_01-46-37_UTC.jpg',], fps = 0.5)
clip.ipython_display(width = 360)
