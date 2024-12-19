import streamlit as st
import pandas as pd
import numpy as np
import koreanize_matplotlib
from sklearn.metrics.pairwise import cosine_similarity

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('age2411.csv')
    return data

data = load_data()

# 제목
st.title('인구 구조가 비슷한 동네 찾기')

# 지역 선택
selected_region = st.selectbox('당신의 동네를 선택하세요', data['행정구역'].unique())

# 선택된 지역의 데이터
selected_data = data[data['행정구역'] == selected_region].iloc[0, 3:103].values.reshape(1, -1)

# 모든 지역의 데이터
all_regions_data = data.iloc[:, 3:103].values

# 코사인 유사도 계산
similarities = cosine_similarity(selected_data, all_regions_data)

# 유사도가 가장 높은 5개 지역 찾기
top_5_indices = similarities[0].argsort()[-6:][::-1][1:]
top_5_regions = data.iloc[top_5_indices]['행정구역'].tolist()
top_5_similarities = similarities[0][top_5_indices]

# 결과 출력
st.write(f"'{selected_region}'과(와) 가장 인구 구조가 비슷한 5개 동네:")
for region, similarity in zip(top_5_regions, top_5_similarities):
    st.write(f"{region}: 유사도 {similarity:.4f}")

# 선택된 지역과 가장 유사한 지역의 인구 구조 비교
st.subheader('인구 구조 비교')
selected_age_data = data[data['행정구역'] == selected_region].iloc[0, 3:103]
most_similar_region = top_5_regions[0]
most_similar_age_data = data[data['행정구역'] == most_similar_region].iloc[0, 3:103]

comparison_df = pd.DataFrame({
    '선택한 지역': selected_age_data,
    '가장 유사한 지역': most_similar_age_data
}, index=[f'{i}세' for i in range(100)])

st.line_chart(comparison_df)
