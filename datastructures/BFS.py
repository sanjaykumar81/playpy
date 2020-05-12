class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class BT:

    def __init__(self, data):
        self.node = Node(data)

    def insert(self, data):
        self.node = self.__insertNode(self.node, data)

    def __insertNode(self, node, data):
        if node is None:
            return Node(data)
        elif node.data >= data:
            cur = self.__insertNode(node.left, data)
            node.left = cur
        else:
            cur = self.__insertNode(node.right, data)
            node.right = cur

        return node

    def levelOrder(self, root):
        queue = [root]
        self.printOrder(queue)

    def printOrder(self, queue):
        if len(queue) == 0:
            return
        left = queue[1].left
        right = queue[1].right
        if left is not None:
            queue.append(left)
        if right is not None:
            queue.append(right)

        print(queue[1].data, end = ' ')# this replaces "\n" char with a space ' '. so next print statement is printed on same line.
        queue = queue[1:]
        self.printOrder(queue)
