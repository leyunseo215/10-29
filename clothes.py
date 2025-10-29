import streamlit as st
import random
import time

# 앱 설정
st.set_page_config(page_title="한화이글스 우승기원🦅🔥", page_icon="🧡", layout="centered")

# 배경색 + 스타일 설정
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

# 세션 저장
if "messages" not in st.session_state:
    st.session_state["messages"] = []

msg = st.text_input("🗣️ 응원 메시지를 남겨주세요:", placeholder="예: 류현진 믿는다!! 🦅🔥")

if st.button("보내기 🚀"):
    if msg.strip():
        st.session_state["messages"].append(msg)
        st.balloons()
        emoji_list = ["🦅", "🔥", "🏆", "✨", "🍊", "💪", "🎆", "💥", "🧡", "🧨", "🎉"]
        emoji_rain = "".join(random.choices(emoji_list, k=random.randint(50, 100)))
        st.markdown(
            f"<div style='font-size:40px; text-align:center;'>{emoji_rain}</div>",
            unsafe_allow_html=True,
        )
        time.sleep(0.5)
        st.success("🔥 응원 완료! 당신의 함성이 구장을 달군다!! 🦅")

# 응원 피드
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>📣 실시간 팬 응원 피드 🧡</h2>", unsafe_allow_html=True)

for i, message in enumerate(reversed(st.session_state["messages"])):
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
            🦅 <b>팬 {len(st.session_state["messages"]) - i}</b> : {message} 🍊🔥
        </div>
        """,
        unsafe_allow_html=True,
    )
