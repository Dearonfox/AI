# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.


import inspect
import sys
import random
from collections import deque

def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)


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
        pass

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        pass

    def getSuccessors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        pass

    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        pass


def random_search(problem):
    """
    Search the nodes in the search tree randomly.

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm.

    This random_search function is just example not a solution.
    You can write your code by examining this function
    """
    start = problem.getStartState()
    node = [(start, "", 0)]   # class is better
    frontier = [node]       #탐색할 경로 리스트
    explored = set()        #방문한 상태 저장 집합
    while frontier:
        node = random.choice(frontier)
        state = node[-1][0] 
        if problem.isGoalState(state):
            return [x[1] for x in node][1:]

        if state not in explored:
            explored.add(state)

            for successor in problem.getSuccessors(state):
                if successor[0] not in explored:
                    parent = node[:]
                    parent.append(successor)
                    frontier.append(parent)

    return []


def depth_first_search(problem):
    """Search the deepest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    stack = []  # DFS는 스택 사용
    stack.append([(problem.getStartState(), "", 0)])  # (state, action, cost)
    explored = set()
    MAX_DEPTH = 50  # 탐색 깊이 제한 (조정 가능)

    while stack:
        node = stack.pop()
        state = node[-1][0]  # 현재 상태

        if problem.isGoalState(state):  # 목표 도달 시 경로 반환
            return [x[1] for x in node][1:]

        if state not in explored:
            explored.add(state)

            # 탐색 깊이 제한 추가
            if len(node) <= MAX_DEPTH:
                for successor in problem.getSuccessors(state):
                    if successor[0] not in explored:
                        new_path = node + [successor]  # 새로운 경로 생성
                        stack.append(new_path)

    return []  # 목표 상태를 찾지 못한 경우



def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = deque()
    queue.append([(problem.getStartState(), "", 0)])  # 초기 경로
    explored = set()

    while queue:
        node = queue.popleft()
        state = node[-1][0]  # 현재 상태

        if problem.isGoalState(state):
            return [x[1] for x in node][1:]  # 경로만 반환

        if state not in explored:
            explored.add(state)

            for successor in problem.getSuccessors(state):
                if successor[0] not in explored:
                    new_path = node + [successor]
                    queue.append(new_path)  # FIFO: 큐에 맨 뒤로 추가

    return []
    
def uniform_cost_search(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    raiseNotDefined()


def heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    "*** YOUR CODE HERE ***"
    return 0


def aStar_search(problem, heuristic=heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    raiseNotDefined()


# Abbreviations
rand = random_search
bfs = breadth_first_search
dfs = depth_first_search
astar = aStar_search
ucs = uniform_cost_search
