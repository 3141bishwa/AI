# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class Node:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    fringe = Stack()

    visited = dict()

    root_node = Node(pos = problem.getStartState(), path = [])

    fringe.push(root_node)

    while not fringe.isEmpty():
        node = fringe.pop()

        if problem.isGoalState(node.pos):
            return node.path

        if node.pos not in visited:
            visited[node.pos] = 1
            for successor in problem.getSuccessors(node.pos):
                new_node = Node(
                        pos = successor[0], path = node.path + [successor[1]])
                fringe.push(new_node)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue

    fringe = Queue()

    visited = dict()

    root_node = Node(pos=problem.getStartState(), path=[])

    fringe.push(root_node)

    while not fringe.isEmpty():

        node = fringe.pop()

        if problem.isGoalState(node.pos):
            return node.path

        if node.pos not in visited:
            visited[node.pos] = 1
            for successor in problem.getSuccessors(node.pos):
                new_node = Node(
                        pos = successor[0], path = node.path + [successor[1]])
                fringe.push(new_node)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue

    fringe = PriorityQueue()

    visited = dict()

    start = problem.getStartState()

    root_node = Node(pos=start, path=[], priority = 0.0)

    fringe.push(root_node,0)

    while not fringe.isEmpty():
        node = fringe.pop()

        if problem.isGoalState(node.pos):
            return node.path

        if node.pos not in visited:
            visited[node.pos] = 1
            for successor in problem.getSuccessors(node.pos):
                # Setting the cost of a node as the cumulative cost of reaching
                # that node through a specific path
                new_node = Node(pos = successor[0], path  = node.path + \
                        [successor[1]],priority = node.priority + successor[2])
                fringe.update(new_node, node.priority + successor[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the
    nearest goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue

    #import code
    #code.interact(local=dict(globals(), **locals()))
    fringe = PriorityQueue()

    start = problem.getStartState()

    root_node = Node(pos=start, path = [], cost_priority = 0.0,
            heuristic_priority = heuristic(start, problem))

    fringe.push(root_node,0)

    visited = set()

    while not fringe.isEmpty():
        node = fringe.pop()

        if problem.isGoalState(node.pos):
            return node.path

        if node.pos not in visited:
            visited.add(node.pos)
            for successor in problem.getSuccessors(node.pos):
                # Setting the cost of a node as the cumulative cost of reaching
                # that node through a specific path
                new_node = Node(pos = successor[0], path = node.path + \
                        [successor[1]], cost_priority = node.cost_priority + successor[2],
                        heuristic_priority = heuristic(successor[0], problem))

                fringe.update(new_node,
                        new_node.cost_priority + new_node.heuristic_priority)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
