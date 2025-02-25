import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as f



class ProdNN_Train(nn.Module):

    def __init__(self):
        super().__init__()
        self.a1 = nn.Parameter(torch.Tensor([3.0]), requires_grad=False)
        self.b1 = nn.Parameter(torch.Tensor([10.9]), requires_grad=False)
        self.f1 = nn.Parameter(torch.Tensor([-10.8]), requires_grad=False)
        self.delta = nn.Parameter(torch.Tensor([.0]), requires_grad=True)

    def forward(self, data):
        relu_input_1 = data * self.a1 + self.b1
        relu_output_1 = f.relu(relu_input_1) * self.f1
        output = f.relu(relu_output_1 + self.delta)
        return output



if __name__ == '__main__':

    model = ProdNN_Train()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.005)

    input_df = pd.read_csv('inputs.csv')
    label_df = pd.read_csv('labels.csv')

    input_dataset = torch.Tensor(input_df['data'].values)
    label_dataset = torch.Tensor(label_df['data'].values)

    epochs = 1000
    lost_threshold = 0.001

    for epoch in range(epochs):
        total_loss = 0

        for i in range(len(input_df)):
            input_i = input_df.iloc[i, 1]
            label_i = label_df.iloc[i, 1]

            output_i = model(input_i)
            loss = (output_i - label_i) ** 2
            loss.backward()
            total_loss += float(loss)

        if total_loss < lost_threshold:
            print("Num steps: " + str(epoch))
            break

        optimizer.step()
        optimizer.zero_grad()
        print("Step: " + str(epoch) + " Delta: " + str(model.delta) + "\n")

    print("Final Optimized Delta: " + str(model.delta) + "\n")

