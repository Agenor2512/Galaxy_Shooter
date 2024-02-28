import pygame
from pygame.sprite import Group

# Classe représentant un projectile
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/projectile_ally.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 40
        
    def remove_shoots(self):
        #supprimer le projectile (en dehors de l'écran)
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        for enemy in self.player.game.check_collision(self, self.player.game.all_enemies):
            self.remove_shoots()
            enemy.damage(self.player.attack)
        
        if self.rect.x > 1080:
            self.remove_shoots()
            print("Projectile supprimé !")