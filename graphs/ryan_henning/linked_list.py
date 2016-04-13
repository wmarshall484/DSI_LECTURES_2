
class Node:
    '''
    This class represents a node in a linked list.
    Every node contains a value and a reference to the
    next node in the list (or None if this node is the
    last node in the list).
    '''

    def __init__(self, value, next_node=None):
        '''Initializes this node with a value and a next node reference'''
        self.value = value
        self.next_node = next_node

    def insert_after(self, node):
        '''Inserts 'node' AFTER 'self' in the list'''
        node.next_node = self.next_node
        self.next_node = node

    def pop_after(self):
        '''Pops the node that is AFTER 'self' from the list and returns it'''
        node = self.next_node
        self.next_node = node.next_node
        node.next_node = None
        return node


def build():
    '''
    Builds and returns a demo linked list for testing purposes.
    '''
    a = Node(4)
    b = Node(8)
    c = Node(15)
    d = Node(16)
    e = Node(23)
    f = Node(42)

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = e
    e.next_node = f
    f.next_node = None  # <-- not needed; here just for show

    return a


def print_forward(node):
    '''
    Treats 'node' as the first node of a linked list.
    Prints the 'value' of every node in this linked list
    in forward-order.
    '''
    while node is not None:
        print node.value
        node = node.next_node


def print_backward(node):
    '''
    Treats 'node' as the first node of a linked list.
    Prints the 'value' of every node in this linked list
    in backward-order.
    '''
    l = []
    while node is not None:
        l.append(node.value)
        node = node.next_node
    for v in reversed(l):
        print v


def r_print_forward(node):
    '''
    Same as print_forward(), except this function uses recursion!
    '''
    if node is not None:
        print node.value
        r_print_forward(node.next_node)


def r_print_backward(node):
    '''
    Same as print_backward(), except this function uses recursion!
    '''
    if node is not None:
        r_print_backward(node.next_node)
        print node.value


def print_helper(first_node, title, print_function):
    '''
    A little helper function for printing linked lists in a pretty manner.
    '''
    print title
    print_function(first_node)
    print


if __name__ == '__main__':

    first_node = build()

    print_helper(first_node, "forward:", print_forward)
    print_helper(first_node, "backward:", print_backward)

    print_helper(first_node, "forward (via recursion):", r_print_forward)
    print_helper(first_node, "backward (via recursion):", r_print_backward)

    new_node = Node(100)
    first_node.insert_after(new_node)
    print_helper(first_node, "After inserting 100:", print_forward)

    popped_node = new_node.pop_after()
    popped_value = popped_node.value
    print_helper(first_node, "After popping %d:" % popped_value, print_forward)

