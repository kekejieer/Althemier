import nibabel as nib
import os
import numpy as np
import pdb
from skimage import transform

#剪切3D图片
def jianqie3Dimg(img, aa):
    dic = []
    dicimg = []
    if img.shape[aa]==182:
        for i in range(img.shape[aa]):
            if i >= 20 and i <= 180:     #选定范围
                img_2d = img[:, :, i]  # 取出一张图像
                dic.append(img_2d)
    if img.shape[aa] == 218:
        for i in range(img.shape[aa]):  # 对切片进行循
            if i >= 20 and i <= 200:
                img_2d = img[:, :, i]  # 取出一张图像
                dic.append(img_2d)
    if len(dic) < 180:
        for start, end in zip(range(0, len(dic), 20), range(96, len(dic), 20)):
            dicimg.append(dic[start:end])
    if len(dic) > 180:
        for start, end in zip(range(0, len(dic), 20), range(120, len(dic), 20)):
            dicimg.append(dic[start:end])
    return dicimg


#pic_all装所有的图片
def all(dic2):
    pic_all = []
    for heng in dic2:
        heng1 = np.array(heng)
        jianqie = jianqie3Dimg(heng1, aa=-1)
        pic_all.extend(jianqie)
    return pic_all


#主程序
pathnibimage = 'E:\dataset\ORI_dataset\ADNI-teacher'
pathsaveimge = 'E:\dataset\ORI_dataset\ADNI-3Dslipe2'   # 保存新图片的地址
imageinfo = os.listdir(pathnibimage)

for labelname in imageinfo:
    print(labelname)
    if labelname != 'AD':      #选定标签
        pathsaveimge1 = os.path.join(pathsaveimge, labelname)  # 保存新图片的文件夹
        pathnibimage1 = os.path.join(pathnibimage, labelname)  # 要切割3D图片的子文件夹

        for NIIname in os.listdir(pathnibimage1):    #遍历所有的图片名称
            if NIIname[-9:] == 'brain.nii':        # 选中字符为'brain.nii'的名称
                pathsaveimge2 = os.path.join(pathsaveimge1, NIIname[:-3] )   #给保存的新图片命名
                pathnibimage2 = os.path.join(pathnibimage1, NIIname, NIIname)  #打开要切割的图片
                if not os.path.exists(pathsaveimge2):
                    os.makedirs(pathsaveimge2)           #新建保存图片的文件夹
                NIIimg = nib.load(pathnibimage2)         #下载nii MRI
                img = NIIimg.get_data()                  #读取nii MRI
                ref_affine = NIIimg.affine               #为保存图片—仿射
                jianqie1 = jianqie3Dimg(img, aa=-1)
                jianqie2=all(jianqie1)
                jianqie3=all(jianqie2)
                for i,patch in enumerate(jianqie3):     #
                    patch = np.array(patch)
                    mx = patch.max(axis=0).max(axis=0).max(axis=0)
                    patch = np.array(patch) / mx
                    patch = transform.resize(patch, (32, 40, 32), mode='constant')   #resize到相同大小
                    patch = nib.Nifti1Image(patch, ref_affine)                       #仿射为nii文件
                    savepath = os.path.join(pathsaveimge2, str(i) + '_' + NIIname[:-4] + '.nii')   #保存名称
                    nib.save(patch,  savepath)                                       #保存.nii文件