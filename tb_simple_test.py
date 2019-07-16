# The following codes from https://pytorch.org/docs/stable/tensorboard.html


import torch
from torch import nn
import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms

# Writer will output to ./runs/ directory by default
writer = SummaryWriter()

x = torch.randn(1,8)
model = nn.Sequential()
model.add_module('W0',nn.Linear(8,4))
model.add_module('W1',nn.Linear(4,5))
writer.add_graph(model, x)
writer.close()




