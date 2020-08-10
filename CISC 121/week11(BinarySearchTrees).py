def add(tree, value):
    if tree == None:
        newNode = {"data":value, "left":None, "right":None}
        return newNode
    elif tree["data"] == value:
        return tree
    elif value < tree["data"]:
        tree["left"] = add(tree["left"], value)
        return tree
    elif value > tree["data"]:
        tree["right"] = add(tree["right"], value)
        return tree

def height(tree):
    if tree == None:
        return 0
    leftHeight = height(tree["left"])
    rightHeight = height(tree["right"])
    tallestChildHeight = max(leftHeight, rightHeight)
    return 1+ tallestChildHeight

def search(tree, value):
    if tree == None:
        return False
    elif tree["data"] == value:
        return True
    elif value < tree['data']:
        return search(tree['left'],value)
    elif value > tree['data']:
        return search(tree['right'],value)

def toList(tree):
    if tree == None:
        return []
    else:
        leftList = toList(tree['left'])
        rightList = toList(tree['right'])
        return leftList + [tree['data']] + rightList

def display(tree, indent = 0):
    if tree == None:
        return
    else:
        display(tree['right'], indezt +4)
        print(' '*indent + str(tree['data']))
        display(tree['left'], indezt +4)

def delete(tree, value):
    if tree == None:
        return
    elif value < tree['data']:
        tree['left'] = delete(tree['left'], value)
        return tree
    elif value > tree['data']:
        tree['right'] = delete(tree['right'], value)
        return tree
    else:
        ### no subtrees - root is only noode in the tree
        if tree['left'] == None and tree['right'] == None:
            return None
        ### root has a right subtree, but no left subtree
        elif tree['left'] == None:
            return tree['right']
        ### root has a left subtree, but no right subtree
        elif tree['right'] == None:
            return tree['left']
        ###
        else:
            newRoot = maxValue(tree['left'])
            tree['data'] = newRoot
            tree['left'] = delete[tree['left'], newRoot)
            return tree

def maxValue(tree):
    if tree['right'] == None:
        return tree['data']
    else:
        return maxValue(tree['right']











        
