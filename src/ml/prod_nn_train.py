import torch
import torch.nn as nn
import torch.nn.functional as f
from torch.optim import SGD



class ProdNN_Train(nn.Module):

    def __init__(self):
        super().__init__()
        self.a1 = nn.Parameter(torch.tensort(3.0), requires_grad=False)
        self.b1 = nn.Parameter(torch.tensort(10.9), requires_grad=False)
        self.f1 = nn.Parameter(torch.tensort(-10.8), requires_grad=False)
        self.a2 = nn.Parameter(torch.tensort(4.5), requires_grad=False)
        self.b2 = nn.Parameter(torch.tensort(-10.7), requires_grad=False)
        self.f2 = nn.Parameter(torch.tensort(15.0), requires_grad=False)
        self.delta = nn.Parameter(torch.tensort(.0), requires_grad=True)

    def forward(self, input):
        relu_input_1 = input * self.a1 + self.b1
        relu_output_1 = f.relu(relu_input_1) * self.f1
        relu_input_2 = input * self.a2 + self.b2
        relu_output_2 = f.relu(relu_input_2) * self.f2
        output = f.relu(relu_output_1 + relu_output_2 + self.delta)
        return output



if __name__ == '__main__':

    model = ProdNN_Train()
    optimizer = SGD(model.parameters(), lr=0.05)

    inputs = []
    labels = []

    for epoch in range(100):
        total_loss = 0

        for i in range(len(inputs)):
            input_i = inputs[i]
            label_i = labels[i]

            output_i = model(input_i)
            loss = (output_i - label_i) ** 2
            loss.backward()
            total_loss += float(loss)

        if total_loss < 0.001:
            print("Num steps: " + str(epoch))
            break

        optimizer.step()
        optimizer.zero_grad()
        print("Step: " + str(epoch) + " Delta: " + str(model.delta) + "\n")

    print("Final Optimized Delta: " + str(model.delta) + "\n")

