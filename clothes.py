import streamlit as st

# 🌤️ 기본 페이지 설정
st.set_page_config(page_title="오늘의 패션 추천 👕🧤", page_icon="🌈", layout="centered")

# 🌸 타이틀 & 설명
st.markdown(
    """
    <h1 style='text-align:center; font-size:50px;'>👗 오늘의 패션 추천 🎩</h1>
    <p style='text-align:center; font-size:20px;'>
    ☀️ 날씨와 온도를 입력하면, 오늘의 스타일을 추천해드려요! 💃🕺<br>
    화려한 이모지와 함께 기분까지 UP! 🌈✨
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 🌦️ 입력창
weather = st.selectbox(
    "오늘의 날씨는 어떤가요? 🌤️",
    ["☀️ 맑음", "🌤️ 구름 조금", "☁️ 흐림", "🌧️ 비", "🌨️ 눈", "🌪️ 바람 많음"]
)

temperature = st.slider("현재 온도를 알려주세요 🌡️", -10, 40, 20)

st.markdown("---")

# 👕 추천 로직
def recommend_outfit(weather, temp):
    if temp >= 28:
        return "😎 여름 한가운데! 반팔티 + 반바지 + 선글라스 🕶️ + 시원한 샌들 🩴"
    elif 23 <= temp < 28:
        return "🌞 따뜻한 날씨엔 반팔티 + 얇은 셔츠 + 슬랙스 + 운동화 👟"
    elif 17 <= temp < 23:
        return "🍂 선선한 날씨엔 긴팔티 + 가디건 or 얇은 자켓 🧥 + 청바지 👖"
    elif 10 <= temp < 17:
        return "🌬️ 조금 쌀쌀해요! 맨투맨 or 니트 + 코트 🧥 + 스카프 🧣"
    elif 4 <= temp < 10:
        return "❄️ 추운 날씨엔 패딩 🧊 + 목도리 🧣 + 장갑 🧤"
    else:
        return "🥶 매우 추워요! 롱패딩 + 털모자 + 방한부츠 필수! ⛄"

# 날씨별 디테일 추가
extra = {
    "☀️ 맑음": "햇빛이 강하니 선크림 ☀️ + 선글라스 🕶️ 꼭 챙기세요!",
    "🌤️ 구름 조금": "산책하기 딱 좋은 날씨예요 🚶‍♀️☁️",
    "☁️ 흐림": "조금 어두워요 🌫️ 밝은 색 옷 추천 💛",
    "🌧️ 비": "우산 ☂️ + 방수 신발 👢 필수!",
    "🌨️ 눈": "미끄러우니 따뜻하고 미끄럼 방지 신발 👢 신어요!",
    "🌪️ 바람 많음": "바람막이 자켓 🧥 or 후드티 추천 🌬️"
}

# 🎯 추천 결과 출력
if st.button("✨ 나의 패션 추천 보기 ✨"):
    outfit = recommend_outfit(weather, temperature)
    st.markdown(
        f"""
        <div style='text-align:center; font-size:25px; background-color:#fff7e6; padding:20px; border-radius:20px;'>
        <h2>{weather}</h2>
        <p style='font-size:30px;'>{outfit}</p>
        <p style='font-size:20px;'>{extra[weather]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 🎨 꾸밈용 이모지 폭발 효과
    st.markdown(
        "<p style='text-align:center; font-size:40px;'>💖🌸🌈✨👒🧣👕👗🧥👟🕶️🩴🧤🎀💫</p>",
        unsafe_allow_html=True
    )

# 👠 하단 문구
st.markdown(
    """
    ---
    <p style='text-align:center; font-size:16px; color:gray;'>
    Made with ❤️ by <b>Streamlit</b> & ChatGPT GPT-5 ✨<br>
    Stay stylish, always! 👑
    </p>
    """,
    unsafe_allow_html=True
)
