import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('age2411.csv')
    return data

data = load_data()

# 제목
st.title('우리 동네의 인구 이야기')

# 지역 선택
selected_region = st.selectbox('지역을 선택하세요', data['행정구역'].unique())

# 선택된 지역의 데이터
region_data = data[data['행정구역'] == selected_region].iloc[0]

# 연령대별 인구 데이터 추출
age_data = region_data.iloc[3:103]  # 0세부터 99세까지의 데이터

# 그래프 그리기
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(range(len(age_data)), age_data.values)
ax.set_xlabel('나이')
ax.set_ylabel('인구 수')
ax.set_title(f'{selected_region}의 연령별 인구 구조')

# 그래프 표시
st.pyplot(fig)

# 총 인구수 표시
total_population = region_data['2024년11월_계_총인구수']
st.write(f'{selected_region}의 총 인구수: {total_population:,}명')

# 연령대별 비율 계산 및 표시
age_groups = {
    '0-9세': age_data[:10].sum(),
    '10-19세': age_data[10:20].sum(),
    '20-29세': age_data[20:30].sum(),
    '30-39세': age_data[30:40].sum(),
    '40-49세': age_data[40:50].sum(),
    '50-59세': age_data[50:60].sum(),
    '60-69세': age_data[60:70].sum(),
    '70세 이상': age_data[70:].sum()
}

st.write('연령대별 비율:')
for group, population in age_groups.items():
    ratio = population / total_population * 100
    st.write(f'{group}: {ratio:.2f}%')
