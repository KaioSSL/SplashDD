import pygame
from pygame.locals import *
from bala import Bala
import random
import time as time_  
branco=(255,255,255)
red=(255,0,0)
preto=(0,0,0)
cor_blue = (167,234,226)
red=(255,0,0)
def millis():
    return int(round(time_.time() * 1000))

class Tanque(pygame.sprite.Sprite):
	def __init__(self, id_tanque,x, y, tela):
		
		pygame.sprite.Sprite.__init__(self)
		self.time = 0
		self.id_tanque = id_tanque
		self.image = pygame.image.load('Imagens/Tanque%d.png' % id_tanque)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y      
		self.vida = 300
		self.tempo = 0
		self.velocidade = 2.5
		self.limite_movimento = 0
		self.lista_tiro = []
		self.forca=0
		self.alpha=30
		
						
		
	def movimentoDireita(self, inimigo):
		
		self.rect.right += self.velocidade
		self.movimento()
		a,b= (self.rect.left,self.rect.top)        
		if pygame.sprite.collide_rect(self, inimigo):
			print("Colisao")           
			
			
	def movimentoEsquerda(self, inimigo):
		
		self.rect.left -= self.velocidade
		self.movimento()           
		if pygame.sprite.collide_rect(self, inimigo):
			print("Colisao")     
			
			   
	def movimento(self):        
		if self.vida > 0:
			if self.rect.centerx <=0 :
				self.rect.centerx=1
			elif self.rect.centerx >=1500:
				self.rect.centerx = 1499                 
	
	def atirar(self,vel,alpha,tempo):
		global tempo_tiro
		tempo_tiro = tempo        
		self.lista_tiro.append(Bala(self,vel,alpha))


	def atualizador(self):
		
		return len(self.lista_tiro) > 0
	
			
	def trajeto(self, inimigo, tela):
		for tiro in self.lista_tiro:
			tiro.colocar(tela)
			tiro.mover()
			if(millis() - tempo_tiro > 200):
				if tiro.colisao(inimigo):                
					damage = int(random.randrange(20,50) * random.uniform(1,2))
					self.lista_tiro.remove(tiro)
					inimigo.vida -= damage
					img_colisao = pygame.image.load('Imagens/Colisao.png')
					tela.blit(img_colisao, tiro.rect.center)
					
				if tiro.colisao(self):
					damage = int(random.randrange(20,50) * random.uniform(1,2))
					self.lista_tiro.remove(tiro)
					self.vida -= damage
					img_colisao = pygame.image.load('Imagens/Colisao.png')
					tela.blit(img_colisao, tiro.rect.center)
					
			else:
				self.time = millis()
			if tiro.fora_tela(tela):
				self.lista_tiro.remove(tiro)
		self.time = 0
		pygame.display.update()
			

	def colocar(self, tela, nome , posx):
		
		#Textos
		font_nick = pygame.font.SysFont(pygame.font.get_default_font(), 30)
		font_angle=pygame.font.SysFont(pygame.font.get_default_font(), 25)
		text = font_nick.render(nome, 1, (cor_blue))
		tela.blit(text, (self.rect.left + 20, self.rect.top -20))
		tela.blit(self.image, self.rect)
		#Retangulos_VIDA
		pygame.draw.rect(tela,branco,(posx,0,300,30))
		pygame.draw.rect(tela,red,(posx,0,300-(300-self.vida),30))
		life= font_nick.render("Vida:"+str(self.vida),1,(preto))
		tela.blit(life,(posx+20,10))
		#Retangulos_FORÇA
		pygame.draw.rect(tela, branco,(self.rect.centerx-20,350,50,100))
		pygame.draw.rect(tela,red,(self.rect.centerx-20,350,50,100-self.forca))
		power=font_nick.render("F"+str(int(self.forca)),1,(preto))
		tela.blit(power,(self.rect.centerx-15,400))
		#Retangulos_ANGULO
		angle=font_angle.render("º"+str(int(self.alpha)),1,(branco))
		tela.blit(angle,(self.rect.centerx-50,self.rect.centery-15))
		
	   
		

		
	def limite(self):
		if self.limite_movimento >=100:
			self.velocidade=0
