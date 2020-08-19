__AUTHOR__ = "Aboubacar DIAWARA"
__EMAIL__ = "aboubacardiawara909@gmail.com"
___DATE___ = "18/08/2020"

# Importation de modules
from render_connect4 import *

# Constantes

############################ Principale #############################


### 2  Setting up of the game Puissance 4

## 2.1 Representation of the board, initialization and display
'''
 - Do a function who initialize a grid with nr lines and nc columns,
	who does not contain any disc

 - Do a functions who nr() and nc who return respectively the number 	of lines and columns of a grid

 - Do a function who dispaly a grid with caracters.
  		For example red disc will be represented by 'O', yellow disc by 'X' and empty case by '-'.
 '''
def initialize_grid(nr:int, nc:int)->list:
	"""
		initialize a grid with nr lines and nc columns,	who does not contain any disc

		:param nr: (int) number of lines
		:param nc: (int) number of columns
		:return: (list) the grill
		:CU: nr > 0 and nc > 0

		:Exemple:
		>>> initialize_grid(5, 5)[0].__len__()
		5
		>>> initialize_grid(4, 3)[0].__len__()
		3
		>>> initialize_grid(3, 4).__len__()
		3
		>>> initialize_grid(0, 0)
		[]
	"""
	assert nr >= 0 and nc >= 0, "The grid cannot have nagative number of columns or lines"
	return [[0]*nc for i in range(nr)]

def nr(grid:list)->int:
	"""
		return the number of lines of grid
		:param grid: (list) a grid (list of list)
		:return: (int) number of lines
		:CU: nothing

		:Exemple:
		>>> g = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
		>>> nr(g)
		5
		>>> nr([])
		0

	"""
	return len(grid)

def nc(grid:list)->int:
	"""
		return the number of columns of grid
		:param grid: (list) a grid (list of list)
		:return: (int) number of columns
		:CU: 

		:Exemple:
		>>> g = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
		>>> nc(g)
		3
		>>> nc([])
		0

	"""
	if len(grid) == 0:
		return 0
	return len(grid[0])

def show_grid(grid:list)->None:
	"""
		dispaly a grid with caracters.
  		For example red disc will be represented by 'O', yellow disc by 'X' and empty case by '-'.
		:param gid: (list) list of list
		CU: Nothing

		Exemple:
		>>> g = [[2,0,0,0],[1,0,0,2],[1,0,2,1]]
		>>> show_grid(g)
		X---
		O--X
		O-XO
		====
		0123
	"""
	nc_grid = nc(grid)

	representation = {0:"-", 1:"O", 2:"X"}
	for line in grid:
		for column in line:
			print(representation[column], end="")
		print()
	print("="*nc_grid)
	for i in range(nc_grid):
		print(i, end='')
	#print("\n################################################\n")


## 2.2  Play one step
"""
	To play one step, you should ask the player one column.
	This one must be valid: We can't play if the column is full.
	To modify the grid according to the column we play, we must determine on witch line the disc will fall. 

	We then propose to decompose this step as follows:
		- Determine if a column c of grid g is a valid or not.
		- Ask to the player p to enter a valid column of g.
		- Determine the line r where the disc will fall in the 			column c of the grid g.
		- Modify the grid with the last dicq who the player insert.

	We will programm these functions this step :-)
"""

def is_valide_column(c:int, grid:list)->bool:
	"""
		Check if the the column c of the grid g can be shoosed by the player.
		:param c: (int)
		:param grid: (list) 
		:return: (bool)
			- True if the column is valid
			- False if not
		:CU: 0 <= c < nc(g)

		Exemple
        >>> g = [[2,0,0,0],[1,0,0,2],[1,0,2,1]]
        >>> is_valide_column(1, g)
        True
        >>> is_valide_column(2, g)
        True
        >>> is_valide_column(0, g)
        False
	"""
	assert 0 <= c < nc(grid)
	# create a liste of case of the column
	column = [ligne[c] for ligne in grid]
	# if the column is full, we won't find a 0 in. Otherwise, we'll
	return 0 in column

def enter_column(p:int, g:list):
    """
        Ask a player to enter a column while it isn't valid.
        :param p: (int)
        :param g: (int)
        :return: (int)
    """
    while True:
    	c = int(input("Player {} enter a valid column: ".format(p)))	
    	if is_valide_column(c, g):
    		return c

def line_fall_disc(c:int, g:list)->int:
	"""
		return the line of g where the discq will fall in the column c.
        :param c: (int) column
        :param g: (list) grid
        :return: (int) the line
        :CU: the column c must be valid

        Exemple
        >>> g = [[2,0,0,0],[1,0,0,2],[1,0,2,1]]
        >>> line_fall_disc(1, g)
        2
        >>> line_fall_disc(2, g)
        1
        >>> line_fall_disc(3, g)
        0
    """
	assert is_valide_column(c, g), "The colum must be valid"
	index_line = -1
	for line in g:
		contain_column = line[c]
		if contain_column == 0:
			index_line += 1
		else:
			break
	return index_line


def modify_grid(g:list, p:str, c:int)->None:
	"""
        Modify the grid g
        :param g: (list) the grid
        :param p: (str)	the player
        :param c: (int) the column
        :return: (None)
    """
	line = line_fall_disc(c, g)
	g[line][c] = p

