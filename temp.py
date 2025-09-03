# import pickle 

# with open('/raid/liujie/code_recon/data/X-ray/X-Gaussian/chest_50.pickle', 'rb') as f: 
#     data = pickle.load(f)

# # print(data)

# for k, v in data.items(): 
#     if k == 'image': 
#         print(k, v.shape) 
#     elif k == 'train' or k == 'val': 
#         for kk, vv in data[k].items(): 
#             print(k, kk, vv.shape) 
#     else: 
#         print(k, type(v), v) 


import torch 

x = torch.ones((1, 64, 64)) 
y = x[:3, :, :] 

print(y.shape)