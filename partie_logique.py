__AUTHOR__ = "Aboubacar DIAWARA"
__EMAIL__ = "abdpro909@gmail.com"
___DATE___ = "18/08/2020"

# Importation de modules
from render_connect4 import *
import random

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
		Check if the the column c of the grid g can be choosed by the player.
		:param c: (int)
		:param grid: (list) 
		:return: (bool)
			- True if the column is valid
			- False if not
		:CU: None

		Exemple
        >>> g = [[2,0,0,0],[1,0,0,2],[1,0,2,1]]
        >>> is_valide_column(1, g)
        True
        >>> is_valide_column(2, g)
        True
        >>> is_valide_column(0, g)
        False
	"""
	if not 0 <= c < nc(grid):
		return False
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
	#assert is_valide_column(c, g), "The colum must be valid"
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

        :Example:
        >>> g = initialize_grid(5, 5)
        >>> g1 = initialize_grid(5, 5)
        >>> modify_grid(g, 2, 4)
        >>> g1[4][4] = 2
        >>> g1 == g
        True
    """
	line = line_fall_disc(c, g)
	g[line][c] = p

def play_one_step(player:int, grid:list, c)->int:
	"""
		Allow to a player to play one step
	"""
	modify_grid(grid, player, c)
	 

## 2.3  Jeu à 2 joueurs
"""
For the game with 2 players, just repeat the steps 2.2 'play one step' and 2.1 'display a grid' beetween the 2 players.
For each iteration, we change the player (from player 1 to player 2 or conversely)
"""

def play(p1, p2, grid, is_ia_player1=False, is_ia_player2=False):
	"""
		run the gam beatween two humains players
		:param p1: (int) Player 1
		:param p2: (int) Player 2
		:param grid: (list) a grid
		:param is_ia_player1: (bool) determin if p1 is ia or human.
		:param is_ia_player2: (bool) determin if p2 is ia or human.
	"""
	is_ia = {1:is_ia_player1, 2:is_ia_player2}
	game_over = False
	has_played_player1 = False
	while not game_over:
		if not has_played_player1:
			player = p1
		elif has_played_player1:
			player = p2

		# if player is an IA, the computer will choose the column
		if is_ia[player]:
			c = ia_win(grid, player)
		else:
			c = enter_column(player, grid)
		r = line_fall_disc(c, grid)
		play_one_step(player, grid, c)
		game_over = is_win(grid, r, c, player)

		
		#show_grid(grid) # Affichage dans la console
		draw_connect4(grid) # Affichage graphique
		has_played_player1 = not has_played_player1 # permet d'alterner le tour entre les deux joueurs
	print("Player{} is the winner".format(player))


