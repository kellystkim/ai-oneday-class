from openai import OpenAI
import time
import streamlit as st

# 코드스니펫 - 제목
st.title('제품 홍보 포스터 만들어봐용')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세용.")

if st.button('생성 얍!'):
    st.write(':blue[빨리] *빨리* :blue-background[빨리] :sunglasses:')
    with st.spinner('Wait for it...'):

        client = OpenAI(api_key=st.secrets["API_KEY"])

        chat_completion = client.chat.completions.create(
            messages=[{
                "role":
                "user",
                "content":
                keyword + '라는 주제로 새로운 제품을 홍보할 수 있는 카피를 100자 이내로 작성해줘',
            }],
            model="gpt-4o",
        )

        chat_result = chat_completion.choices[0].message.content
        # 코드스니펫 - 글쓰기
        # st.write(chat_result)
        st.write(f':blue-background[{chat_result}]')

        client = OpenAI(api_key=st.secrets["API_KEY"])

        response = client.images.generate(
            model="dall-e-3",
            prompt=keyword,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        # 코드스니펫 - 이미지
        st.image(image_url)
