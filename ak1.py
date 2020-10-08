import pygame 
import os
import math
import random
from tkinter import messagebox

pygame.init()

WIDTH,HEIGHT=1000,1000

win=pygame.display.set_mode((WIDTH,HEIGHT))
RADIUS=20
GAP=20
letters=[]
startx=round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty=400
A=65
for i in range(26):
	x=startx+GAP*2+((RADIUS*2+GAP)*(i%13))
	y=starty+(i//13)*(GAP+RADIUS*2)
	letters.append([x,y,chr(A+i),True])

LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT= pygame.font.SysFont('comicsans',60)

images=[]
for i in range (7):
	image=pygame.image.load("hangman"+str(i)+".jpg")
	images.append(image)

hangman_status=0
word=["ABTRUPTLY","HELLO","COMPUTER"]
words=random.choice(word)

guessed=[]

def draw():
	win.fill((255,255,255))
	display_word=""
	for letter in words:
		if letter in guessed:
			display_word+=letter+""
		else:
			display_word+="_  "

	text=WORD_FONT.render(display_word,1,(0,0,0))
	win.blit(text,(400,200))



	for letter in letters:
		x,y,ltr,visible=letter
		if visible:
			pygame.draw.circle(win,(0,0,0), (x,y) ,RADIUS,3)
			text=LETTER_FONT.render(ltr,1,(0,0,0))
			win.blit(text,(x - text.get_width()/2, y - text.get_height()/2))

	win.blit(images[hangman_status],(5,5))
	pygame.display.update()


FPS=60
clock=pygame.time.Clock()

running=True

while running:
	clock.tick(FPS)

	
	draw()

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			m_x, n_y =pygame.mouse.get_pos()
			for letter in letters:
				x,y,ltr,visible=letter
				if visible:
					dis=math.sqrt((x-m_x)**2+(y-n_y)**2)
					if dis<RADIUS:
						letter[3]=False
						guessed.append(ltr)
						if ltr not in words:
							hangman_status+=1
						
    		



pygame.quit()





