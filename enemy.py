import pygame
import random
from enemy_projectile import EnemyProjectile

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 2)
        self.all_enemies_projectiles = pygame.sprite.Group()
        self.original_image = pygame.image.load("assets/spaceship_enemy.png")
        self.image = pygame.transform.scale(self.original_image, (180, 130))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 100 + random.randint(0, 300)

    # méthodes propres à la classe du joueur
    def launch_enemies_projectile(self):
        self.all_enemies_projectiles.add(EnemyProjectile(self, self.game))
        
    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = 300 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            
            if self.game.comet_event.is_full_loaded():
                self.game.all_enemies.remove(self)

                # appel pour tenter de déclencher l'évènement
                self.game.comet_event.attempt_fall()
        
    def update_health_bar(self, surface):
        
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 60, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 60, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            
        else:
            self.game.player.damage(self.attack)

    
