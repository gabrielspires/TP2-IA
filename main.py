#!/usr/bin/python3

#taxa de aprendizado (α), o fator de exploração (ε) e o número de iterações que executará (N)

import sys
import maze as m
import qlearning as q

myMaze = m.Maze(sys.argv[1])
alpha = float(sys.argv[2])
epsilon = float(sys.argv[3])
n = int(sys.argv[4])

myMaze.show_maze()
qLearning = q.Qlearning(myMaze, epsilon, alpha, n)
qLearning.learn()
print(qLearning.show_q_table())
print(qLearning.show_policy())

with open('q.txt','w') as q_table_file:
    q_table_file.write(qLearning.show_q_table())
with open('pi.txt','w') as policy_file:
    policy_file.write(qLearning.show_policy())
    