import streamlit as st
import pathlib
from PIL import Image, ImageDraw

st.set_page_config( 
    layout="wide"
)
col_num=5
cols = st.columns(col_num, gap="medium")

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
            line_width = 4
            line_color = (0,0,0)
            if len(img.name.split('_')) == 4:
                num = img.name.split('_')[2].split('-')[0]
                if o <= int(num) <= z:
                    name = img.name
                    image = Image.open(str(img))
                    sw,sh = image.size
                    #キャンバス作成
                    cw,ch = sw + line_width*2, sh + line_width*2
                    canvas_im = Image.new('RGB', (cw, ch))
                    # キャンバスのImageDrawオブジェクトを作成
                    canvas = ImageDraw.Draw(canvas_im)
                    # キャンバスを単色で塗りつぶす
                    canvas.rectangle([(0, 0), (cw, ch)], fill=line_color)
                    # キャンバスの画像に元の画像を貼り付け
                    canvas_im.paste(image, (line_width, line_width))
                    

                    if i % col_num == 0:
                        with st.container():
                            cols[0].image(canvas_im, caption=name)
                        
                    if i % col_num == 1:
                        with st.container():
                            cols[1].image(canvas_im, caption=name)
                        
                    if i % col_num == 2:
                        with st.container():
                            cols[2].image(canvas_im, caption=name)
                        
                    if i % col_num == 3:
                        with st.container():
                            cols[3].image(canvas_im, caption=name)
                        
                    if i % col_num == 4:
                        with st.container():
                            cols[4].image(canvas_im, caption=name)