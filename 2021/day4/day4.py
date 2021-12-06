def create_boards(_input):
    boards = []
    board_number = 0
    i = 2
    single_board = []
    for line in _input[2:]:
        line_split = line.split(" ")
        [single_board.append(int(x)) for x in line_split if x != ""]
        if len(line) == 0 or line == _input[-1]:
            boards.append(single_board)
            single_board = []
    board_numbers = list(range(len(boards)))
    return boards, board_numbers

def play_bingo(numbers, boards, board_numbers, mode="win"):
    bingo = []
    for x in boards:
        bingo.append({"row": [0, 0, 0, 0, 0], "col": [0, 0, 0, 0, 0]})
    for draw in numbers:
        for board in boards:
            try:
                i = boards.index(board)
                pos = board.index(draw)
                row = pos // 5
                col = pos % 5
                bingo[i]["row"][row] += 1
                bingo[i]["col"][col] += 1
                if bingo[i]["row"][row] == 5 or bingo[i]["col"][col] == 5:
                    if mode == "win":
                        winner = board
                        return winner, draw
                    else:
                        last_board = board_numbers.pop(board_numbers.index(i))
                        if len(board_numbers) == 0:
                            winner = board
                            return winner, draw
            except ValueError:
                pass
        else:
            continue
        break

with open("2021/day4/input.txt", "r") as file:
    _input = [x.strip() for x in file.readlines()]

numbers = _input[0].split(",")
numbers = [int(x) for x in numbers]


# part 1
boards, board_numbers = create_boards(_input)
winner, draw = play_bingo(numbers, boards, board_numbers, mode="win")
used_numbers = numbers[:numbers.index(draw)+1]
sum_of_unmarked = sum([x for x in winner if x not in used_numbers])
final_score = sum_of_unmarked * draw
print(f"Part 1: {final_score}")


# part 2
boards, board_numbers = create_boards(_input)
winner, draw = play_bingo(numbers, boards, board_numbers, mode="lose")
used_numbers = numbers[:numbers.index(draw)+1]
sum_of_unmarked = sum([x for x in winner if x not in used_numbers])
final_score = sum_of_unmarked * draw
print(f"Part 2: {final_score}")
