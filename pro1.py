class Graph:
    def addNode(node, connectedNode):
        if node not in graph :
                graph[node] = []

        if connectedNode not in graph :
            graph[connectedNode] = []

        graph[node].append(connectedNode)
        graph[connectedNode].append(node)

    def printGraph():
        for i in graph :
            print(i, end = " : ")
            print(graph[i])

    def dfs(root):
        if root not in visited :
            print(root)
            visited.append(root)
        for i in graph[root] :
            if i not in visited :
                Graph.dfs(i)

    def bfs(queue) :
        if not queue:
            return
        
        currentNode = queue.pop(0)
        print(currentNode)
        visited.append(currentNode)

        for i in graph[currentNode] :
            if i not in visited :
                visited.append(i)
                queue.append(i)
                
        Graph.bfs(queue)



if(__name__ == "__main__") :
    graph = {}
    for i in range(int(input("Enter Total number of Edges : "))) :
        node = input("Enter Node : ")
        connectedNode = input("Enter Connected Node : ")
        Graph.addNode(node, connectedNode)

    visited = []
    root = input("\nEnter Start Node : ")
    queue = [root]
    Graph.bfs(queue)
    
    # visited = []
    # root = input("Enter Start ")
    # Graph.dfs(root)
