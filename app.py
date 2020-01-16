from twilio.rest import Client
from flask import Flask, render_template, request, jsonify

from keras.models import model_from_json

import numpy as np
from PIL import Image
import io
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("plant_model8.h5")
print("Loaded model from disk")
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
account_sid = 'AC08ac61213eef427665f6604c686d401b'
auth_token = '9ecf348cbf6a6f15b53aa41d0c631d59'
app = Flask(__name__)


@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == "GET":
        return render_template("index.html")
   
    if request.files and 'picfile' in request.files:
        f = request.files["picfile"].read()
        img = Image.open(io.BytesIO(f))
        img.save('test.jpg')
        img = np.asarray(img) / 255.
        img = np.expand_dims(img, axis=0)
        pred = loaded_model.predict(img)
        
        x = np.argmax(pred, axis=-1)
        if x == [0] :
            print("Pepper_bell_Bacterial_spot")
   
    
   
            client = Client(account_sid, auth_token)
            message = client.messages \
            .create(
                body="Pepper_bell_Bacterial_spot",
                from_='+12036354778',
                to='+91 8766315644'
                )
            print(message.sid)
            return message.sid
            
        if x == [1]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body= "Pepper_bell_Healthy",
                from_="+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
            
        if x == [2]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "POTATO EARLY BRIGHT",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
        if x == [3]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease potato healthy",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
        
        if x == [4]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease potato late blight",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
        if x == [5]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease tomato target spot",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
            
        if x == [6]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease tomato mosaic virus",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)     
            return message.sid
        if x == [7]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato Yellow Leaf Curl Virus.",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
            
        if x == [8]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato Bacterial Spot",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)    
            return message.sid
        if x == [9]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato Early Blight",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)   
            return message.sid
            
        if x == [10]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato healthy",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid) 
            return message.sid
            
            
        if x == [11]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato Late Blight",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
            
            
        if x == [12]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato leaf mold",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)
            return message.sid
            
        if x == [13]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato Septoria leaf spot",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)  
            return message.sid
            
        if x == [14]:
            client = Client(account_sid,auth_token)
            message = client.messages \
            .create(
                body = "the plant has the following disease Tomato Spider Mites Two Spotted Spider Mite",
                from_= "+12036354778",
                to = "+91 8766315644"
                )
            print(message.sid)  
            return message.sid
            
        return message.sid    
         
    return render_template("index.html")  
    
@app.route("/offline.html")
def offline():
    return app.send_static_file('offline.html')
        
             
@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')     
        
    
    
if __name__ == '__main__':
   app.run(debug = False)        