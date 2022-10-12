from __future__ import annotations
from collections import deque
# There's a cleaner solution w/ a string representation that is essentially a set of nested tuples which represents the tree.
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments


class TreeNode:
    def __init__(self, val: int | None, depth: int | None = None) -> None:
        self.val = val
        self.left = None
        self.right = None
        # extra attribute used in the serialization step
        # keeps track of whether we saw any nodes at the previous depth; if not, stop encoding (which has place holders for missing nodes)
        # technically, our process should start w/ a root node that doesn't have this attribute and add it as part of the process
        # we created the original tree w/ this depth attribute to begin with (see create_tree())
        self.depth = depth


class TreeCodec:
    def __init__(self) -> None:
        self.serialized = ""  # not bytes or bits, but an encoding of the object into a small string
        self.char_list = None  # self.serialized.split(",") will be helpful when self.serialized is a string like "1,2,3,_,_,4,5"
        self.bfs_queue = deque([])  # to store TreeNodes for connection during serialization process

    def serialize(self, curr_node: TreeNode) -> str:
        """save the tree as a BFS-ordered list but with _ for missing nodes. So we have a full row of values at each depth.
        So this turns a depth-2 tree into say '1,2,3,_,_,4,5' where children index (if they exist) are 2i + 1 and 2i + 2"""
        self.bfs_queue.append(curr_node)
        val_seen_at_depth = {0: True}
        stop_flag = False

        while not stop_flag:
            curr_node = self.bfs_queue.popleft()

            if curr_node.val is None:
                # first encode it
                self.serialized += '_,'
                # then note whether we didn't see anything in the last round
                seen = val_seen_at_depth.get(curr_node.depth - 1, False)
                if not seen:
                    stop_flag = True
            else:
                # first encode it
                self.serialized += str(curr_node.val) + ","
                # then note we saw something in this row for the next row
                val_seen_at_depth[curr_node.depth] = True

            if curr_node.left:
                self.bfs_queue.append(curr_node.left)
            else:
                self.bfs_queue.append(TreeNode(None, curr_node.depth + 1))

            if curr_node.right:
                self.bfs_queue.append(curr_node.right)
            else:
                self.bfs_queue.append(TreeNode(None, curr_node.depth + 1))

        # Find nth occurrence of comma in string; this is our split below point.
        comma_index_list = [i for i in range(len(self.serialized)) if self.serialized[i] == ","]
        half_comma_idx = len(comma_index_list)//2 - 1 - 1  # -1 because index starts at 0, and -1 for the math
        last_char_idx = comma_index_list[half_comma_idx]

        # Drop the entire additional row of of nodes all of which are .val = None. These nodes were not in our original tree.
        self.serialized = self.serialized[:last_char_idx]
        self.char_list = self.serialized.split(",")
        return self.serialized

    def deserialize(self) -> TreeNode:
        """go from a string back to connected tree node objects. we bootstrap the process by creating the first tree node."""
        root_node = TreeNode(int(self.char_list[0]))  # we don't care about the depth attribute anymore
        self.connect_children(root_node, 0)  # recursively connects the entire tree
        return root_node

    def connect_children(self, parent_node: TreeNode, i: int) -> None:
        """recursive call to that keeps adding left and right children attributes"""
        if 2 * i + 1 < len(self.char_list):
            if self.char_list[2 * i + 1] != "_":
                parent_node.left = TreeNode(self.char_list[2 * i + 1])
                self.connect_children(parent_node.left, 2 * i + 1)
            else:
                parent_node.left = None

        if 2 * i + 2 < len(self.char_list):
            if self.char_list[2 * i + 2] != "_":
                parent_node.right = TreeNode(self.char_list[2 * i + 2])
                self.connect_children(parent_node.right, 2 * i + 2)
            else:
                parent_node.right = None


def create_tree(node_vals: list[int | None]) -> list[TreeNode]:
    """turn a list integer values into a bunch of connected TreeNode objects and return a list of the node objects."""
    node_obj_list = []
    depth = 0
    bfs_queue = deque([TreeNode(node_vals[0], 0)])
    i = 0

    while i < len(node_vals):
        # -1 for the index starting at 0; -1 for it being part of the math of the upper limit
        if i > 2**(depth + 1) - 1 - 1:
            depth += 1

        new_node = bfs_queue.popleft()

        if 2*i + 1 < len(node_vals):
            new_node.left = TreeNode(node_vals[2*i + 1], depth + 1)
        else:
            new_node.left = TreeNode(None, depth + 1)

        if 2*i + 2 < len(node_vals):
            new_node.right = TreeNode(node_vals[2*i + 2], depth + 1)
        else:
            new_node.right = TreeNode(None, depth + 1)

        node_obj_list.append(new_node)
        bfs_queue.append(new_node.left)
        bfs_queue.append(new_node.right)

        i += 1

    return node_obj_list


# list as tree read in order of depth, from top tree row, to bottom tree row/depth, w/ Nones for no children at that depth
# like a heap...
# children = 2i + 1 and 2i + 2; e.g. index 0's children are 1 and 2 (values 2 and 3); index 2's children are index 5 and 6
node_val_list = [1, 2, 3, None, None, 4, 5]

list_of_nodes = create_tree(node_val_list)
print("Let's see the tree node object attributes. The first node will be our root node. It is put into serialize() method in TreeCodec obj")
print("node, node.val, .left, .right, .depth for node in node_obj_list",
      [(node, node.val, node.left, node.right, node.depth) for node in list_of_nodes])
root = list_of_nodes[0]
codec = TreeCodec()
codec.serialize(root)
print()
print("Serialized Tree Obj (as a string)", type(codec.serialized), codec.serialized)
tree_root_node_again = codec.deserialize()
print()
print("Let's decompress the serialized object (and get the root node back)", tree_root_node_again)
print("Here's a view of the reconstructed root node object attributes (at a new memory location):",
      tree_root_node_again, tree_root_node_again.val, tree_root_node_again.left, tree_root_node_again.right, tree_root_node_again.depth)
print()
print("checks:")
print("left child of root node should have val of 2. does it?", tree_root_node_again.left.val)
print("right child of root node should have val of 3. does it?", tree_root_node_again.right.val)
print("left, left child of root node should have val of None. does it?", tree_root_node_again.left.left)
print("right, left child of root node should have val of 4. does it?", tree_root_node_again.right.left.val)


