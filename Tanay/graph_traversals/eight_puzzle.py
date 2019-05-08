from node import Node


class EightPuzzle(Node):
    def __init__(self, board_state, parent=None, level=0):
        Node.__init__(self, state=board_state, parent=parent, level=level)
        pass

    def __repr__(self):
        row = ['\t'.join(x) for x in self.state]
        return '\n'.join(row)+'\n'

if __name__ == '__main__':
    n1 = EightPuzzle([['1', '2', '3'],[' ', '4', '6'],['7', '5', '8']])
    n2 = EightPuzzle([[' ', '2', '3'],['1', '4', '6'],['7', '5', '8']], parent=n1, level=1)
    n3 = EightPuzzle([['1', '2', '3'],['7', '4', '6'],[' ', '5', '8']], parent=n1, level=1)
    n4 = EightPuzzle([['1', '2', '3'],['4', ' ', '6'],['7', '5', '8']], parent=n1, level=1)
    n1.add_child(n2)
    n1.add_child(n3)
    n1.add_child(n4)
    n5 = EightPuzzle([['2', ' ', '3'],['1', '4', '6'],['7', '5', '8']], parent=n2, level=2)
    n2.add_child(n5)
    n6 = EightPuzzle([['1', '2', '3'],['7', '4', '6'],['5', ' ', '8']], parent=n3, level=2)
    n3.add_child(n6)
    n7 = EightPuzzle([['1', '2', '3'],['4', '5', '6'],['7', ' ', '8']], parent=n4, level=2)
    n8 = EightPuzzle([['1', '2', '3'],['4', ' ', '6'],['7', '5', '8']], parent=n1, level=2)
    n9 = EightPuzzle([['1', ' ', '3'],['4', '2', '6'],['7', '5', '8']], parent=n1, level=2)
    n4.add_child(n7)
    n4.add_child(n8)
    n4.add_child(n9)

    print('\nDFS')
    n1.dfs(goal_state=[['1', '2', '3'],['4', '5', '6'],['7', ' ', '8']])
    print('\nBFS')
    n1.bfs(goal_state=[['1', '2', '3'],['4', '5', '6'],['7', ' ', '8']])
    print('\nDLS')
    n1.dls(1, goal_state=[['1', '2', '3'],['4', '5', '6'],['7', ' ', '8']])
    print('\nIDS')
    n1.ids(2, goal_state=[['1', '2', '3'],['4', '5', '6'],['7', ' ', '8']])
    
    
