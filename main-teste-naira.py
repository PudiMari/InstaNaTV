from  pil_video  import  make_video 
""" 
Faça uma lista de imagens PIL na sequência em que deseja fazer um vídeo, digamos que 
você tenha feito uma lista chamada test 
""" 

teste = ['C:/Users/Naíra Souza/Desktop/Naíra/Sistemas Embarcados/InstaNaTV-master/teste/2020-04-03_01-39-12_UTC_1.jpg', 
         'C:/Users/Naíra Souza/Desktop/Naíra/Sistemas Embarcados/InstaNaTV-master/teste/2020-04-03_01-46-37_UTC.jpg'
         ]
# O primeiro argumento é a lista composta por imagens PIL 
# o segundo argumento é o FPS do vídeo que você deseja gerar 
# se houver mais imagens e você especificar menos FPS, o vídeo será mais longo 
# A API abaixo gerará o vídeo, reproduza-o. No processo, ele usará seu diretório /tmp 
# para criar alguns arquivos temporários e eles serão excluídos após a reprodução do vídeo. 
make_video (teste,  fps = 0.5, delete_folder = False)
# há um terceiro argumento opcional delete_folder, que é o padrão True, mas se você quiser ter o vídeo e 
# imagens para sua referência, você pode passar isso como false, para que não seja excluído automaticamente 
#make_video (teste ,  fps = 20 ,  delete_folder = False ) 
# Há um quarto argumento opcional play_video que é True por padrão. Se for passado como False, o vídeo não será reproduzido. Usado em cenários em que você está trabalhando em um terminal remoto e não faz o encaminhamento X para o seu PC 
#make_video (teste ,  fps = 20 ,  delete_folder =False ,  play_video = False )