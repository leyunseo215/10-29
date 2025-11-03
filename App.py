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
# 데이터 불러오기 (네가 올린 파일)
# ---------------------------
df = pd.read_csv("TalkFile_World.csv.csv")

# 최신 연도 데이터만 선택
latest_year = df["year"].max()
latest_data = df[df["year"] == latest_year]

# NaN 제거 및 단위 변환
latest_data = latest_data[["country", "iso_code", "year", "co2", "gdp", "population", "co2_per_capita"]].dropna()
latest_data.rename(columns={
    "country": "국가",
    "iso_code": "ISO",
    "co2": "CO₂ 배출량(백만톤)",
    "co2_per_capita": "1인당 CO₂(톤)",
    "population": "인구(명)",
    "gdp": "GDP(달러)"
}, inplace=True)

# ---------------------------
# 첫 화면: 지도 시각화
# ---------------------------
if st.session_state.page == "start":
    st.title("🌍 지구 키우기 🌱💚")
    st.markdown("""
    전 세계 나라별 CO₂ 배출 현황을 확인하고,  
    **마우스를 올려 각 나라의 세부 정보를 살펴보세요!** 🌏
    """)

    fig = px.choropleth(
        latest_data,
        locations="ISO",
        color="CO₂ 배출량(백만톤)",
        hover_name="국가",
        hover_data={
            "1인당 CO₂(톤)": True,
            "GDP(달러)": True,
            "인구(명)": True
        },
        color_continuous_scale="Reds",
        labels={"CO₂ 배출량(백만톤)": "CO₂ 배출량"},
        title=f"{latest_year}년 세계 CO₂ 배출 지도"
    )

    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

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
                st.balloons()
                st.success(f"{action.split()[0]} 실천 완료! 💚🌿✨")

    st.subheader(f"현재 점수: {st.session_state.score}")
    happiness = min(st.session_state.score / 50, 1.0)
    st.progress(happiness)

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
