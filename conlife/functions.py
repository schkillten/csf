import pygame, buttons

# This is the functin that gives the initial state of the grid
# I got tired of manually changing each point in the grid for the inital state
# So now I can just save a file in the text_files/ directory
# and just draw the figure with 0's and add a "-" at the end of each ilne
# I did this because i was having a problem with python keeping the "\n"
# when i put it through a loop so i needed a way to know it was the end of the line
# once it opens the file, I put all the text into one variable, "read" then iterate
# through the whole file, if a "0" comes up, it changes that grid[x][y] position into a "1"
# In order to keep track of where to add it into the grid, i just initialized an x and y at 0
# Then whenever the "-" was reached i would increase the x by 1 since that represented a new line
# the y was reset at that point as if the grid was moved back to the first point of the new line
def getInitialState(grid, text_file):
	text_file = "text_files/" + text_file
	open_file = open(text_file, "r")
	x = 0
	y = 0
	grid_size = len(grid)
	read = open_file.read()
	total = 0
	for line in read:

		if line == "0":
			# this is just here to count the total zeros to make sure I was getting the correct total
			total += 1
			grid[x][y] = "1"

		y += 1
		if line == "-":
			x += 1
			y = 0

		if y > grid_size - 1:
			y = 0
		if x > grid_size - 1:
			x = 0
	open_file.close()

# generates a blank grid a list of lists depending on the size thats input
def makeGrid(grid_size):
	grid = []

	for i in range(grid_size):
		grid.append(["0"] * grid_size)

	return grid

# If you want to print the grid onto the terminal this is the function you would use
# just prints a zero where there is a 1 in the grid, and if there is nothing, then it prints a space
# and at the end of each row it prints a new line with the empty print statement
def printGrid(grid):

	for row in grid:
		for l in row:
			if l == "1":
				#sys.stdout.write(u'\u2588'),
				print "0",
			else:
				#sys.stdout.write(' '),
				print " ",
		print

# This is a private function, its used inside of the checkRule function
# The checkRule function iterates through the whole grid
# and for each element in the grid, it is passed into the neighborsCount
# function, as an (x,y) position, then it checks each 8 neighbors, and
# adds it into the total, that total is what determines what the rule
# that we need to use is.

def neighborsCount(grid, x, y):

	#print "start"
	#print "pos: (%d, %d)" % ( x, y)
	total = 0
	size = len(grid) - 1
	#	    U  D  R  L U/R  U/L D/R D/L (Up Down Right Left Up/Right Up/Left Down/Right Down/Left)
	x_check = [-1, 1, 0, 0, -1, -1, 1, 1]
	y_check = [0, 0, 1, -1, 1, -1, 1, -1]

	for i in range(8):
		# Thiese checks are the edge cases for when the neighbors are outside of the grid
		# it is just assumed to be zero
		if (x + x_check[i]) < 0:
			total += 0
		elif (x + x_check[i]) > size:
			total += 0
		elif (y + y_check[i]) < 0:
			total += 0
		elif (y + y_check[i]) > size:
			total += 0
		else:
			check_position = int(grid[x + x_check[i]][y + y_check[i]])
			total += check_position
	return total

# This function determines what rule to apply to each cell in the grid
# after passing each cell and checking how many total neighbors it has,  it determines
# which cells live or die, the ones that live, are moved into a list
# the ones that die, move into another seperate list since we have to wait
# until the end to update the list otherwise we would alter the other cells
# then we take those lists and just iterate through it changing them to 0's or 1's
def checkRule(grid):
	live_cells = []
	dead_cells = []
	size = len(grid)

	for x in range(size):
		for y in range(size):
			value = int(grid[x][y])
			total_neighbors = neighborsCount(grid, x , y)
			# first checks if the cells are living
			if grid[x][y] == "1":
				# checks if its under populated
				if total_neighbors < 2:
					dead_cells.append((x,y))
					#print "Under population: (%d, %d)" % (x,y)
				# checks if its over populated
				elif total_neighbors > 3:
					dead_cells.append((x,y))
					#print "Over population: (%d, %d)" % (x,y)
				# checks if it is between 2 or 3 to keep alive
				else:
					live_cells.append((x,y))
					#print "Just right population: (%d, %d)" % (x,y)
			else:
				# checks to see if the cell is dead and needs to be turned to a living cell
				if total_neighbors == 3:
					live_cells.append((x,y))
					#print "Cell reproduction: (%d, %d)" % (x,y)

	for i in range(len(live_cells)):
		grid[live_cells[i][0]][live_cells[i][1]] = "1"
	for i in range(len(dead_cells)):
		grid[dead_cells[i][0]][dead_cells[i][1]] = "0"


# x and y are there only for where the grid appears in the pop up window
# width and height control the size of each indivisual cell yoou can make them larger
# but make sure width and height are the same number for an even sized cell (square)
# grid is what controls the size of the grid shown

# The pygame library has x left/right and y up/down (different then how i store my points )
# so i swapped the l and h otherwise the shape would be sideways
# the file name is taken in just to change the caption at the top of the window
# I'm not sure why I named this function newGrid when it has nothing to do with it
# But basically it is what generates the Graphical part using pygame
def newGrid(x,y,width,height,grid, file_name):

	window = pygame.display.set_mode((1920,1080))

	pygame.display.set_caption("Conway's game of life" +"-" + file_name)


	grid_size = len(grid)
	# The x_pos and y_pos is somewhat of a copy so I don't actually lose the original x,y positions
	y_pos = y
	x_pos = x

	background_color = (103,17,117)
	#cell_color = (0,0,0)
	cell_color = (56,232,14)

	for l in range(grid_size):
		for h in range(grid_size):

			if grid[h][l] == "1":
				pygame.draw.rect(window, (cell_color), ((x_pos, y_pos), (width, height)))
			elif grid[h][l] == "0":
				pygame.draw.rect(window,(background_color), ((x_pos, y_pos), (width, height)))

			y_pos += float(width + height) / float(2) + 5

		y_pos = y
		x_pos += float(width + height) / float(2) + 5
	pygame.display.flip()

def makeButton(window, color, pos, size):
	return pygame.draw.rect(window, color, (pos, size))