# 2.5 Winner
"""
	When the player p choose the column c, the disc will be in the column c at the line r.

	To know if player p is the winner, we must sheck if the column he/she/it choose has provoked an alignment of 4 disc.
	
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
		>>> grid3 = [[0, 0, 0, 0, 0],
                ...  [0, 0, 0, 1, 0],
                ...  [0, 0, 1, 2, 0],
                ...  [0, 1, 2, 1, 0],
                ...  [1, 2, 2, 2, 0]]
		>>> r, c = 1, 3
		>>> lc = [(r-3, c+3), (r-2, c+2),
		...  (r-1, c+1), (r, c), (r+1, c-1),
		...  (r+2, c-2), (r+3, c-3)]
		>>> is_align4(grid3, lc, 1)
		True
		>>> r, c = 2, 2
		>>> grid4 = [[1, 0, 0, 0, 0],
                ...  [2, 1, 0, 1, 0],
                ...  [1, 2, 1, 2, 0],
                ...  [2, 1, 2, 1, 0],
                ...  [1, 2, 2, 1, 0]]
                >>> lc = [(r-3, c-3), (r-2, c-2), (r-1, c-1), (r, c),(r + 1, c+1), (r+2, c+2), (r+3, c+3)]
		>>> is_align4(grid4, lc, 1)
		True
		
	"""		

	valor_consecutives_cases = ""
	for r, c in lc:
		#print((r, c), is_valid_case((r, c), g))
		if is_valid_case((r, c), g):
			valor = g[r][c]
			valor_consecutives_cases += str(valor)
	#print("Fin: " + str(p)*4 + "vs" + valor_consecutives_cases)
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
		>>> is_win(g, 0, 5, 1)
		True
		>>> 
	"""

	# list of horizontal cases
	lc_horiz = [(r, c-3), (r, c-2),
			    (r, c-1), (r, c), (r, c+1), (r, c+2), (r, c+3)]
	
 	# lists of vertical cases
	lc_diag1 = [(r-3, c-3), (r-2, c-2),
			    (r-1, c-1), (r, c), 
			    (r+1, c+1), (r+2, c+2), (r+3, c+3)]

	lc_diag2 = [(r+3, c-3),
			    (r+2, c-2), (r+1, c-1), (r, c), (r-1, c+1), 
			    (r-2, c+2), (r-3, c+3)]

    # list of vertical cases
	lc_vertic = [(r-3, c), (r-2, c), (r-1, c),
			     (r, c), (r+1, c), (r+2, c), (r+3, c)]

	return is_align4(g, lc_vertic, p) or is_align4(g, lc_diag1, p) or is_align4(g, lc_diag2, p) or is_align4(g, lc_horiz, p)

### 3 Implemantation of the IA
## 3.1: randomly shoot
def is_alea(grid:list)->bool:
	"""
		return randomly a valid column of th grid grid.
		:param grid: (list) a grid

		:Exemple:
		>>> g = initialize_grid(5, 5)
		>>> l = [0 <= is_alea(g) < nc(g) for i in range(100)]
		>>> not False in l
		True
	"""
	is_valid_col = False
	while not is_valid_col:
		c = random.randint(0, nc(grid))
		is_valid_col = is_valide_column(c, grid)
	return c

## 3.2 Analyse all the possibilities
# 3.2.1 Analyse of the victorie
"""
	To upgrade a little bit the decision of the computer, it'll try every column: it modify the grid by pllaying the column c, then it determin (with the function is_win) if it's a winning shoot.
	If that is the case, it'll choose the current column, otherwise it'll will check the next column.

	Let implemant the function unmove who allows to cancel a computer choose then the function ia_win(g, p)
"""

def unmove(grid:list, c:int)->None:
    """
    	modify the grid by removing the last disc who has been put in the column c.
        :param grid: (list) the grid
        :param c: (int) the column
        :return : (None) moify the grid

        :Example:
        >>> g = initialize_grid(5, 5)
        >>> g1 = initialize_grid(5, 5)
        >>> modify_grid(g, 2, 4)
        >>> g1[4][4] = 2
        >>> g1 == g
        True
        >>> unmove(g, 4)
        >>> g1[4][4] = 0
        >>> g1 == g
        True
    """
    r = line_fall_disc(c, grid)
    grid[r+1][c] = 0
        
def ia_win(g:list, p:int)->int:
	"""
		return the column who can help the computer to win the game, if that is not possible, it's return randomly one column.

		:param g: (list) a grid
		:param p: (int) a player
		:return : (int) a column
		:CU: None

		:Exemple:
		>>> g = [[1, 2, 2, 1, 1, 0, 1, 2]]
		>>> ia_win(g, 1)
		5
		>>> g =     [[1, 0, 0, 0, 0],
                ...  [2, 1, 0, 0, 0],
                ...  [1, 2, 1, 2, 0],
                ...  [2, 1, 2, 2, 0],
                ...  [1, 2, 2, 1, 2]]
        >>> ia_win(g, 1)
        3


	"""
	for c in range(nc(g)):
		if is_valide_column(c, g):
			r = line_fall_disc(c, g)
			play_one_step(p, g, c)

			#print(c, g, is_win(g, r, c, p))
			
			if is_win(g, r, c, p):
				unmove(g, c)
				return c
			else:
				unmove(g, c)

			#print(c, g, '\n')
	return is_alea(g)


# 3.2.2 Evaluation of the grid.
"""
	We're still improving the choose of the computer a little bit. This time for each column tried, the IA will analyse the entire grid (not just the victory around the square played).

	The analysis of the entire grid will result in a score. A hight score will correspond to a 'favorable grid' for an IA unlike a small score. So the IA will try therefore test each of the possible columns (as previously) and choose the one that leads to the most favorable grid (the one with the highest score).

	Now, let determinate the the function for the evaluation of the score. A possible strategie is to test all the quadruplets of the possible consecutives cases of the grid. 
