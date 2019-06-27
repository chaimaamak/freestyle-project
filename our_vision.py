#vision.py

import io
import os
from dotenv import load_dotenv
from google.cloud import vision
from google.cloud.vision import types
#from oauth2client.service_account import ServiceAccountCredentials

load_dotenv() # load implicit creds GOOGLE_APPLICATION_CREDENTIALS

#
## SETUP
#

def new_client():
    ##credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    #credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)

    client = vision.ImageAnnotatorClient() # todo: explicit credentials
    #return client
    

def landmark_description(img_filepath):
    print("ANNOTATIONS:", len(annotations))
for annotation in annotations:
    print("---------------")
    print(type(annotation), annotation.locale)
    print(annotation.description)
 each  annotation is a <class 'google.cloud.vision_v1.types.EntityAnnotation'>



if __name__ == "__main__":

    #img_filepath = os.path.join(os.path.dirname(__file__), "images", file_selection)
    #print("IMAGE FILEPATH:", os.path.isfile(img_filepath), img_filepath)
    #print(os.path.isfile(img_filepath)
#
    image_folder = input ("Please Enter Folder Directory Containing Your Image Files:") 
    folder_content = os.listdir(image_folder)
    print (image_folder)
    print (folder_content)
    if not os.path.exists(image_folder):
        print ("Path of the file is invalid")
    else:
        image_selection = input ("Enter a Valid Image Name (In Lower Case Only): ")
        print(folder_content)
    
    if image_selection.lower() in folder_content:
        print("Your Landmark Detection is on Its Way!")
    else:
        print("Oops! I Don't See This File In Your Folder. Please Try Again")  # rerun the original input prompt
    
    file_path = os.path.join(str(image_folder), str(image_selection))
    with image.open(file_path),'rb') as image:
        content = image.read()
    image = types.Image(content=content) #> <class 'google.cloud.vision_v1.types.Image'>

    breakpoint()
# 
# 
# print("CREDENTIALS FILEPATH:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
#

#    

#
#    print(type(client))
#    response = client.landmark_detection(image=image)
#    print(type(response))
#
#  
#    breakpoint()
