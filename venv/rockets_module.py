import pygame

# Clase para los cohetes
class Rocket:
    def __init__(self, x, y):
        # Carga la imagen del cohete
        self.image = pygame.image.load('rocket.png')  # Asegúrate de que el archivo exista
        self.image = pygame.transform.scale(self.image, (20, 50))  # Ajusta el tamaño si es necesario
        self.rect = self.image.get_rect(center=(x, y))
    
    def move(self):
        self.rect.y += 5  # Velocidad de caída del cohete

    def draw(self, screen):
        screen.blit(self.image, self.rect)
