#!/usr/bin/python3
import sys
import maze as m
import qlearning as q

myMaze = m.Maze(sys.argv[1])
alpha = float(sys.argv[2])
epsilon = float(sys.argv[3])
n = int(sys.argv[4])

qLearning = q.Qlearning(myMaze, epsilon, alpha, n)
qLearning.learn()

with open('q.txt','w') as q_table_file:
    q_table_file.write(qLearning.show_q_table())
with open('pi.txt','w') as policy_file:
    policy_file.write(qLearning.show_policy())

with open('rewards/'+sys.argv[1]+'_'+str(alpha)+'_'+str(epsilon)+'_'+str(n)+'_'+str(n)+'.txt', 'w') as reward_mean_file:
    reward_mean_file.write(qLearning.show_mean_reward())