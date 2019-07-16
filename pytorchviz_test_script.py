
import torch
from torch import nn
from torchviz import make_dot,make_dot_from_trace


x = torch.randn(1,8)
model = nn.Sequential()
model.add_module('W0',nn.Linear(8,4,bias=False))
model.add_module('W1',nn.Linear(4,6,bias=False))

dot = make_dot(model(x),params=dict(model.named_parameters()))
dot.render('gradient.gv',view=True)
#with torch.onnx.set_training(model,False):
#    trace,_= torch.jit.get_trace_graph(model,args=(x,))
#forward_dot = make_dot_from_trace(trace)
#forward_dot.render('forward.gv',view=True)

