# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:07:39 2020

@author: 小洋洋
"""
import scipy.io as scio
import os
file1 = os.getcwd()
filepath = file1 + "\\仿真本体数据"

#读取cif仿真文件
for i in range(100):
    cif = "\\cif\\OV-6b作战状态转换模型"+ str(i) + ".trajdata"
    cifpath = filepath + cif
    
    with open(cifpath) as file_obj:
        ciflist = []
        for content in file_obj.readlines():
            ciflist.append(content)
        cifmax = len(ciflist)
    
    lastdata = ciflist[cifmax - 1]
    Car1D = float(lastdata.split()[11])
    Car1V = float(lastdata.split()[15])
    Car2D = float(lastdata.split()[18])
    Car2V = float(lastdata.split()[22])
    
    ##判断cif标签
    
    cifLabel = True
    
    if Car1D > 3100 or Car2D > 3100 or Car1V > 0.01 or Car2V > 0.01 or (Car1D - Car2D) < 4.6:
        cifLabel = False


##读取simulink仿真文件
    
    matlab = "\\simulink\\data"
    
    
    
    ##v1距离
    v1pxpath = filepath + matlab + "\\v1px\\v1px" + str(i) + ".mat" 
    data = scio.loadmat(v1pxpath)
    timelist1 = data['v1px'][0][0][0]
    v1pxlist = data['v1px'][0][0][1][0][0][0]
    datamax1 = len(timelist1)
    matlabtime = float(timelist1[datamax1 - 1])
    MCar1D = float(v1pxlist[datamax1 - 1])
    
    ##v1速度
    v1vxpath = filepath + matlab + "\\v1vx\\v1vx" + str(i) + ".mat" 
    data = scio.loadmat(v1vxpath)
    timelist2 = data['v1vx'][0][0][0]
    v1vxlist = data['v1vx'][0][0][1][0][0][0]
    datamax2 = len(timelist2)
    MCar1V = float(v1vxlist[datamax2 - 1])
    
    ##v2距离
    v2pxpath = filepath + matlab + "\\v2px\\v2px" + str(i) + ".mat" 
    data = scio.loadmat(v2pxpath)
    timelist3 = data['v2px'][0][0][0]
    v2pxlist = data['v2px'][0][0][1][0][0][0]
    datamax3 = len(timelist3)
    MCar2D = float(v2pxlist[datamax3 - 1])
    
    
     ##v2速度
    v2vxpath = filepath + matlab + "\\v2vx\\v2vx" + str(i) + ".mat" 
    data = scio.loadmat(v2vxpath)
    timelist4 = data['v2vx'][0][0][0]
    v2vxlist = data['v2vx'][0][0][1][0][0][0]
    datamax4 = len(timelist4)
    MCar2V = float(v2vxlist[datamax4 - 1])
    
    # print(matlabtime,MCar1D,MCar2D,MCar1V,MCar2V)
    ##判断matlab标签
    matlabLabel = True
    if matlabtime < 200 or MCar1D > 3100 or MCar2D > 3100 or MCar1V > 0.01 or MCar2V > 0.01 or (MCar1D - MCar2D) < 4.6:
        matlabLabel = False
 #   print(matlabLabel)
            
    Label = cifLabel and matlabLabel
    # print(Label)
    # print("cifLabel",cifLabel)
    # print("matlabLabel",matlabLabel)
    
    Labeltxt = filepath + "\\Label.txt"

    with open(Labeltxt,"a") as file:
        
        if Label:
            
            file.write(str(1) + "\n")
        else:
            file.write(str(0) + "\n")
