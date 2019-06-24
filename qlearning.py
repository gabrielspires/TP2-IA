import random

class Qlearning(object):
    def __init__(self, maze, epsilon, alpha, n):
        self.maze = maze
        self.actual_state = (1,1)
        
        # Criação da Q-Table
        self.q_table = []
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                item = self.maze[i][j]
                if item == '-' or item == '&' or item == '0':
                    self.q_table.append([i,j,'R',0.0])
                    self.q_table.append([i,j,'L',0.0])
                    self.q_table.append([i,j,'U',0.0])
                    self.q_table.append([i,j,'D',0.0])


    def show_q_table(self):
        print("\nQ-Table")
        for i in range(len(self.q_table)):
            for j in range(len(self.q_table[i])):
                if j>0: print(',',end='')
                print(self.q_table[i][j], end='')
            print()
    
    def learn(self):

        if random.uniform(0, 1) < self.epsilon:
            """
            Explore: select a random action
            """
        else:
            """
            Exploit: select the action with max value (future reward)
            """
    