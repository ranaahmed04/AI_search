if __name__ == '__main__':
    graph = {
        '5': (0, [('3',0),('7',0)]),
        '3': (0, [('2',0),('4',0)]),
        '7': (0, [('8',0)]),
        '2': (0, []),
        '4': (0, [('8',0)]),
        '8': (0, [])
    }

    visited = []  # List for visited nodes.
    queue = []  # Initialize a queue


    def bfs(visited, graph, start):  # function for BFS
        visited.append(start)
        queue.append(start)

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)
            print(m, end=" ")

            for neighbour in graph[m][1]:
                if neighbour[0] not in visited:
                    visited.append(neighbour[0])
                    queue.append(neighbour[0])


    # Driver Code
   #print("Following is the Breadth-First Search")
   # bfs(visited, graph, '5')  # function calling


def dfs(visited, graph, start):  # function for dfs
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
        for neighbour in graph[start][1]:
            dfs(visited, graph, neighbour[0])

    # Driver Code

print("Following is the Depth-First Search")
dfs(visited, graph, '5')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
