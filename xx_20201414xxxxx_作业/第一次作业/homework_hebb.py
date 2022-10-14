import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

correct0=np.array([-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1])
correct1=np.array([-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1])
correct2=np.array([1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1])

row0=correct0.reshape(correct0.size,1)
row1=correct1.reshape(correct1.size,1)
row2=correct2.reshape(correct2.size,1)

w=np.matmul(row0,row0.T)+np.matmul(row1,row1.T)+np.matmul(row2,row2.T)
# w

def my_plot(input_list,s,num):
    fig=plt.figure(facecolor='white')
    ax=fig.add_subplot(1,1,1)
    for i in range(input_list.size):
        j=i%5
        if input_list[i]==-1:
            res=matplotlib.patches.Rectangle((0+j*10,50-math.floor(i/5)*10),10,10,color='grey')
        else:
            res=matplotlib.patches.Rectangle((0+j*10,50-math.floor(i/5)*10),10,10,color='black')
        ax.add_patch(res)
    plt.xlim([0,50])
    plt.ylim([0,60])
    
    if s=="before":
        if num==0:
            plt.title("Num 0 Before")
        elif num==1:
            plt.title("Num 1 Before")
        else:
            plt.title("Num 2 Before")
    else:
        if num==0:
            plt.title("Num 0 After")
        elif num==1:
            plt.title("Num 1 After")
        else:
            plt.title("Num 2 After")
            
    plt.show()
 
def output_list(w,test,num):
    test=test.reshape(test.size,1)
    res=np.matmul(w,test)
    for i in range(res.size):
        res[i]=1 if res[i]>=0 else -1
    my_plot(res,"after",num)


# test number 0
test0=[-1]*30
test0[0:15]=correct0[0:15]
my_plot(np.array(test0),"before",0)
output_list(w,np.array(test0),0)

# test number 1
test1=[-1]*30
test1[0:15]=correct1[0:15]
my_plot(np.array(test1),"before",1)
output_list(w,np.array(test1),1)

# test number 2
test2=[-1]*30
test2[0:15]=correct2[0:15]
my_plot(np.array(test2),"before",2)
output_list(w,np.array(test2),2)