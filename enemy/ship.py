import pygame
import random
from enemy.enemy import Enemy

class Ship(Enemy):
    def __init__(self, game):
        self.game = game
        self.loot_amount = 20
        self.set_loot_amount(self.loot_amount)
        original_image = pygame.image.load("assets/spaceship_enemy.png")
        max_health = 100
        attack = 0.3
        velocity = random.randint(1, 2)
        image = pygame.transform.scale(original_image, (180, 130))
        x = 1000 + random.randint(0, 300)
        y = 100 + random.randint(0, 300)
        super().__init__(game, max_health, attack, velocity, image, x, y)


    def damage(self, amount):
        super().damage(amount)
                
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            self.game.add_score(self.loot_amount)


        if self.game.comet_event.is_full_loaded():
            self.game.all_enemies.remove(self)

            # appel pour tenter de déclencher l'évènement
            self.game.comet_event.attempt_fall()
