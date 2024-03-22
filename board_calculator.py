import pprint

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
    while True:
        board.append(cutlist[0])
        for part in cutlist[1:]:
            board.append(part)
            if sum(board) > (raw_material - calculated_waste):
                board.remove(part)
        board_collector.append(board)
        for item in board:
            cutlist.remove(item)
            board = []
        boards_needed += 1
        if not cutlist:
            break
    return boards_needed, board_collector
        
def load_cutlist_from_file(filename):
    cutlist = []
    with open(filename, 'r') as file:
        for line in file:
            #Skip emty line (if the line variable is only whitespace than False)
            if line.strip():
                #Decimal "," replace to ".", if there is no "," nothing happens.
                line = line.replace(",",".")
                cutlist.append(float(line.strip()))
    return cutlist
                

#Creating the cutlist
cutlist = load_cutlist_from_file('board.txt')

#Asking for general data for the output

#Printing out the results
number_of_boards, boards_divided = calculate_boards_needed(cutlist)
print("Number of 6-meter boards needed: " + str(number_of_boards) + " pcs. ")
print("Here is the cutlist:")
pp = pprint.PrettyPrinter(width=100)
pp.pprint(boards_divided)
