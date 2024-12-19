import streamlit as st
import pandas as pd

st.title("🧠 MBTI 성격유형별 직업 및 인간관계 분석기 🔍")

mbti_types = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", 
              "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

mbti_data = {
    "ISTJ": {
        "직업": ["회계사 💼", "경찰관 👮", "군인 🪖", "판사 ⚖️", "프로젝트 매니저 📊"],
        "잘 맞는 유형": ["ESTJ", "ISTJ", "ENTJ", "ISFJ"],
        "설명": "ISTJ는 체계적이고 책임감 있는 성격으로, 규칙과 전통을 중요시합니다. 이들은 정확성과 신뢰성을 요구하는 직업에서 뛰어난 능력을 발휘합니다. 🏛️"
    },
    "ENFP": {
        "직업": ["작가 ✍️", "배우 🎭", "상담사 🤗", "마케터 📣", "기업가 💡"],
        "잘 맞는 유형": ["INTJ", "INFJ", "ENTJ", "ENFJ"],
        "설명": "ENFP는 열정적이고 창의적인 성격으로, 새로운 아이디어를 만들어내는 데 탁월합니다. 이들은 자유롭고 유연한 환경에서 최고의 성과를 냅니다. 🌈"
    },
    # 나머지 MBTI 유형들에 대한 데이터도 이와 같은 형식으로 추가
}

if selected_mbti in mbti_data:
    st.header(f"🌟 {selected_mbti} 유형의 특징")
    
    st.subheader("🚀 추천 직업")
    for job in mbti_data[selected_mbti]["직업"]:
        st.write(f"- {job}")
    
    st.subheader("❤️ 잘 맞는 MBTI 유형")
    for compatible in mbti_data[selected_mbti]["잘 맞는 유형"]:
        st.write(f"- {compatible}")
    
    st.subheader("💡 성격 설명")
    st.write(mbti_data[selected_mbti]["설명"])
else:
    st.error("선택한 MBTI 유형에 대한 정보가 없습니다.")

st.balloons()
