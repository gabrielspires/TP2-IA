import random

class Maze(object):
    def __init__(self, entrada):
        with open(entrada, 'r') as pacmaze:
            dimension = pacmaze.readline().split()
            self.numLines = int(dimension[0])
            self.numCols = int(dimension[1])
            self.maze = []

            for line in pacmaze:
                maze_line = list(line)
                if maze_line[-1] == '\n':
                    maze_line.pop()
                self.maze.append(maze_line)
    
    def random_valid_positon(self):
        while(1):
            x = random.randint(0,self.numLines-1)
            y = random.randint(0,self.numCols-1)
            if self.maze[x][y] == '-':
                return (x,y)

    def show_maze(self):
        for line in self.maze:
            for item in line:
                print(item, end=' ')
            print()