
import numpy as np
import tifffile as tiff
import subprocess
import glob
import os

imagelocation = 'C:\\Users\\hwilson23\\Documents\\MN_pdgfb_slide3_8_take1_spc\\'
filelist =[]
print(glob.glob(imagelocation ))
for files in glob.glob(imagelocation +'*.spc'):
    filelist.append(files)
print(f'this is filelist:{filelist}')

overloaded = []

for f in filelist:
    currentfile = f
    print(f)
    outputfile =  f'{currentfile[:-4]}_spcmod'
    subprocess.check_output(['D:\\flim_lineclock_bh_spc.exe', '--pixel-time=200','--width=256','--height=256',currentfile, outputfile],shell=True)

    for files2 in glob.glob(imagelocation + '*spcmod'):
        file = np.fromfile(files2, dtype=np.uint16).reshape(-1,256,256,256)

        #file = numpy.fromfile('D:\outputspctest_sum', dtype=numpy.uint16).reshape(256,256,256)
        file = file.sum(axis=3)
        print(file.shape)

        checked_portion = np.ravel(file)[-16384:]
        if file.shape[0] != 90 or np.all(checked_portion==0):
            overloaded = [overloaded, files2]
            print(f'this file overloaded: {files2}')

        tiff.imwrite(f'{files2}.tif',file.astype(np.uint16))
        os.remove(files2)

print(f'overloads: {overloaded}')
print("Done :)")

##can remove tif convert if not needed and just check to see if frames is 90 or if 90 is empty then print list