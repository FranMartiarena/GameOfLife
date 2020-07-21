import pygame
import random



pygame.init()

screen = pygame.display.set_mode((1100,1000))
screen.fill((0,0,0))
blockSize = 10
dis = 1000 // 100
limits = []
limits2 = []
corners = [[0,0],[0,99],[99,0],[99,99]]


glider = [[0, 10], [1, 10], [2, 10], [2, 9], [1, 8]]

strange_square = [[0, 24], [0, 74], [1, 24], [1, 74], [2, 24], [2, 74], [3, 24], [3, 74], [4, 24], [4, 74], [5, 24], [5, 74], [6, 24], [6, 74], [7, 24], [7, 74], [8, 24], [8, 74], [9, 24], [9, 74], [10, 24], [10, 74], [11, 24], [11, 74], [12, 24], [12, 74], [13, 24], [13, 74], [14, 24], [14, 74], [15, 24], [15, 74], [16, 24], [16, 74], [17, 24], [17, 74], [18, 24], [18, 74], [19, 24], [19, 74], [20, 24], [20, 74], [21, 24], [21, 74], [22, 24], [22, 74], [23, 24], [23, 74], [24, 0], [24, 1], [24, 2], [24, 3], [24, 4], [24, 5], [24, 6], [24, 7], [24, 8], [24, 9], [24, 10], [24, 11], [24, 12], [24, 13], [24, 14], [24, 15], [24, 16], [24, 17], [24, 18], [24, 19], [24, 20], [24, 21], [24, 22], [24, 23], [24, 24], [24, 25], [24, 26], [24, 27], [24, 28], [24, 29], [24, 30], [24, 31], [24, 32], [24, 33], [24, 34], [24, 35], [24, 36], [24, 37], [24, 38], [24, 39], [24, 40], [24, 41], [24, 42], [24, 43], [24, 44], [24, 45], [24, 46], [24, 47], [24, 48], [24, 49], [24, 50], [24, 51], [24, 52], [24, 53], [24, 54], [24, 55], [24, 56], [24, 57], [24, 58], [24, 59], [24, 60], [24, 61], [24, 62], [24, 63], [24, 64], [24, 65], [24, 66], [24, 67], [24, 68], [24, 69], [24, 70], [24, 71], [24, 72], [24, 73], [24, 74], [24, 75], [24, 76], [24, 77], [24, 78], [24, 79], [24, 80], [24, 81], [24, 82], [24, 83], [24, 84], [24, 85], [24, 86], [24, 87], [24, 88], [24, 89], [24, 90], [24, 91], [24, 92], [24, 93], [24, 94], [24, 95], [24, 96], [24, 97], [24, 98], [24, 99], [25, 24], [25, 74], [26, 24], [26, 74], [27, 24], [27, 74], [28, 24], [28, 74], [29, 24], [29, 74], [30, 24], [30, 74], [31, 24], [31, 74], [32, 24], [32, 74], [33, 24], [33, 74], [34, 24], [34, 74], [35, 24], [35, 74], [36, 24], [36, 74], [37, 24], [37, 74], [38, 24], [38, 74], [39, 24], [39, 74], [40, 24], [40, 74], [41, 24], [41, 74], [42, 24], [42, 74], [43, 24], [43, 74], [44, 24], [44, 74], [45, 24], [45, 74], [46, 24], [46, 74], [47, 24], [47, 74], [48, 24], [48, 74], [49, 24], [49, 74], [50, 24], [50, 74], [51, 24], [51, 74], [52, 24], [52, 74], [53, 24], [53, 74], [54, 24], [54, 74], [55, 24], [55, 74], [56, 24], [56, 74], [57, 24], [57, 74], [58, 24], [58, 74], [59, 24], [59, 74], [60, 24], [60, 74], [61, 24], [61, 74], [62, 24], [62, 74], [63, 24], [63, 74], [64, 24], [64, 74], [65, 24], [65, 74], [66, 24], [66, 74], [67, 24], [67, 74], [68, 24], [68, 74], [69, 24], [69, 74], [70, 24], [70, 74], [71, 24], [71, 74], [72, 24], [72, 74], [73, 24], [73, 74], [74, 0], [74, 1], [74, 2], [74, 3], [74, 4], [74, 5], [74, 6], [74, 7], [74, 8], [74, 9], [74, 10], [74, 11], [74, 12], [74, 13], [74, 14], [74, 15], [74, 16], [74, 17], [74, 18], [74, 19], [74, 20], [74, 21], [74, 22], [74, 23], [74, 24], [74, 25], [74, 26], [74, 27], [74, 28], [74, 29], [74, 30], [74, 31], [74, 32], [74, 33], [74, 34], [74, 35], [74, 36], [74, 37], [74, 38], [74, 39], [74, 40], [74, 41], [74, 42], [74, 43], [74, 44], [74, 45], [74, 46], [74, 47], [74, 48], [74, 49], [74, 50], [74, 51], [74, 52], [74, 53], [74, 54], [74, 55], [74, 56], [74, 57], [74, 58], [74, 59], [74, 60], [74, 61], [74, 62], [74, 63], [74, 64], [74, 65], [74, 66], [74, 67], [74, 68], [74, 69], [74, 70], [74, 71], [74, 72], [74, 73], [74, 74], [74, 75], [74, 76], [74, 77], [74, 78], [74, 79], [74, 80], [74, 81], [74, 82], [74, 83], [74, 84], [74, 85], [74, 86], [74, 87], [74, 88], [74, 89], [74, 90], [74, 91], [74, 92], [74, 93], [74, 94], [74, 95], [74, 96], [74, 97], [74, 98], [74, 99], [75, 24], [75, 74], [76, 24], [76, 74], [77, 24], [77, 74], [78, 24], [78, 74], [79, 24], [79, 74], [80, 24], [80, 74], [81, 24], [81, 74], [82, 24], [82, 74], [83, 24], [83, 74], [84, 24], [84, 74], [85, 24], [85, 74], [86, 24], [86, 74], [87, 24], [87, 74], [88, 24], [88, 74], [89, 24], [89, 74], [90, 24], [90, 74], [91, 24], [91, 74], [92, 24], [92, 74], [93, 24], [93, 74], [94, 24], [94, 74], [95, 24], [95, 74], [96, 24], [96, 74], [97, 24], [97, 74], [98, 24], [98, 74], [99, 24], [99, 74]]


