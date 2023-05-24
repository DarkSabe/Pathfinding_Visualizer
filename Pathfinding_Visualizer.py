"""
@Author: Jaden Chang
Created: 2023-05-04
"""
import pygame, math
from queue import PriorityQueue

#Initializes pygame
pygame.init()

#RGB colour values and assigns them
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (57,255,20)
RED = (255,49,49)
GREY = (169,169,169)
CYAN = (0,100,100)
PURPLE = (160,32,240)
YELLOW = (255,255,0)

#Initializes the pygame screen
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, WIDTH))
screen.fill(WHITE)
pygame.display.update()

#A class to define each node
class Node:
    #Node class constructor
    def __init__(self,row,col,width,total_rows):
        self.colour = WHITE
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.neighbours = []

    #Sets the state of the node
    def set_start(self):
        self.colour = GREEN
    def set_end(self):
        self.colour = RED
    def set_visted(self):
        self.colour = PURPLE
    def set_open(self):
        self.colour = CYAN
    def set_path(self):
        self.colour = YELLOW
    def set_wall(self):
        self.colour = BLACK
    def set_unvisited(self):
        self.colour = WHITE

    #Checks the state of the node
    def is_start(self):
        return self.colour == GREEN
    def is_end(self):
        return self.colour == RED
    def is_visited(self):
        return self.colour == PURPLE
    def is_open(self):
        return self.colour == CYAN
    def is_path(self):
        return self.colour == YELLOW
    def is_wall(self):
        return self.colour == BLACK
    def is_unvisited(self):
        return self.colour == WHITE
    
    #Draws the node onto the screen
    def draw_node(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.width))

    def neighbours(self):
        pass

#Creates the grid and each node
def add_grid(rows, width):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, width // rows, rows)
            grid[i].append(node)
    return grid

#Draws the grid lines
def draw_grid(screen, width, rows):
    node_width = width // rows
    for i in range(rows):
        pygame.draw.line(screen, GREY, (0, node_width * i), (width, node_width * i))
        pygame.draw.line(screen, GREY, (node_width * i, 0), (node_width * i, width))

#Draws all of the visual components 
def draw_all(screen, width, rows, grid):
    screen.fill(WHITE)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw_node(screen)
    draw_grid(screen, width, rows)
    pygame.display.update()

#Main function that computes user's input
def main(screen, width):
    rows = 36 #Have the user specify later on how many rows (set amount 36, 100, etc)

    grid = add_grid(rows, width)
    start = None
    end = None

    running = True
    started = False

    while running:
        draw_all(screen, width, rows, grid)
        #Checks user's event actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                (point_x, point_y) = pygame.mouse.get_pos()
                (pos_x, pos_y) = ((point_x // (width // rows)), (point_y // (width // rows)))
                if start == None and end != grid[pos_x][pos_y]:
                    start = grid[pos_x][pos_y]
                    grid[pos_x][pos_y].set_start()
                elif start != None and end == None and start != grid[pos_x][pos_y]:
                    end = grid[pos_x][pos_y]
                    grid[pos_x][pos_y].set_end()
                elif start != grid[pos_x][pos_y] and end != grid[pos_x][pos_y]:
                    grid[pos_x][pos_y].set_wall()
                           
            if pygame.mouse.get_pressed()[2]:
                (point_x, point_y) = pygame.mouse.get_pos()
                (pos_x, pos_y) = ((point_x // (width // rows)), (point_y // (width // rows)))
                if start == grid[pos_x][pos_y]:
                    start = None
                elif end == grid[pos_x][pos_y]:
                    end = None
                grid[pos_x][pos_y].set_unvisited()
                
main(screen, WIDTH)