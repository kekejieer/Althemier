#图像切割切片 2D
import matplotlib.pyplot as plt
import pdb
import os
import nibabel as nib
from skimage import io,data
import numpy as np
from pandas import DataFrame
path='E:\dataset\ORI_dataset\ADNI-3Dslipe1\AD\AD_001\\1_AD_001.nii'
newpath1='E:\dataset\\new'   #保存图片的路径
for file in os.listdir(path):
    if file =='AD':
        for filename in os.listdir(os.path.join(path, file)):
            #if filename[-9:]=='brain.nii':
            if filename[-3:] == 'nii':
                for filename1 in os.listdir(os.path.join(path, file,filename)):
                    pathsave=path+'\\'+file+'\\'+filename+'\\'+filename1
                    img = nib.load(pathsave)
                    img = img.get_data()
                    # plt.imshow(img_arr[100])
                    # plt.show()
                    data = np.zeros((20, 182, 182, ), dtype='float32')
                    for i in range(img.shape[1]):  # 对切片进行循
                        #if i>=30 and i<=190:
                        img_2d = img[:, i, :]  # 取出一张图像
                        #plt.imshow(img_2d)
                        #plt.show()
                        pathsave=newpath1+'\\'+file+'\\'+filename[:-4]
                        if not os.path.exists(pathsave):
                            os.makedirs(pathsave)
                        io.imsave(pathsave+'\\'+filename[:-4]+str(i)+'.nii', img_2d )