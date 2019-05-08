from node import Node


class WaterJug(Node):
    cap1 = 0
    cap2 = 0

    def __init__(self,initial_values, parent, level=0):
        Node.__init__(self, parent=parent, state=initial_values, level=level)
        self.val1 = initial_values[0]
        self.val2 = initial_values[1]

    # def __repr__(self):
    #     return f'jug1={self.val1}, jug2={self.val2}'

    def is_goal_state(self, goal_state):
        if goal_state[0] == 1 and self.val1 == goal_state[1]:
            return True
        if goal_state[0] == 2 and self.val2 == goal_state[1]:
            return True
        return False

    def set_capacity(cp1, cp2):
        WaterJug.cap1 = cp1
        WaterJug.cap2 = cp2

    def empty(self, jug_no):
        if jug_no == 1 and self.val1 != 0:
            return [0, self.val2]
        elif jug_no == 2 and self.val2 != 0:
            return [self.val1, 0]
        else:
            return False

    def fill(self, jug_no):
        if jug_no == 1 and self.val1 != self.cap1:
            return [WaterJug.cap1, self.val2]
        elif jug_no == 2 and self.val2 != self.cap2:
            return [self.val1, WaterJug.cap2]
        else:
            return False

    def transfer(self, from_jug, to_jug):
        if from_jug == 1 and to_jug == 2:
            if self.val1 == 0:
                return False
            if self.val1+self.val2 <= WaterJug.cap2:
                return [0, self.val2+self.val1]
            else:
                rem_in_2 = WaterJug.cap2-self.val2
                return [self.val1-rem_in_2, self.cap2]

        elif from_jug == 2 and to_jug ==1:
            if self.val2 == 0:
                return False
            if self.val1+self.val2 <= WaterJug.cap1:
                return [self.val2+self.val1, 0]
            else:
                rem_in_1 = WaterJug.cap1-self.val1
                return [self.cap1, self.val2-rem_in_1]

        else:
            return False


def generate_state_space(initial_state, goal_state, max_nodes=100):
    count_nodes = 0
    root = WaterJug(initial_state, parent=None)
    new_node = root
    queue = [root]
    uniques = [initial_state]

    while count_nodes < max_nodes and queue:
        print(new_node)
        new_node = queue.pop(0)
        if not new_node.is_goal_state(goal_state):
            x = new_node.empty(1)
            if x and x not in uniques and x not in uniques:
                uniques.append(x)
                x = WaterJug(x, new_node, new_node.level+1)
                
                queue.append(x)
                new_node.add_child(x)
                count_nodes += 1

            x = new_node.empty(2)
            if x and x not in uniques:
                uniques.append(x)
                x = WaterJug(x, new_node, new_node.level+1)
                
                queue.append(x)
                new_node.add_child(x)
                count_nodes += 1

            x = new_node.fill(1)
            if x and x not in uniques:
                uniques.append(x)
                x = WaterJug(x, new_node, new_node.level+1)
                queue.append(x)
                
                new_node.add_child(x)
                count_nodes += 1
                
            x = new_node.fill(2)
            if x and x not in uniques:
                uniques.append(x)
                x = WaterJug(x, new_node, new_node.level+1)
                
                queue.append(x)
                new_node.add_child(x)
                count_nodes += 1
                
            x = new_node.transfer(1, 2)
            if x and x not in uniques:
                uniques.append(x)
                x = WaterJug(x, new_node, new_node.level+1)
                
                queue.append(x)
                new_node.add_child(x)
                count_nodes += 1

            x = new_node.transfer(2, 1)
            if x and x not in uniques:
                uniques.append(x)
                x = WaterJug(x, new_node, new_node.level+1)
                
                queue.append(x)
                new_node.add_child(x)
                count_nodes += 1
    return root


if __name__ == '__main__':
    cap1 = int(input('Enter capacity for jug 1:'))
    cap2 = int(input('Enter capacity for jug 2:'))
    WaterJug.set_capacity(cap1, cap2)
    root = generate_state_space([0,0], [2,2], 500)

    print('\nDFS')
    root.dfs(goal_state=[2,2])
    print('\nBFS')
    root.bfs(goal_state=[2,2])
    print('\nDLS, limit=6')
    root.dls(6,goal_state=[2,2])
    print('\nIDS, limit=6')
    root.ids(6,goal_state=[2,2])