square =[[39, 39], [39, 40], [39, 41], [39, 42], [39, 43], [39, 44], [39, 45], [39, 46], [39, 47], [39, 48], [39, 49], [39, 50], [39, 51], [39, 52], [39, 53], [39, 54], [39, 55], [39, 56], [39, 57], [39, 58], [40, 39], [41, 39], [42, 39], [43, 39], [44, 39], [45, 39], [46, 39], [47, 39], [48, 39], [49, 39], [50, 39], [51, 39], [52, 39], [53, 39], [54, 39], [55, 39], [56, 39], [57, 39], [58, 39], [39, 39], [39, 40], [39, 41], [39, 42], [39, 43], [39, 44], [39, 45], [39, 46], [39, 47], [39, 48], [39, 49], [39, 50], [39, 51], [39, 52], [39, 53], [39, 54], [39, 55], [39, 56], [39, 57], [39, 58], [39, 59], [40, 39], [40, 59], [41, 39], [41, 59], [42, 39], [42, 59], [43, 39], [43, 59], [44, 39], [44, 59], [45, 39], [45, 59], [46, 39], [46, 59], [47, 39], [47, 59], [48, 39], [48, 59], [49, 39], [49, 59], [50, 39], [50, 59], [51, 39], [51, 59], [52, 39], [52, 59], [53, 39], [53, 59], [54, 39], [54, 59], [55, 39], [55, 59], [56, 39], [56, 59], [57, 39], [57, 59], [58, 39], [58, 59], [59, 39], [59, 40], [59, 41], [59, 42], [59, 43], [59, 44], [59, 45], [59, 46], [59, 47], [59, 48], [59, 49], [59, 50], [59, 51], [59, 52], [59, 53], [59, 54], [59, 55], [59, 56], [59, 57], [59, 58], [59, 59]]


