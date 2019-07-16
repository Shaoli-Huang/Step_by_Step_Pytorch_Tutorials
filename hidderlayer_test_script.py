import matplotlib
matplotlib.use("Agg")
import torch
from torch import nn
import hiddenlayer as hl

x = torch.randn(1,8)
model = nn.Sequential()
model.add_module('W0',nn.Linear(8,4))

graph = hl.build_graph(model,x)
dot = graph.build_dot()
dot.view()

