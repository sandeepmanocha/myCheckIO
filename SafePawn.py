def safe_pawns(pawns):
    chess_board = {}
    chess_board_pawns_pos = []
    # Create Chess Board and transform <Alpha><Num> to (x,y) pos on board and Set the Pawns
    for x in range(0, 8):
        cb = []
        for y in range(0, 8):
            pawn_key = chr(x + 97) + str(y + 1)
            if pawn_key in pawns:
                chess_board[pawn_key] = (x, y)
                cb.append(1)
            else:
                chess_board[pawn_key] = (x, y)
                cb.append(0)
        chess_board_pawns_pos.append(cb)

    chess_board_pawns_pos_t = []
    for y in (range(8)):
        cb = []
        for x in range(8):
            cb.append(chess_board_pawns_pos[x][y])
        chess_board_pawns_pos_t.append(cb)

    for i in reversed(range(8)):
        print(i, "->", chess_board_pawns_pos_t[i])

    print("    ",[0,1,2,3,4,5,6,7])

    safe_pawn = 0

    for pawn in pawns:
        pawn_x = chess_board[pawn][0]
        pawn_y = chess_board[pawn][1]

        saver_left = ( pawn_y - 1, pawn_x - 1)
        saver_right = (pawn_y - 1, pawn_x + 1)
        safe_left = 0
        safe_right = 0

        #print(pawn, saver_left, saver_right, chess_board_pawns_pos[saver_left[0]][saver_left[1]],
              #chess_board_pawns_pos[saver_right[0]][saver_right[1]])

        #print(saver_left[0], saver_left[1])
        if saver_left[0] >= 0 and saver_left[1] >= 0:
            safe_left = chess_board_pawns_pos_t[saver_left[0]][saver_left[1]]

        #print(saver_right[0], saver_right[1])
        if saver_right[0] >= 0 and saver_right[1] >= 0 and saver_right[0] < 8 and saver_right[1] < 8:
            safe_right = chess_board_pawns_pos_t[saver_right[0]][saver_right[1]]


        if safe_left + safe_right >= 1:
            safe_pawn = safe_pawn + 1

        print(pawn, chess_board[pawn], saver_left, safe_left, saver_right, safe_right)

            # print (pawn,chess_board[pawn][0],chess_board[pawn][1], chess_board[pawn][2])
            # print (pawn,chess_board[pawn][0],chess_board[pawn][1])
            # print (pawn,chess_board[pawn])

    #print (chess_board)
    return safe_pawn


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})) # == 6
#print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})) # == 1
#print(safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}))