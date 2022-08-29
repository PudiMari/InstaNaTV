import os
import sys
import subprocess
import shlex

CaminhoArquivoControle="/tmp/ControleRadio"

def TocaPlaylist():
    
    ComandoMPlayer = "mplayer -input file=/tmp/ControleRadio -slave -playlist "
    Playlists=["https://player.hdradios.net/player-home-page/6990"]        
    NomesRadios=["Radio IFMT Campus Cuiaba"] 
 
    os.system("pkill -f mplayer")
    ComandoPlaylist = ComandoMPlayer + Playlists[0]
     
    FNULL = open(os.devnull,'w')
    args = shlex.split(ComandoPlaylist)
    InterfaceMPlayer = subprocess.Popen(args, shell=False, stdin=subprocess.PIPE, stdout=FNULL, stderr=subprocess.STDOUT)
    return

def CriaArquivoControle():
    if (os.path.exists(CaminhoArquivoControle)):
        return
 
    try:
        os.mkfifo(CaminhoArquivoControle)
    except:
        print ("Falha ao criar arquivo de controle. Por favor, verifique o caminho de criacao do arquivo")
        exit(1)

CriaArquivoControle()

TocaPlaylist()
