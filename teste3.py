import numpy as np
from moviepy.editor import * 
from moviepy.video.tools.segmenting import findObjects 

screensize = (1080, 720) 
txtClip = TextClip('GeeksforGeeks', color = 'red', font = "Arial", 
                   kerning = 5, fontsize = 80) 
cvc = CompositeVideoClip( [txtClip.set_pos('center')], 
                        size = screensize) 
rotMatrix = lambda a: np.array( [[np.cos(a), np.sin(a)],  
                                 [-np.sin(a), np.cos(a)]] ) 
  
  
  
def effect3(screenpos, i, nletters): 
      
    v = np.array([-1, 0]) 
      
    d = lambda t : max(0, 3-3 * t) 
      
    
    return lambda t: screenpos-400 * v*d(t-0.2 * i) 

def effect4(screenpos, i, nletters): 
      
    
    d = lambda t : max(0, t)  
      
     
    a = i * np.pi / nletters 
      
    v = rotMatrix(a).dot([-1, 0]) 
      
    if i % 2 : v[1] = -v[1] 
          
    
    return lambda t: screenpos + 400 * d(t-0.1 * i)*rotMatrix(-0.2 * d(t)*a).dot(v) 
  
  
  
letters = findObjects(cvc)  
  
  
def moveLetters(letters, funcpos): 
      
    return [ letter.set_pos(funcpos(letter.screenpos, i, len(letters))) 
              for i, letter in enumerate(letters)] 
clips = [ CompositeVideoClip( moveLetters(letters, funcpos), 
                              size = screensize).subclip(0, 5) 
          for funcpos in [effect3, effect4] ] 
final_clip = concatenate_videoclips(clips) 
final_clip.fps = 24
final_clip.ipython_display() 