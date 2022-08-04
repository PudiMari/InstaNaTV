import pafy
import vlc

url = "https://www.youtube.com/watch?v=AyX_LL9nWSE"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()
