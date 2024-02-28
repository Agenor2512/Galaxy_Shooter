import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.original_image = pygame.image.load('assets/spaceship_allier.png')
        self.image = pygame.transform.scale(self.original_image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
        
    def move_up(self):
        self.rect.y -= self.velocity
        
    def move_down(self):
        self.rect.y += self.velocity