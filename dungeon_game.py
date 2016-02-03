import random

CELLS =[(0, 0), (0, 1), (0 ,2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)]


# function for random location

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)
    
    if monster == door or monster == start or door == start:
        return get_locations()
        
    return monster, door, start


def move_player(player, move):

    # player is a tuple (x, y)
    
    x, y = player
    
    if move == "LEFT":
        y -= 1
    elif move == "RIGHT":
        y += 1
    elif move == "UP":
        x -= 1
    elif move == "DOWN":
        x += 1
        
    return x, y
 
def move_monster(monster):

    # monster is a tuple (x, y)
    
    x, y = monster
    
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    
    if monster[1] == 0:
        moves.remove("LEFT")
    if monster[1] == 2:
        moves.remove("RIGHT")
    if monster[0] == 0:
        moves.remove("UP")
    if monster[0] == 2:
        moves.remove("DOWN")
    
    move = random.choice(moves)
    
    if move == "LEFT":
        y -= 1
    elif move == "RIGHT":
        y += 1
    elif move == "UP":
        x -= 1
    elif move == "DOWN":
        x += 1
        
    return x, y
    

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # player = (x, y)
    
    if player[1] == 0:
        moves.remove("LEFT")
    if player[1] == 2:
        moves.remove("RIGHT")
    if player[0] == 0:
        moves.remove("UP")
    if player[0] == 2:
        moves.remove("DOWN")
    
    return moves
    
    
def draw_map(player, monster):
    print(' _ _ _')
    tile = '|{}'
    
    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format("X"), end = "")
            elif cell == monster:
                print(tile.format("M"), end = "")
            else: 
                print(tile.format('_'), end = "")
        else:
            if cell == player:
                print(tile.format("X|"))
            elif cell == monster:
                print(tile.format("M|"))
            else:
                print(tile.format("_|"))
              
monster, door, player = get_locations()

print("Welcome to the dungeon!")

while True:

    moves = get_moves(player)
    
   
    print("You are currently in room {}".format(player)) 
    
    monster = move_monster(monster)

        
    draw_map(player, monster)
    if monster == player:
        print("You were eaten by the grue!!!")
        break
    
    print("You can move {}".format(moves)) 
    print("Enter QUIT to quit")
    
    move = input("> ")
    move = move.upper()
    
    if move == "QUIT":
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("** Walls are hard... stop walking into them! **")
        continue
        
    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the grue!!!")
        break
        
 