import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from sklearn.model_selection import train_test_split
import torch.optim as optim

ticker: str = "AMD"
data = pd.read_csv("Data/{}_test_train_data.csv".format(ticker))

X = data.iloc[:,:-3]
y = data["Profit-Bool"] #.iloc[:,-3:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class Net(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(len(X.columns), 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 2)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)
        

net = Net()
print(net)

# X = torch.Tensor(X.values)
# output = net(X)
# print(output)

optimiser = optim.Adam(net.parameters(), lr=0.001)

EPOCHS = 3

for epoch in range(EPOCHS):
    for dataset in zip(X_train, y_train):
        # dataset is a batch of featuresets and labels
        X, y = dataset
        net.zero_grad()
        # Batch size helps generalisation
        output = net(X.view())
        loss = F.nll_loss(output, y)  # One hot vector, mean squared error    # Scalar vector use nll_loss
        loss.backward()
        optimiser.step()
    print(loss)
    














