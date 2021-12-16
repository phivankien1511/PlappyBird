import pygame
from random import randint
pygame.init();
screen_width ,screen_height =400,600
screen = pygame.display.set_mode((400,600))
running = True
pausing =False

clock = pygame.time.Clock()
#
TUBE_WIDTH = 50
TUBE_VELOCITY =3
TUBE_GAP = 150
#
tube1_x = 600
tube2_x = 800
tube3_x = 1000
score =0
#tọa độ chim
BIRD_X = 50   
BIRD_Y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity =0
GRAVITY =0.5
plus = 1
ms = 0.5
level =1
kill =2
tube1_pass= False
tube2_pass= False
tube3_pass= False

level_pass=False
#ảnh nền và chim màu
GREEN =(0,255,0)
BLUE =(0,0,255)
RED =(255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)


font= pygame.font.SysFont('sans',30)
backgroud_img = pygame.image.load("backgr.jpg")
backgroud_img = pygame.transform.scale(backgroud_img,(screen_width+100,screen_height))
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img,(BIRD_WIDTH,BIRD_HEIGHT))

#random độ cao của ống
tube1_height =randint(100,400)
tube2_height =randint(100,400)
tube3_height =randint(100,400)

while running:
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(backgroud_img,(0,0 ))

	tube1_rect= pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WIDTH,tube1_height))
	tube2_rect=pygame.draw.rect(screen,BLUE,(tube2_x,0,TUBE_WIDTH,tube2_height))
	tube3_rect=pygame.draw.rect(screen,BLUE,(tube3_x,0,TUBE_WIDTH,tube3_height))

	tube1_rect_inv=pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height+TUBE_GAP,TUBE_WIDTH,screen_height- tube1_height))
	tube2_rect_inv=pygame.draw.rect(screen,BLUE,(tube2_x,tube2_height+TUBE_GAP,TUBE_WIDTH,screen_height- tube2_height))
	tube3_rect_inv=pygame.draw.rect(screen,BLUE,(tube3_x,tube3_height+TUBE_GAP,TUBE_WIDTH,screen_height- tube3_height))
	bird_rect=screen.blit(bird_img,(BIRD_X,BIRD_Y))
	BIRD_Y +=bird_drop_velocity
	bird_drop_velocity +=GRAVITY


	tube1_x = tube1_x - TUBE_VELOCITY
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY


	if tube1_x < -50:
		tube1_x = 550
		tube1_pass=False
		level_pass=False
		tube1_height=randint(100,400)
	if tube2_x < -50:
		tube2_x = 550
		tube2_pass=False
		level_pass=False
		tube2_height=randint(100,400)
	if tube3_x < -50:
		tube3_x = 550
		tube3_pass=False
		level_pass=False
		tube3_height=randint(100,400)
	score_text = font.render("Score:"+str(score) , True,WHITE)
	screen.blit(score_text,(0,0))
	level_text = font.render("Level:"+str(level) , True,WHITE)
	screen.blit(level_text,(300,0))

	if tube1_x +TUBE_WIDTH <= BIRD_X and tube1_pass==False:
		score+=1
		tube1_pass=True
		level_pass=True

	if tube2_x +TUBE_WIDTH <= BIRD_X and tube2_pass==False:
		score+=1
		tube2_pass=True
		level_pass=True

	if tube3_x +TUBE_WIDTH <= BIRD_X and tube3_pass==False:
		score+=1
		tube3_pass=True
		level_pass=True



	if score !=0 and score % 3 ==0 and level_pass ==False:
		level +=1
		TUBE_VELOCITY +=ms
		level_pass=True


	for tube in[tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv]:
		if bird_rect.colliderect(tube):
			TUBE_VELOCITY =0
			bird_drop_velocity =0
			pausing=True
			gameover_text = font.render("Game Over",True,WHITE)
			screen.blit(gameover_text,(180,280))
			gamscore_text = font.render("Score:"+str(score) +"\n Level"+str(level),True,WHITE)
			screen.blit(gamscore_text,(150,310))


		if BIRD_Y >600:
			TUBE_VELOCITY =0
			bird_drop_velocity =0
			pausing=True
			gameover_text = font.render("Game Over",True,WHITE)
			screen.blit(gameover_text,(150,280))
			gamscore_text = font.render("Score:"+str(score)+"\n Level"+str(level),True,WHITE)
			screen.blit(gamscore_text,(150,310))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if pausing:
					BIRD_Y = 400
					TUBE_VELOCITY =3
					tube1_x = 600
					tube2_x=800
					tube3_x = 1000
					score = 0
					level =1
					pausing = False

				bird_drop_velocity=0
				bird_drop_velocity -=5


	pygame.display.flip()

pygame.quit()
