from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import io
import gradio as gr

# Authenticate client
prediction_endpoint = "https://cvgradio-prediction.cognitiveservices.azure.com"
prediction_key = "7290a12026054f7fa6b49ea9d033222c"
project_id = "6a07261c-a976-4f9c-b3f9-1c0dffdc6fa8"
model_name = "Iteration1"

credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=credentials)

def predict_image(input_img): 
    h, w, ch= np.array(input_img).shape 
    img_byte_arr = io.BytesIO() 
    input_img.save(img_byte_arr, format='png') 
    img_bytes = img_byte_arr.getvalue() 
    results = predictor.detect_image(project_id, model_name, img_bytes) 

    fig = plt.figure(figsize=(8,8)) 
    plt.axis('off') 

    draw = ImageDraw.Draw(input_img) 
    lineWidth = int(w/100) 
    color = 'magenta' 

    for prediction in results.predictions: 
        if (prediction.probability*100) > 50: 
            left = prediction.bounding_box.left * w 
            top = prediction.bounding_box.top * h 
            width = prediction.bounding_box.width * w 
            height = prediction.bounding_box.height * h 

            points = ((left,top), (left+width,top), (left+width,top+height), (left,top+height),(left,top)) 
            draw.line(points, fill=color, width=lineWidth) 
            plt.annotate(prediction.tag_name + ' {0:.2f}%'.format(prediction.probability * 100), (left, top), color=color)

    plt.imshow(input_img)
    
    # Save the plot to a BytesIO object in PNG format
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    
    # Read the BytesIO object back into a PIL Image and return it
    output_img = Image.open(buf)
    
    return output_img

demo = gr.Interface(fn=predict_image, inputs=gr.Image(type='pil'), outputs='image') 
demo.launch(share=True)
