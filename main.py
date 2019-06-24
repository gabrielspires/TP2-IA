#!/usr/bin/python3

import sys
import maze as m
import qlearning as q

myMaze = m.Maze(sys.argv[1])
alpha = sys.argv[2]
epsilon = sys.argv[3]
n = sys.argv[4]

qLearning = q.Qlearning(myMaze.maze, epsilon, alpha, n)
# qLearning.show_q_table()