import os
import time
start = time.perf_counter()


检测文件夹缓存=os.listdir()
文件夹存在=False
for 检测文件夹缓存1 in 检测文件夹缓存:
    if 检测文件夹缓存1=="bili合并":
        文件夹存在=True

if 文件夹存在==False:
    os.mkdir('./bili合并')
    print("创建文件夹bili合并")


当前目录文件=os.listdir('./bili合并')

print(当前目录文件)
筛选后文件=[]
for 文件名 in 当前目录文件:
    if 文件名.find('.')>0:
        筛选后文件.append(文件名)
qqq=筛选后文件
筛选后文件=[]
当前目录文件=qqq
for i in range(0,len(当前目录文件) - 1,2):
    文件名=当前目录文件[i]
    文件名p = 当前目录文件[i+1]
    if (文件名.split(".")[-1]=='m4a'):
        if(文件名p.split(".")[-1]=='mp4'):
            if (文件名.split(".")[-2]==文件名p.split(".")[-2]):
                筛选后文件.append(文件名)
                筛选后文件.append(文件名p)

print(筛选后文件)
for i in range(0,len(筛选后文件) - 1,2):
    # os.system('ffmpeg -y -hide_banner -i "1.m4a" -i "1.mp4" -c:v copy -b:a 256k "2.m4a"')
    文件名 = 筛选后文件[i]
    print(文件名,i)
    文件名p = 筛选后文件[i + 1]
    a='ffmpeg -y -hide_banner -i "./bili合并/'+文件名+'" -i "./bili合并/'+文件名p+'" -c:v copy -b:a 256k "./bili合并/_'+文件名p+'"'
    os.system(a)


end = time.perf_counter()
print("运行耗时", end-start)