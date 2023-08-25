import numpy as np
import sys

a = np.log2(np.arange(1.,50.,0.1))

(num,bins) = np.histogram(a, bins = 10, range = (0,6))

bins1 = list(bins)

n = 0

writefilename = "histogram.txt"

with open(writefilename, 'wt') as output_file:
    
    while (n < 10):
        
        hist = []

        lower_bound = str(bins1[n])
        
        hist.append(lower_bound)
        hist.append(", ")
        
        upper_bound = str(bins1[n + 1])
        
        hist.append(upper_bound)
        hist.append(", ")
        
        col_val = str(num[n])
        
        hist.append(col_val)
        
        output_file.writelines(hist)
        output_file.writelines("\n")

        n = n + 1
        
sys.exit("Programme finished")