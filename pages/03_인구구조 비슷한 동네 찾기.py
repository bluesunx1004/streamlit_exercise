import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re

# 데이터 로드 함수
@st.cache_data
def load_data():
    data = pd.read_csv('age2411.csv')
    # '행정구역' 열에서 괄호와 그 안의 내용을 제거
    data['행정구역'] = data['행정구역'].apply(lambda x: re.sub(r'\(.*\)', '', str(x)).strip())
    return data

data = load_data()

# 인구 비율 계산 함수
def calculate_population_ratio(row):
    population = row[3:103].values.astype(float)
    total_population = population.sum()
    return population / total_population if total_population > 0 else population

# 인구 비율 계산
data['population_ratio'] = data.apply(calculate_population_ratio, axis=1)

# 사용자 입력
st.title("우리 동네와 비슷한 인구 구조 찾기")
selected_region = st.selectbox('당신의 동네를 선택하세요', data['행정구역'].unique())

# 선택된 지역의 인구 비율 추출
selected_region_ratio = data[data['행정구역'] == selected_region]['population_ratio'].values[0]

# 모든 지역의 인구 비율 추출 및 유사도 계산
all_regions_ratio = np.vstack(data['population_ratio'].values)
similarities = cosine_similarity([selected_region_ratio], all_regions_ratio)
most_similar_index = similarities[0].argsort()[-2]  # 자기 자신 제외
most_similar_region = data.iloc[most_similar_index]['행정구역']
most_similar_region_ratio = data.iloc[most_similar_index]['population_ratio']

# 결과 출력
st.write(f"'{selected_region}'과(와) 가장 비슷한 인구 구조를 가진 동네는 '{most_similar_region}'입니다.")

# 그래프 출력
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(range(100), selected_region_ratio, label=selected_region)
ax.plot(range(100), most_similar_region_ratio, label=most_similar_region)
ax.set_xlabel('연령')
ax.set_ylabel('인구 비율')
ax.set_title(f'{selected_region}과(와) {most_similar_region}의 인구 구조 비교')
ax.legend()
st.pyplot(fig)
