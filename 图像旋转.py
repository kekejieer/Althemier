#图像旋转，增多数据集
#找到文件
#旋转
#保存
from keras.preprocessing import image
import os
import pdb
from skimage import io,transform
from skimage import io,data
# 读取图像
path1='F:\dataset\ADNI-slice3\sNC'    #保存文件夹
datapath='F:\dataset\ADNI-slice3\sNC1'    #数据文件夹
for pathimg in os.listdir(datapath):
    pathnew=os.path.join(path1,pathimg)   #新加路径
    if not os.path.exists(pathnew):
        os.makedirs(pathnew)
    newdatapath=os.path.join(datapath,pathimg)
    for i,imgname in enumerate(os.listdir(newpath)):
        im = io.imread(os.path.join(newpath, imgname))
        if i%2==0:    #每隔两张
            im= transform.rotate(im, 45)  #旋转45度
        im.reshape(182, 182)
        #name=imgname[0:4]+'addIm'+imgname[9:]       #保存名字
        io.imsave(pathnew + '\\' + imgname,im )

# 指定逆时针旋转的角度