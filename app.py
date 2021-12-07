import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')


st.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
st.dataframe(df.style.highlight_max(axis=0), width=500, height=300)
st.table(df.style.highlight_max(axis=0))

"""
# header 1
## header 2
### header 3

```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)

"""
## マップ
"""
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)

"""
## Display Image
"""
if st.checkbox('Show Image'):
    img = Image.open('avatar.png')
    st.image(img, caption='Sample', use_column_width=True)

st.write('## Interactive widgets')
st.sidebar.write('# Interactive widgets')
option = st.sidebar.selectbox(
    '好きな数字は？',
    options=list(range(1, 11))
)
'あなたの好きな数字は、', option, 'ですね。'


input_txt = st.sidebar.text_input('あなたの趣味は？')
'あなたの趣味は、', input_txt, 'ですね。'

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション、', condition


st.write('## Columns')
left_column, right_cloumn = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_cloumn.write('ここに文字を書く')


st.write('## プログレスバー')
'Start!!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)
'Done!!!'


st.write('## Expander')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
