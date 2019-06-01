"""
回溯法 回溯法又称试探法 按选优条件向前搜索 当搜索到某一步发现原先选择并不优
或达不到目标时 就退回一步重新选择 其实就是枚举 往一个方向枚举下试试 如果行就
继续 如果不行 就回来换个方向继续枚举
"""
'''
骑士巡逻 是指按照国际象棋中骑士的规定走法走遍整个棋盘的每一个方格 而且每个
网格只能够经过一次 假如骑士能够走回最初的位置 则称为封闭巡逻
'''
#
# SIZE = 5
# total = 0
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             # 使用字符串的居中方法
#             print(str(col).center(4), end='')
#         print()
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col <SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法：')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
#
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
# if __name__ == '__main__':
#     main()

'''
想要搞明白回溯算法，没有别的方法只能多做题！做着做着就明白了！

问题描述：
地上有一个m行和n列的机器人,一个机器人从坐标0, 0的格式开始移动，每一次只能向左、右、上、下
四个方向移动一格 但是不能进入行坐标和列坐标的数位之和大于K的格子。例如，当K为18时，机器人能够
进入方格(35, 37)，因为3+5+3+7 = 18 但是，它不能进入方格(35, 38),因为3+5+3+8 = 19
请问该机器人能够达到多少个格子？

问题分析：
当机器人每走到一个点呢，我们就让它继续去走接下来的四个方向。如果碰到回溯点，也就是边界条件，那么
就返回上一步，这个思维可以用什么实现呢？递归！每次传入的参数就是接下来的方向！那么，边界条件是什么呢？
1. 坐标出去了 2. 这个格子已经走过了 3. K < sum
'''
def k_sum(k, row, col):
    """用来判定K和两个坐标和的关系"""

    coordi_str = str(row) + str(col)
    coordi_sum = 0
    for num in coordi_str:
        coordi_sum += int(num)
    return coordi_sum <= k

def trverse(k, cur_row, cur_col, board):
    """回溯函数"""

    # 边界条件 回溯
    if cur_row >= len(board) or cur_col >= len(board[0]) or \
            cur_row < 0 or cur_col < 0:
        return
    if board[cur_row][cur_col]:
        return
    if not k_sum(k, cur_row, cur_col):
        return
    # 标记当前格子走过了
    board[cur_row][cur_col] = 1
    global count
    count += 1
    # 向四个方向走 其实也就是挨个试探 试探之后如果不行就回来 然后往另一个方向走
    trverse(k, cur_row + 1, cur_col, board)
    trverse(k, cur_row , cur_col + 1, board)
    trverse(k, cur_row - 1, cur_col , board)
    trverse(k, cur_row, cur_col - 1, board)
    # 回溯之后 并不需要取消标记 是因为现在的问题是要记录一共
    # 能走的格子数目 并不是找路径 因此并不需要撤销标记
    # board[cur_row][cur_col] = 0

if __name__ == '__main__':
    m, n, k, count = 5, 4, 3, 0
    board = [[0] * n for _ in range(m)]
    trverse(k, 0, 0, board)
    print(count)

































