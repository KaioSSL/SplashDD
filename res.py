import pygame, sys
from pygame.locals import *
import guerra

White=(255,255,255)
Largura=800
Altura=480
cor=(255,150,100)

def restart(xv,xp):
        pygame.init()
        tela=pygame.display.set_mode((Largura,Altura))
        pygame.display.set_caption("Guerra de Tanques")
        #Imganes
        l_img=150
        a_img=88
        img_fundo=pygame.image.load('Imagens/FundoRestart.jpg')
        img_start=pygame.image.load('Imagens/Start.png')
        img_quit=pygame.image.load('Imagens/Quit.png')
        posx=100
        posx_quit=posx + 500
        posy=400
        #Sounds
        
        sound_start= pygame.mixer.Sound("Sounds/Iniciar.ogg")
        #Fontes Texto
        
        font = pygame.font.get_default_font()
        text=pygame.font.SysFont(font,30)    
        play=text.render("Restart",1,(White))
        sair=text.render("Quit",1,(White))
        vencedor=text.render("Com grande esforço e suor, o vencedor "+str(xv),1,White)
        perdedor=text.render("venceu o invencível "+str(xp),1,White)
        #Blitagens
        
        tela.blit(img_fundo,(0,0))
        tela.blit(img_start,(posx,posy))
        tela.blit(img_quit,(posx_quit,posy))
        
        while True:
                click=pygame.mouse.get_pressed()
                mous_pos=pygame.mouse.get_pos()
                tela.blit(play,(posx+40,posy-25))
                tela.blit(sair,(posx_quit,posy-25))
                tela.blit(vencedor,(100,200))
                tela.blit(perdedor,(100,220))
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if posx + l_img > mous_pos[0] > posx and posy + a_img > mous_pos[1] > posy:
                        if click[0]==1:
                            sound_start.play()
                            pygame.mixer.music.stop()
                            guerra.guerra()
                            
                    if posx_quit + l_img > mous_pos[0] > posx_quit and posy + a_img > mous_pos[1]> posy:
                        if click[0]==1:
                            pygame.quit()
                            pygame.mixer.music.stop()
                            quit()
                pygame.display.update()

