import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="🌍 지구 키우기", layout="wide")

# ---------------------------
# 페이지 상태 초기화
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "start"
if "score" not in st.session_state:
    st.session_state.score = 0
if "actions" not in st.session_state:
    st.session_state.actions = []

# ---------------------------
# 페이지 전환 함수
# ---------------------------
def go_to(page):
    st.session_state.page = page

# ---------------------------
# 데이터: 탄소 배출 예시
# ---------------------------
data = pd.DataFrame({
    "국가": ["중국", "미국", "인도", "한국", "일본"],
    "CO2(억 톤)": [100, 50, 30, 7, 12],
    "ISO": ["CHN", "USA", "IND", "KOR", "JPN"]
})

# ---------------------------
# 첫 화면: 탄소 배출 지도
# ---------------------------
if st.session_state.page == "start":
    st.title("🌍 지구 키우기 🌱💚")
    st.markdown("""
    지구의 탄소 배출량을 확인하고, 작은 실천으로 지구를 행복하게 만들어보세요! 🎉
    """)

    # Plotly 지도 시각화
    fig = px.choropleth(
        data, locations="ISO",
        color="CO2(억 톤)",
        hover_name="국가",
        color_continuous_scale="Reds",
        labels={"CO2(억 톤)": "CO2 배출량"}
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig)

    st.button("🌱 환경 실천하러 가기", on_click=go_to, args=("action",))

# ---------------------------
# 행동 스코어 화면
# ---------------------------
elif st.session_state.page == "action":
    st.header("🌱 환경 행동으로 지구를 행복하게 해주세요!")

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
                st.session_state.actions.append(action.split(" ")[0])
                st.balloons()  # 🎉 폭발 효과
                st.success(f"{action.split()[0]} 실천 완료! 💚🌿✨")

    # 행복도 계산
    st.subheader(f"현재 점수: {st.session_state.score}")
    happiness = min(st.session_state.score / 50, 1.0)
    st.progress(happiness)

    # 지구 감정 변화
    st.header("🌍 지구 감정")
    if happiness < 0.3:
        st.markdown("😢 슬퍼하는 지구...")
    elif happiness < 0.7:
        st.markdown("🙂 조금 괜찮아진 지구...")
    else:
        st.markdown("😁🌿💚 행복한 지구! 지구가 춤춰요! 💃🎉✨")

    st.button("📋 행동 기록 & 미션 보기", on_click=go_to, args=("mission",))

# ---------------------------
# 행동 기록 & 미션 화면
# ---------------------------
elif st.session_state.page == "mission":
    st.header("✅ 오늘 실천한 행동")
    if st.session_state.actions:
        for i, act in enumerate(st.session_state.actions, 1):
            st.write(f"{i}. {act} ✅")
    else:
        st.write("아직 실천한 행동이 없어요 🌱")

    st.header("🎯 오늘의 환경 미션")
    missions = [
        "플라스틱 컵 1개 줄이기 🥤❌",
        "전기 사용 1시간 줄이기 💡⚡",
        "텀블러로 음료 마시기 ☕🌿",
        "분리수거 철저히 하기 ♻️💚"
    ]
    st.info(f"오늘의 미션: {missions[st.session_state.score % len(missions)]}")

    st.button("🏠 처음 화면으로 돌아가기", on_click=go_to, args=("start",))