spaceship = [[1, 3], [2, 3], [3, 3], [4, 3], [4, 4], [4, 5], [3, 6], [0, 4], [0, 6]]

spider = [[22, 44], [22, 43], [21, 43], [19, 43], [18, 43], [18, 42], [19, 42], [21, 41], [22, 41], [21, 40], [21, 39], [21, 38], [20, 38], [19, 39], [18, 39], [17, 39], [17, 40], [23, 40], [23, 39], [23, 38], [24, 39], [25, 39], [25, 38], [26, 37], [27, 38], [28, 38], [29, 40], [29, 41], [29, 42], [31, 42], [31, 41], [31, 40], [32, 38], [33, 38], [34, 37], [35, 38], [35, 39], [36, 39], [37, 39], [37, 38], [37, 40], [38, 41], [39, 41], [39, 40], [39, 39], [39, 38], [40, 38], [41, 39], [42, 39], [43, 39], [43, 40], [39, 43], [38, 43], [38, 44], [41, 43], [41, 42], [42, 42], [42, 43]]

copperhead = [[44, 18], [45, 18], [45, 19], [44, 19], [44, 21], [45, 21], [46, 21], [43, 21], [43, 22], [42, 22], [46, 22], [47, 22], [48, 23], [41, 23], [41, 25], [41, 26], [48, 25], [48, 26], [43, 26], [46, 26], [44, 27], [45, 27], [45, 28], [44, 28], [43, 29], [46, 29], [47, 29], [42, 29]]

Schick_engine = [[29, 28], [29, 29], [29, 30], [30, 30], [31, 30], [32, 30], [33, 29], [30, 27], [33, 27], [29, 34], [30, 34], [31, 34], [32, 34], [29, 35], [29, 36], [30, 37], [33, 35], [33, 37], [35, 33], [35, 32], [35, 31], [36, 31], [37, 31], [36, 33], [37, 33], [36, 32], [38, 32], [39, 32], [42, 30], [43, 30], [43, 31], [44, 31], [43, 33], [44, 33], [43, 34], [42, 34], [46, 32], [47, 32], [48, 32]]


def message(generacion, vivos):
    pygame.draw.rect(screen, (0,0,0), (1010, 0, 90,40))
    font = pygame.font.SysFont(None, 25)
    screen_txt1 = font.render(f"Gen: {str(generacion)}", True, (255,255,255))
    screen_txt2 = font.render(f"Cells: {str(vivos)}", True, (255,255,255))
    screen.blit(screen_txt1, [1010,0])
    screen.blit(screen_txt2, [1010,20])
    pygame.display.flip()

def getNeighbours(position):

    if position in corners:
        if position == corners[0]:
            return [[1,0],[1,1],[0,1]]
        elif position == corners[1]:
            return [[0,98],[1,99],[1,98]]
        elif position == corners[2]:
            return [[98,0],[98,1],[99,1]]
        elif position == corners[3]:
            return [[98,99],[98,98],[99,98]]
    elif position in limits:
        if position[0] == 0:
            return [[position[0]+99,position[1]], [position[0]+99,position[1]-1], [position[0]+99,position[1]+1], [position[0],position[1]-1], [position[0],position[1]+1], [position[0]+1,position[1]], [position[0]+1,position[1]-1], [position[0]+1,position[1]+1]]
        elif position[0] == 99:
            return [[position[0]-99,position[1]], [position[0]-99,position[1]-1], [position[0]-99,position[1]+1], [position[0],position[1]-1], [position[0],position[1]+1], [position[0]-1,position[1]], [position[0]-1,position[1]-1], [position[0]-1,position[1]+1]]
        elif position[1] == 0:
            return [[position[0],position[1]+99], [position[0]+1,position[1]+99], [position[0]-1,position[1]+99], [position[0],position[1]+1], [position[0]-1,position[1]], [position[0]-1,position[1]+1], [position[0]+1,position[1]+1], [position[0]+1,position[1]]]
        elif position[1] == 99:
            return [[position[0],position[1]-99], [position[0]+1,position[1]-99], [position[0]-1,position[1]-99], [position[0],position[1]-1], [position[0]-1,position[1]], [position[0]-1,position[1]-1], [position[0]+1,position[1]-1], [position[0]+1,position[1]]]
    else:
        return [[position[0]-1,position[1]-1], [position[0],position[1]-1], [position[0]+1,position[1]-1], [position[0]-1,position[1]], [position[0]-1,position[1]+1], [position[0],position[1]+1], [position[0]+1,position[1]+1], [position[0]+1,position[1]]]



