import cv2
import dropbox
import time
import random

start_time = time.time()


def takeImage():
    vco = cv2.VideoCapture(0)
    result = True
    number = random.randint(0,100)

    while (result):
        ret, frame = vco.read()
        imageName = "img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        start_time = time.time
        result = False
    return imageName
    print("image capture")
    vco.release()
    cv2.destroyAllWindows()


def upload_file(imageName):
    access_token = 'sl.AlJGYt94Tem2bFWGT-wx2hH8v6FiVw1n4LpsAdBovHwiWxuz4UU2xD7pCXTANPZSK8XytiaV7nrJeP9XRppqw2nOesNVGmlmzCX7KMKW-25osyVVZLLshFsOmtBFfBSXYezyJMxbVuk'
    file = imageName
    filefrom = file
    file_to = '/102/'+file
    dbx = dropbox.Dropbox(access_token)

    with open(filefrom, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode= dropbox.file.WriteMode.overWrite)
        print('uploaded')


def main():
    while(True):
        if((time.time()-start_time) >= 2):
            name = takeImage()
            upload_file(name)
main()