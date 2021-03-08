import pygame
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()

width = 1200
height = 871
rows = 40

numOne = pygame.image.load('numbers/number_1.png')
numTwo = pygame.image.load('numbers/number_2.png')
numThree = pygame.image.load('numbers/number_3.png')
numFour = pygame.image.load('numbers/number_4.png')
numFive = pygame.image.load('numbers/number_5.png')
numSix = pygame.image.load('numbers/number_6.png')

numOne = pygame.transform.scale(numOne, (30, 30))
numTwo = pygame.transform.scale(numTwo, (30, 30))
numThree = pygame.transform.scale(numThree, (30, 30))
numFour = pygame.transform.scale(numFour, (30, 30))
numFive = pygame.transform.scale(numFive, (30, 30))
numSix = pygame.transform.scale(numSix, (30, 30))

rectOne = numOne.get_rect()
rectTwo = numTwo.get_rect()
rectThree = numThree.get_rect()
rectFour = numFour.get_rect()
rectFive = numFive.get_rect()
rectSix = numSix.get_rect()

# rectOne = rectOne.move(300, 0)
# rectTwo = rectTwo.move(330, 0)
# rectThree = rectThree.move(360, 0)
# rectFour = rectFour.move(390, 0)
# rectFive = rectFive.move(420, 0)
# rectSix = rectSix.move(450, 0)

# numberList = [numOne, numTwo, numThree, numFour, numFive, numSix]
# rectList = [rectOne, rectTwo, rectThree, rectFour, rectFive, rectSix]

gridNumbers = []

for column in range(29):
	temp = []
	for row in range(20):
		temp.append(random.randrange(1, 7))
		if row == 19:
			gridNumbers.append(temp)

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

def drawRect(x, y, number):
	if number == 1:
		rectOne = numOne.get_rect()
		rectOne = rectOne.move(x, y)
		return rectOne
	elif number == 2:
		rectTwo = numTwo.get_rect()
		rectTwo = rectTwo.move(x, y)
		return rectTwo
	elif number == 3:
		rectThree = numThree.get_rect()
		rectThree = rectThree.move(x, y)
		return rectThree
	elif number == 4:
		rectFour = numFour.get_rect()
		rectFour = rectFour.move(x, y)
		return rectFour
	elif number == 5:
		rectFive = numFive.get_rect()
		rectFive = rectFive.move(x, y)
		return rectFive
	elif number == 6:
		rectSix = numSix.get_rect()
		rectSix = rectSix.move(x, y)
		return rectSix

def drawNumbers(surface, gridNumbers):
	x = 300
	y = 0
	count_x = 0
	count_y = 0
	for column in gridNumbers:
		for row in column:
			if row == 1:
				surface.blit(numOne, drawRect(x + (30*count_x), y + (30*count_y), 1))
				count_x += 1
			elif row == 2:
				surface.blit(numTwo, drawRect(x + (30*count_x), y + (30*count_y), 2))
				count_x += 1
			elif row == 3:
				surface.blit(numThree, drawRect(x + (30*count_x), y + (30*count_y), 3))
				count_x += 1
			elif row == 4:
				surface.blit(numFour, drawRect(x + (30*count_x), y + (30*count_y), 4))
				count_x += 1
			elif row == 5:
				surface.blit(numFive, drawRect(x + (30*count_x), y + (30*count_y), 5))
				count_x += 1
			elif row == 6:
				surface.blit(numSix, drawRect(x + (30*count_x), y + (30*count_y), 6))
				count_x += 1
		count_x = 0
		count_y += 1


def redrawWindow(surface):
	global width, height, rows, gridNumbers
	surface.fill((255,255,255))
	drawGrid(width, height, rows, surface)
	drawNumbers(surface, gridNumbers)
	pygame.display.update()


def main():
	global width, height, gridNumbers
	pygame.display.set_caption("Matching Numbers")
	win = pygame.display.set_mode((width, height))
	run = True
	clock = pygame.time.Clock()
	count = 0

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				x = int(x/30) - 10
				y = int(y/30)
				if x < 0 or x > 20 or y < 0 or y > 29:
					continue
				if count%2 == 0:
					firstNum = gridNumbers[y][x]
					count += 1
					print(firstNum)
				else:
					secondNum = gridNumbers[y][x]
					count += 1
					print(secondNum)
				if count%2==0 and firstNum == secondNum:
					print("Correct")


		pygame.time.delay(50)
		clock.tick(10)
		redrawWindow(win)

	pygame.quit()

main()