"""

def score_quadruplet(grid, quadruplet:list, p)->int:
	"""
		return the score of the qudruplet
		:param grid: 
		:param quadruplet: (list) list of posiiton (r_i, c_i)
		:param p: (int) the IA
		:return : (int) the score of the quadruplet
		:CU:

		:Exemple:
		>>> g =     [[1, 0, 0, 0, 0],
                ...  [2, 1, 0, 0, 0],
                ...  [1, 2, 1, 2, 0],
                ...  [2, 1, 2, 2, 0],
                ...  [1, 2, 2, 1, 2]]
		>>> score_quadruplet(g, [(1, 2), (2, 2), (3, 2), (4, 2)], 1)
		0
		>>> score_quadruplet(g, [(4, 0), (3, 1), (2, 2), (1, 3)], 1)
		1000
	"""
	assert len(quadruplet) == 4, f"Attention, {quadruplet} n'est pas un quadruplet"
	list_pawns = [grid[r][c] for r, c in quadruplet]
	if list_pawns.count(1) > 0 and list_pawns.count(2) > 0 or list_pawns.count(0) == 4:
		return 0
	elif list_pawns.count(p) + list_pawns.count(0) == 4:
		if list_pawns.count(p) == 1:
			return 1
		elif list_pawns.count(p) == 2:
			return 10
		elif list_pawns.count(p) == 3:
			return 1000
		elif list_pawns.count(p) == 4:
			return 100000
	elif list_pawns.count(p) == 0 and list_pawns.count(0) < 4:
		if list_pawns.count(0) == 3:
			return -1
		elif list_pawns.count(0) == 2:
			return -10
		elif list_pawns.count(0) == 1:
			return -500

def evaluate_score_case(grid:list, case:tuple, p)->int:
	"""
		return the score of case in the grid.
		:param grid: (list) a grid.
		:param case: (tuple) position in the grid.
		:return: (int) the score of case.
		:param p: (int) the IA.
		:CU: Nothing

		:Exemple:
		>>> g =     [[1, 0, 0, 0, 0],
                ...  [2, 1, 0, 0, 0],
                ...  [1, 2, 1, 2, 0],
                ...  [2, 1, 2, 2, 0],
                ...  [1, 2, 2, 1, 2]]
        >>> evaluate_score_case(g, (0, 3), 2)
        20
	"""
	r, c = case
	number_lines = nr(grid)
	number_columns = nc(grid)
	score = 0
	if r + 3 <= number_lines: # vertical bottom quadruplet
		quadruplet = [(r, c), (r+1, c), (r+2, c), (r+3, c)]
		score += score_quadruplet(grid, quadruplet, p)
	if c + 3 <= number_columns: # horizontal right quadruplet
		quadruplet = [(r, c), (r, c+1), (r, c+2), (r, c+3)]
		score += score_quadruplet(grid, quadruplet, p)
	if c  >= 3 and r + 3 <= number_lines: # diagonal left quadruplet
		quadruplet = [(r, c), (r+1, c-1), (r+2, c-2), (r+3, c-3)]
		score += score_quadruplet(grid, quadruplet, p)
	if r + 3 <= number_lines and c + 3 <= number_columns: # diagonal right quadruplet
		quadruplet = [(r, c), (r+1, c+1), (r+2, c+2), (r+3, c+3)]
		score += score_quadruplet(grid, quadruplet, p)
	return score
	
def score_grille(g:list, p:int)->int:
	"""
		return the sum of the scores of the entire grid
	"""
	return sum(evaluate_score_case(g, (r, c), p) for r in g for c in r)





if __name__ == '__main__':
	import doctest, time
	doctest.testmod()

	grid = initialize_grid(10, 10)
	#play(1, 2, grid, is_ia_player1=True)
	###### Debugage
	"""
	grid3 = [[0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 1, 2, 0],
                [0, 1, 2, 1, 0],
                [1, 2, 2, 2, 0]]
	r, c = 2, 2
	lc = [(r-3, c-3), (r-2, c-2), (r-1, c-1), (r, c),(r + 1, c+1), (r+2, c+2), (r+3, c+3)]
	is_align4(grid3, lc, 2)
	"""
	###### Fin debugage
	

	wait_quit()
	time.sleep(5)
