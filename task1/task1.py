import sys
import numpy as np
if __name__ == '__main__':
    data=sys.argv[1]
    numbers = []
    with open(data, 'r') as f:
        numbers = [line.strip() for line in f]
    for i in range(len(numbers)):
        numbers[i]=int(numbers[i])
    perc=np.percentile(numbers,90)
    median=np.percentile(numbers,50)
    print('%.2f' % perc,end='\n')
    print('%.2f' % median,end='\n')
    print('%.2f' % max(numbers),end='\n')
    print('%.2f' % min(numbers),end='\n')
    print('%.2f' % np.mean(numbers),end='\n')
