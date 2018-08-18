import pygame

#Initiation function
pygame.init()

#Game's width and height
#Tuple: 800 x 600

display_width = 800
display_length = 600

#RGB Colors
black = (0  , 0   , 0)
white = (255, 255 , 255)
red   = (255, 0   , 0)

gameDisplay = pygame.display.set_mode((display_width, display_length))


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

x = (display_width * 0.45)
y = (display_length * 0.82)

x_change = 0


#Game Loop = logic for the game
#the only thing that will break us out of the 
#game loop is if we crash

crashed = False

while not crashed:

	# list of events per frame per second
	for event in pygame.event.get():

		# If it's a quit, then we quit
		if event.type == pygame.QUIT:
			crashed = True

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

	#update the entire screem
	pygame.display.update()

	# Frames per second
	clock.tick(60)


pygame.quit()
quit()



