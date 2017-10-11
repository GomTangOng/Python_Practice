# Broadcast : 스칼라값과의 계산이 넘파이 배열의 원소별로 한 번씩 수행됨.
# --> EX) 스칼라 * 행렬
#

import numpy as np

x =  np.array([[1, 2], [3, 4]])
y =  np.array([10,20])

print(x * y)