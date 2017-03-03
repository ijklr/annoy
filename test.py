import numpy as np
from annoy import AnnoyIndex

X = np.random.rand(100000, 60)
Y = np.random.rand(500, 60)

annoy1 = AnnoyIndex(60)
annoy1.set_seed(100)
for i in range(X.shape[0]):
    annoy1.add_item(i, X[i, :])

annoy1.build(10)

annoy2 = AnnoyIndex(60)
annoy2.set_seed(100)
for j in range(X.shape[0]):
    annoy2.add_item(j, X[j, :])

annoy2.build(10)

result1 = []
result2 = []

for k in range(Y.shape[0]):
    print "annoy1", annoy1.get_nns_by_vector(Y[k, :], 3)
    result1 += annoy1.get_nns_by_vector(Y[k, :], 3)
    print "annoy2", annoy2.get_nns_by_vector(Y[k, :], 3)
    result2 += annoy2.get_nns_by_vector(Y[k, :], 3)

