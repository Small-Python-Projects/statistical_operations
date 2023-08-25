from scipy.constants import h, k, c
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as c_f

data_1 = np.genfromtxt('5000K_data_Ovenden, James (py16jo).csv')
    
#data_2 = np.genfromtxt('corrected_data_assessed (py16jo).csv',delimiter = " ",skip_header=1)
data_2 = np.genfromtxt('corrected_data_Kyriacou, Phillipos (el15pk).csv',delimiter = " ",skip_header=1)
data_3 = np.genfromtxt('corrected_data_Ovenden, James (py16jo).csv',delimiter = " ",skip_header=1)
    
#plt.semilogx(data_1[:,0],data_1[:,1])
    
x = data_2[:,0]
y = data_2[:,1]
noise = data_2[:,2]
sigma = noise

plt.errorbar(x,y,yerr=sigma,capsize=3,fmt='ro',label='data')

def planck_law(v, I, T):
    
    equ = ((2*h*(v**3))/(c**2))*(((np.exp((h*v)/(k*T))) - 1)**(-1))

    return I*equ

popt,pcov=c_f(planck_law,x,y,p0=[70,6000],sigma=noise,absolute_sigma=True)
perr=np.sqrt(np.diag(pcov))
for param,val,err in zip("IT",popt,perr):
    print('{} = {} +/- {}'.format(param,val,err))
x_fit = np.linspace(x.min(),x.max(),5001)
y_fit = planck_law(x_fit,*popt)
plt.semilogx(x_fit,y_fit,"b-")

#KBA9-MB2B-R56S-0DAN