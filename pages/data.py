

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os


# 한글 폰트 설정 (NanumGothic-Regular.ttf)
font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')
if os.path.exists(font_path):
	fm.fontManager.addfont(font_path)
	plt.rc('font', family='NanumGothic')
	plt.rcParams['axes.unicode_minus'] = False

st.title("📊 예시 성적 데이터 분석")

# 예시 데이터 생성
@st.cache_data
def load_data():
	np.random.seed(42)
	names = [f"학생{i+1}" for i in range(30)]
	scores_kor = np.random.randint(60, 100, size=30)
	scores_eng = np.random.randint(50, 100, size=30)
	scores_math = np.random.randint(40, 100, size=30)
	df = pd.DataFrame({
		"이름": names,
		"국어": scores_kor,
		"영어": scores_eng,
		"수학": scores_math
	})
	df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1)
	return df

df = load_data()

st.header("1. 전체 데이터 미리보기")
st.dataframe(df)

st.header("2. 요약 통계")
st.write(df.describe())


st.header("3. 과목별 점수 분포 시각화 (한글 폰트 적용)")
subjects = ["국어", "영어", "수학"]
for subject in subjects:
	st.subheader(f"{subject} 점수 분포")
	fig, ax = plt.subplots(figsize=(8, 3))
	df_sorted = df.sort_values(subject, ascending=False)
	ax.bar(df_sorted["이름"], df_sorted[subject], color="#4C72B0")
	ax.set_xlabel("이름")
	ax.set_ylabel("점수")
	ax.set_title(f"{subject} 점수 분포")
	plt.xticks(rotation=45, ha='right', fontsize=8)
	st.pyplot(fig)

st.header("4. 학생별 점수 조회 및 필터")
min_avg = st.slider("평균 점수 최소값", 40, 100, 60)
filtered = df[df["평균"] >= min_avg]
st.write(f"평균 {min_avg}점 이상 학생 수: {len(filtered)}명")
st.dataframe(filtered)

st.header("5. 상위/하위 학생 랭킹")
top_n = st.number_input("상위/하위 학생 수", min_value=1, max_value=10, value=5)
st.subheader("상위 학생")
st.table(df.sort_values("평균", ascending=False).head(top_n))
st.subheader("하위 학생")
st.table(df.sort_values("평균").head(top_n))
