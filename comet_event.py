import pygame
from comet import Comet

# créer une classe pour gérer cet evenement
class CometFallEvent:
    
    # lors du changement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 20
        self.game = game
        self.fall_mode = False
        self.counter = 0

        # groupe de sprites pour stocker les comètes
        self.all_comets = pygame.sprite.Group()
    
    # permet d'ajouter un pourcentage à la barre en contrôlant sa vitesse de progression
    def add_percent(self):
        self.percent +=  self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0
       
    # vérifie si la barre est remplie 
    def is_full_loaded(self):
        return self.percent >= 100
    
    # ajoute les comètes dans leur groupe de sprites
    def comet_fall(self):
        # permet d'ajouter plusieurs comètes
        for i in range(1, 10):
            self.all_comets.add(Comet(self))
    
    # active l'évènement grâce au booléen fall_mode
    def attempt_fall(self):
        self.counter += 1

        if self.is_full_loaded() and len(self.game.all_enemies) == 0:
            print("Pluie de cometes !!")
            self.comet_fall()
            self.fall_mode = True
        
    def update_event_bar(self, surface):
        
        # appel à la méthode d'ajout des pourcents
        self.add_percent()
        
        # barre noire (en arrière plan)
        pygame.draw.rect(surface, (105, 105, 105), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenetre
            10 # epaisseur de la barre
        ])
        
        # barre bleue (jauge d'event)
        pygame.draw.rect(surface, (135, 206, 250), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la fenetre
            10 # epaisseur de la barre
        ])
    
        