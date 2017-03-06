import os
import sys

from lp_utils import decode_state

parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(parent), "aimacode"))
import unittest
from aimacode.utils import expr
from aimacode.planning import Action
from example_have_cake import have_cake
from my_air_cargo_problems import air_cargo_p2, air_cargo_p1
from my_planning_graph import (
    PlanningGraph, PgNode_a, PgNode_s, mutexify
)

class defineplanningclass():
    def setUp(self):
        self.p = have_cake()
        self.pg = PlanningGraph(self.p, self.p.initial)


def test_add_action_level(self):
     for level, nodeset in enumerate(self.pg.a_levels):
         for node in nodeset:
             print("Level {}: {}{})".format(level, node.action.name, node.action.args))
    #self.assertEqual(len(self.pg.a_levels[0]), 3, len(self.pg.a_levels[0]))
    #self.assertEqual(len(self.pg.a_levels[1]), 6, len(self.pg.a_levels[1]))


if __name__ == '__main__':
    p = air_cargo_p1()

    print("Initial state for this problem is {}".format(p.initial))
    print("Actions for this domain are:")
    print(len(p.initial))
    print(len(p.state_map))
    for a in p.actions_list:
        print('   {}{}'.format(a.name, a.args))
    print("Fluents in this problem are:")
    for f in p.state_map:
        print('   {}'.format(f))
    print("Goal requirement for this problem are:")
    for g in p.goal:
        print('   {}'.format(g))
    #print(decode_state(p.initial, p.state_map))
    p2 = air_cargo_p1()
    #pg = PlanningGraph(p2, p2.initial)
    #print(pg.p.actions_list)
    pg =PlanningGraph(p,p.initial)

    level_tracker=0

    level_count=len((pg.s_levels))
    print(level_count)



    while level_tracker<level_count:
        for  level,state in enumerate(pg.s_levels[level_tracker]):

            print('currrent leve   {}'.format(level_tracker))
            print(state.literal)
        level_tracker=level_tracker+1


    #for state_node in (range(len((pg.s_levels))):

    for level, state in  enumerate(pg.s_levels[0]): # level 0 state

        #print(level)

        print (state.literal)
    #a1=PgNode_a()
    #print(a1.show())

    #for action_node in pg.a_levels:
     #   print(action_node.show)
    #print(pg.h_levelsum())