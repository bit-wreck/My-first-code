import pygame,random

pygame.init()

# Ukuran screen
WIDTH = 720
HEIGHT = 480
RED = (255,0,0)
GREEN = (0,210,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BACKGROUND_COLOR = (0,0,0)

# Ukuran Player
Player_size = 50
Player_pos = [WIDTH/2, HEIGHT-2*Player_size]
enemy_size = 50
enemy_pos =[random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

# utilities
SPEED = 7
skor = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("Consolas", 35)
pygame.display.set_caption("GAME PERTAMA GW NIH")

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()


bg = pygame.image.load("Background Game.jpg").convert()

# Nge set tombol
def pause() :
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					paused = False	

		# message_to_screen("paused", black , -100 , size="large")
		# message_to_screen("PRESS S TO CONTINUE",black , 25)d
		# # clock.tick(5) 

# Nyalain Background music
pygame.mixer.music.load("Alan Walker Lily.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def drop_enemy(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0, WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos , y_pos])


def draw_enemy(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, GREEN ,(enemy_pos[0], enemy_pos [1], enemy_size, enemy_size))

 # Ngatur skor disini, tapi masih nge bug 
def update_enemy_positions(enemy_list, skor):
	for idx , enemy_pos in enumerate(enemy_list,):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else: enemy_list.pop(idx)
		skor += 0
	return skor
			  	

def collision_check(enemy_list, Player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, Player_pos):
			return True
	return False		

def detect_collision(Player_pos, enemy_pos):
	p_x = Player_pos[0]
	p_y = Player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + Player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + Player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False
		
# Game loop jangan di otak atik
while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				x = Player_pos [0]
				y = Player_pos [1]

				if event.key == pygame.K_LEFT:
					x -= Player_size
				elif event.key == pygame.K_RIGHT:
					x += Player_size
				elif event.key == pygame.K_p:
					pause()


				Player_pos =[x,y]			

		screen.fill(BACKGROUND_COLOR)
		screen.blit(bg,[0,0])

		drop_enemy(enemy_list)
		skor = update_enemy_positions(enemy_list, skor)
		
		text = "skor:" + str(skor)
		label = myFont.render(text, 1, YELLOW)
		screen.blit(label, (WIDTH-200, HEIGHT-40))

		
		if collision_check(enemy_list, Player_pos):
			game_over = True
			break

		draw_enemy(enemy_list)		
		pygame.draw.rect(screen, RED, (Player_pos[0], Player_pos[1] , Player_size, Player_size))		

		clock.tick(30)

		pygame.display.update()


