def moves(mat):
 
 done=False
 for i in range ((len(mat))):
    
     for j in range ((len(mat[i]))-1):
         
         if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
             mat[i][j]=mat[i][j]*2
             mat[i][j+1]=0
             done=True
 return (mat,done)            
             
                       
 ##...................................................................
 #adding two randomly at any zero place
import random
def random_two(mat):
    lmat=[]
    lj=[]
    for i in range ((len(mat))):
        for j in range (len(mat[i])):
            if mat[i][j]==0:
                lmat.append(str(i)+str(j))
                index=random.choice(lmat)
    i=int(index[0])
    j=int(index[1])
    mat[i][j]=2
    return(mat) 
  
 
##............................................................................ 

def order(mat):
    done=False
    l=[]
    c=0
    for i in range(len(mat)):
        l.append([])
        for j in range(len(mat[i])):
            if mat[i][j]!=0:
                l[i].append(mat[i][j])
            elif mat[i][j]==0:
                 c=c+1
        for j in range (0,c):
            l[i].append(0)
            c=0
            done=True
    mat=l
    return(mat,done)
   

##..................................................................... 
 
 
#mirror
def matrixmirror(mat):
    l=[]
    for i in range ((len(mat))):
        l.append(mat[i][len(mat[i]): :-1])
    
         
    return(l)
    
##.....................................................................     



def matT(mat):

    l=[]
    for i in range(len(mat)):
        l.append([])
        
        for j in range(len(mat[i])):
            l[i].append(mat[j][i])
    return (l)
            
#matT([[1,2,3,1],[4,5,6,7],[8,4,20,3],[3,4,6,5]])
###..........................................................................

def left(MAT):
    MAT,done=moves(MAT)
    temp= order(MAT)
    MAT=temp[0]
    done=done or temp[1]
    MAT=moves(MAT)[0]
    #random_two(MAT)
    return(MAT,done)
    
####..........................................................................    
def right(MAT):
  MAT=matrixmirror(MAT)
  MAT,done=moves(MAT)
  temp= order(MAT)
  MAT=temp[0]
  done=done or temp[1]
  MAT=moves(MAT)[0]
  MAT= matrixmirror(MAT)
  #random_two(MAT)
  return(MAT,done)
  
  
  
##right([[0,0,1,1],[0,0,2,2],[0,0,3,3],[0,0,4,4]])  
                
##............................................................................                
#up == trans (moves)  order/ tran
def up(MAT):
    MAT= matT(MAT)
    
    MAT,done=moves(MAT)
    temp= order(MAT)
    MAT=temp[0]
    done=done or temp[1]
    MAT=moves(MAT)[0]
    
    MAT= matT(MAT)
    #random_two(MAT)
   
    return(MAT,done)
    
    
##...............................................................
#down==trans , mirror  (move) order/ mirror , trans

def down(MAT):
    MAT= matT(MAT)
    MAT= matrixmirror(MAT)
    MAT,done=moves(MAT)
    temp= order(MAT)
    MAT=temp[0]
    done=done or temp[1]
    MAT=moves(MAT)[0]
    MAT= matrixmirror(MAT)
    MAT = matT(MAT)
    #random_two(mat)
    return(MAT,done)
#..........................................................
###***********************************************************************************************************************************************************************************************************************************************************************************************************
def start(n):
    mat = []

    for i in range(n):
        mat.append([0] * n)
    return mat  
   
   
   
   
def wingame(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==2048:
                return 'win'


    
