import pygame
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()

width = 1200
height = 871
rows = 40

numberOne = pygame.image.load('numbers/number_1.png')
numberOne = pygame.transform.scale(numberOne, (300, 300))
rect = numberOne.get_rect()
rect = rect.move(300, 300)
numberTwo = pygame.image.load('numbers/number_2.png')
numberThree = pygame.image.load('numbers/number_3.png')



def message_box(subject, content):
	root = tk.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	messagebox.showinfo(subject, content)
	try:
		root.destroy()
	except:
		pass

def drawGrid(width, height, rows, surface):
	sizeBetween = width // rows

	x = 0
	y = 0

	for i in range(rows+1):
		if sizeBetween*10 <= x <= sizeBetween*30:
			pygame.draw.line(surface, (0, 0, 0), (x,0), (x, height))
			x = x + sizeBetween
		else:
			x = x + sizeBetween
		pygame.draw.line(surface, (0, 0, 0), (sizeBetween*10,y), (width-sizeBetween*10, y))
		y = y + sizeBetween
	surface.blit(numberOne, rect)

def redrawWindow(surface):
	global width, height, rows
	surface.fill((255,255,255))
	drawGrid(width, height, rows, surface)
	pygame.display.update()


def main():
	global width, height
	pygame.display.set_caption("Matching Numbers")
	win = pygame.display.set_mode((width, height))
	run = True
	clock = pygame.time.Clock()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				if rect.collidepoint(x, y):
					print('clicked on image')



		pygame.time.delay(50)
		clock.tick(10)
		redrawWindow(win)

	pygame.quit()

main()