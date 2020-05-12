class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        data_set = {head.data}
        previous_node = head
        current_node = previous_node.next
        while current_node is not None:
            if current_node.data in data_set:
                previous_node.next = current_node.next
                current_node = current_node.next
            else:
                data_set.add(current_node.data)
                previous_node = current_node
                current_node = current_node.next

        return head


if __name__ == "__main__":

    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    head = mylist.removeDuplicates(head)
    mylist.display(head);
