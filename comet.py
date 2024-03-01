import pygame
import random

# Classe représentant une comète
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # définition de l'image de la comète
        self.image = pygame.image.load("assets/comet.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.origin_image = self.image
        self.angle = 0
        self.comet_event = comet_event

    def rotate(self):
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove_comets(self):
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets) == 0:
            # reset la barre à 0
            self.comet_event.reset_percent()

            if self.comet_event.counter < 2:
                # fait apparaître les monstres
                self.comet_event.game.spawn_enemy()
                self.comet_event.game.spawn_enemy()
            else:
                self.comet_event.game.spawn_boss()
                self.comet_event.game.sound_manager.stop("start")
                self.comet_event.game.sound_manager.play("boss")
        
    def fall(self, surface):
        self.rect.y += self.velocity
        self.rotate()
        
        # vérifie que la comète touche le sol
        if self.rect.y >= surface.get_height():
            self.remove_comets()

            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("Joueur est touché!")
            self.remove_comets()
            self.comet_event.game.player.damage(20)
            