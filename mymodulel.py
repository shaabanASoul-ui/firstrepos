#
# def helo(name):
#       return " Hello "+name
#
# def posval(ints):
#        if ints <0:
#               return -1*ints
#        else:
#               return ints
#
#
# def popa(l):
#         print("the  list before del l[1]",l)
#         print("*"*34)
#
#         for i in range((len(l)-1)):
#             print("the  list before del l[1]", l)
#             del(l[1])
#             print("the list after del l[1]",l)
#         return l
#
#
#
#
# def foral( l):
#        lk=[]
#
#        for i in l:
#               i=i//2
#
#               lk.append(i)
#               y=[]
#               for i in lk:
#                  i=i//5
#                  y.append(i)
# import pygame
# import random
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the game window
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("DFS Game")
#
# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
#
# # DFS class
# class DFS:
#     def __init__(self):
#         self.board = [[0 for _ in range(10)] for _ in range(10)]
#         self.start = None
#         self.end = None
#
#     def set_start(self, x, y):
#         if 0 <= x < 10 and 0 <= y < 10:
#             self.start = (x, y)
#             self.board[x][y] = 'S'
#
#     def set_end(self, x, y):
#         if 0 <= x < 10 and 0 <= y < 10:
#             self.end = (x, y)
#             self.board[x][y] = 'E'
#
#     def dfs(self):
#         if self.start is None or self.end is None:
#             return False
#
#         visited = set()
#         stack = [self.start]
#
#         while stack:
#             x, y = stack.pop()
#             if (x, y) == self.end:
#                 return True
#
#             if (x, y) not in visited:
#                 visited.add((x, y))
#                 directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#                 random.shuffle(directions)
#                 for dx, dy in directions:
#                     nx, ny = x + dx, y + dy
#                     if 0 <= nx < 10 and 0 <= ny < 10 and self.board[nx][ny] == 0:
#                         stack.append((nx, ny))
#                         self.board[nx][ny] = 'P'
#
#         return False
#
# # Game class
# class Game:
#     def __init__(self):
#         self.dfs = DFS()
#         self.autoplay = True
#         self.running = True
#
#     def draw_board(self):
#         screen.fill(WHITE)
#         for y in range(10):
#             for x in range(10):
#                 rect = pygame.Rect(x * 80, y * 80 + 100, 80, 80)
#                 if self.dfs.board[x][y] == 'S':
#                     pygame.draw.rect(screen, (255, 0, 0), rect)
#                 elif self.dfs.board[x][y] == 'E':
#                     pygame.draw.rect(screen, (0, 255, 0), rect)
#                 elif self.dfs.board[x][y] == 'P':
#                     pygame.draw.rect(screen, (0, 0, 255), rect)
#                 else:
#                     pygame.draw.rect(screen, BLACK, rect, 2)
#
#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 x //= 80
#                 y = (y - 100) // 80
#                 if self.dfs.board[x][y] == 0:
#                     self.dfs.set_start(x, y)
#                 elif self.dfs.board[x][y] == 'S':
#                     self.dfs.set_end(x, y)
#                 elif self.dfs.board[x][y] == 'P':
#                     self.dfs.board[x][y] = 0
#
#     def update(self):
#         if self.autoplay:
#             if not self.dfs.dfs():
#                 print("No path found")
#             else:
#                 print("Path found!")
#
#     def run(self):
#         clock = pygame.time.Clock()
#         while self.running:
#             self.handle_events()
#             self.update()
#             self.draw_board()
#             pygame.display.flip()
#             clock.tick(60)
#
# # Main function
# def main():
#     game = Game()
#     game.run()
#
# if __name__ == "__main__":
#     main()



print("helloo")
if __name__=="__main__":
             print("the apply is Directed ")
             def hel():
                  print("hello function  ")
else:
          print("the apply is not from  same file ")


hel()



