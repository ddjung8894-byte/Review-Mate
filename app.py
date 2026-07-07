import streamlit as st

st.set_page_config(
    page_title="Review Mate",
    page_icon="RM",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root {
        --navy: #162544;
        --navy-soft: #243858;
        --ink: #152033;
        --muted: #718096;
        --line: #e8edf5;
        --paper: #ffffff;
        --soft: #f6f8fb;
        --accent: #eef4ff;
    }

    .stApp {
        background: linear-gradient(180deg, #ffffff 0%, #f7f9fc 100%);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0.78);
        backdrop-filter: blur(14px);
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 760px;
        padding: 1.2rem 1rem 3.5rem;
    }

    .app-shell {
        max-width: 540px;
        margin: 0 auto;
    }

    .hero {
        padding: 1.8rem 0 1.15rem;
    }

    .logo-row {
        display: flex;
        align-items: center;
        gap: 0.72rem;
        margin-bottom: 0.82rem;
    }

    .logo-mark {
        width: 42px;
        height: 42px;
        border-radius: 14px;
        background: var(--navy);
        color: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        letter-spacing: 0;
        box-shadow: 0 14px 28px rgba(22, 37, 68, 0.18);
    }

    .brand-name {
        font-size: 1.55rem;
        line-height: 1.1;
        font-weight: 820;
        color: var(--navy);
        letter-spacing: 0;
    }

    .hero-copy {
        margin: 0;
        color: #526073;
        font-size: 1.02rem;
        line-height: 1.62;
    }

    .mobile-card {
        background: var(--paper);
        border: 1px solid var(--line);
        border-radius: 26px;
        padding: 1.18rem;
        box-shadow: 0 18px 46px rgba(22, 37, 68, 0.08);
        margin-bottom: 1rem;
    }

    .section-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.9rem;
    }

    .section-title h2 {
        margin: 0;
        font-size: 1.05rem;
        line-height: 1.3;
        color: var(--navy);
        letter-spacing: 0;
    }

    .section-badge {
        color: var(--navy);
        background: var(--accent);
        border-radius: 999px;
        padding: 0.28rem 0.66rem;
        font-size: 0.78rem;
        font-weight: 700;
        white-space: nowrap;
    }

    .hint {
        margin: -0.2rem 0 1rem;
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.55;
    }

    div[data-testid="stFileUploader"] section {
        border: 1.5px dashed #cfd8e7;
        background: #fbfcff;
        border-radius: 22px;
        padding: 1rem;
    }

    .stTextInput label, .stTextArea label, .stSelectbox label {
        color: var(--navy) !important;
        font-weight: 760 !important;
        font-size: 0.92rem !important;
    }

    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 18px !important;
        border-color: #dde5f0 !important;
        background: #fbfcff !important;
        color: var(--ink) !important;
        font-size: 0.98rem !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--navy) !important;
        box-shadow: 0 0 0 3px rgba(22, 37, 68, 0.08) !important;
    }

    .stButton > button, .stDownloadButton > button {
        width: 100%;
        border: 0;
        border-radius: 18px;
        background: var(--navy);
        color: #ffffff;
        font-weight: 800;
        font-size: 1rem;
        padding: 0.82rem 1rem;
        box-shadow: 0 14px 30px rgba(22, 37, 68, 0.18);
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        background: var(--navy-soft);
        color: #ffffff;
        border: 0;
    }

    .prompt-box textarea {
        font-size: 0.94rem !important;
        line-height: 1.58 !important;
    }

    .mini-note {
        color: #8994a5;
        text-align: center;
        font-size: 0.82rem;
        margin: 1.2rem 0 0;
    }

    @media (max-width: 520px) {
        .block-container {
            padding-left: 0.78rem;
            padding-right: 0.78rem;
        }

        .mobile-card {
            border-radius: 24px;
            padding: 1rem;
        }

        .brand-name {
            font-size: 1.42rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def safe_value(value: str, fallback: str = "미입력") -> str:
    value = value.strip()
    return value if value else fallback


def build_review_prompt(
    product_name: str,
    reason: str,
    good_points: str,
    bad_points: str,
    real_story: str,
    recommend_to: str,
    photo_note: str,
    mode: str,
) -> str:
    extra_request = ""
    if mode == "리뷰 + 제목 + 한줄 요약":
        extra_request = "\n추가로 마지막에 제목 후보 5개와 한줄 요약 5개도 따로 제안해주세요."
    elif mode == "제목 5개만":
        extra_request = "\n본문 리뷰는 쓰지 말고, 쿠팡 리뷰 제목 후보 5개만 제안해주세요."
    elif mode == "한줄 요약 5개만":
        extra_request = "\n본문 리뷰는 쓰지 말고, 한줄 요약 5개만 제안해주세요."

    return f"""아래 메모를 바탕으로 쿠팡 리뷰처럼 자연스럽게 써줘.

조건:
- 존댓말 사용
- 과장 금지
- 광고 문구 금지
- 효능 보장처럼 보이는 표현 금지
- 실제 사람이 직접 사용하고 작성한 후기처럼 자연스럽게
- 리뷰 본문은 소제목이나 번호 없이 하나의 글로 자연스럽게 이어서 작성
- 리뷰 본문은 최소 500자, 최대 700자 사이로 작성
- 구매 이유, 첫인상, 실제 사용 후기, 장점, 단점, 추천 대상을 글 안에 자연스럽게 포함
- 사용자가 적은 표현, 말투, 유머 감각이 있으면 어색하지 않게 살려서 반영
- 단점은 공격적으로 쓰지 말고 솔직하지만 부드럽게
- 너무 정돈된 광고글처럼 보이지 않게, 사람이 직접 쓴 후기처럼 약간의 생활감 포함
{extra_request}

상품명:
{safe_value(product_name)}

왜 구매했나요?:
{safe_value(reason)}

좋았던 점:
{safe_value(good_points)}

아쉬웠던 점:
{safe_value(bad_points)}

실제 사용하면서 있었던 일:
{safe_value(real_story)}

추천할 사람:
{safe_value(recommend_to)}

사진을 보고 내가 적어둔 메모:
{safe_value(photo_note, '사진 분석은 하지 않고, 사용자가 직접 적은 메모만 참고')}
""".strip()


if "prompt_text" not in st.session_state:
    st.session_state.prompt_text = ""

st.markdown('<main class="app-shell">', unsafe_allow_html=True)
st.markdown(
    """
    <section class="hero">
        <div class="logo-row">
            <div class="logo-mark">RM</div>
            <div class="brand-name">Review Mate</div>
        </div>
        <p class="hero-copy">메모를 정리해서 ChatGPT에 붙여넣을 리뷰 프롬프트를 만들어드립니다.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="mobile-card">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-title">
        <h2>리뷰 재료 입력</h2>
        <span class="section-badge">무료 사용</span>
    </div>
    <p class="hint">API 결제 없이 사용합니다. 여기서 만든 프롬프트를 ChatGPT Plus에 붙여넣으면 됩니다.</p>
    """,
    unsafe_allow_html=True,
)

mode = st.selectbox(
    "만들 결과",
    ["리뷰 + 제목 + 한줄 요약", "리뷰 본문만", "제목 5개만", "한줄 요약 5개만"],
)
photos = st.file_uploader(
    "상품 사진 업로드",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True,
    help="이 버전은 사진을 AI가 분석하지 않습니다. 사진을 보며 느낀 점은 아래 메모칸에 직접 적어주세요.",
)

if photos:
    st.caption(f"사진 {min(len(photos), 5)}장을 선택했습니다. 사진 내용은 아래 메모에 직접 적어주세요.")
    if len(photos) > 5:
        st.warning("사진은 최대 5장 기준으로만 메모하는 것을 추천합니다.")

product_name = st.text_input("상품명", placeholder="예: 무기자차 선스틱, 어린이 유산균, 조립식 선반")
reason = st.text_area("왜 구매했나요?", placeholder="예: 출근 전에 빠르게 바를 선스틱이 필요했어요.", height=92)
good_points = st.text_area("좋았던 점", placeholder="예: 밀림이 적고 손에 묻지 않아서 편했어요.", height=92)
bad_points = st.text_area("아쉬웠던 점", placeholder="예: 향이 조금 더 약했으면 좋겠어요.", height=92)
real_story = st.text_area("실제 사용하면서 있었던 일", placeholder="예: 출근 전에 발랐는데 마스크에 많이 묻지 않았어요.", height=104)
recommend_to = st.text_input("추천할 사람", placeholder="예: 바쁜 아침에 간편하게 선케어하고 싶은 분")
photo_note = st.text_area("사진을 보고 적어둘 점", placeholder="예: 크기가 생각보다 작고, 패키지는 깔끔했어요.", height=88)

if st.button("붙여넣을 프롬프트 만들기"):
    if not any([product_name, reason, good_points, bad_points, real_story, recommend_to, photo_note]):
        st.error("리뷰 재료를 하나 이상 입력해주세요.")
    else:
        st.session_state.prompt_text = build_review_prompt(
            product_name,
            reason,
            good_points,
            bad_points,
            real_story,
            recommend_to,
            photo_note,
            mode,
        )
        st.success("프롬프트를 만들었습니다. 아래 내용을 복사해서 ChatGPT에 붙여넣으세요.")

st.markdown('</section>', unsafe_allow_html=True)

st.markdown('<section class="mobile-card">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-title">
        <h2>ChatGPT 붙여넣기용</h2>
        <span class="section-badge">복사해서 사용</span>
    </div>
    <p class="hint">아래 박스를 클릭한 뒤 Ctrl + A, Ctrl + C로 복사하면 됩니다.</p>
    """,
    unsafe_allow_html=True,
)

if st.session_state.prompt_text:
    st.markdown('<div class="prompt-box">', unsafe_allow_html=True)
    st.text_area("완성 프롬프트", value=st.session_state.prompt_text, height=420, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    st.download_button(
        "프롬프트 txt로 저장",
        data=st.session_state.prompt_text,
        file_name="review_mate_prompt.txt",
        mime="text/plain",
    )
else:
    st.info("입력 후 붙여넣을 프롬프트 만들기를 누르면 이곳에 결과가 표시됩니다.")

st.markdown('</section>', unsafe_allow_html=True)

st.markdown('<section class="mobile-card">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-title">
        <h2>사용 순서</h2>
        <span class="section-badge">추가 비용 없음</span>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    1. 위 입력칸에 상품 메모를 적습니다.  
    2. 프롬프트 만들기 버튼을 누릅니다.  
    3. 완성 프롬프트를 복사합니다.  
    4. ChatGPT Plus 채팅창에 붙여넣습니다.  
    5. 나온 리뷰를 보고 마음에 안 드는 부분만 다시 고쳐달라고 합니다.
    """
)
st.markdown('</section>', unsafe_allow_html=True)

st.markdown('<p class="mini-note">API 결제 없이 ChatGPT Plus를 활용하는 프롬프트 생성기 버전입니다.</p>', unsafe_allow_html=True)
st.markdown('</main>', unsafe_allow_html=True)