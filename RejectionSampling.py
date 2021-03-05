import numpy as np
import random
import matplotlib.pyplot as plt


#create n random numbers
n=1000000
numbersx=[]
numbersy=[]

for i in range(1,n):
    numbersx.append(random.uniform(0, 1))
    numbersy.append(random.uniform(0, 1))




#curve
x= np.arange(0,1, 0.005)
y=2.6/(10*(2*x-1)**2+1)#2.6 is the normalization factor


#bound or proposal function
#g(x)=2.6

#Where the magic happens
i=0
accepted=[]
for i in range(0, len(numbersx)):
     if numbersy[i]<=1/(10*(2*numbersx[i]-1)**2+1):
         accepted.append(numbersx[i])


         
#Calculate the Efficiency (not sure that is the right spelling)
efficiency=round(len(accepted)/len(numbersx),3)


#Plotting Stuff         
fig,ax=plt.subplots()
weights = np.ones_like(accepted) / len(accepted)
plt.hist(accepted,100, density=True, label='Accepted samples from f(x)')
plt.title("Rejection Sampling")
plt.xlabel("X")
plt.ylabel("Probability")
plt.plot(x,y, label="Target Function f(x)")
plt.axhline(y=2.6, color='m', label='proposal g(x)')
plt.plot([],[],label="Efficiency= "+str(efficiency))
plt.legend(bbox_to_anchor=(0.36, 0.65), loc=1,fontsize=7, borderaxespad=0.)

plt.savefig('DensityEstimation.pdf')

plt.show()


