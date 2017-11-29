import pygame

helicopter_1 = pygame.image.load('sprites/helicopter_11.png')
helicopter_2 = pygame.image.load('sprites/helicopter_1.png')
helicopter_crash_1 = pygame.image.load('sprites/helicopter_crash_1.png')
helicopter_crash_2 = pygame.image.load('sprites/helicopter_crash_2.png')
helicopter_crash_3 = pygame.image.load('sprites/helicopter_crash_3.png')
helicopter_crash_4 = pygame.image.load('sprites/helicopter_crash_4.png')
helicopter_damaged_1 = pygame.image.load('sprites/helicopter_damaged1.png')
helicopter_damaged_2 = pygame.image.load('sprites/helicopter_damaged11.png')

enemy_helicopter_1 = pygame.image.load('sprites/enemy_helicopter1.png')
enemy_helicopter_2 = pygame.image.load('sprites/enemy_helicopter11.png')

boat = pygame.image.load('sprites/boat11.png')

helicopter_list = [helicopter_1, helicopter_2]
damaged_helicopter_list = [helicopter_damaged_1, helicopter_damaged_2]
enemy_helicopter_list = [enemy_helicopter_1, enemy_helicopter_2]

balloon = pygame.image.load('sprites/balloon1.png')

spaceship = pygame.image.load('sprites/spaceship1.png')

icon = pygame.image.load('sprites/icon1.png')
background = pygame.image.load('sprites/background.png')
cloud = pygame.image.load('sprites/cloud.png')

all_sprites = [helicopter_1, helicopter_2, helicopter_damaged_1, helicopter_damaged_2, enemy_helicopter_1,
               enemy_helicopter_2, helicopter_crash_1, helicopter_crash_2, helicopter_crash_3, helicopter_crash_4,
               boat, balloon, spaceship, icon, background, cloud]


