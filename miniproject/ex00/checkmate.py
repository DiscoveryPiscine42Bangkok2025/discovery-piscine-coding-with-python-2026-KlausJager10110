def checkmate(board: str):
    pawn_directions = [(-1, -1), (-1, 1)]
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    queen_directions = rook_directions + bishop_directions

    ### < ตรวจสอบความถูกต้องของกระดาน > ###
    validate_result = validate_board(board)
    # print(x["valid"], x["reason"])

    if not validate_result["valid"]:
        print(f"Error: {validate_result['reason']}")
        return

    ### < แปลงตารางที่เป็น str => array-2D > ###
    board_2d = parse_board_to_array2d(board)
    # print(board_2d)
    # print(board_2d[1][2])


    ### < ค้นหาตำแหน่งของ King > ###
    king_position = None

    for r, row in enumerate(
        board_2d
    ):  # board_2d = [['B', '.', '.', '.'], ['.', '.', 'K', '.'], ['.', '.', 'P', '.'], ['.', '.', '.', '.']]
        # loop 1: r=0, row=['B', '.', '.', '.']
        for c, cell in enumerate(row):  # row=['B', '.', '.', '.']
            # loop 1: c=0, cell='B'
            if cell.upper() == "K":
                king_position = (r, c)
                break

    # print(f"King position: {king_position}")

    ### < ตรวจสอบว่ามีหมากตัวไหนที่สามารถกิน King ได้ > ###
    for r in range(len(board_2d)):
        for c in range(len(board_2d)):

            piece = board_2d[r][c]

            if piece == ".":
                continue
            elif piece.upper() == "K":
                continue

            piece = piece.upper()
            # print(f"Checking piece: {piece} at {(r, c)}")

            if piece == "P":
                for direction in pawn_directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]

                    if 0 <= new_r < len(board_2d) and 0 <= new_c < len(board_2d):
                        if (new_r, new_c) == king_position:
                            print("Success")
                            return

            elif piece == "R":
                for direction in rook_directions:
                    new_r, new_c = r, c
                    while True:
                        new_r += direction[0]
                        new_c += direction[1]
                        if 0 <= new_r < len(board_2d) and 0 <= new_c < len(board_2d):
                            if (new_r, new_c) == king_position:
                                print("Success")
                                return
                            if board_2d[new_r][new_c] != ".":
                                break
                        else:
                            break

            elif piece == "B":
                for direction in bishop_directions:
                    new_r, new_c = r, c
                    while True:
                        new_r += direction[0]
                        new_c += direction[1]
                        if 0 <= new_r < len(board_2d) and 0 <= new_c < len(board_2d):
                            if (new_r, new_c) == king_position:
                                print("Success")
                                return
                            if board_2d[new_r][new_c] != ".":
                                break
                        else:
                            break

            elif piece == "Q":
                for direction in queen_directions:
                    new_r, new_c = r, c
                    while True:
                        new_r += direction[0]
                        new_c += direction[1]
                        if 0 <= new_r < len(board_2d) and 0 <= new_c < len(board_2d):
                            if (new_r, new_c) == king_position:
                                print("Success")
                                return
                            if board_2d[new_r][new_c] != ".":
                                break
                        else:
                            break
    print("Fail")


def validate_board(board: str) -> dict:

    ### < ตรวจสอบว่าตารางไม่ว่าง > ###
    if not isinstance(board, str):
        return {"valid": False, "reason": "Board must be a string."}

    board = board.strip()

    if board == "":
        return {"valid": False, "reason": "Board is empty."}

    lines = board.splitlines()
    lines_without_space = [s.strip() for s in lines]

    row_count = len(lines_without_space)
    # print(lines_without_space, row_count)

    ### < ตรวจสอบว่าเป็นตารางจัตุรัสหรือไม่ หรือมีแถวเปล่า > ###
    for line in lines_without_space:
        if line == "":
            return {"valid": False, "reason": "Board contains empty lines."}
        if len(line) != row_count:
            return {"valid": False, "reason": "Board is not square."}

    ### < ตรวจสอบว่ามีตัวอักษรที่ไม่ถูกต้อง > ###
    valid_pieces = {"K", "Q", "B", "P", "R"}
    for line in lines_without_space:
        for char in line:
            if char != "." and char.upper() not in valid_pieces:
                return {
                    "valid": False,
                    "reason": f"Invalid character. Character must be one of {valid_pieces} or '.'",
                }

    ### < ตรวจสอบว่ามีตัว King อยู่เพียง 1 ตัว > ###
    king_count = sum(line.upper().count("K") for line in lines_without_space)
    if king_count != 1:
        return {
            "valid": False,
            "reason": f"Board must have exactly one king, found {king_count}.",
        }

    return {"valid": True, "reason": "Board is valid."}


def parse_board_to_array2d(board: str) -> list:
    lines = board.strip().splitlines()
    lines = [line.strip() for line in lines]

    # new_board = [list(line) for line in lines]
    board_2d = list(map(list, lines))
    # print(new_board)

    # txt = "hello"
    # txt = list(txt)
    # print(txt)

    return board_2d

## Cr: ไอ่-Chorn