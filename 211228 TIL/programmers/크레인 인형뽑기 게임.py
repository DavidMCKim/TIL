def solution(board, moves):
    new_board = [[board[x][y] for x in range(len(board))] for y in range(len(board))]
    board = new_board
    answer = 0
    stack = []
    for _ in moves:
        for num in range(len(board)):
            if board[_-1][num] == 0:
                pass
            else:
                stack.append(board[_-1][num])
                board[_-1][num] = 0
                break
    for num in range(len(stack)):
        for _ in range(1,len(stack)):
            if stack[_] == 0:
                pass
            elif stack[_-1] == stack[_]:
                stack[_]=0
                stack[_-1] = 0
                answer += 1
        for _ in range(stack.count(0)):
            stack.remove(0)
    answer = answer * 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board,moves)
