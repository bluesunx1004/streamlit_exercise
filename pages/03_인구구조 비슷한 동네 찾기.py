import streamlit as st
import pandas as pd
import numpy as np
import koreanize_matplotlib
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# 데이터 로드 및 정리
@st.cache_data
def load_data():
    data = pd.read_csv('age2411.csv')
    data['행정구역'] = data['행정구역'].apply(lambda x: re.sub(r'\(.*\)', '', x).strip())
    return data

data = load_data()

# 사용자 입력
st.title("우리 동네와 비슷한 인구 구조 찾기")
selected_region = st.selectbox('당신의 동네를 선택하세요', data['행정구역'].unique())

# 선택한 지역의 인구 구조 추출
selected_region_structure = data[data['행정구역'] == selected_region].iloc[0, 3:103].values

# 모든 지역의 데이터 추출 및 유사도 계산
all_regions_structure = data.iloc[:, 3:103].values
similarities = cosine_similarity([selected_region_structure], all_regions_structure)
most_similar_index = similarities[0].argsort()[-2]  # 자기 자신 제외
most_similar_region = data.iloc[most_similar_index]['행정구역']
most_similar_region_structure = data.iloc[most_similar_index, 3:103].values

# 결과 출력
st.write(f"'{selected_region}'과(와) 가장 비슷한 인구 구조를 가진 동네는 '{most_similar_region}'입니다.")

# 그래프 출력
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(range(100), selected_region_structure, label=selected_region)
ax.plot(range(100), most_similar_region_structure, label=most_similar_region)
ax.set_xlabel('연령')
ax.set_ylabel('인구 수')
ax.set_title(f'{selected_region}과(와) {most_similar_region}의 인구 구조 비교')
ax.legend()
st.pyplot(fig)
