import random
import pprint as pp

class Qlearning(object):
    def __init__(self, maze, epsilon, alpha, n):
        self.maze = maze.maze
        self.epsilon = epsilon
        self.alpha = alpha
        self.n = n
        self.actual_state = maze.random_valid_positon()     
        self.moves = ['R','L','U','D']
        
        # Criação da Q-Table
        self.q_table = {}
        for i in range(len(self.maze)):
            self.q_table[str(i)] = {}
            for j in range(len(self.maze[i])):
                self.q_table[str(i)][str(j)] = {}
                item = self.maze[i][j]
                if item == '-' or item == '&' or item == '0':
                    for move in self.moves:
                        self.q_table[str(i)][str(j)].update({move: 0.0})


    def show_q_table(self):
        print("\nQ-Table")
        for x in self.q_table:
            for y in self.q_table[x]:
                for move in self.q_table[x][y]:
                    print(f'{x},{y},{move},{"%0.3f" % self.q_table[x][y][move]}')
    
    def move(self, direction):
        if direction == 'R':
            new_x = self.actual_state[0]
            new_y = self.actual_state[1] + 1
        elif direction == 'L':
            new_x = self.actual_state[0]
            new_y = self.actual_state[1] - 1
        elif direction == 'U':
            new_x = self.actual_state[0] - 1
            new_y = self.actual_state[1]
        elif direction == 'D':
            new_x = self.actual_state[0] + 1
            new_y = self.actual_state[1]
        
        #if new_x >= 0 and new_x < self.maze.
        # Q[state, action] = Q[state, action] + self.alpha * (reward + 0.9 * np.max(Q[new_state, :]) — Q[state, action]


    def learn(self):
        episode_ended = False
        while(not episode_ended):
            if random.uniform(0, 1) < self.epsilon:
                """
                Explore: select a random action
                """
                move(random.choice(self.moves))
                # episode_ended = True
            else:
                """
                Exploit: select the action with max value (future reward)
                """
                