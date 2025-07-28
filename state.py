'''
 0   1   2   3   4   5   6   7
URF UFL ULB UBR DFR DLF DBL DRB


0  1  2  3
UR UF UL UB

4  5  6  7 
DR DF DL DB

8  9  10 11
FR FL BL BR


0 - blue
1 - red
2 - white
3 - orange
4 - green
5 - yellow

'''
corner_facelets = [
    [18, 37, 21],   # URF
    [16, 19, 3],    # UFL
    [10, 1, 48],    # ULB 
    [12, 46, 39],   # UBR
    [30, 27, 43],   # DFR
    [28, 9, 25],    # DLF
    [34, 54, 7],    # DBL
    [36, 45, 52],   # DRB
]

corner_colors = [
    [1, 4, 2], 
    [1, 2, 0], 
    [1, 0, 5], 
    [1, 5, 4], 
    [3, 2, 4], 
    [3, 0, 2], 
    [3, 5, 0], 
    [3, 4, 5]
]

edge_facelets = [
    [15, 38],   # UR
    [17, 20],   # UF
    [13, 2],    # UL
    [11, 47],   # UB
    [33, 44],   # DR
    [29, 26],   # DF
    [31, 8],    # DL
    [35, 53],   # DB
    [24, 40],   # FR
    [22, 6],    # FL
    [51, 4],    # BL
    [49, 42]    # BR
]

edge_colors = [
    [1, 4], 
    [1, 2], 
    [1, 0], 
    [1, 5], 
    [3, 4], 
    [3, 2], 
    [3, 0], 
    [3, 5], 
    [2, 4], 
    [2, 0], 
    [5, 0],
    [5, 4]
]

# TODO: fix the orientations


C_n_k = [[0 for i in range(12)] for j in range(12)]

for n in range(12):
    if n == 0:
        C_n_k[n][0] = 1
        continue
    C_n_k[n][0] = 1
    for k in range(1, n + 1):
        C_n_k[n][k] = C_n_k[n - 1][k - 1] + C_n_k[n - 1][k]


class Corner:
    def __init__(self, c, o):
        self.c = c
        self.o = o


class Edge:
    def __init__(self, e, o):
        self.e = e
        self.o = o


def get_cubies_by_facelets(facelets):
    cubies = [[], []] # 0 - corners, 1 - edges
    for corner in corner_facelets:
        cur_corner = [facelets[corner[i] - 1] for i in range(3)]
        flag1 = True
        for j in range(8):
            for offset in range(3):
                flag = True
                for q in range(3):
                    if cur_corner[q - offset] != corner_facelets[j][q]:
                        flag = False
                        break
                if flag:
                    cubies[0].append(Corner(j, offset))
                    flag1 = False
                    break
            if not flag1:
                break
        
    for edge in edge_facelets:
        cur_edge = [facelets[edge[i] - 1] for i in range(2)]
        flag1 = True
        for j in range(12):
            for offset in range(2):
                flag = True
                for q in range(2):
                    if cur_edge[q - offset] != edge_facelets[j][q]:
                        flag = False
                        break
                if flag:
                    cubies[1].append(Edge(j, offset))
                    flag1 = False
                    break
            if not flag1:
                break

    return cubies
            

def get_facelets_by_colors(colors):
    facelets = [5 + i * 9 for i in range(6) for j in range(9)]
    corners = []
    for corner in corner_facelets:
        cur_colors = [colors[corner[i] - 1] for i in range(3)] # цвета угла
        found = False
        for j in range(8):
            for offset in range(3):
                flag = True
                for q in range(3):
                    if cur_colors[q] != corner_colors[j][q - offset]:
                        flag = False
                        break
                if flag:
                    found = True
                    corners.append([j, offset])
                    break
            if found:
                break
    edges = []
    for edge in edge_facelets:
        cur_colors = [colors[edge[i] - 1] for i in range(2)] # цвета ребра
        found = False
        for j in range(12):
            for offset in range(2):
                flag = True
                for q in range(2):
                    if cur_colors[q] != edge_colors[j][q - offset]:
                        flag = False
                        break
                if flag:
                    found = True
                    edges.append([j, offset])
                    break
            if found:
                break
    for i in range(8):
        for j in range(3):
            facelets[corner_facelets[i][j] - 1] = corner_facelets[corners[i][0]][j - corners[i][1]]
    for i in range(12):
        for j in range(2):
            facelets[edge_facelets[i][j] - 1] = edge_facelets[edges[i][0]][j - edges[i][1]]

    return facelets


class State:
    def __init__(self, facelets):
        self.cubies = get_cubies_by_facelets(facelets)

        self.facelets = facelets

        self.coordinates = [0, 0, 0, 0]
        self.update_coordinates()

    def update(self, facelets):
        self.cubies = get_cubies_by_facelets(facelets)
        self.facelets = facelets
        self.update_coordinates()

    def update_facelets(self):
        for i in range(8):
            corner = self.cubies[0][i]
            for j in range(3):
                self.facelets[corner_facelets[i][j] - 1] = corner_facelets[corner.c][j - corner.o]

        for i in range(12):
            edge = self.cubies[1][i]
            for j in range(2):
                self.facelets[edge_facelets[i][j] - 1] = edge_facelets[edge.e][j - edge.o]


    def update_coordinates(self):
        self.coordinates[0] = 0
        factor = 1
        for i in range(7):
            self.coordinates[0] += self.cubies[0][7 - i].o * factor
            factor *= 3

        self.coordinates[1] = 0
        factor = 1
        for i in range(11):
            self.coordinates[1] += self.cubies[1][11 - i].o * factor
            factor *= 2

        self.coordinates[2] = 0
        factor = 1
        for i in range(7, 0, -1):
            cnt = 0
            for j in range(i):
                if self.cubies[0][j].c > self.cubies[0][i].c:
                    cnt += 1
            self.coordinates[2] += cnt * factor
            factor *= 8

        self.coordinates[3] = 0
        factor = 1
        for i in range(11, 0, -1):
            cnt = 0
            for j in range(i):
                if self.cubies[1][j].e > self.cubies[1][i].e:
                    cnt += 1
            self.coordinates[3] += cnt * factor
            factor *= 12


    def implement_move(self, move):
        new_corners = []
        new_edges = []
        for i in range(8):
            new_corners.append(Corner(self.cubies[0][move.c_table[i][0]].c, (self.cubies[0][move.c_table[i][0]].o + move.c_table[i][1]) % 3))
        for i in range(12):
            new_edges.append(Edge(self.cubies[1][move.e_table[i][0]].e, self.cubies[1][move.e_table[i][0]].o + move.e_table[i][1]))
        self.cubies = [new_corners, new_edges]
        self.update_facelets()
        self.update_coordinates()

class PhaseOneState(State):
    def __init__(self, facelets):
        super().__init__(facelets)
        self.UDSlice = 0
        self.update_UDSlice()
    
    def update_UDSlice(self):
        self.UDSlice = 0
        k = -1
        for i in range(12):
            if self.cubies[1][i].e >= 8:
                k += 1
            elif k >= 0:
                self.UDSlice += C_n_k[i][k]

    def update(self, facelets):
        super().update(facelets)

        self.update_UDSlice()

    def implement_move(self, move):
        super().implement_move(move)
        self.update_UDSlice()


        
