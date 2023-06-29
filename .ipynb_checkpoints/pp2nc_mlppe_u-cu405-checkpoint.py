#!/usr/bin/env python
# python script to load ppfiles and save to netcdf

#libs
import cf
import os
import time
import glob

#------------------------------------------------------------------------------------------------------------------------
# import paths and files

pathin='/gws/nopw/j04/cidar/data/UM_yeartest/u-cu045/'
pathout='/work/scratch-nopw/bassett/u-cu045/'
filename1='umnsaa_mlppe000' # also what to call the filename out, and make a new directory, also the folder name
fileoutname='umnsaa_mlppe000'

#------------------------------------------------------------------------------------------------------------------------

# make a new directory for the output
try:
    os.mkdir(os.path.join(pathout, fileoutname))
except FileExistsError :
    pass
except :
    raise

# list all the files
filelisting1 = glob.glob(pathin + '**/' + filename1 +'*', recursive=True)

#filelisting1 = filelisting1[0:1] # just for testing

# set variable names as the long name (some variables have missing standard names)
def long_name_function():
    for x in range(0, len(f), 1):
        f[x].standard_name=f[x].long_name 

# loop through open all files and save as netcdf
for x in range(len(filelisting1)):
    print(x)
    f=cf.read(filelisting1[x])
    long_name_function()
    filedate = filelisting1[x]
    filedate=filedate.split("/")[-6]
    filedate=filedate.replace("T0000Z", "")
    fileoutname2=os.path.join(pathout, fileoutname, fileoutname  + '_' + filedate + ".nc")
    print(fileoutname2)
    cf.write(f, fileoutname2, verbose=-1, compress=1)

print('finished')
