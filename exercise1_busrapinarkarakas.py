Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> matrix=np.random.rand(3,3)
>>> print(matrix)
[[0.0072514  0.42190723 0.98432589]
 [0.76810083 0.53308636 0.72435292]
 [0.78521926 0.08341897 0.39213133]]
>>> matrix_2=np.random.rand(3,3)
>>> print(matrix_2)
[[0.4227581  0.41014908 0.74587931]
 [0.23898302 0.75489767 0.30563204]
 [0.90466862 0.24110234 0.44785723]]
>>> result=np.dot(matrix,matrix_2)
>>> print(result)
[[0.994383   0.55879422 0.57519451]
 [1.1074188  0.89210468 1.06024548]
 [0.70664243 0.47957353 0.78679316]]
