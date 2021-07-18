import cv2
import dropbox
import time
import random

start_time= time.time()

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    number=random.randint(0,100)
    while(result):
        ret, frame= videoCaptureObject.read()
        img_name="img" + str(number) + ".jpg"
        cv2.imwrite(img_name, frame)
        start_time=time.time()
        result= False
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='sl.A02DyDvTpDcfwxseX-Tm2HE4I7jAVE4sFYDwJWWE8mobC-8trp6VFY6Hv4r3balWPeOseMaCJP1xOqHsUuidORc8gK-7CWbUWAnaeN9VY2BXYLp003ien85gAFg5Ft2kHSNB-l4'
    fileFrom=img_name
    fileTo='/NewFolder/'+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()


