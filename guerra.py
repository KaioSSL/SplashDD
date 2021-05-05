import pygame, sys
from pygame.locals import *
from tanque import Tanque
from res import restart
import random
import time as time_

White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Largura=1500
Altura=700
cor=(255,0,255)
posx1=random.randrange(0,400)
posx2=random.randrange(1000,1400)
#Calculo_do_Tempo_Atirar
def millis():
    return int(round(time_.time() * 1000))

def guerra():
    #Iniciador
    pygame.init()
    #Variaveis_atirar
    angleControl=0.2
    forceControl=0.5
    time = 0    
    inverter = False
    #Conf_Tela
    
    tela = pygame.display.set_mode((Largura,Altura))
    pygame.display.set_caption("Guerra de Tanques")

    #Fundo
    imagemfundo = pygame.image.load('Imagens/Fundo3.jpg')    
    
    #Jogadores    
    Syn = Tanque(1, posx1, 670, tela)
    Dog = Tanque(2, posx2, 670,tela)
    
    #Cores
    
    cor_blue = (167,234,226)
    cor_green = (79,248,164)    
    branco=(255,255,255) 
      
    #Fontes_Texto
    font_nick = pygame.font.SysFont(pygame.font.get_default_font(),30) 
    font_partida=pygame.font.SysFont(pygame.font.get_default_font(),30)
    font_turno=pygame.font.SysFont(pygame.font.get_default_font(),50)

   #Turno_aleatorio    
    firstplay=random.randrange(0,100)    
    if firstplay > 50 :
        Turno=2
    elif firstplay <= 50:
        Turno=1
        
    #Atualizador    
    relogio = pygame.time.Clock()
    
    #Boleanas
    
    Texto=False
    Jogando=True

    #Audios
    
    pygame.mixer.music.load('Sounds/Jogando.ogg')
    pygame.mixer.music.play()
    som_tiro=pygame.mixer.Sound('Sounds/Tiro.ogg')
    
    while True:       
        
        #Atualizações_da_tela
        tela.fill(cor)        
        tela.blit(imagemfundo, (0,0))
        relogio.tick(1000)
        
        #Posiciona_os_tanques_na_tela
        
        Syn.colocar(tela,"Syn",50)
        Dog.colocar(tela,"Dog",1150)

        		
		#Lopp_Dos_Eventos#	
	
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
			#JOGADOR1  

        if Turno==1:         
            Dog.velocidade=2.5
            if Syn.vida>0:
                vez_de_jogar=font_turno.render("Vez do Syn Jogar",1,(branco))
                tela.blit(vez_de_jogar,(500,150))
                if evento.type == pygame.KEYDOWN and evento.key == K_UP:
                    if Syn.alpha<90:
                        Syn.alpha+=angleControl
                    
                if evento.type == pygame.KEYDOWN and evento.key == K_DOWN:
                    if Syn.alpha>0:
                        Syn.alpha-=angleControl
                if evento.type == pygame.KEYDOWN and evento.key == K_LEFT:
                    Syn.movimentoEsquerda(Dog)
                    Syn.limite()
                    if Syn.velocidade>0:
                        Syn.limite_movimento+=1
                if evento.type == pygame.KEYDOWN and evento.key == K_RIGHT:                    
                    Syn.movimentoDireita(Dog)
                    Syn.limite()
                    if Syn.velocidade>0:
                        Syn.limite_movimento+=1
                if evento.type == pygame.KEYDOWN and evento.key == K_c:
                    if(time > 0 and millis() - time > 200):
                        som_tiro.play()                        
                        Syn.atirar(Syn.forca,Syn.alpha,millis())
                                             
                        Texto=False
                        Turno=2
                        Syn.limite_movimento=0
                        time , Syn.forca =(0,0)
                        inverter = False
                    else:
                        time = millis()
                        if (inverter) :
                            Syn.forca-=forceControl
                        else:
                            Syn.forca+=forceControl
                            
                        if (Syn.forca > 100):
                            inverter = True
                        if (Syn.forca < 0) :
                            inverter = False  
                        

                        
                                              
            else:       
                Jogando=False
                
                        #JOGADOR2
                
        if Turno==2:         
            Syn.velocidade=2.5
            if Dog.vida>0:
                vez_de_jogar=font_turno.render("Vez do Dog Jogar",1,(branco))
                tela.blit(vez_de_jogar,(500,150))
                if evento.type == pygame.KEYDOWN and evento.key == K_w:
                    if Dog.alpha<90:
                        Dog.alpha+=angleControl                        
                if evento.type== pygame.KEYDOWN and evento.key == K_s:
                    if Dog.alpha>0:
                        Dog.alpha-=angleControl                       
                if evento.type == pygame.KEYDOWN and evento.key == K_a:
                    Dog.movimentoEsquerda(Syn)
                    Dog.limite()
                    if Dog.velocidade>0:
                        Dog.limite_movimento+=1
                if evento.type == pygame.KEYDOWN and evento.key == K_d:                    
                    Dog.movimentoDireita(Syn)
                    Dog.limite()
                    if Dog.velocidade>0:
                        Dog.limite_movimento+=1
                if evento.type == pygame.KEYDOWN and evento.key == K_SPACE:                                                      
                    if(time > 0 and millis() - time > 200):
                        som_tiro.play()                        
                        Dog.atirar(Dog.forca,180-Dog.alpha,millis())                       
                        Texto=False
                        Turno=1
                        Dog.limite_movimento=0
                        time , Dog.forca=(0,0)
                        inverter = False
                        
                    else:
                        time = millis()
                        if Dog.forca > 100:
                            inverter = True
                        if Dog.forca <=0 :
                            inverter = False
                        if (inverter) :
                            Dog.forca-=forceControl
                        else:
                            Dog.forca+=forceControl
                        
                        
            else:                        
                Jogando=False 
        

        if Jogando==False:
            if Syn.vida<=0:
                win="Dog"
                los="Syn"
                restart(win,los)
            elif Dog.vida<=0:
                win="Syn"
                los="Dog"
                restart(win,los)


            
                
        if Syn.atualizador():
            Syn.trajeto(Dog,tela)
        if Dog.atualizador():
            Dog.trajeto(Syn,tela)

    
        pygame.display.update()
