from node import Node
from copy import deepcopy


class EightPuzzle(Node):
    goal_state = None

    def __init__(self, board_state, action='initial', parent=None, level=0):
        Node.__init__(self, state=board_state, parent=parent, level=level)
        self.heuristic()
        self.action = action

    def __repr__(self):
        row = ['\t'.join(x) for x in self.state]
        return '\n'.join(row)+'\t['+self.action+']\n'

    def heuristic(self):
        tiles = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
        for tile in tiles:
            i1,j1 = find_tile(self.state, tile)
            i2,j2 = find_tile(EightPuzzle.goal_state, tile)
            self.h += abs(i1-i2)
            self.h += abs(j1-j2)

    def calc_g(self):
        if self.parent:
            self.g = self.parent.g + 1

    def evaluate_children(self):
        # find all possible children
        self.move_left()
        self.move_right()
        self.move_up()
        self.move_down()

    def move_left(self):
        if self.action == 'right':
            return
        i,j = find_tile(self.state, ' ')
        if j != 0:
            new_state = deepcopy(self.state)
            temp = new_state[i][j]
            new_state[i][j] = new_state[i][j-1]
            new_state[i][j-1] = temp
            self.add_child(EightPuzzle(new_state, action='left', parent=self, level=self.level+1))

    def move_right(self):
        if self.action == 'left':
            return
        i,j = find_tile(self.state, ' ')
        if j != 2:
            new_state = deepcopy(self.state)
            temp = new_state[i][j]
            new_state[i][j] = new_state[i][j+1]
            new_state[i][j+1] = temp
            self.add_child(EightPuzzle(new_state, action='right', parent=self, level=self.level+1))

    def move_up(self):
        if self.action == 'down':
            return
        i,j = find_tile(self.state, ' ')
        if i != 0:
            new_state = deepcopy(self.state)
            temp = new_state[i][j]
            new_state[i][j] = new_state[i-1][j]
            new_state[i-1][j] = temp
            self.add_child(EightPuzzle(new_state, action='up', parent=self, level=self.level+1))

    def move_down(self):
        if self.action == 'up':
            return
        i,j = find_tile(self.state, ' ')
        if i != 2:
            new_state = deepcopy(self.state)
            temp = new_state[i][j]
            new_state[i][j] = new_state[i+1][j]
            new_state[i+1][j] = temp
            self.add_child(EightPuzzle(new_state, action='down', parent=self, level=self.level+1))


def find_tile(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return i,j
    print(tile)
    return False


# EightPuzzle.goal_state = [['1','2','3'], ['8',' ','4'], ['7','6','5']]
# root = EightPuzzle([['8','1','3'],[' ','2','4'],['7','6','5']])
EightPuzzle.goal_state = [['1', '2', '3'],['4', '5', '6'],['7', ' ', '8']]
root = EightPuzzle([['1', '2', '3'],[' ', '4', '6'],['7', '5', '8']])
print('A star search:')
root.a_star(EightPuzzle.goal_state)

print('\nGreedy bfs:')
root.greedy_bfs(EightPuzzle.goal_state)
