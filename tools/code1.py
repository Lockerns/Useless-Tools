import numpy as np

a = np.array([0.5, 0.8, 0.7, 0.3, 0.9, 0.1, 0.6])
b = np.array([200, 400, 700, 464, 176, 646, 354])

for i in range(len(a)):
    t = '(' + str(a[i]) + ',' + str(b[i]) + ')'
    # print(t)
a_mean = np.mean(a)
a_std = np.std(a)
b_mean = np.mean(b)
b_std = np.std(b)


a_norm = (a - a_mean) / a_std
b_norm = (b - b_mean) / b_std
a_norm = np.round(a_norm, decimals=2)
b_norm = np.round(b_norm, decimals=2)
print(a)
print(b)
