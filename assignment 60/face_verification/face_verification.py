!pip install insightface
!pip install matplotlib
!pip install pyfiglet
!pip install numpy
!pip install argparse
!pip install mxnet
!pip install onnxruntime

import cv2
import pyfiglet
from insightface.app import FaceAnalysis
import numpy as np
import argparse

app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
app.prepare(ctx_id=0, det_size=(640, 640))

image_1 = cv2.imread("/content/face_bank/robert pattinson/r1.jpg")
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)

result = app.get(image_1)
embeding1 = result[0]["embedding"]

image_2 = cv2.imread("/content/face_bank/robert pattinson/r2.jpg")
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)

result2 = app.get(image_2)
embeding2 = result2[0]["embedding"]

if np.sqrt(np.sum((embeding1 - embeding2)**2))<25:
    out = pyfiglet.figlet_format("same")
    print(out)
else:
    out = pyfiglet.figlet_format("Different")
    print(out)
