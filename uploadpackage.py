# coding=utf-8
import os
print os.getcwd()
basedir= os.path.join(os.getcwd(),"node_modules")
dirlist= os.listdir(basedir)
for dir in dirlist:
    ##只对非uploaded的文件夹进行上传--以uploaded开头的都已经上传成功了
    if not dir.startswith("uploaded"):
        if dir.startswith('@'):
          #以@开头的，需要进入下层目录进行上传
            subdirlist = os.listdir(os.path.join(basedir,dir))
            for subdir in subdirlist:
                os.chdir(os.path.join(os.path.join(basedir,dir),subdir))
                print 'upload',dir,"---",subdir
                i=os.system('npm publish')
                print "commond return ",i
                if i == 0:
                    #如果返回成功，则将文件名重命名为uploaded开头的文件夹
                    os.chdir(os.path.join(basedir,dir))
                    os.rename(subdir,"uploaded"+subdir)
                else:
                    print "upload erro, continue next"
        else:
            os.chdir(os.path.join(basedir,dir))
            print "upload",dir
            i = os.system("npm publish")
            if i == 0:
                os.chdir(basedir)
                os.rename(dir,"uploaded"+dir)
