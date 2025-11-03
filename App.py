import streamlit as st
from PIL import Image

# ---------------------------
# 앱 타이틀 & 소개
# ---------------------------
st.set_page_config(page_title="지구 키우기", layout="centered")
st.title("🌍 지구 키우기")
st.markdown("""
이 앱은 환경 오염의 심각성을 보여주고, 환경 친화적 행동을 통해 지구를 행복하게 만드는 게임입니다.
""")

# ---------------------------
# 시작 화면: 환경 문제 시각화
# ---------------------------
st.header("지금 지구 상태")
st.markdown("""
전 세계적으로 환경 오염이 심각합니다.  
- 연간 플라스틱 쓰레기: 3억 톤  
- 기후변화로 해수면 상승: 연 3.7mm  
지금 지구는 슬퍼하고 있어요 😢
""")
sad_earth = Image.open("sad_earth.png")  # 슬픈 지구 이미지
st.image(sad_earth, width=300)

# ---------------------------
# 행동 스코어 시스템
# ---------------------------
st.header("🌱 환경 행동으로 지구를 행복하게 해주세요!")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "actions" not in st.session_state:
    st.session_state.actions = []

# 행동 버튼과 점수
actions_dict = {
    "분리수거 ♻️ (+5)": 5,
    "텀블러 사용 ☕ (+3)": 3,
    "대중교통 이용 🚌 (+4)": 4,
    "일회용품 줄이기 🛍️ (+5)": 5
}

cols = st.columns(len(actions_dict))
for i, (action, points) in enumerate(actions_dict.items()):
    with cols[i]:
        if st.button(action):
            st.session_state.score += points
            st.session_state.actions.append(action.split(" ")[0])  # 행동 이름만 저장

# 스코어 바 & 지구 행복도
st.subheader(f"현재 점수: {st.session_state.score}")
happiness = min(st.session_state.score / 50, 1.0)
st.progress(happiness)

# 지구 캐릭터 변화
if happiness < 0.3:
    earth_img = Image.open("sad_earth.png")
elif happiness < 0.7:
    earth_img = Image.open("neutral_earth.png")
else:
    earth_img = Image.open("happy_earth.png")
st.image(earth_img, width=300)

# ---------------------------
# 실천한 행동 목록
# ---------------------------
st.header("✅ 오늘 실천한 행동")
if st.session_state.actions:
    for i, act in enumerate(st.session_state.actions, 1):
        st.write(f"{i}. {act}")
else:
    st.write("아직 실천한 행동이 없어요. 위 버튼을 눌러 지구를 행복하게 해주세요!")

# ---------------------------
# 환경 미션
# ---------------------------
st.header("🎯 오늘의 환경 미션")
missions = [
    "플라스틱 컵 1개 줄이기",
    "전기 사용 1시간 줄이기",
    "텀블러로 음료 마시기",
    "분리수거 철저히 하기"
]
st.info(f"오늘의 미션: {missions[st.session_state.score % len(missions)]}")
