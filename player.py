import pygame
from projectile import Projectile

# Classe représentant notre joueur (le vaisseau allié)
class Player(pygame.sprite.Sprite):
    
    # définition des propriétés du joueur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 12
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.original_image = pygame.image.load('assets/spaceship_ally.png')
        self.image = pygame.transform.scale(self.original_image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()
        
    def update_health_bar(self, surface):
        
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y - 20, self.health, 5])
         
    
    # méthodes propres à la classe du joueur
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_enemies):
            self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
        
    def move_up(self):
        self.rect.y -= self.velocity
        
    def move_down(self):
        self.rect.y += self.velocity