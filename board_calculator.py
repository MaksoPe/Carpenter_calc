def calculate_boards_needed(cutlist):
    cutlist.sort(reverse = True) #Descending order
    raw_material = 600 #5x15 cm boards in 600 cm length
    calculated_waste = 12 #calculated waste, because of end-cracking / saw kerf.
    
    #Total amount of raw material to buy based on the cutlist
    boards_needed = 0
    
    #Board collector => list of boards where the boards are divided further into parts.
    board_collector = []
    board = []

    #Main loop the idea is to take the first item, than loop through the rest of the list, and try
    # to combine them in order to achive as little as possible waste.
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
        
#This comes from the 3D modell / SW
#insert here function that takes the cutlist from an excel / txt
cutlist = [250, 250, 250, 250, 250, 318, 318, 180, 100, 60, 60, 50, 50, 42, 38, 38, 38, 45, 45, 62.5, 62.5, 31.8, 25, 25, 18]

number_of_boards, boards_divided = calculate_boards_needed(cutlist)
print("Number of 6-meter boards needed: " + str(number_of_boards) + " pcs. " + "Here is the cutlist:" + str(boards_divided))
