import os
from PIL import Image
from io import BytesIO
from uuid import uuid4
base = os.environ.get("BASE")


def file_url(name):
    return "/utilities/images/"+name


def getphoto(username):
    return "/utilities/images/thumbnail/user_"+username+".png"

def saveimg(file,*,path,name=None,type="PNG",quality=85,fastapi=True):
    """
    file: string of bytes or file_name
    path: where to store the file
    name: name of the file to be saved without extension
    type: type of the file (png/jpg)
    quality: quality of the file
    """
    if not name:
        name = str(uuid4())+"."+type.lower()
    else:
        name = name+"."+type.lower()
    if fastapi:
        img = Image.open(file.file)
    else:
        img = Image.open(file)
    #buf = BytesIO()
    img.save(os.path.join(path,name), type, quality=quality)
    # img.save(buf, type, quality=quality)
    # print(os.path.join(path,name))
    # with open(os.path.join(path,name), 'wb') as f:
    #     try:
    #         f.write(buf.read())
    #     except Exception as e:
    #         print(e)
    return file_url(name)
