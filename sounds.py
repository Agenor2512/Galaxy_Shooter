import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            "tir": pygame.mixer.Sound("assets/sounds/pewpew_15.wav"),
            "start": pygame.mixer.Sound("assets/sounds/colorspectrum.wav"),
            "welcome": pygame.mixer.Sound("assets/sounds/mountains.flac"),
            "boss": pygame.mixer.Sound("assets/sounds/final_boss.ogg"),
            "game_over": pygame.mixer.Sound("assets/sounds/game_over.wav"),
            "asteroid": pygame.mixer.Sound("assets/sounds/asteroid_fall.ogg"),
        }

    def play(self, name, loops=0):
        self.sounds[name].set_volume(0.08)
        self.sounds[name].play(loops=loops)

    def stop(self, name):
        self.sounds[name].stop()