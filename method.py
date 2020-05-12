class Astar:
    def __init__(self, start_x, start_y, goal_x, goal_y, bans, R_L, L_L, U_L, D_L):
        self.R_L = R_L
        self.L_L = L_L
        self.U_L = U_L
        self.D_L = D_L
        self.start_x = start_x
        self.start_y = start_y
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.bans = bans
        self.openlist = list()
        self.closedlist = list()
        self.truelist = list()
        self.directionlist = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        self.arrive = False
        self.usedtopoint = list()

    def open_node(self, node):
        node.rcost = abs(self.start_x - node.x) + abs(self.start_y - node.y)
        node.hcost = abs(self.goal_x - node.x) + abs(self.goal_y - node.y)
        if node.hcost == 0:
            self.truelist.append(node)
            self.arrive = True
        node.score = node.rcost + node.hcost
        if [node.x, node.y] not in self.usedtopoint and [node.x, node.y] not in self.bans:
            self.openlist.append(node)
            self.usedtopoint.append([node.x, node.y])

    def open_around(self, node):
        for i in range(len(self.directionlist)):
            if not (node.x + self.directionlist[i][0] > self.L_L and node.x + self.directionlist[i][0] < self.R_L):
                continue
            if not (node.y + self.directionlist[i][1] > self.U_L and node.y + self.directionlist[i][1] < self.D_L):
                continue
            new_node = Node(
                node.x + self.directionlist[i][0], 
                node.y + self.directionlist[i][1],
                node
                )
            self.open_node(new_node)
        self.closedlist.append(node)
        self.openlist.remove(node)

    def run_method(self):
        node = Node(self.start_x, self.start_y, 0)
        self.open_node(node)
        while not self.arrive:
            self.open_around(
                self.openlist[
                    [i.score for i in self.openlist].index(
                        min(
                            [
                                i.score for i in self.openlist
                            ]
                        )
                    )
                ]
            )
            # print([[i.x, i.y, i.score] for i in self.openlist])

    def output_root(self):
        while not (self.truelist[-1].x == self.start_x and self.truelist[-1].y == self.start_y):
            self.truelist.append(self.truelist[-1].p)
        # print([[i.x, i.y] for i in self.truelist])
        return [[i.x, i.y] for i in self.truelist]


class Node:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.rcost = 0
        self.hcost = 0
        self.score = 0
        self.p = p

if __name__ == "__main__":
    Bans = []
    a = Astar(0, 0, 10, 10, Bans)
    a.run_method()
    print(a.output_root())
