import streamlit as st
import random
import time

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="AI 병맛 고민상담소",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# 스타일
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:white;
    margin-bottom:10px;
}

.sub {
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:30px;
}

.result-box {
    background: linear-gradient(135deg, #ff6b6b, #ffb347);
    padding:40px;
    border-radius:25px;
    text-align:center;
    color:white;
    font-size:35px;
    font-weight:bold;
    margin-top:25px;
    box-shadow:0px 0px 35px rgba(255,255,255,0.3);
    animation: pop 0.4s ease-in-out;
}

.comment-box {
    background:#111827;
    padding:30px;
    border-radius:20px;
    color:white;
    font-size:24px;
    margin-top:20px;
    text-align:center;
    border:2px solid #ffb347;
}

@keyframes pop {
    0% {transform: scale(0.7);}
    100% {transform: scale(1);}
}

.stButton>button {
    width:100%;
    height:65px;
    border:none;
    border-radius:20px;
    background:linear-gradient(90deg,#ff6b6b,#ffb347);
    color:white;
    font-size:24px;
    font-weight:bold;
}

.stButton>button:hover {
    transform:scale(1.02);
}

textarea {
    font-size:20px !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    "<div class='title'>🤖 AI 병맛 고민상담소</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub'>고민은 맡기고 웃고 가세요.</div>",
    unsafe_allow_html=True
)

# -----------------------------
# 병맛 답변 리스트
# -----------------------------
answers = [

    "그 고민... 미래의 네가 알아서 해결함 😎",
    "일단 밥 먹자. 인간은 배고프면 부정적이 됨 🍚",
    "괜찮아. 공룡도 멸종했는데 너 정도는 버틴다 🦖",
    "그건 네 잘못이 아니라 수성 역행 때문임 🌌",
    "인생은 원래 억까의 연속이다 😌",
    "생각보다 아무도 너 신경 안 씀. 자유롭게 살아 🔥",
    "일단 자고 일어나면 30%는 해결됨 🛌",
    "그 사람? 네 매력을 감당 못한 거임 😏",
    "실패가 아니라 스토리 빌드업 중임 📈",
    "너 지금 주인공 버프 받는 중임 🎬",
    "걱정 마. 넌 이미 평균 이상이야 📊",
    "지구도 쉬지 않고 도는데 너도 잘하고 있음 🌍",
    "오늘 힘들면 내일도 힘들 수 있음. 하지만 치킨은 맛있다 🍗",
    "포기하지 마. 인터넷 끊긴 와이파이도 다시 연결됨 📶",
    "넌 생각보다 훨씬 괜찮은 인간임 👍",
    "지금은 흑역사지만 나중엔 술안주 썰 된다 🍻",
    "세상은 넓고 이상한 사람은 많다. 넌 양반임 😌",
    "자존감 낮아질 땐 통장 말고 얼굴 보셈 ✨",
    "네 존재 자체가 이미 콘텐츠임 📸",
    "걱정 금지. 넌 웃길 자격이 충분함 🤣"

]

# -----------------------------
# 자존감 코멘트
# -----------------------------
boost_comments = [

    "🔥 넌 진짜 생각보다 훨씬 괜찮은 사람이다.",
    "👑 오늘도 살아남은 것 자체가 대단한 거임.",
    "💎 넌 어디 가도 존재감 있는 타입임.",
    "🚀 네 미래는 생각보다 훨씬 잘 풀릴 예정.",
    "😎 넌 이미 주인공 재질이다.",
    "🌟 너 은근 사람들한테 인기 많을 스타일임.",
    "🎯 넌 잘될 놈이라 아직 스토리 진행 중인 거다.",
    "🧠 너 정도면 솔직히 상위권 인간임.",
    "🍀 운도 결국 널 따라오게 되어 있음.",
    "🔥 자신감 가져. 네가 생각하는 것보다 훨씬 멋진 사람임."

]

# -----------------------------
# 말투 모드
# -----------------------------
mode = st.selectbox(
    "상담 모드 선택",
    [
        "🤖 기본 병맛 모드",
        "😈 악마 모드",
        "👩 엄마 모드",
        "🧠 정신승리 모드"
    ]
)

# -----------------------------
# 고민 입력
# -----------------------------
worry = st.text_area(
    "고민을 입력하세요",
    placeholder="예: 시험 망했어요..."
)

# -----------------------------
# 버튼
# -----------------------------
if st.button("🔮 고민 상담 받기"):

    if worry.strip() == "":
        st.warning("고민을 입력해주세요 😅")

    else:

        loading = st.empty()

        for i in range(6):

            dots = "." * (i % 4)

            loading.markdown(
                f"""
                <div class='comment-box'>
                🤖 AI가 병맛 분석 중{dots}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.4)

        answer = random.choice(answers)
        boost = random.choice(boost_comments)

        # 모드별 추가
        if mode == "😈 악마 모드":
            answer += " 그리고 그건 좀 네가 웃김 😈"

        elif mode == "👩 엄마 모드":
            answer += " 밥은 먹었니? 🍚"

        elif mode == "🧠 정신승리 모드":
            answer += " 사실 상대가 손해 본 거다 😎"

        st.balloons()

        loading.markdown(
            f"""
            <div class='result-box'>
            {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class='comment-box'>
            {boost}
            </div>
            """,
            unsafe_allow_html=True
        )
