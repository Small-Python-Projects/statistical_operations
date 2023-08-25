import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('Fourier Data.csv', delimiter=',', dtype = 'float')

fourier_func_5 = data[:,1] + data[:,2] + data[:,3] + data[:,4] + data[:,5]
fourier_func_10 = (fourier_func_5) + data[:,6] + data[:,7] + data[:,8] + data[:,9] + data[:,10]
fourier_func_all = fourier_func_10

for i in range(10, 31):
    
    fourier_func_all = fourier_func_all + data[:,i]

plt.plot(fourier_func_5)
plt.plot(fourier_func_10)
plt.plot(fourier_func_all)

plt.xlabel('t')
plt.ylabel('F(t)')
plt.title('Fourier series')
plt.legend()
plt.show()
