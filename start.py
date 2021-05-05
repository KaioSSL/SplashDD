import pygame, sys
from pygame.locals import *
from guerra import guerra


Branco=(255,255,255)

def  Menu():
    pygame.init()
    tela = pygame.display.set_mode((1200,768))
    pygame.display.set_caption("Guerra de Tanques")
    img_fundo=pygame.image.load('Imagens/FundoIntro.jpg')
    img_start=pygame.image.load('Imagens/Start.png')
    img_quit=pygame.image.load('Imagens/Quit.png')   
    tela.fill(Branco)
    tela.blit(img_fundo,(0,0))
    tela.blit(img_start,(100,650))
    tela.blit(img_quit,(1000,650))
    l_img=150
    a_img=88
    music_intro=pygame.mixer.music.load('Sounds/Intro2.mp3')
    pygame.mixer.music.play(10)
    sound_start= pygame.mixer.Sound("Sounds/Iniciar.ogg")
    #sound_quit=pygame.mixer.Sound('Sounds/Quit.mp3')
    
    #Fontes Texto
    font= pygame.font.get_default_font()
    text=pygame.font.SysFont(font,50)    
    play=text.render("Play",1,(Branco))
    sair=text.render("Quit",1,(Branco))
    while True:
        click=pygame.mouse.get_pressed()
        mous_pos=pygame.mouse.get_pos()
        tela.blit(play,(140,625))
        tela.blit(sair,(1000,625))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if 100 + l_img > mous_pos[0] > 100 and 650 + a_img > mous_pos[1] > 650:
                if click[0]==1:
                    sound_start.play()
                    pygame.mixer.music.stop()
                    guerra()
                    
            if 1000 + l_img > mous_pos[0] > 1000 and 650 + a_img > mous_pos[1]> 650:
                if click[0]==1:
                    pygame.quit()
                    pygame.mixer.music.stop()
                    quit()
                
        pygame.display.update()
                
Menu()                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
