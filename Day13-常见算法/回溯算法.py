"""
回溯法 回溯法又称试探法 按选优条件向前搜索 当搜索到某一步发现原先选择并不优
或达不到目标时 就退回一步重新选择
"""
'''
骑士巡逻 是指按照国际象棋中骑士的规定走法走遍整个棋盘的每一个方格 而且每个
网格只能够经过一次 假如骑士能够走回最初的位置 则称为封闭巡逻
'''
import sys
import time

SIZE = 5
total = 0

def print_board(board):
    for row in board:
        for col in row:
            # 使用字符串的居中方法
            print(str(col).center(4), end='')
        print()

def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col <SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法：')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0

def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)

if __name__ == '__main__':
    main()






































