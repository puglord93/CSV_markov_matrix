import os, sys
import csv 
import numpy as np 

# Open a file
path = "C:/Users/JingJie/Desktop/Virgo Video Count/Sample3"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
    w=path+"/"+file
    print w
    out=open(w, "rb") 
    data=csv.reader(out)
    data=[row for row in data]
    out.close()
    
    size=len(data[0])
    I=[]
    O=[]
    row_one=data[0]
    row_two=[]
    
    row_one=row_one[1:-1]
    print row_one
    for i in row_one:
        if i != '':
            row_two.append(i)
    print " S  P  A  C  E"
    print row_two
            
    
    for i in data: #i refers to each main row in data
        for u in i: #u refers to each element in 1 row      
            if u=='I':
                i_index=i.index(u)
                I.append(i_index)
            if u=='O':
                o_index=i.index(u)
                O.append(o_index)
    
    IO=zip(I,O)
    #print IO
    
    matrix=np.zeros((size-1,size-1)) #10 nodes
    for a in IO:
        c=a[0]
        v=a[1]
        matrix[c-1][v-1]+=1
    print matrix
    #matrix = np.vstack([matrix, row_one])
    #print matrix
    
    markov_max=matrix
    
    row_max=np.sum(matrix,axis=1)
    #print row_max
    
    for i in range(len(matrix)):
        if row_max[i] != 0:
            markov_max[i]=matrix[i]/row_max[i]
    print markov_max    
                    
    yoyo=np.sum(matrix)
    prob_matrix=np.divide(matrix,yoyo)
    #print prob_matrix
    #print size
    
    A= file[7:12] + " " + file[3:6] + " Node.csv"
    B = file[7:12] + " " + file[3:6] + " Markov Node.csv" 
    
    
    #-----------------------------------------
    doc=open(A, "wb")
    output=csv.writer(doc)
    
    for row in matrix:
        output.writerow(row)
        
    doc.close()
    
    #----------------------------------------
    
    doc=open(B, "wb")
    output=csv.writer(doc)
    
    for row in markov_max:
        output.writerow(row)
        
    doc.close()
    