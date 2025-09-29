import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit 요소 예시", layout="wide")

st.title("Streamlit 주요 요소 예시")
st.header("1. 텍스트/마크다운/코드")
st.subheader("- 텍스트")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** _지원!_ :sunglasses:")
st.code("print('Hello, Streamlit!')", language="python")
st.latex(r"E=mc^2")

st.header("2. 입력 위젯")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")
color = st.radio("좋아하는 색상은?", ("빨강", "파랑", "초록"))
option = st.selectbox("과일을 선택하세요", ["사과", "바나나", "체리"])
multi = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "여행"])
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")
st.button("버튼")
st.slider("슬라이더", 0, 100, 50)
st.file_uploader("파일 업로드")

st.header("3. 데이터 표시")
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["A", "B", "C"]
)
st.dataframe(df)
st.table(df.head(3))
st.json({"이름": name, "나이": age, "동의": agree})

st.header("4. 차트/그래프")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.header("5. 미디어")
st.image(
    "https://static.streamlit.io/examples/cat.jpg",
    caption="고양이 이미지 예시",
    use_column_width=True
)
st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    format="audio/mp3"
)
st.video(
    "https://www.youtube.com/watch?v=5qap5aO4i9A"
)

st.header("6. 레이아웃")
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

with st.expander("더보기 (Expander)"):
    st.write("이곳에 추가 정보를 넣을 수 있습니다.")

st.sidebar.title("사이드바 예시")
st.sidebar.button("사이드바 버튼")

st.header("7. 진행상황/상태")
st.progress(70)
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")

st.header("8. 기타")
if st.balloons:
    st.balloons()
if st.snow:
    st.snow()
