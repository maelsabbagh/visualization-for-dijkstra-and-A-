from enum import Enum
from Maze2Graph import Maze2Graph
from queue import PriorityQueue

oo = 0x3f3f3f3f3f3f3f3f

class GraphAlgorithm(Enum):
    ASTAR = 1,
    DIJKSTRA = 2


class Graph:
    def __init__(self, maze, algorithm_type):
        q=Maze2Graph(maze.maze_cells, maze.cell_size).transform2Graph()
        self.graph_nodes=q[0]
        self.graph_edges= q[1]
        self.h=q[2]
        self.maze=q[3]
        self.graph_algorithm = algorithm_type

    def find_shortest_path(self):
        ## Path for the debugging_level.lvl
        # remove this line when running your code.
       # return [self.graph_nodes[0][0], self.graph_nodes[2][0], self.graph_nodes[1][0], self.graph_nodes[3][0]]
        ########################

        if self.graph_algorithm == GraphAlgorithm.ASTAR:
            return self.__run_astar()

        if self.graph_algorithm == GraphAlgorithm.DIJKSTRA:
            return self.__run_dijkstra()

    def __run_astar(self):
        openQueue = PriorityQueue()
        parentList = []
        closedList = []
        distance = []
        start=0
        destination=len(self.graph_nodes) - 1
        for i in self.graph_edges:
            distance.append(oo)
            parentList.append(-1)

        openQueue.put((self.h[start], start))
        distance[start] = 0
        while (not openQueue.empty()):
            l = openQueue.get()
            closedList.append(l)
            node = l[1]

            if (node == destination):
                break
            for neigh in self.graph_edges[node]:
                val1 = neigh[0]
                val2 = neigh[1]
                c = distance[node] + val2
                if (c < distance[val1]):
                    distance[val1] = c
                    parentList[val1] = node

                f = distance[val1] + self.h[val1]
                if (not ((f, val1) in closedList)):
                    openQueue.put((f, val1))

        shortestpath = []
        shortestpath.append(destination)
        p = parentList[destination]
        while p != -1:
            shortestpath.append(p)
            p = parentList[p]
        shortestpath.reverse()
        final = []
        for a in shortestpath:
            for b in self.graph_nodes:
                if self.graph_nodes.index(b) == a:
                    final.append(b[0])
                    break
        return final,self.maze



    def __run_dijkstra(self):
        dis = []
        par = []

        src = 0
        des = len(self.graph_nodes) - 1
        for i in self.graph_edges:
            dis.append(oo)
            par.append(-1)
        dis[src] = 0
        pq = PriorityQueue()
        pq.put((0, src))
        while (not pq.empty()):
            t = pq.get()
            u = t[1]
            c = -t[0]
            if (dis[u] != c):
                continue
            for neigh in self.graph_edges[u]:
                v = neigh[0]
                vc = neigh[1]
                if dis[u] + vc < dis[v]:
                    dis[v] = dis[u] + vc
                    par[v] = u
                    pq.put((-dis[v], v))
        path = []
        path.append(des)
        parent = par[des]
        while parent != -1:
            path.append(parent)
            parent = par[parent]
        path.reverse()
        final = []
        for a in path:
            for b in self.graph_nodes:
                if self.graph_nodes.index(b) == a:
                    final.append(b[0])
                    break
        print(final)
        return final,self.maze

