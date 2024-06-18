import streamlit as st


st.title('Trà sữa CoTAI')


col1 , col2 = st.columns(2)
with col1:
  st.image('lEpdPsT.jpeg')

with col2:
  size = st.radio('kích Cỡ', options=('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'), horizontal=True)

  st.write('Thêm')
  coloption1 , coloption2 = st.columns(2)

  with coloption1:
    milk = st.checkbox('Sữa (5K)') ; cafe = st.checkbox('Cà phê (8K)')
  with coloption2:
    cream = st.checkbox('Kem (10K)') ; egg = st.checkbox('Trứng (15K)')


coloption3 , coloption4 = st.columns(2)
with coloption3:
  option = st.multiselect('Topping' , ('Trân châu trắng (5K)' , 'Trân châu đen (5K)' , 'Thạch rau câu (6K)' , 'Vải (7K)' , 'Nhãn (8K)' , 'Đào (10K)'))

with coloption4:
  n = st.number_input('Số lượng', min_value=1, max_value=100, step=1)


ghichu = st.text_area('Ghi chú')


if st.button('Đặt hàng', use_container_width=True):
  if size is 'Nhỏ (30K)':
    st.write('Cỡ nhỏ')
  if size is 'Vừa (40K)':
    st.write('Cỡ vừa')
  if size is 'Lớn (50K)':
    st.write('Cỡ lớn')

  m = []
  tien = 0
  if milk is True:
    m.append('Sữa')
    tien += 5
  if cafe is True:
    m.append('Cà phê')
    tien += 8
  if cream is True:
    m.append('Kem')
    tien += 10
  if egg is True:
    m.append('Trứng')
    tien += 15

  st.write('Thêm:', ', '.join(m))

  st.write('Topping:' , ', '.join(option))

  st.write(ghichu)

  st.write(f'Số lượng: {n}')


  tiensize = 0
  if size == 'Nhỏ (30K)':
    tiensize = 30
  elif size == 'Vừa (40K)':
    tiensize = 40
  else:
   tiensize = 50
  
  tientopping = 0
  if 'Trân châu trắng (5K)' in option:
    tientopping  += 5
  if 'Trân châu đen (5K)' in option:
    tientopping += 5
  if 'Thạch rau câu (6K)' in option:
    tientopping += 6
  if 'Vải (7K)' in option:
    tientopping += 7
  if 'Nhãn (8K)' in option:
    tientopping += 8
  if 'Đào (10K)' in option:
    tientopping += 10
  
  tongtien = (tiensize + tien + tientopping) * n
  tongtien = str(tongtien)
  st.write('Thành tiền:', tongtien + 'K')