def drawNextGen(vivos, muertos):
    gen = 0
    while True:
        gen += 1
        new_vivos = []
        new_muertos = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawCells()

        for pos in vivos:
            vecinos_muertos = []
            neighbours = getNeighbours(pos)
            vc = 0
            mc = 0

            for n in neighbours:
                if n in vivos:
                    vc += 1
                elif n in muertos:
                    vecinos_muertos.append(n)
                    mc += 1
            if vc < 2 or vc > 3:
                new_muertos.append(pos)
            elif vc == 2 or vc == 3:
                pass
            for vm in vecinos_muertos:
                v = 0
                m = 0
                for n2 in getNeighbours(vm):
                    if n2 in vivos:
                        v += 1
                    elif n2 in muertos:
                        m += 1
                if v == 3 and vm not in new_vivos:
                    new_vivos.append(vm)

        for nv in new_vivos:
            muertos.remove(nv)
            vivos.append(nv)
            pygame.draw.rect(screen, (255,255,255), ((nv[0])*dis+1, (nv[1])*dis+1, dis-1, dis-1 ))
            pygame.display.flip()

        for nm in new_muertos:
            muertos.append(nm)
            vivos.remove(nm)
            pygame.draw.rect(screen, (0,0,0), ((nm[0])*dis+1, (nm[1])*dis+1, dis-1, dis-1 ))
            pygame.display.flip()

        message(gen, len(vivos))

def drawGrid():
    muertos = []
    vivos = []
    sys = random.choice([glider, strange_square, square, spaceship, spider, copperhead, Schick_engine])
    sys = []
    for x in range(110):
        for y in range(100):
            if x > 100:
                limits2.append([x,y])
                 #rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)#left, top, width, height
                 #pygame.draw.rect(screen, (25,25,25), rect, 1)
            if [x,y] in sys:
                pygame.draw.rect(screen, (255,255,255), ((x)*dis+1, (y)*dis+1, dis-1, dis-1 ))
                vivos.append([x,y])
            else:
                muertos.append([x,y])
                if x == 0 or x == 99 or y == 0 or y == 99:
                    if [x,y] in corners:
                        pass
                    else:
                        limits.append([x,y])
    pygame.display.flip()
    return vivos, muertos

def drawCells():
    screen.fill((0,0,0))
    vivos, muertos = drawGrid()
    message(0,0)
    click = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = 1

            elif event.type == pygame.MOUSEBUTTONUP:
                click = 0

            if click == 1:
                posx, posy = pygame.mouse.get_pos()
                posx = posx // dis
                posy = posy // dis
                if [posx,posy] in limits2:
                    pass
                else:
                    pygame.draw.rect(screen, (255,255,255), ((posx)*dis+1, (posy)*dis+1, dis-1, dis-1 ))
                    if [posx,posy] in vivos:
                        pass
                    else:
                        muertos.remove([posx,posy])
                        vivos.append([posx,posy])

                    pygame.display.flip()

            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    drawNextGen(vivos, muertos)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        else:
            drawCells()

    pass
