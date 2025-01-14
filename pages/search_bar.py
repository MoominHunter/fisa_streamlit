import streamlit as st

#검색창 만들기
#text를 입력하는 검색창을 하나 입력
#ani_list에 있는 단어를 검색하면
#img_list에 있는 이미지를 출력

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

search = st.text_input("검색하실 애니메이션을 입력하세요")


for ani in ani_list:
    if search in ani:
        img_dix = ani_list.index(search)
