import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x: torch.Tensor):
        return torch.exp(x) / torch.exp(x).sum()


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x: torch.Tensor):
        z = x - torch.max(x)
        return torch.exp(z) / torch.exp(z).sum()


if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)

    softmax_stable = SoftmaxStable()
    output_stable = softmax_stable(data)
    print(output_stable)
