# Classic Knights Tour

# Author: Ashin Basil John
# 08/22/18

board=[]
#bs=raw_input("Input board size ")
#bs=int(bs)
bs=4   #boardsize

#Make Board
for i in range(0,bs):
    board.append([])
    for j in range (0,bs):
        board[i].append(0)

def showboard():
    global board
    for i in range(0,bs):
            print( board[i])
#showboard()
# count represent the number of locations taken
# prow represent the last knights row location
# pcol represent the last knights column location

count=0
prow=0
pcol=0

#this function checks the given location is a possible move from last position
def knightmove(prow,pcol):
    if prow<=bs and pcol <=bs:
        print("but why",prow,pcol)
        for row in range(0,bs):
            for col in range(0,bs):
                if ( abs(row-prow)== 3 and abs(col-pcol)==1 )or \
                     ( abs(row-prow)== 1 and abs(col-pcol)==3 ):
                       #board[row][col]=1
                        print("position",row,col)
                        if board[row][col] == 0: # Position is not taken
                            print("I'm Free")
                            return True
    return False

def markplace(col):
    showboard()
    global board,bs,count,prow,pcol
    if count<0:
        print(" In no case shall count go below 2")
        return False
    elif count == bs*bs:
        print("Placed all knights")
        return True
    elif (col>=bs):
        # check the position is outside board
        print("Position outside board")
        return False
    else:
        #Row will be handled here
        #Column by recurssion
        
        for row in range(0,bs):
            print("egh",row,col,knightmove(row,col))
            if knightmove(row,col)== True:
                # logic for a possible location && check not taken
                #Add this location as next move
                board[row][col]=count+1
                count=count+1
#                prow=row
#                pcol=col

                # Make a plan with this move
                if markplace(col+1)==True:
                    return True
                else:
                #Unmark this location from move i.e. back track
                    board[row][col]=0
                    count=count-1

    return False

markplace(0)
showboard()
        
