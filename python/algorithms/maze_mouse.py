def canGo(maze, dire, position):
    try:
        if dire == 1: # Direita
            if maze[position[0]][position[1]+1]!=0:
                return True
        else: # Baixo
            if maze[position[0]+1][position[1]]!=0:
                return True
    except:
        return False
best_steps = 9999
best_way = None
def maze_rec(maze, init = [0,0], end = [0,0], steps = 0, way = []):
    global best_steps
    global best_way
    way = list(way)
    way.append(list(init))
    if init == end:
        if best_steps > steps:
            best_steps = steps
            best_way  = way
    elif init[0] > len(maze) and init[1] > len(maze):
        pass
    else:
        if canGo(maze,0, init):
            maze_rec(maze, [ init[0] +1, init[1] ], end, steps+1, way)
        if canGo(maze,1,init):
            maze_rec(maze, [ init[0] , init[1]+1], end, steps+1, way)
        







maze = [
    [1,0,0,0],
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,1]
]
maze_rec(maze, [0,0], [2,2])
print("Menor caminho {} passos : {} ".format(best_steps, best_way))