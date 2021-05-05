import pygame
from math import sin, cos, radians

class Bala(pygame.sprite.Sprite):    
    
    def __init__(self, tanque,vel,alpha):
		
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(
            'Imagens/Bala%d.png' % tanque.id_tanque
        )
        self.rect = self.image.get_rect()
        self.rect.center = tanque.rect.center
        self.alpha = alpha
        self.xo, self.yo = self.rect.center
        self.vo = vel*1.5
        self.vx = self.vo * cos(radians(self.alpha))
        self.vy = -self.vo * sin(radians(self.alpha))        
        self.t = 0
                
    def mover(self, dt=.3, g=9.81):
        
        self.rect.centerx = self.xo + self.vx * self.t
        self.rect.centery = self.yo + self.vy * self.t + 0.5 * g * self.t ** 2
        self.t += dt
        

    def colocar(self, superficie):        
        superficie.blit(self.image, self.rect)
        
    def colisao(self, inimigo):        
        return pygame.sprite.collide_rect(self, inimigo)
        
    def fora_tela(self, tela):        
        return self.rect.centerx < 0 or self.rect.centerx > tela.get_width() or self.rect.centery > tela.get_height()
  
