import streamlit as st
import random
import time

st.set_page_config(page_title="한화이글스 우승 기원🔥", page_icon="🦅", layout="centered")

st.markdown(
    """
    <h1 style='text-align:center; color:#ff6600;'>
        🧡 한화이글스 우승 가자앗!! 🦅🔥
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown("#### ✨ 응원 한마디를 남겨주세요! (이모지가 터집니다 🎇)")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

msg = st.text_input("🗣️ 응원 메시지:", placeholder="예: 류현진 믿는다!! 🦅🔥")

if st.button("보내기 🚀"):
    if msg:
        st.session_state["messages"].append(msg)
        st.balloons()
        emoji_list = ["🦅", "🔥", "🏆", "✨", "🍊", "💪", "🎆", "💥", "🧡"]
        emoji_rain = "".join(random.choices(emoji_list, k=random.randint(20, 40)))
        st.markdown(
            f"<div style='font-size:30px; text-align:center;'>{emoji_rain}</div>",
            unsafe_allow_html=True,
        )
        time.sleep(0.3)
        st.success("응원 완료! 💬")

st.markdown("---")
st.markdown("### 🧡 실시간 응원 피드")

for i, message in enumerate(reversed(st.session_state["messages"])):
    st.markdown(
        f"""
        <div style='background-color:#fff7e6; padding:10px; border-radius:10px; margin-bottom:8px;'>
            <b>🦅 팬 {len(st.session_state["messages"]) - i}:</b> {message}
        </div>
        """,
        unsafe_allow_html=True,
    )
