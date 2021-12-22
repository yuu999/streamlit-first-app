import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# -----------------------
# タイトル
# -----------------------
st.title('Streamlit 超入門')

# -----------------------
# ヘッダー
# -----------------------
st.header('ヘッダー')

# -----------------------
# サブヘッダー
# -----------------------
st.subheader('サブヘッダー')

# -----------------------
# Markdown記法
# -----------------------
md = """
---
**マークダウン**記法にも対応している。
# header 1
## header 2
### header 3

- List1
- List2

```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
```
"""
st.markdown(md)

# -----------------------
# DataFrameと表、チャート
# -----------------------
st.header('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
st.dataframe(df.style.highlight_max(axis=0), width=500, height=300) # インタラクティブな表が作成可能（ソート可能）
st.table(df.style.highlight_max(axis=0))                            # スタティックな表が作成可能（ソート不能）

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)

# -----------------------
# マップ
# -----------------------
st.header('Map')
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)

# -----------------------
# 画像の表示
# -----------------------
st.header('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Sample', use_column_width=True)

# -----------------------
# インタラクティブなウィジェット
# -----------------------
st.header('Interactive widgets')
st.sidebar.header('Interactive widgets')
num = st.sidebar.selectbox(
    '好きな数字は？',
    options=list(range(1, 11))
)
st.write('##### サイドバーの好きな数字を指定すると？')
st.write('あなたの好きな数字は、', num, 'ですね。')

input_txt = st.sidebar.text_input('あなたの趣味は？')
st.write('##### サイドバーの趣味を入力すると？')
st.write('あなたの趣味は、', input_txt, 'ですね。')

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
st.write('##### サイドバーの調子を調整すると？')
st.write('コンディション、', condition)

# -----------------------
# カラム表示
# -----------------------
st.write('## Columns')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "25 °C", "3.0 °C")
col2.metric("Wind", "9 m/s", "-8%")
col3.metric("Humidity", "86%", "4%")

# -----------------------
# プログレスバー 
# -----------------------
st.write('## プログレスバー')
if st.button('Start Progress Bar'):
    'Start!!!'
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Iteration {i + 1}')
        bar.progress(i + 1)
        time.sleep(0.05)
    'Done!!!'

# -----------------------
# 拡張、縮小機能
# -----------------------
st.write('## Expander')
expander = st.expander('Question')
expander.write('Anser 1')
expander.write('Anser 2')
