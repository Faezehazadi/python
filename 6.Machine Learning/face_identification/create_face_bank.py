!pip install insightface
!pip install onnxruntime
!pip install numpy
!pip install mxnet

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis

app = FaceAnalysis(name="buffalo_s", providers=['CUDAExecutionProvider']) 
app.prepare(ctx_id=0, det_size=(640, 640)) 

face_bank_path = "/content/face_bank"

face_bank = [] 
for person_name in os.listdir(face_bank_path):
  folder_path = os.path.join(face_bank_path, person_name)
  if os.path.isdir(folder_path): 
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = app.get(image)

        if len(result) > 1:  
            print("Warning: more than one face detevted in image")
            continue  
        embedding = result[0]['embedding']  
        my_dict = {"name": person_name, "embedding": embedding}
        face_bank.append(my_dict)

np.save("face_bank.npy",face_bank )  