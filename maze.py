class Maze(object):
    def __init__(self, entrada):
        self.moves = ['U','D','L','R']

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
            
            
                
            

        