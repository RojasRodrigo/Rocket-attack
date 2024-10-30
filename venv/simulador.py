import pygame
import sys
import random  # Para generar posiciones aleatorias para los cohetes
from rockets_module import Rocket  # Importa la clase Rocket del módulo rockets

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulador de Vida')

# Carga la imagen de fondo y ajusta su tamaño a la pantalla
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Carga la música de fondo y los efectos de sonido
pygame.mixer.music.load('background_music.mp3')  # Música de fondo
pygame.mixer.music.play(-1)  # Reproducir en bucle infinito

impact_sound = pygame.mixer.Sound('explosion.mp3')  # Sonido de impacto

# Clase para el personaje
class Character:
    def __init__(self, x, y):
        self.image = pygame.image.load('avion.webp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Inicializa el personaje
character = Character(WIDTH // 2, HEIGHT // 2)

# Lista para almacenar los cohetes
rockets = []

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del personaje
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        character.move(5, 0)
    if keys[pygame.K_UP]:
        character.move(0, -5)
    if keys[pygame.K_DOWN]:
        character.move(0, 5)

    # Generar un nuevo cohete cada 30 frames
    if random.randint(1, 30) == 1:
        new_rocket = Rocket(random.randint(0, WIDTH - 10), 0)
        rockets.append(new_rocket)

    # Actualizar la posición de los cohetes
    for rocket in rockets[:]:
        rocket.move()
        if rocket.rect.colliderect(character.rect):
            print("¡Boom! El avión ha sido destruido.")
            impact_sound.play()  # Reproduce el sonido de impacto
            rockets.remove(rocket)  
        if rocket.rect.y > HEIGHT:
            rockets.remove(rocket)

    # Dibuja la imagen de fondo
    screen.blit(background, (0, 0))

    # Dibuja al personaje
    character.draw(screen)

    # Dibuja los cohetes
    for rocket in rockets:
        rocket.draw(screen)

    pygame.display.flip()

    # Controla la tasa de refresco
    pygame.time.Clock().tick(60)
