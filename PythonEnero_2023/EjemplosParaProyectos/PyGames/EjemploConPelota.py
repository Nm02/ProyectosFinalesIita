import sys,pygame
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 1000, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("Juego BALL")
# Inicializamos variables
width, height = 1000, 600
speed = [1, 1]
white = 255, 255, 255
# Crea un objeto imagen pelota y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.move_ip(height/2+ballrect.height,width/2-ballrect.width)
# Crea un objeto Player1 y obtengo su rectángulo
Player1 = pygame.image.load("rectanguloNegro.png")
Player1rect = Player1.get_rect()
# Crea un objeto Player2 y obtengo su rectángulo
Player2 = pygame.image.load("rectanguloNegro.png")
Player2rect = Player2.get_rect()
# Pongo el player1 en el centro de la pantalla
Player1rect.move_ip(0, (height/2)-(Player1.get_width()/2))
# Pongo el player1 en el centro de la pantalla
Player1rect.move_ip(width-(Player2.get_width()), (height/2)-(Player2.get_height())/2)
# Comenzamos el bucle del juego
run=True
while run:
	# Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
	pygame.time.delay(2)
	# Capturamos los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir de la ventana, terminamos
		if event.type == pygame.QUIT: run = False
	# Compruebo si se ha pulsado alguna tecla
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		Player1rect=Player1rect.move(0, -1)
	if keys[pygame.K_DOWN]:
		Player1rect=Player1rect.move(0, 1)
	if keys[pygame.K_w]:
		Player2rect=Player2rect.move(0,-1)
	if keys[pygame.K_s]:
		Player2rect=Player2rect.move(0,1)
	# Compruebo si hay colisión
	if Player1rect.colliderect(ballrect):
		speed[0] = - speed[0]
		speed[1] = - speed[1]
	if Player2rect.colliderect(ballrect):
		speed[0] = - speed[0]
		speed[1] = - speed[1]
	# Muevo la pelota
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[1] = -speed[1]
	#Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
	# screen.fill(white)
	screen.blit(ball, ballrect)
	screen.blit(Player1,Player1rect)
	screen.blit(Player2,Player2rect)
	pygame.display.flip()
# Salgo de pygame
pygame.quit()