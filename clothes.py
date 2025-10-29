import streamlit as st
import random
import time

# 앱 설정
st.set_page_config(page_title="한화이글스 우승기원🦅🔥", page_icon="🧡", layout="centered")

# 스타일
st.markdown("""
    <style>
    body {
        background-color: #ff8c1a;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #fff2e6;
        color: #ff6600;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #ff6600;
        color: white;
        border-radius: 15px;
        font-size: 20px;
        padding: 10px 25px;
        font-weight: bold;
        box-shadow: 0px 0px 15px #ffcc80;
    }
    .stButton>button:hover {
        background-color: #ff9933;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("""
    <h1 style='text-align:center; font-size:60px;'>
        🧡🔥 한화이글스 2025 우승 가자앗!!! 🦅🍊🏆
    </h1>
    <h3 style='text-align:center;'>🎆 팬들의 함성으로 대전을 불태우자 💥💪</h3>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "username" not in st.session_state:
    st.session_state["username"] = None

# 랜덤 팬 응원 멘트 리스트 (30개)
random_fans = [
    "류현진 오늘 완봉 가자🔥", "정은원 홈런 예감🍊", "한화는 질 수 없다💪",
    "이글스는 살아있다🦅", "오늘도 불꽃 타선💥", "대전구장 불타오른다🔥",
    "팬심이 곧 승리다🏆", "우리의 봄은 오렌지색🌸", "끝까지 간다 한화💪",
    "오늘 10점차로 이긴다😁", "김태균 시절이 돌아온다🔥", "이글스 포에버🦅",
    "류현진 7이닝 무실점 가즈아🔥", "한화 사랑해요🧡", "타자들 미쳤다💥",
    "역전의 한화!!🍊", "우승 트로피는 대전으로🏆", "우리팀이 최고야🎆",
    "이정후도 한화가 무섭대😎", "오늘 경기 레전드각💣", "이글스 불패신화🔥",
    "지금 분위기 완전 좋아🍊", "전광판 터질 준비 완료💥", "팬심 모이면 우승각🧡",
    "한화팬이라 행복하다😭", "류현진 믿는다🦅", "홈런쇼 기대중💪",
    "한화의 날씨는 항상 맑음☀️", "대전은 오늘도 오렌지빛🍊", "한화이글스 포레버🧡"
]

# 닉네임 설정
if not st.session_state["username"]:
    st.markdown("### 💬 먼저 닉네임(응원명)을 정해주세요!")
    username = st.text_input("닉네임을 입력:", placeholder="예: 불꽃한화팬123")
    if st.button("입장하기 🦅"):
        if username.strip():
            st.session_state["username"] = username
            st.success(f"환영합니다 {username}님! 🎉🔥")
            st.balloons()
            st.rerun()
else:
    st.markdown(f"### 🧡 환영합니다, **{st.session_state['username']}** 님! 응원을 남겨주세요🔥")

    msg = st.text_input("🗣️ 응원 메시지:", placeholder="예: 류현진 믿는다!! 🦅🔥")

    if st.button("보내기 🚀"):
        if msg.strip():
            user = st.session_state["username"]
            st.session_state["messages"].append(f"{user}: {msg}")
            
            # 랜덤 팬글 1~3개 자동 추가
            for _ in range(random.randint(1, 3)):
                fake_user = f"팬{random.randint(1, 99)}"
                fake_msg = random.choice(random_fans)
                st.session_state["messages"].append(f"{fake_user}: {fake_msg}")

            st.balloons()
            emoji_list = ["🦅", "🔥", "🏆", "✨", "🍊", "💪", "🎆", "💥", "🧡", "🧨", "🎉"]
            emoji_rain = "".join(random.choices(emoji_list, k=random.randint(60, 120)))
            st.markdown(
                f"<div style='font-size:45px; text-align:center;'>{emoji_rain}</div>",
                unsafe_allow_html=True,
            )
            time.sleep(0.5)
            st.success("🔥 응원 완료! 팬심이 불타오른다!! 🦅")

    # 피드 표시
    st.markdown("---")
    st.markdown("<h2 style='text-align:center;'>📣 실시간 팬 응원 피드 🧡</h2>", unsafe_allow_html=True)

    for i, message in enumerate(reversed(st.session_state["messages"][-30:])):
        bg_color = random.choice(["#fff2e6", "#ffe0b3", "#ffcc80"])
        st.markdown(
            f"""
            <div style='background-color:{bg_color};
                        color:#ff6600;
                        padding:15px;
                        border-radius:15px;
                        margin:10px 0;
                        font-weight:bold;
                        font-size:20px;
                        box-shadow: 0px 0px 10px #ffcc80;'>
                🦅 {message} 🍊🔥
            </div>
            """,
            unsafe_allow_html=True,
        )
