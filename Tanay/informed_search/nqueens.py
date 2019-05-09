from node import Node
from copy import deepcopy


class NQueens(Node):
    def __init__(self, state=None, parent=None, level=0, n=4):
        self.n = n
        if not state:
            state = [-1 for x in range(n)]
        Node.__init__(self, state=state, parent=parent, level=level)
        if self.parent:
            self.level = self.parent.level + 1

    def heuristic(self, goal_state=None):
        # goal_state parameter not required. added for compatibility
        num_attacking = 0
        for i in range(self.level):
            j = self.state[i]
            for k in range(self.level):
                if k != i:
                    # i,j and k,l = positions
                    l = self.state[k]
                    # in same column
                    if j == l:
                        num_attacking += 1
                    # diagonal
                    if i+j == k+l or i-j == k-l:
                        num_attacking += 1
        return 2*num_attacking + 2*self.n - 2*self.level

    def is_goal_state(self, goal_state=None):
        if self.heuristic() == 0:
            return True
        else:
            return False

    def evaluate_children(self):
        if self.level == self.n:
            return
        i = self.level

        state1 = deepcopy(self.state)
        state1[i] = 0
        n1 = NQueens(state1, parent=self, level=i)
        n1.h = n1.heuristic()
        self.add_child(n1)

        state2 = deepcopy(self.state)
        state2[i] = 1
        n2 = NQueens(state2, parent=self, level=i)
        n2.h = n2.heuristic()
        self.add_child(n2)

        state3 = deepcopy(self.state)
        state3[i] = 2
        n3 = NQueens(state3, parent=self, level=i)
        n3.h = n3.heuristic()
        self.add_child(n3)

        state4 = deepcopy(self.state)
        state4[i] = 3
        n4 = NQueens(state4, parent=self, level=i)
        n4.h = n4.heuristic()
        self.add_child(n4)

    def calc_g(self):
        if self.parent:
            self.g = self.parent.g + 1
        
if __name__ == '__main__':
    print('A star')
    root = NQueens([-1, -1, -1, -1])
    root.a_star()
    print('Greedy bfs')
    root.greedy_bfs()