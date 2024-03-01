import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            "tir": pygame.mixer.Sound("assets/sounds/pewpew_15.wav"),
            "start": pygame.mixer.Sound("assets/sounds/colorspectrum.wav"),
            "welcome": pygame.mixer.Sound("assets/sounds/mountains.flac"),
            "boss": pygame.mixer.Sound("assets/sounds/final_boss.flac"),
            "game_over": pygame.mixer.Sound("assets/sounds/game_over.wav"),
            "asteroid": pygame.mixer.Sound("assets/sounds/asteroid_fall.ogg"),
        }

    def play(self, name):
        self.sounds[name].set_volume(0.08)
        self.sounds[name].play()

    def stop(self, name):
        self.sounds[name].stop()