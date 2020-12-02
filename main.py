import pygame
import datetime
import random
import translate

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
NUMBEROFWORDS = 6

running = True
key = ""
words = []
no_typed = 0
character = 0

def choose_word():
	global character
	global words
	f = open("words.txt", "r")
	k = f.readlines()
	words.append((k[random.randrange(1, 1000)])[:-1]+" ")
	f.close()
	character = 0
for q in range(NUMBEROFWORDS):
	choose_word()

def show_text():
	score_to_show = font.render(f"words: {no_typed}", True, (TEXT_COLOR))
	screen.blit(score_to_show, (20, 20))
	current = font.render(f"current: {words[0][character]}", True, (TEXT_COLOR))
	screen.blit(current, (20, 50))
	word_to_type = font.render(words[0], True, (255, 255, 255))
	screen.blit(word_to_type, (get_space("".join(words)), 270))
	text = font.render("".join(words[1:]), True, (TEXT_COLOR))
	screen.blit(text, (get_space_after(get_space("".join(words))), 270))

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
			elif translate.translate[event.key] == words[0][character]:
				if character+1 < len(words[0]):
					character+=1
				else:
					words.pop(0)
					choose_word()
					no_typed+=1
	screen.fill(BACKGROUND_COLOR)
	show_text()
	pygame.display.update()

pygame.quit()