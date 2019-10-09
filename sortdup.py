
import os
#import json
from imagededup.methods import CNN

image_dir='../aaa'

cnn = CNN()
#encoding = cnn.encode_image(image_file='a.jpg')
#print(encoding,encoding.shape)
encodings = cnn.encode_images(image_dir=image_dir)
duplicates = cnn.find_duplicates(encoding_map=encodings)
print(duplicates)


#with open('dup.json') as f:
#    content = json.load(f)
content=duplicates
    
    
result = list()
is_exist=False
def check_add(keys,result):
    is_exst=False
    for item in result:
        for k in keys:
            if k in item:
                for each_key in keys:
                    item.add(each_key)
                is_exst=True
                return is_exst
    return is_exst

for k in content:
    v = content[k]
    v.append(k)
    is_exist=check_add(v,result)
    if is_exist == False:
        result.append(set(v))


cnt=0
for item in result:
    dir_name="%d_%d"%(cnt,len(item))
    os.mkdir(dir_name)
    for path in item:
        os.system('cp "%s/%s" %s/'%(image_dir,path,dir_name))
    cnt=cnt+1
print(result)


