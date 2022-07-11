import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt
import scipy
import mpmath as mp

x = np.linspace(-10,10,50)#points on the x axis
x1 = np.linspace(-10,0,50)
y1 = np.zeros(50)
x2 = np.linspace(0,10,50)
y2 = 1 - np.exp(-x2/2)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../codes/uni.dat',dtype='double')
randvar = -2*np.log(1 - randvar)
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

# theory function
def cdf(x):
    if x < 0:
        return 0
    else:
        return (1 - np.exp(-x/2))

#vectorize
vect = scipy.vectorize(cdf, otypes=[np.float64])

plt.plot(x,err,'.')#plotting the CDF
plt.plot(x, vect(x))
plt.grid() #creating the grid
plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/exp_cdf.png')
