import sklearn
import pandas as pd
import numpy as np
import streamlit as st
import easyocr
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

st.set_page_config(page_title='Text Extractor')
st.title("แปลงข้อความจากรูปภาพ - EasyOCR") 

input = st.file_uploader('', type = ['jpg', 'jpeg', 'png'])
if input is not None:
    image = Image.open(input) 
    reader = easyocr.Reader(['th','en']) 
    result = reader.readtext(np.array(image))

    textdic_easyocr = {} 
    for idx in result: 
        pred_text = idx[1]
        pred_confidence = idx[2] 
        textdic_easyocr[pred_text] = {} 
        textdic_easyocr[pred_text]['ค่าความเชื่อมั่น'] = pred_confidence
    df = pd.DataFrame.from_dict(textdic_easyocr).T
    st.table(df)

    draw = ImageDraw.Draw(image)
    for res in result:
        top_left = tuple(res[0][0]) 
        bottom_right = tuple(res[0][2]) 
        draw.rectangle((top_left, bottom_right), outline="blue", width=2)
    st.image(image)