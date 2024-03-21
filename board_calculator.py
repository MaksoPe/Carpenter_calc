def calculate_boards_needed(cutlist):
    cutlist.sort(reverse = True) #Descending order
    raw_material = 600 #5x15 cm boards in 600 cm length
    calculated_waste = 12 #calculated waste, because of end-cracking / saw kerf.

    boards_needed = 0
    total_length = 0
    
    board_collector = []
    board = []
    
    for index, start_part in enumerate(cutlist):
        board = [start_part]
        for part in cutlist[index+1:]:
            board.append(part)
            if sum(board) > (raw_material - calculated_waste):
                board.remove(part)
        board_collector.append(board)
        for item in board:
            cutlist.remove(item)
        boards_needed += 1

    return boards_needed, board_collector
        
#insert here function that takes the cutlist from an excel / txt
cutlist = [250, 250, 250, 250, 250, 318, 318, 180, 100, 60, 60, 50, 50, 42, 38, 38, 38, 45, 45, 62.5, 62.5, 31.8, 25, 25, 18]

number_of_boards, boards_divided = calculate_boards_needed(cutlist)
print("Number of 6-meter boards needed: " + str(number_of_boards) + " pcs. " + "Here is the cutlist:" + str(boards_divided))
