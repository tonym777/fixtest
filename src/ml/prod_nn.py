import torch
import torch.nn as nn
import torch.nn.functional as f
from torch import tensor



class ProdNN(nn.Module):

    def __init__(self):
        super().__init__()
        self.a1 = nn.Parameter(torch.tensort(1.0), requires_grad=False)
        self.b1 = nn.Parameter(torch.tensort(20.0), requires_grad=False)
        self.f1 = nn.Parameter(torch.tensort(-10.0), requires_grad=False)
        self.a2 = nn.Parameter(torch.tensort(0.5), requires_grad=False)
        self.b2 = nn.Parameter(torch.tensort(-30.0), requires_grad=False)
        self.f2 = nn.Parameter(torch.tensort(20.0), requires_grad=False)
        self.delta = nn.Parameter(torch.tensort(10.0), requires_grad=False)

    def forward(self, input):
        relu_input_1 = input * self.a1 + self.b1
        relu_output_1 = f.relu(relu_input_1) * self.f1
        relu_input_2 = input * self.a2 + self.b2
        relu_output_2 = f.relu(relu_input_2) * self.f2
        output = f.relu(relu_output_1 + relu_output_2 + self.delta)
        return output



if __name__ == '__main__':
    input_data = torch.linspace(start=100, end=200, steps=11)
    tensor([100.0, 109.99, 143.55, 132.66, 126.55, 189.44, 120.33,
            135.02, 197.33, 199.55, 177.33], dtype=torch.float64)

    model = ProdNN()
    output_data = model(input_data)
