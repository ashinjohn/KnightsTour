# Classic Knights Tour

# Author: Ashin Basil John
# 08/22/18

board=[]
#bs=raw_input("Input board size ")
#bs=int(bs)
bs=6   #boardsize

#Make Board
for i in range(0,bs):
    board.append([])
    for j in range (0,bs):
        board[i].append(0)

def showboard():
    global board
    for i in range(0,bs):
            print( board[i])

# count represent the moving order of knight
count=0

def markplace(row,col):
    global board,bs,count,prow,pcol
    if count<0:
        print(" In no case shall count go below 2")
        return False
    elif count == bs*bs-1:
            print("Placed all knights")
            showboard()
            return True
    else:
        for i in range(0,bs):        
            for j in range(0,bs):
                if ( abs(i-row)== 2 and abs(j-col)==1 and board[i][j]==0)or \
                     ( abs(i-row)== 1 and abs(j-col)==2 and board[i][j]==0):
                    # logic for a possible location && check not taken
                    #Add this location as next move
                    board[row][col]=count+1

#                    print("--Adding--")
                    count=count+1

                    # Make a plan with this move
                    if markplace(i,j)==True:
                        return True
                    else:
                        #Unmark this location from move i.e. back track
                        board[row][col]=0
                        count=count-1
#                        print("--Subtracting--")
    return False

if not markplace(0,0):
    print("Not Possible")





        
