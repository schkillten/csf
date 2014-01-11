from time import sleep
import sys, pygame
from functions import makeGrid, printGrid, checkRule, neighborsCount, getInitialState, newGrid, makeButton

pygame.init()
window = pygame.display.set_mode((1024, 768))
button_orig = (25,25)
button_size = (200,200)
button_color = (56,232,14)

button1_pos = button_orig
button2_pos = (button1_pos[0], (button1_pos[1] + button_size[1] + 10))
button3_pos = (button2_pos[0], (button2_pos[1] + button_size[1] + 10))

mouse_over_color = (103,17,117)


font_style = pygame.font.SysFont("monospace", 20)
label_1 = font_style.render("<-- Left click for gun, Right click for a stick figure ", 1, (255,255,0))
label_2 = font_style.render("<-- Left click for lexicon, Right click for Diamondish thing", 1, (255,255,0))
label_3 = font_style.render("<-- Left click for a puffer train, Right click for a random thing", 1, (255,255,0))

window.blit(label_1, (button_orig[0] + button_size[0] + 10, button_orig[1] + button_size[0]/2.0))
window.blit(label_2, (button2_pos[0] + button_size[0] + 10, button2_pos[1] + button_size[0]/2.0))
window.blit(label_3, (button3_pos[0] + button_size[0] + 10, button3_pos[1] + button_size[0]/2.0))


### Conways Game of life!
def main():
	picking = True
	while picking:




		button1 = makeButton(window, (button_color), (button1_pos), (button_size))
		button2 = makeButton(window, (button_color), (button2_pos), (button_size))
		button3 = makeButton(window, (button_color), (button3_pos), (button_size))

		# This is where i'm handling a few events, was too lazy to put it anywhere else
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

			if event.type == pygame.MOUSEMOTION:
				if button1_pos[0] <= event.pos[0] <= button1_pos[0] + button_size[0] and button1_pos[1] <= event.pos[1] <= button1_pos[1] + button_size[1]:
					print event.pos, "button1"
					button1 = makeButton(window, (mouse_over_color), (button1_pos), (button_size))

				if button2_pos[0] <= event.pos[0] <= button2_pos[0] + button_size[0] and button2_pos[1] <= event.pos[1] <= button2_pos[1] + button_size[1]:
					print event.pos, "button2"
					button2 = makeButton(window, (mouse_over_color), (button2_pos), (button_size))

				if button3_pos[0] <= event.pos[0] <= button3_pos[0] + button_size[0] and button3_pos[1] <= event.pos[1] <= button3_pos[1] + button_size[1]:
					print event.pos, "button3"
					button3 = makeButton(window, (mouse_over_color), (button3_pos), (button_size))


			# mouse clicks left and right
			if event.type == pygame.MOUSEBUTTONUP:
				# left mouse click
				if event.button == 1:

					if button1_pos[0] <= event.pos[0] <= button1_pos[0] + button_size[0] and button1_pos[1] <= event.pos[1] <= button1_pos[1] + button_size[1]:
						text_file = "gun"
						picking = False

					if button2_pos[0] <= event.pos[0] <= button2_pos[0] + button_size[0] and button2_pos[1] <= event.pos[1] <= button2_pos[1] + button_size[1]:
						text_file = "lexicon"
						picking = False

					if button3_pos[0] <= event.pos[0] <= button3_pos[0] + button_size[0] and button3_pos[1] <= event.pos[1] <= button3_pos[1] + button_size[1]:
						text_file = "puffer"
						picking = False
				# right mouse click
				elif event.button == 3:
					if button1_pos[0] <= event.pos[0] <= button1_pos[0] + button_size[0] and button1_pos[1] <= event.pos[1] <= button1_pos[1] + button_size[1]:
                                        	text_file = "stick"
                                                picking = False

                               		if button2_pos[0] <= event.pos[0] <= button2_pos[0] + button_size[0] and button2_pos[1] <= event.pos[1] <= button2_pos[1] + button_size[1]:
                                                text_file = "diamondish"
                                                picking = False

                                       	if button3_pos[0] <= event.pos[0] <= button3_pos[0] + button_size[0] and button3_pos[1] <= event.pos[1] <= button3_pos[1] + button_size[1]:
                                                text_file = "random"
                                        	picking = False


			print event

			pygame.display.flip()


	#Controls the sizie of the grid
	# the larger the grid, the slower the game runs, I believe its because the way i check the points
	# I am checking every single cell every single time through when the grid is displayed
	grid = makeGrid(75)

	# Lets you pick from a list of text files I've made or you can save one and run it also
	#print "Text file name:"
	#text_file = raw_input(">>> ")
	# Appends "text_files/" to the beginning to go into the directory
	# may need to change depending on os
	getInitialState(grid, text_file)

	newGrid(25,25,15,15,grid, text_file)
	# just here to get a view of the initial state before it starts going through generations
	sleep(1)

	# Gives you a chance to view the initial state before running loop
	# infinite loop to keep making new generations

	while True:

		# Added this in just to mess around more with events
		# Its not working and I am assuming its due to me drawing multiple screens
		# so the new screen is just canceled out by the newGrid function
		# that creats a new screen with the updated generation
		# Am keeping it in here in hopes that i eventually fix the multiply screens issue
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

			if event.type == pygame.KEYUP:
				if event.key == 292:
					pygame.display.toggle_fullscreen()
				elif event.key == 49:
					pygame.display.set_mode((360,360))
				elif event.key == 50:
					pygame.display.set_mode((720,720))
				elif event.key == 51:
					pygame.display.set_mode((1024,720))
				elif event.key == 52:
					pygame.display.set_mode((1920, 1080))


		pygame.display.flip()
		checkRule(grid)
		#printGrid(grid)
		newGrid(25,25,15,15,grid, text_file)

main()
