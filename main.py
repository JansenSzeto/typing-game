import pygame
import datetime
import random

pygame.init()

SCREENWIDTH = 1000
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("TYPE")
icon = pygame.image.load("keyboard.png")
pygame.display.set_icon(icon)
font = pygame.font.Font('RobotoMono-VariableFont_wght.ttf', 32)
BACKGROUND_COLOR = (15, 31, 44)
TEXT_COLOR = (86, 195, 183)

running = True
key = ""
words = []
no_typed = 0

def choose_word():
	global words
	f = open("words.txt", "r")
	k = f.readlines()
	words = []
	for x in range(6):
		words.append((k[random.randrange(1, 1000)])[:-1])
	f.close()
choose_word()

def show_text():
	word_to_type = font.render(words[0], True, (255, 255, 255))
	screen.blit(word_to_type, (get_space(" ".join(words)), 270))
	text = font.render(" ".join(words[1:]), True, (TEXT_COLOR))
	screen.blit(text, (get_space_after(get_space(" ".join(words))), 270))

def get_space(a):
    space_between = (SCREENWIDTH-(len(a)*18))//2
    return space_between

def get_space_after(a):
    space_between = a+len(words[0])*18+18
    return space_between

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_TAB:
				choose_word()
			elif event.key == pygame.K_SPACE:
				if len(words) != 1:
					words.pop(0)
				else:
					choose_word()
	screen.fill(BACKGROUND_COLOR)
	show_text()
	pygame.display.update()

pygame.quit()