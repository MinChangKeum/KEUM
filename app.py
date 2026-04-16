import streamlit as st

st.set_page_config(page_title="가공식품 트렌드 대시보드", layout="wide")

# ----------------------
# 데이터 (샘플)
# ----------------------
categories = [
    "오일·발사믹", "과자·스낵", "파스타면", "소스", "향신료",
    "HMR", "유제품", "음료", "치즈", "샤퀴테리", "캐비아"
]

metrics = [
    ("트렌드 점수", "92", "+14.8%"),
    ("객단가", "48,200원", "+6.2%"),
    ("신규 브랜드", "67개", "+12"),
    ("주의 카테고리", "일반가공", "-8.3%")
]

# ----------------------
# 상태 관리
# ----------------------
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ----------------------
# 사이드바
# ----------------------
with st.sidebar:
    st.title("📊 Trend Suite")
    st.markdown("가공식품 트렌드 플랫폼")

    if st.button("🏠 대시보드"):
        st.session_state.selected_category = None

    st.markdown("---")
    st.markdown("### 카테고리")
    for c in categories:
        if st.button(c):
            st.session_state.selected_category = c

# ----------------------
# 메인 화면
# ----------------------
st.title("가공식품 트렌드 대시보드")

# ----------------------
# 1. 대시보드
# ----------------------
if st.session_state.selected_category is None:

    st.subheader("📈 핵심 지표")

    cols = st.columns(4)
    for i, (title, value, change) in enumerate(metrics):
        with cols[i]:
            st.metric(label=title, value=value, delta=change)

    st.markdown("---")

    st.subheader("📊 카테고리 트렌드 (클릭 가능)")

    cols = st.columns(4)
    for i, c in enumerate(categories):
        with cols[i % 4]:
            if st.button(c, key=c):
                st.session_state.selected_category = c

    st.markdown("---")

    st.subheader("📉 트렌드 그래프 (예시)")
    st.line_chart([10, 20, 15, 30, 40, 60])

# ----------------------
# 2. 카테고리 상세 페이지
# ----------------------
else:
    c = st.session_state.selected_category

    if st.button("← 전체로 돌아가기"):
        st.session_state.selected_category = None

    st.header(f"{c} 트렌드 리포트")

    st.markdown("### 🔥 핵심 인사이트")
    st.write(f"""
    - {c} 카테고리는 최근 **프리미엄화 + 기능성 중심**으로 성장
    - 건강, 저당, 고단백 키워드 강세
    - 수입 브랜드 및 PB 상품 확대 필요
    """)

    st.markdown("### 📌 추천 액션")
    st.write("""
    - 프리미엄 상품군 확대
    - 시즌 프로모션 기획
    - 핵심 브랜드 집중 소싱
    """)

    st.markdown("### 🔗 공유")
    share_url = f"https://your-site.com/category/{c}"
    st.code(share_url)

    st.info("👉 이 링크를 담당자에게 공유하세요")
