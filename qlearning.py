import random

class Qlearning(object):
    def __init__(self, maze, epsilon, alpha, n):
        self.maze = maze
        self.epsilon = epsilon
        self.alpha = alpha
        self.n = n
        self.actual_state = maze.random_valid_positon()     
        self.moves = ['R','L','U','D']

        self.mean_reward = []
        self.episode = 0
        
        # Criação da Q-Table
        self.q_table = {}
        for i in range(len(self.maze.maze)):
            self.q_table[str(i)] = {}
            for j in range(len(self.maze.maze[i])):
                self.q_table[str(i)][str(j)] = {}
                item = self.maze.maze[i][j]
                if item == '-' or item == '&' or item == '0':
                    for move in self.moves:
                        self.q_table[str(i)][str(j)].update({move: 0.0})
		

    def show_q_table(self):
        q_table = ''
        for x in self.q_table:
            for y in self.q_table[x]:
                for move in self.q_table[x][y]:
                    if self.maze.maze[int(x)][int(y)] == '-':
                        q_table += f'{x},{y},{move},{"%0.3f" % self.q_table[x][y][move]}\n'
        return q_table
    
    def reward(self, x, y):
        x = int(x) ; y = int(y)
        if self.maze.maze[x][y] == '-':
            return -1
        if self.maze.maze[x][y] == '0':
            return 10
        if self.maze.maze[x][y] == '&':
            return -10
        

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
        
        if self.maze.maze[new_x][new_y] == '#':
            new_x = self.actual_state[0]
            new_y = self.actual_state[1]

        new_x = str(new_x)
        new_y = str(new_y)

        old_x = str(self.actual_state[0])
        old_y = str(self.actual_state[1])

        max_new_state = self.q_table[new_x][new_y][max(self.q_table[new_x][new_y], key=self.q_table[new_x][new_y].get)]
        self.q_table[old_x][old_y][direction] += self.alpha*(self.reward(new_x,new_y) + 0.9 * max_new_state - self.q_table[old_x][old_y][direction])
        self.actual_state = (int(new_x), int(new_y))

        new_state = self.maze.maze[self.actual_state[0]][self.actual_state[1]]

        if new_state == "&" or new_state == '0':
            #fim do episodio
            self.actual_state = self.maze.random_valid_positon()
            self.n -= 1

            mean_reward = 0
            num_rewards = 0
            for x in self.q_table:
                for y in self.q_table[x]:
                    if self.maze.maze[int(x)][int(y)] != '-':
                        continue
                    for action in self.q_table[x][y]:
                        mean_reward += self.q_table[x][y][action]
                        num_rewards += 1

            mean_reward /= num_rewards
            self.mean_reward.append([self.episode, mean_reward])
            self.episode += 1

    def show_mean_reward(self):
        values = ''
        for episode in self.mean_reward:
            values += str(episode[0]) + ' ' + str(episode[1]) + '\n'
        return values

    def learn(self):
        while(self.n):
            if random.uniform(0, 1) < self.epsilon:
                """
                Explore: select a random action
                """
                self.move(random.choice(self.moves))
            else:
                """
                Exploit: select the action with max value (future reward)
                """
                x = str(self.actual_state[0])
                y = str(self.actual_state[1])
                best_move = max(self.q_table[x][y], key=self.q_table[x][y].get)
                self.move(best_move)
    
    def show_policy(self):
        policy = ''
        for x in range(self.maze.numLines):
            for y in range(self.maze.numCols):
                if self.maze.maze[x][y] == '-':
                    policy += max(self.q_table[str(x)][str(y)], key=self.q_table[str(x)][str(y)].get)
                else:
                    policy += self.maze.maze[x][y]
            policy += '\n'
        return policy
