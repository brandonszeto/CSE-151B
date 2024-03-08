import torch
from d2l import torch as d2l

def corr2d_multi_in(X, K):
    return sum(d2l.corr2d(x, k) for x, k in zip(X, K))

X = torch.tensor([[[0.0, 1.0, 0.0, -1.0, 1.0], [1.0, 1.0, 0.0, -1.0, 0.0], [1.0, 1.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0], [1.0, 0.0, -1.0, -1.0, 0.0]], [[1.0, 1.0, 1.0, 0.0, 0.0], [0.0, -1.0, 1.0, 0.0, 0.0], [0.0, 1.0, -1.0, -1.0, 1.0], [-1.0, 1.0, -1.0, 0.0, 1.0], [1.0, 1.0, -1.0, 0.0, 0.0]]])

K = torch.tensor([[[1.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -1.0]], [[1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [-1, -1, -1]]])

print(corr2d_multi_in(X, K))
