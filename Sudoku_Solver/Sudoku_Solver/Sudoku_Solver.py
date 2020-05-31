
#init the sudoko board
Sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

counter = 0
### to check: how to print unicode in py
#function to print the sudoko board

def read_board():
    i=0
    sudoku_input=[]
    while(i < 81):
        print(i)
        sudoku_input.extend( [int(a) for a in input("Enter the Sudoku table numbers: ").split()] )
        i=len(sudoku_input)
    
    for i in range(9):
        for j in range(9):
            Sudoku[i][j]=sudoku_input.pop(0)



def print_sudoku(li):
    for i in range(len(li)):
        if i % 3 == 0:
            print("  - -- -- -- -- -- -- -- -- -- -- -- -")

        for j in range(len(li)):
            if j% 3 ==0:
                print(" | ", end="")
            if li[i][j]==0:
                print(" . ",end="")
            else:
                print(" " + str(li[i][j]) + " ",end="")

            if j==8:    
                print(" |")
        if i==8:
            print("  - -- -- -- -- -- -- -- -- -- -- -- -\n")



#find an empty slot (in the board it will be = 0)
def find_slot(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i][j]==0:
                return (i,j)

    return None


def isValid(li,num,pos):
    #check the row
    for j in range(len(li)):
        if li[pos[0]][j] == num and j!=pos[1]:
            ##print("==") #testing ------------------------
            return False
    
    #check the column
    for i in range(len(li)):
        if li[i][pos[1]] == num and i!=pos[0]:
            ##print("||") #testing ------------------------
            return False

    #check the box
    i= pos[0] - (pos[0] % 3)
    j= pos[1] - (pos[1] % 3)
    ##print("({},{})".format(i,j)) #testing ------------------------
    for i_offset in range(3):
        for j_offset in range(3):
            if li[i+i_offset][j+j_offset] == num and (i+i_offset,j+j_offset) != pos:
                ##print("({},{})".format(i+i_offset , j+j_offset) ) #testing ------------------------
                ##print("[]") #testing ------------------------
                return False
    
    return True



def solve_board(li):
    
    slot = find_slot(li)
    if not slot:
        return True

    for i in range(1,10):
        #Testing------------------------
        #print("({},{}) - {}".format(slot[0],slot[1],i))
        global counter
        counter+=1     ##number of tries/iterations
        
        if isValid(li, i, slot):
            li[slot[0]][slot[1]] = i

            if solve_board(li):
                
                return True
            li[slot[0]][slot[1]] = 0

    return False



print_sudoku(Sudoku)

#read_board()
#print_sudoku(Sudoku)

#testing free slot position -- printing first possible free slot 
slot = find_slot(Sudoku)
print(slot) 

##testing num -- the number in slot
num = Sudoku[slot[0]][slot[1]]
print (num)
#isValid(Sudoku,num,slot)

solve_board(Sudoku)
print(counter)
print_sudoku(Sudoku)




