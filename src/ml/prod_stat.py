import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD



class ProdNN(nn.Module):

    def __init__(self):
        super().__init__()
        self.a1 = nn.Parameter(torch.tensort(1.0), requires_grad=False)
        self.b1 = nn.Parameter(torch.tensort(0.0), requires_grad=False)
        self.a2 = nn.Parameter(torch.tensort(0.5), requires_grad=False)
        self.b2 = nn.Parameter(torch.tensort(0.0), requires_grad=False)

    def forward(self, input):
        relu_input_1 = input * self.a1 + self.b1
        relu_output_1 = F.relu(relu_input_1)
        relu_input_2 = input * self.a2 + self.b2
        relu_output_2 = F.relu(relu_input_2)
        output = F.relu(relu_output_1+relu_output_2)
        return output