import torch
#doc file fire.pt
file_path = "fire.pt"
data = torch.load(file_path)
print(data)