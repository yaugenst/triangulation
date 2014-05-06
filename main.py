import pygame, sys
import triangulate
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('art gallery problem')
screen.fill(WHITE)

myfont = pygame.font.SysFont("Lucida Console", 12)
label = myfont.render("finish (ENTER), triangulate (C), clear (BACKSPACE), load preset (L), exit (ESCAPE)", 1, BLACK)
screen.blit(label, (10, WINDOW_HEIGHT - 20))

clock = pygame.time.Clock()

preset = [(264, 29), (373, 26), (482, 73), (510, 183), (486, 325), (408, 394), (294, 417), (169, 327), (147, 212), (205,123), (358, 108), (421, 166), (412, 245), (321, 311), (234, 288), (223, 217), (288, 158), (349, 186), (331, 254), (367, 233), (383, 152), (293, 136), (215, 166), (198, 264), (317, 359), (400, 329), (479, 212), (443, 106), (310, 76), (255, 72)]

lock = 0
pts = []

### MAIN LOOP

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
			pygame.quit()
			sys.exit()
			
		if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and lock != 1:
			mpos = pygame.mouse.get_pos()
			pts.append(mpos)
			pygame.draw.circle(screen, BLACK, mpos, 3)
			if len(pts) > 1:
				pygame.draw.aaline(screen, BLUE, pts[len(pts) - 2], mpos)
				
		if event.type == KEYDOWN and pygame.key.get_pressed()[K_RETURN] and lock != 1 and len(pts) > 2:
			pygame.draw.aaline(screen, BLUE, mpos, pts[0])
			lock = 1
			
		if event.type == KEYDOWN and pygame.key.get_pressed()[K_l] and lock != 1:
			pts = preset[:]
			lock = 1
			for x in preset:
				pygame.draw.circle(screen, BLACK, x, 3)
			pygame.draw.aalines(screen, BLUE, True, preset)
			
		if event.type == KEYDOWN and pygame.key.get_pressed()[K_c] and lock == 1:
			tri = []
			plist = pts[::-1] if triangulate.IsClockwise(pts) else pts[:]
			while len(plist) >= 3:
				a = triangulate.GetEar(plist)
				if a == []:
					break
				tri.append(a)
			pygame.draw.polygon(screen, GREEN, tri[-1], 4)
			for x in tri:
				pygame.draw.polygon(screen, RED, x, 1)
			
		if event.type == KEYDOWN and pygame.key.get_pressed()[K_BACKSPACE]:
			screen.fill(WHITE)
			pts = []
			lock = 0
			screen.blit(label, (10, WINDOW_HEIGHT - 20))
	pygame.display.update()