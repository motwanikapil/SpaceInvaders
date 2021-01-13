# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pygame
import random
import math
#initializing the pygame

pygame.init()

#creating the screen

screen = pygame.display.set_mode((800,600))

#adding background

background = pygame.image.load('background.png')

# whatever we do in the game window is known as event
# Quitting the game is also an event
# Also hovering mouse also is an event


#Title and Icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('alien2.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 20

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = random.randint(0,800)
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"
score = 0

 # Ready state means you can't see the bullet but its
# ready to fire
# fire state is when the bullet is fired
def player(x,y):
	screen.blit(playerImg, (x,y))
 # The following is the game loop

def enemy(x,y):
	screen.blit(enemyImg , (x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX , enemyY , bulletX, bulletY):
	distance = math.sqrt((math.pow((enemyX-bulletX),2))+(math.pow((enemyY-bulletY),2)))
	if distance < 27:
		return True
	else:
		return False

running = True
while running:
	screen.fill((0,0,0))

	#background image

	screen.blit(background, (0,0))

	# the following line returns all the events of pygame window

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# if keystroke is pressed check 
	# whether its right or left keystroke

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change  = -2

			if event.key == pygame.K_RIGHT:
				playerX_change = 2

			if event.key == pygame.K_SPACE:
				if bullet_state is "ready":
					# Get X coordinate of the spaceship
					bulletX = playerX
					fire_bullet(bulletX,bulletY)
			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0



	# RGB - Red , Green , Blue

	# we called the player method in while loop because we want
	# player to be shown always on the screen.
	playerX += playerX_change
	enemyX += enemyX_change
	#following lines are added to add boundaries to the game.

	# checking the boundaries of spaceship

	if playerX < 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	#checking the boundaries of enemy movement

	if enemyX < 0:
		enemyX_change = 0.6
		enemyY += enemyY_change
	elif enemyX >= 736:
		enemyX_change = -0.6
		enemyY += enemyY_change

	# fire bullet
	if bulletY <= 0:
		bulletY = 480
		bullet_state = "ready"

	if bullet_state is "fire":

		fire_bullet(bulletX,bulletY)
		bulletY -= bulletY_change

	#collision
	collision = isCollision(enemyX,enemyY,bulletX , bulletY)
	if collision:
		bulletY = 480
		bullet_state = "ready"
		score += 1
		print(score)

	player(playerX,playerY)
	enemy(enemyX , enemyY)
	pygame.display.update()