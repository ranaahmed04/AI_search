# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ucs( graph, start, goal):
    visited = []
    queue = [[start,0]]
    while len(queue) > 0:
        newQueue = []
        min = 99999
        minNode = None
        while queue:
            (node,cost) = queue.pop(0)
            if cost < min:
                newQueue.append((minNode, min))
                min = cost
                minNode = node
            else:
                newQueue.append((node,cost))
        queue = newQueue
        if minNode in visited:
            continue
        if minNode in goal:
            visited.append(minNode)
            print("goal reached")
            print(visited)
            return minNode
            break
        else:
            visited.append(minNode)
            nextNodes = graph[minNode][1]
            for (node,cost) in nextNodes:
                queue.append((node, cost + min))


if __name__ == '__main__':
    graph = {
        'S': (0,[('A', 2), ('B', 3), ('D', 5)]),
        'A': (0,[('C', 4)]),
        'B': (0,[('D', 4)]),
        'C': (0,[('D', 1), ('G', 2)]),
        'D': (0,[('G', 5)]),
        'G': (0,[])
    }
    solution = ucs(graph,'S','G')
    print('Solution is ', solution)