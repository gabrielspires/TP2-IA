#!/usr/bin/python3

#taxa de aprendizado (α), o fator de exploração (ε) e o número de iterações que executará (N)

import sys
import maze as m
import qlearning as q

myMaze = m.Maze(sys.argv[1])
alpha = float(sys.argv[2])
epsilon = float(sys.argv[3])
n = float(sys.argv[4])

qLearning = q.Qlearning(myMaze, epsilon, alpha, n)
qLearning.show_q_table()
# myMaze.show_maze()
# print(myMaze.random_valid_positon())
qLearning.learn()