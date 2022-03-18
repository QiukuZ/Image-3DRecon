import subprocess
import os
import io
import whatimage
import pyheif
import traceback
from PIL import Image 
 
# 图片解码
# byteIo为解码数据
# filename 为传入的文件名保存时使用
def decodeImage(bytesIo,filename):
     try:
        fmt = whatimage.identify_image(bytesIo)
        print(fmt)
        if fmt in ['heic']:
            i = pyheif.read_heif(bytesIo)
            pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
            pi = pi.resize((800,600))
            pi.save(filename, format="png")
            print("文件转换成功并保存到：" + filename)
     except:
             traceback.print_exc()
  
 
# 读取图片文件
# filename为要打开的文件路径
def readImage(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data
  
    
# 遍历path指定文件夹下的所有HEIC文件并转换为PNG文件   
def convertImages(path):
    filenames=os.listdir(path)
    os.makedirs(path+'/png')
    for name in filenames:
        filename = path +"/"+ name                                     # 完成路径
        print('当前转换文件：'+filename) 
        data = readImage(filename)                                 # 读取图像文件
        decodeImage(data,path+'/png/' + name.split('.')[0]+'.png')   # 转换
 
# 开始转换
convertImages("/home/qk/Documents/NewPipeline/Image_Point_Mesh/data/CSEdesk/heic")
