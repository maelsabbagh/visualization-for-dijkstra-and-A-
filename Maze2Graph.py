# todo: get a map as input, transform the map to a graph based on BFS algorithm.
#       For each edge calculate the cost and for each node, calculate the Heuristic
from Maze import MazeCellType
from Utils import ShortestPathBFS
import math


class Maze2Graph:
    def __init__(self, maze_2d, cell_size):
        self.maze = maze_2d
        self.cell_size = cell_size

    def transform2Graph(self):
        graph_nodes = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                       if self.maze[row][col] == MazeCellType.DOOR]
        start = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.START_DOOR][0]
        target = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                  if self.maze[row][col] == MazeCellType.TARGET_DOOR][0]

        graph_nodes.insert(0, start)
        graph_nodes.append(target)

        graph_edges = []

        for i in range(len(graph_nodes)):
            graph_edges.append([])

        ## Student Code: Connect Edges,
        # for each node,
        #   Find the reachable doors. Hint: use BFS on the given array
        #   Add an edge between the current node and each reachable doors
        for i in graph_nodes:
            for j in graph_nodes:
                boo = False
                # print(i[0]," ",j[0])
                cost = ShortestPathBFS.get_shortest_path(self.maze, i[0], j[0])
                print("COST : ", cost)
                if len(cost) != 0:
                    for m in cost:
                        for n in graph_nodes:
                            if m == n[0] and m != cost[0]:
                                boo = True
                                print("LA2ETOOO : ", m)
                                break
                        if boo == True:
                            break
                    if not boo:
                        x = graph_nodes.index(j)
                        y = graph_nodes.index(i)
                        tuple1 = (x, len(cost))
                        graph_edges[y].append(tuple1)
                        print("EDGE : ", tuple1)
        # print(graph_edges)
        ##############################################################

        ## Student Code: Calculate H(n)
        #   After adding the edges, loop on the node and calculate the H(n) where n is the node index
        #   H(n) is saved as the second value in the node,
        #   where the first value is its original location in the maze
        #   Hint: H(n) is the euclidian distance between the node and the Target Node
        h = []
        for i in graph_nodes:
            x1 = i[0][0]
            y1 = i[0][1]
            x2 = target[0][0]
            y2 = target[0][1]

            h1 = math.pow(abs(x2 - x1), 2) + math.pow(abs(y2 - y1), 2)
            H = math.sqrt(h1)
            h.append(H)
        #
        ###############################################################

        ## Output for Test Case: debugging_level.lvl
        # Comment/remove this line when you are done
        # return graph_nodes, [[(2, 2)], [(2, 4), (3, 4)], [(0, 2), (1, 4)], [(1, 4)]]
        #########################################################################################

        return graph_nodes, graph_edges, h, self.maze