def play_one_step(player:int, grid:list)->None:
	"""
		Allow to a player to play one step
	"""
	column = enter_column(player, grid)
	modify_grid(grid, player, column)

## 2.3  Jeu à 2 joueurs
"""
For the game with 2 players, just repeat the steps 2.2 'play one step' and 2.1 'display a grid' beetween the 2 players.
For each iteration, we change the player (from player 1 to player 2 or conversely)
"""

def play(player1, player2, grid):
	"""
		run the gam beatween two humains players
	"""
	has_played_player1 = False
	while True:
		if not has_played_player1:
			play_one_step(player1, grid)
		elif has_played_player1:
			play_one_step(player2, grid)
		
		#show_grid(grid) # Affichage dans la console
		draw_connect4(grid) # Affichage graphique

		has_played_player1 = not has_played_player1 # permet d'alterner le tour entre les deux joueurs


# 2.5 Winner
"""
	When the player p shoose the column c, the disc will be in the column c at the line r.

	To know if player p is the winner, we must sheck if the column he/she/it shoose has provoked an alignment of 4 disc.
	
	The alignment can be on the line r, on the column c or one of the twos the diagonals who contain the case (r, c).

	Whatever the direction, we'll consider 7 consecutivs cases from the 3 before (r,c) to the 3 next cases.

	For example, for the case (r, c), we will consider this list of case: 
	lc=[(r,c-3),(r,c-2),(r,c-1),(r,c),(r,c+1),(r,c+2),(r,c+3)].

	And we will check if we have at least 4 consecutives cases with p as valor. 

"""

def is_valid_case(case:tuple, grid:list)->bool:
	"""
		Check is case of grid is valid
		:param case: (tuple) the format of case (line, column)
		:param grid: (list) the grid
		:return : (bool) 
				  - True if the case is in the grid
				  - False if not
		:CU: Nothing

		:Exemple:
		>>> grid = initialize_grid(5, 5)
		>>> is_valid_case((0, 0), grid)
		True
		>>> is_valid_case((5, 5), grid)
		False
		>>> is_valid_case((-1, -1), grid)
		False
	"""
	r, c = case
	number_lines = nr(grid)
	number_columns = nc(grid)
	return 0 <= r < number_lines and 0 <= c < number_columns

def is_align4(g:list, lc:list, p:int)->bool:
	"""
		Check if at least 4 cases of the list of cases lc are aligned.

		:param g: (list) grid
		:param lc: (list) list of 7 cases
		:param p: (int) the player
		:return : (bool) 
				  - True if 4 cases of lc are aligned.
				  - False if not
		:CU: Nothing

		Exemple:
		>>> lc = [(0,-2),(0,-1),(0,0),(0,1),(0,2),(0,3),(0,4)]
		>>> grid = [[1, 2, 2, 1, 1, 1, 1, 2]]
		>>> is_align4(grid, lc, 1)
		False
		>>> is_align4(grid, lc, 1)
		False
		>>> grid2 = [[2, 2, 2, 2, 1, 1, 1, 2]]
		>>> is_align4(grid, lc, 1)
		False
		>>> is_align4(grid2, lc, 2)
		True
	"""		

	valor_consecutives_cases = ""
	for r, c in lc:
		if is_valid_case((r, c), g):
			valor = g[r][c]
			valor_consecutives_cases += str(valor)
	return str(p)*4 in valor_consecutives_cases


"""
	To check if the case (r, c) is a winning shot, we can call the function is_align4 by builing correctly for the nexts(4) events:
	- On the line r: from (r, c-3) to (r, c+3)
	- On one of the two diagonals: from (r-3, c-3) to (r+3, c+3)
	- And the same way, on the column c and the other diagonal.

	We can now implement the function is_win(g, r, p)
"""
def is_win(g:list, r:int, c:int, p:int)->bool:
	"""
		check if the case (r, c) is a winning shot
		:param g: (list) a grid
		:param r: (int) a line
		:param c: (int) a column
		:param p: (int) a player
		:return: (int) 
				 - True if after choosing this column, p will win.
				 - False if not
		:CU: Nothing

		:Exemple:
		>>> g = [[1, 2, 2, 1, 1, 1, 1, 2]]
		>>> is_win(g, 0, 6, 1)
		True
	"""

	# list of horizontal cases
	lc_horiz = [(r, c-3), (r, c-2), (r, c-1), (r, c), (r, c+1), (r, c+2), (r, c+3)]
	
 	# lists of vertical cases
	lc_diag1 = [(r-3, c-3), (r-2, c-2), (r-1, c-1), (r, c), (r + 1, c+1), (r+2, c+2), (r+3, c+3)]
	lc_diag2 = [(r-3, c+3), (r-2, c+2), (r-1, c+1), (r, c), (r+1, c-1), (r+2, c-2), (r+3, c-3)]

    # list of vertical cases
	lc_vertic = [(r-3, c), (r-2, c), (r-1, c), (r, c), (r+1, c), (r+2, c), (r+3, c)]

	return is_align4(g, lc_vertic, p) or is_align4(g, lc_diag1, p) or is_align4(g, lc_diag2, p) or is_align4(g, lc_horiz, p)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

	grid = initialize_grid(10, 10)
	play(1, 2, grid)

	wait_quit()