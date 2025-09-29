import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="광합성 실험 활동지", layout="wide")

st.title("🌱 광합성 실험 활동지")
st.markdown("""
#### 실험 목표
광합성에 영향을 주는 다양한 조건(빛의 세기, 온도, 이산화탄소 농도 등)에 따라 광합성 속도의 변화를 관찰한다.
""")

st.sidebar.header("실험 변수 입력")
student_name = st.sidebar.text_input("이름")
date = st.sidebar.date_input("실험 날짜")
light = st.sidebar.slider("빛의 세기 (lux)", 0, 10000, 5000, step=500)
temp = st.sidebar.slider("온도 (℃)", 0, 50, 25)
co2 = st.sidebar.slider("CO₂ 농도 (ppm)", 0, 2000, 400, step=50)
time = st.sidebar.number_input("측정 시간 (분)", min_value=1, max_value=60, value=10)

st.header("1. 실험 변수 요약")
st.write(f"**이름:** {student_name}")
st.write(f"**실험 날짜:** {date}")
st.write(f"**빛의 세기:** {light} lux")
st.write(f"**온도:** {temp} ℃")
st.write(f"**CO₂ 농도:** {co2} ppm")
st.write(f"**측정 시간:** {time} 분")

st.header("2. 광합성 속도 예측 및 시각화")
# 예시: 단순 모델 (실제 실험에서는 측정값 입력)
def predict_photosynthesis(light, temp, co2):
    # 빛, 온도, CO2에 따른 임의의 함수 (예시)
    return max(0, (light/10000) * (1 - abs(temp-25)/25) * (co2/2000) * 100)

rate = predict_photosynthesis(light, temp, co2)
st.metric("예상 광합성 속도 (상대값)", f"{rate:.1f}")

# 변수 변화에 따른 그래프
st.subheader("빛의 세기 변화에 따른 광합성 속도")
light_range = np.arange(0, 10001, 500)
rate_light = [predict_photosynthesis(l, temp, co2) for l in light_range]
df_light = pd.DataFrame({"빛의 세기(lux)": light_range, "광합성 속도": rate_light})
st.line_chart(df_light.set_index("빛의 세기(lux)"))

st.subheader("온도 변화에 따른 광합성 속도")
temp_range = np.arange(0, 51, 2)
rate_temp = [predict_photosynthesis(light, t, co2) for t in temp_range]
df_temp = pd.DataFrame({"온도(℃)": temp_range, "광합성 속도": rate_temp})
st.line_chart(df_temp.set_index("온도(℃)"))

st.subheader("CO₂ 농도 변화에 따른 광합성 속도")
co2_range = np.arange(0, 2001, 100)
rate_co2 = [predict_photosynthesis(light, temp, c) for c in co2_range]
df_co2 = pd.DataFrame({"CO₂ 농도(ppm)": co2_range, "광합성 속도": rate_co2})
st.line_chart(df_co2.set_index("CO₂ 농도(ppm)"))

st.header("3. 실험 결과 기록")
st.markdown("실험에서 관찰한 실제 결과를 아래 표에 기록하세요.")
if "records" not in st.session_state:
    st.session_state["records"] = []

with st.form("record_form"):
    obs_time = st.number_input("관찰 시간(분)", min_value=0, max_value=60, value=0)
    obs_bubble = st.number_input("기포 수(광합성 산물)", min_value=0, max_value=100, value=0)
    submitted = st.form_submit_button("기록 추가")
    if submitted:
        st.session_state["records"].append({
            "관찰 시간(분)": obs_time,
            "기포 수": obs_bubble
        })

if st.session_state["records"]:
    df_records = pd.DataFrame(st.session_state["records"])
    st.table(df_records)
    st.line_chart(df_records.set_index("관찰 시간(분)"))
else:
    st.info("아직 기록이 없습니다. 위 폼을 통해 실험 결과를 추가하세요.")

st.header("4. 실험 소감 및 메모")
memo = st.text_area("실험 소감/메모를 작성하세요.")
feedback = ""
if st.button("소감 피드백 받기"):
    if not memo.strip():
        feedback = "소감 내용을 입력해 주세요."
    elif len(memo) < 20:
        feedback = "조금 더 구체적으로 작성해 보세요! 실험 과정, 느낀 점, 궁금한 점 등을 포함하면 좋아요."
    elif any(word in memo for word in ["재미", "흥미", "유익", "어려움", "성공", "실패"]):
        feedback = "실험에 대한 느낌과 경험이 잘 드러나 있어요! 구체적인 사례나 생각을 더 추가해도 좋아요."
    else:
        feedback = "좋은 소감입니다! 실험에서 새롭게 알게 된 점이나 앞으로의 궁금증도 적어보면 더 좋아요."
    st.info(feedback)
if memo:
    st.success("소감이 저장되었습니다!")
