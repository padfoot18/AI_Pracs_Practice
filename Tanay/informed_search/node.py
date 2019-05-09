import heapq
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, state=None, parent=None, level=0):
        self.children = []
        self.state = state
        self.parent = parent
        self.level = level
        self.f = 0
        self.g = 0
        self.h = 0

    def add_child(self, child):
        self.children.append(child)

    def __eq__(self, other):
        return self.f == other.f

    def __lt__(self, other):
        return self.f < other.f

    def is_goal_state(self, goal_state):
        # override in subclass
        if self.state == goal_state:
            return True
        return False

    def path_to_goal_state(self):
        if self.parent:
            self.parent.path_to_goal_state()
            print('-->')
        print(self)

    def __repr__(self):
        return str(self.state)

    def a_star(self, goal_state):
        print('in astar')
        open_nodes = [self]
        heapq.heapify(open_nodes)
        while open_nodes:
            new_node = heapq.heappop(open_nodes)
            print(new_node, 'level =', new_node.level, 'f =', new_node.f, 'g =', new_node.g, 'h =', new_node.h)
            if new_node.is_goal_state(goal_state):
                print('Goal state found\nPath to goal state:')
                new_node.path_to_goal_state()
                return
            # find all possible children, and set their heuristic
            new_node.evaluate_children()
            for child in new_node.children:
                child.calc_g()
                child.f = child.g + child.h
                heapq.heappush(open_nodes, child)

    def greedy_bfs(self, goal_state):
        open_nodes = [self]
        heapq.heapify(open_nodes)
        while open_nodes:
            new_node = heapq.heappop(open_nodes)
            print(new_node, 'level =', new_node.level, 'f =', new_node.f, 'g =', new_node.g, 'h =', new_node.h)
            if new_node.is_goal_state(goal_state):
                print('Goal state found\nPath to goal state:')
                new_node.path_to_goal_state()
                return
            # find all possible children, and set their heuristic
            new_node.evaluate_children()
            for child in new_node.children:
                child.calc_g()
                child.f = child.h
                heapq.heappush(open_nodes, child)
