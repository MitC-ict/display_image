import streamlit as st
import pathlib
from PIL import Image

num=5
cols = st.columns(num, gap="medium")

with st.sidebar:
    st.header('画像表示')

    img_path = st.text_input('画像パスを入力','')
    level = st.text_input('レベルを入力','')
    btn = st.button('画像表示', key=0)
    target_path = rf"{img_path}\{level}"
    st.header(target_path)

ones = list(range(1,201,10))
zeros = list(range(10,201,10))


if btn:
    for o,z in zip(ones,zeros):
        for i,img in enumerate(pathlib.Path(target_path).glob(rf'**\*.png')):
            if len(img.name.split('_')) == 4:
                num = img.name.split('_')[2].split('-')[0]
                if o <= int(num) <= z:
                    name = img.name
                    image = Image.open(str(img))

                    if i % 5 == 0:
                        with st.container():
                            cols[0].image(image, caption=name)
                        
                    if i % 5 == 1:
                        with st.container():
                            cols[1].image(image, caption=name)
                        
                    if i % 5 == 2:
                        with st.container():
                            cols[2].image(image, caption=name)
                        
                    if i % 5 == 3:
                        with st.container():
                            cols[3].image(image, caption=name)
                        
                    if i % 5 == 4:
                        with st.container():
                            cols[4].image(image, caption=name)