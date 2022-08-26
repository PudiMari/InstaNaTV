from moviepy.editor import VideoFileClip, ColorClip, TextClip, CompositeVideoClip

def pos(time):
        return(time*50, 'bottom')

video = VideoFileClip('./clips.mp4')

text = TextClip('Naíra de Moura e Souza', color = 'white', fontsize = 50
    ).set_duration(video.duration)

color = ColorClip(
    text.size, color = (0, 0, 0), duration = video.duration
)

cor_texto = CompositeVideoClip([color, text]).set_position(pos)

compose = CompositeVideoClip([video, cor_texto])

compose.write_videofile('vinheta.mp4')