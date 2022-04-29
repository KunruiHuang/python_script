import os
import glob
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms

class CrypkoDataset(Dataset):
    def __init__(self, fnames, transform):
        self.transform = transform
        self.fnames = fnames
        self.num_samples = len(self.fnames)

    def __getitem__(self,idx):
        fname = self.fnames[idx]
        # 1. Load the image
        img = torchvision.io.read_image(fname)
        # 2. Resize and normalize the images using torchvision.
        img = self.transform(img)
        return img

    def __len__(self):
        return self.num_samples


def get_dataset(root):
    # 打印出该文件夹下的所有路径
    fnames = glob.glob(os.path.join(root, '*'))
    # 1. Resize the image to (64, 64)
    # 2. Linearly map [0, 1] to [-1, 1]
    compose = [
        transforms.ToPILImage(),
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)),
    ]
    transform = transforms.Compose(compose)
    dataset = CrypkoDataset(fnames, transform)
    return dataset
    
workspace_dir = '/mnt/lustre/share_data/huangkunrui'
dataset = get_dataset(os.path.join(workspace_dir, 'faces'))
images = [dataset[i] for i in range(16)]
# print(images)
grid_img = torchvision.utils.make_grid(images, nrow=12)
# print(grid_img.size())
plt.figure(figsize=(10,10))
# plt.imshow(grid_img)
plt.imshow(grid_img.permute(1, 2, 0))
plt.show()