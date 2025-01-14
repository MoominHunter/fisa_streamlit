import streamlit as st

#검색창 만들기
#text를 입력하는 검색창을 하나 입력
#ani_list에 있는 단어를 검색하면
#img_list에 있는 이미지를 출력

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

ani = st.text_input("검색하실 애니메이션을 입력하세요")

if ani == "짱구는못말려":
    st.image('https://i.imgur.com/t2ewhfH.png')
elif ani == "몬스터":
    st.image('https://i.imgur.com/ECROFMC.png')
elif ani == "릭앤모티":
    st.image('https://i.imgur.com/MDKQoDc.jpg')