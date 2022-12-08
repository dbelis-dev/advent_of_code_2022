import sys
import os
from treelib import Tree

def main():
    ## Set the variables/constants
    filepath = './input_file-example'
    result = 0
    tree = Tree()
    parent_node = ""
    dir_stack = []

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, line-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.rstrip()
            line = line.split(' ')
            print(line)
            if line[0].startswith('$'):
                # parse command
                print("new command")
                parent_node = parseCommand(tree, parent_node, dir_stack, line)
            elif line[0].isnumeric():
                # parse new file
                print("new file")
                parent_node = parseFile(tree, parent_node, line)
            print(parent_node)
            print()

    for node in tree.expand_tree(mode=Tree.DEPTH):
        if tree[node].data.type == 'd' and tree[node].data.size < 100000:
            print(tree[node].tag, tree[node].data.type, tree[node].data.size)
            result += tree[node].data.size
    # tree.show(data_property="type")

    ## Ouput the final result
    print("Max directory size: {}".format(result))

def parseCommand(tree, parent_node, dir_stack, param):
    if param[1].startswith("cd"):
        directory = param[2]
        if directory == "/":
            tree.create_node("root", "root", data=File("d", 0))
            directory = "root"
            dir_stack.append(directory)
            print("created root node")
        elif directory == "..":
            current = dir_stack.pop()
            directory = dir_stack[-1]
            tree[directory].data.size += int(tree[current].data.size)
            print("switching to previous dir: " + directory)
        else:
            tree.create_node(directory, directory, parent=parent_node, data=File("d", 0))
            dir_stack.append(directory)
            print("creating new dir: " + directory)
        tree.show()
        # print(dir_stack)
        return directory
    elif param[1].startswith("ls"):
        directory = parent_node
    return directory

def parseFile(tree, parent_node, param):
    size = param[0]
    name = param[1]
    tree.create_node(name, name, parent=parent_node, data=File("f", int(size)))
    tree[parent_node].data.size += int(size)
    # print(tree[parent_node].data.size)
    # tree.show()
    return parent_node

class File(object):
    def __init__(self, type, size):
        self.type = type
        self.size = size

if __name__ == '__main__':
    main()
