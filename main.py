import streamlit as st
import pathlib
from PIL import Image, ImageDraw
import time

st.set_page_config( 
    layout="wide"
)
col_num=5
cols = st.columns(col_num, gap="medium")
cols2 = st.columns(col_num, gap="medium")
cols3 = st.columns(col_num, gap="medium")
cols4 = st.columns(col_num, gap="medium")
cols5 = st.columns(col_num, gap="medium")
cols6 = st.columns(col_num, gap="medium")
cols7 = st.columns(col_num, gap="medium")
cols8 = st.columns(col_num, gap="medium")
cols9 = st.columns(col_num, gap="medium")
cols10 = st.columns(col_num, gap="medium")
cols11 = st.columns(col_num, gap="medium")
cols12 = st.columns(col_num, gap="medium")
cols13 = st.columns(col_num, gap="medium")
cols14 = st.columns(col_num, gap="medium")
cols15 = st.columns(col_num, gap="medium")
cols16 = st.columns(col_num, gap="medium")
cols17 = st.columns(col_num, gap="medium")
cols18 = st.columns(col_num, gap="medium")
cols19 = st.columns(col_num, gap="medium")
cols20 = st.columns(col_num, gap="medium")

with st.sidebar:
    st.header('画像表示')

    img_path = st.text_input('画像パスを入力','')
    level = st.text_input('レベルを入力','')
    btn = st.button('画像表示', key=0)
    target_path = rf"{img_path}\{level}"
    st.header(target_path)

ones = list(range(1,201,10))
zeros = list(range(10,201,10))
folders = [f'{o}_{z}' for o,z in zip(ones,zeros)]

if btn:
    for i,img in enumerate(pathlib.Path(rf'{target_path}\1_10').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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

    # time.sleep(1)

    for i,img in enumerate(pathlib.Path(rf'{target_path}\11_20').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols2[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols2[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols2[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols2[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols2[4].image(canvas_im, caption=name)
                    
    # time.sleep(1)
    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\21_30').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols3[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols3[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols3[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols3[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols3[4].image(canvas_im, caption=name)
                    
    # time.sleep(1)
    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\31_40').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols4[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols4[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols4[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols4[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols4[4].image(canvas_im, caption=name)
                    
    # time.sleep(1)
    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\41_50').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols5[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols5[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols5[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols5[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols5[4].image(canvas_im, caption=name)
                    
    # time.sleep(1)
    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\51_60').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols6[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols6[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols6[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols6[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols6[4].image(canvas_im, caption=name)
                    
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\61_70').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols7[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols7[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols7[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols7[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols7[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\71_80').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols8[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols8[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols8[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols8[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols8[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\81_90').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols9[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols9[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols9[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols9[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols9[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\91_100').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols10[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols10[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols10[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols10[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols10[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\101_110').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols11[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols11[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols11[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols11[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols11[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\111_120').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols12[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols12[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols12[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols12[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols12[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\121_130').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols13[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols13[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols13[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols13[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols13[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\131_140').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols14[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols14[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols14[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols14[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols14[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\141_150').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols15[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols15[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols15[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols15[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols15[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\151_160').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols16[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols16[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols16[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols16[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols16[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\161_170').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols17[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols17[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols17[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols17[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols17[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\171_180').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols18[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols18[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols18[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols18[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols18[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\181_190').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols19[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols19[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols19[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols19[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols19[4].image(canvas_im, caption=name)
                    
    for i,img in enumerate(pathlib.Path(rf'{target_path}\191_200').glob(rf'**\*.png')):
        line_width = 4
        line_color = (0,0,0)
        if len(img.name.split('_')) == 4:
            num = img.name.split('_')[2].split('-')[0]
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
                    cols20[0].image(canvas_im, caption=name)
                
            if i % col_num == 1:
                with st.container():
                    cols20[1].image(canvas_im, caption=name)
                
            if i % col_num == 2:
                with st.container():
                    cols20[2].image(canvas_im, caption=name)
                
            if i % col_num == 3:
                with st.container():
                    cols20[3].image(canvas_im, caption=name)
                
            if i % col_num == 4:
                with st.container():
                    cols20[4].image(canvas_im, caption=name)