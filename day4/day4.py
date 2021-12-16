def score(board):
    sum = 0
    for x in board:
        for y in x:
            if y != '_':
                sum += int(y)

    return sum

def replace_number(board, num):
    return [[y if y != num else '_' for y in x] for x in board]

def wins(board):
    # Rows
    for row in board:
        if all([x == '_' for x in row]):
            return True, score(board)

    # Columns
    for column_idx in range(len(board[0])):
        if all([x == '_' for x in [y[column_idx] for y in board]]):
            return True, score(board)
 
    return False, None

def check_board(board, draw):
    for idx, d in enumerate(draw):
        board = replace_number(board, d)
        if (value := wins(board))[0]:
            return idx, value[1] * int(d)

    return None

def main():
    with open('input') as f:
        content = f.read()

    content = content.split('\n\n')

    draw = [x.strip() for x in content[0].split(',')]
    boards = [[y.split() for y in x.split('\n')] for x in content[1:]]

    scores = [check_board(b, draw) for b in boards]

    scores = sorted(scores, key=lambda x: x[0])

    print(scores[-1])

    
if __name__ == '__main__':
    main()