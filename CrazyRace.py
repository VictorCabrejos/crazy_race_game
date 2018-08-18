import pygame
import time

#Initiation function
pygame.init()

#Game's width and height
#Tuple: 800 x 600

display_width = 800
display_height = 600
car_width = 70

#RGB Colors
black = (0  , 0   , 0)
white = (255, 255 , 255)
red   = (255, 0   , 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))


#Game's Title
pygame.display.set_caption('Crazy Race')

#Define the game's clock

clock = pygame.time.Clock()

# car image
carImg = pygame.image.load('car.png')

def car(x,y):
	"""
	function to display the car in location
	 x and y  

	"""
	# Need Tuple because second argument is a single parameter
	gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):

	# second parameter of .render is for antialiasing
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):

	largeText = pygame.font.Font('freesansbold.ttf', 115)
	textSurf, textRect = text_objects(text, largeText)
	textRect.center = ( (display_width/2), (display_height/2))
	gameDisplay.blit(textSurf, textRect)

	pygame.display.update()
	time.sleep(2)
	game_loop()
	

def crash():
	message_display('You Crashed')

def game_loop():

	x = (display_width * 0.45)
	y = (display_height * 0.82)

	x_change = 0


	#Game Loop = logic for the game
	#the only thing that will break us out of the 
	#game loop is if we crash

	gameExit = False

	while not gameExit:

		# list of events per frame per second
		for event in pygame.event.get():

			# If it's a quit, then we quit
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			# If there is keypress at all
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5

			# If the key has been released
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change 

		# background color
		gameDisplay.fill(white)

		# show car
		car(x,y)

		# Calculating boundaries to exit the game
		if x > (display_width - car_width) or x < -14:
			crash()

		#update the entire screem
		pygame.display.update()

		# Frames per second
		clock.tick(60)


game_loop()
pygame.quit()
quit()



