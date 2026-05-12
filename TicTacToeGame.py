import pygame
import sys

pygame.init()
pygame.font.init()

    
WIDTH, HEIGHT = 600, 750
BG_COLOR = (100,100,100)


class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.winning_line = None
        
        self.running = True
        
    def draw_winning_line(self):
        if not self.winning_line:
            return
        (start_row, start_col), (end_row, end_col) = self.winning_line
        start_pos = (start_col * 200 + 100, start_row * 200 + 100)
        end_pos = (end_col * 200 + 100, end_row * 200 + 100)
        pygame.draw.line(self.screen, (144, 238, 144), start_pos, end_pos, 15)

    def draw_board(self):
        self.screen.fill(BG_COLOR)
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 200), (600, i * 200), 5)
        for row in range(3):
            for col in range(3):
                x = col * 200 + 100
                y = row * 200 + 100
                if self.board[row][col] == "X":
                    pygame.draw.line(self.screen, (255, 0, 0), 
                                   (x - 50, y - 50), (x + 50, y + 50), 15)
                    pygame.draw.line(self.screen, (255, 0, 0), 
                                   (x + 50, y - 50), (x - 50, y + 50), 15)
                elif self.board[row][col] == "O":
                    pygame.draw.circle(self.screen, (0,0,255), (x,y), 50, 15)
        
        if self.winning_line:
            self.draw_winning_line()
            
    def check_win(self,player):
        for i in range(3):
            #vertical and horizontal
            if all(self.board[i][j] == player for j in range(3)):
                self.winning_line = ((i, 0), (i, 2))
                return True
            if all(self.board[j][i] == player for j in range(3)):
                self.winning_line = ((0, i), (2, i))
                return True
            
            #diagonal and backwards diagonal
            if all (self.board[j][j] == player for j in range(3)):
                self.winning_line = ((0, 0), (2, 2))
                return True
            if all (self.board[j][2-j] == player for j in range(3)):
                self.winning_line = ((0, 2), (2, 0))
                return True
        return False
    
    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_win(self.current_player):
                self.game_over = True
                self.winner = self.current_player
            elif all(self.board[r][c] != "" for r in range(3) for c in range(3)):
                self.game_over = True
                self.winner = "No one"
            else:
                if self.current_player == "X":
                    self.current_player = "O" 
                else: self.current_player = "X"
    
    def drawWin(self):
        font = pygame.font.SysFont(None, 45)
        if self.winner == None:
            text = font.render(f"Player {self.current_player}'s turn. Press R to reset.", True, (255, 255, 255))
        else:
            text = font.render(f"{self.winner} wins! Press R to reset.", True, (255, 255, 255))
        self.screen.blit(text, (50, 650))
            
    def get_cell(self, pos):
        x, y = pos
        if x < 200:
            col = 0
        elif x < 400:
            col = 1
        else:
            col = 2
        if y < 200:
            row = 0
        elif y < 400:
            row = 1
        else:
            row = 2
        return row, col
    
    
    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.winning_line = None
        
    def handle_click(self, pos):
        row, col = self.get_cell(pos)
        self.make_move(row, col)
            
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    if event.button == 1:  
                        self.handle_click(event.pos)
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()
            self.draw_board()
            self.drawWin()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
        
        
        
        
        
#Run the game        
game = TicTacToe()
game.run()