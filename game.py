import pygame
from player import Player
from enemy.boss import Boss
from comet_event import CometFallEvent
from enemy.ship import Ship

class Game:
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_bosses = pygame.sprite.Group()
        self.comet_event = CometFallEvent(self)
        self.all_enemies = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_enemy()
        self.spawn_enemy()
        
    def game_over(self):
        # remettre le jeu à neuf, retirer les ennemies, remettre le joueur a 100 de vie et le jeu en attente
        self.all_enemies = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
    
    def update(self, screen):
        # intégration de l'image du joueur
        screen.blit(self.player.image, self.player.rect)
    
        self.player.update_health_bar(screen)
        
        # actualiser la barre d'evenement du jeu
        self.comet_event.update_event_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        for enemy in self.all_enemies:
            enemy.update_state(screen)
            
        for comet in self.comet_event.all_comets:
            comet.fall(screen)

        for boss in self.all_bosses:
            boss.update_state(screen)

        # intégration de l'image du projectile
        self.player.all_projectiles.draw(screen)

        # intégration de l'image de l'ennemi
        self.all_enemies.draw(screen)

        # intégration de l'image de la comète
        self.comet_event.all_comets.draw(screen)

        self.all_bosses.draw(screen)

        # Vérification des touches utilisées par le joueur et récupération de sa position
        # appels des méthodes permettant de déplacer le sprite du joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right() 

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
            
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height():
            self.player.move_down()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemy(self):
        enemy = Ship(self)
        self.all_enemies.add(enemy)

    def spawn_boss(self):
        self.all_bosses.add(Boss(self))