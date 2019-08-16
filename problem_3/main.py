'''
    Given the root to a binary tree, implement serialize(root), which serializes the tree into a
        string, and deserialize(s), which deserializes the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
'''
DEBUG = True

class Node:
    '''
    binary tree node.
    '''
    def __init__(self, val, left=None, right=None):
        '''
        Constructor for a binary tree node
        '''
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    '''
    Serializes a binary tree.

    root is the root node for a binary tree.

    serialized nodes will have the footprint:

    has_left,has_right,"val";

    returns the string representation of the tree.
    '''
    def serialize_node(a_node, output):
        if a_node.left:
            output = serialize_node(a_node.left, output)

        if a_node.right:
            output = serialize_node(a_node.right, output)


        return '{},{},"{}";{}'.format(bool(a_node.left), bool(a_node.right), a_node.val, output)

    return serialize_node(root, '')


def deserialize(source):
    '''
    Deserialize a binary tree.

    source is the serialized tree.

    returns the root node of a binary tree.
    '''
    source = source[:-1]
    source_list = source.split(';')

    def deserialize_node(partial_list):
        a_source = partial_list[0].strip("'")

        has_left = a_source.split(',')[0] == 'True'
        has_right = a_source.split(',')[1] == 'True'
        val = a_source.split(',')[2].strip('"')
        a_node = Node(val)
        partial_list = partial_list[1:]

        if has_right:
            a_node.right, partial_list = deserialize_node(partial_list)

        if has_left:
            a_node.left, partial_list = deserialize_node(partial_list)

        return a_node, partial_list

    node, _ = deserialize_node(source_list)
    return node


if __name__ == "__main__":
    NODE = Node('root', Node('left', Node('left.left')), Node('right'))

    if DEBUG:
        SOURCE = serialize(NODE)
        print(SOURCE)
        UPDATED = deserialize(SOURCE)
        UPDATED_SOURCE = serialize(UPDATED)
        print(UPDATED_SOURCE)

    assert deserialize(serialize(NODE)).left.left.val == 'left.left'
