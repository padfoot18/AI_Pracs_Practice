class Node:
    def __init__(self, parent=None, state=None, level=0):
        self.children = []
        self.state = state
        self.parent = parent
        self.level = level

    def add_child(self, child):
        self.children.append(child)

    def is_goal_state(self, goal_state):
        # override in subclass
        if self.state == goal_state:
            return True
        return False

    def __repr__(self):
        return str(self.state)

    def bfs(self, goal_state=None):
        # visit this node
        print(self, 'level =', self.level)
        if goal_state and self.is_goal_state(goal_state):
            print('Goal found!')
            return

        # queue of unvisited nodes
        unvisited = [f'Children of {self.state}']
        unvisited.extend(self.children[:])

        for node in unvisited:
            if type(node) == str:
                print(f'==== {node} ====')
            else:
                # visit next in queue
                print(node, 'level =', node.level)

                if goal_state and node.is_goal_state(goal_state):
                    print('Goal found!')
                    return

                # add its children to the queue
                if node.children:
                    unvisited.append(f'Children of {node.state}')
                    unvisited.extend(node.children)                    

    def dfs(self, goal_state=None):
        print(self, 'level =', self.level)
        if goal_state and self.is_goal_state(goal_state):
            print('Goal found')
            return True
        for node in self.children:
            if node.dfs(goal_state):
                return True
        return False

    def dls(self, limit, goal_state=None):
        if limit < 0:
            return False
        print(self, 'level =', self.level)
        if goal_state and self.is_goal_state(goal_state):
            print('Goal found.')
            return True
        for node in self.children:
            if node.dls(limit-1, goal_state):
                return True
        return False

    def ids(self, limit, goal_state=None):
        for i in range(limit+1):
            print(f'Iteration = {i}')
            if self.dls(i,goal_state):
                return True



if __name__ == '__main__':
    # for testing
    n1 = Node(1, 0)
    n2 = Node(2, 1)
    n3 = Node(3, 1)
    n4 = Node(4, 2)
    n5 = Node(5, 2)
    n6 = Node(6, 2)
    n7 = Node(7, 2)
    n8 = Node(8, 3)
    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n2.add_child(n5)
    n2.add_child(n6)
    n3.add_child(n7)
    n6.add_child(n8)
    n1.bfs()
    n1.dfs()