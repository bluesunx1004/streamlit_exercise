import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('buceonsiapateugeoraecsv.csv', encoding='cp949')
    return data

data = load_data()

st.title('부천시 아파트 거래 분석')

# 1. 가장 거래가 많은 동
st.header('1. 가장 거래가 많은 동')
top_dongs = data['동'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_dongs.index, y=top_dongs.values, ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_ylabel('거래 건수')
st.pyplot(fig)

# 2. 가장 비싸게 팔린 아파트
st.header('2. 가장 비싸게 팔린 아파트')
most_expensive = data.loc[data['거래금액'].idxmax()]
st.write(f"동: {most_expensive['동']}")
st.write(f"아파트명: {most_expensive['아파트명']}")
st.write(f"거래금액: {most_expensive['거래금액']}만원")
st.write(f"전용면적: {most_expensive['전용면적']}㎡")
st.write(f"층수: {most_expensive['층수']}층")
st.write(f"건설년도: {most_expensive['건설년도']}년")

# 3. 가장 아파트가 비싼 동네
st.header('3. 가장 아파트가 비싼 동네')
avg_prices = data.groupby('동')['거래금액'].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_prices.index, y=avg_prices.values, ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_ylabel('평균 거래금액 (만원)')
st.pyplot(fig)

# 4. 거래가 가장 많은 달
st.header('4. 거래가 가장 많은 달')
monthly_transactions = data['거래월'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=monthly_transactions.index, y=monthly_transactions.values, ax=ax)
ax.set_xlabel('월')
ax.set_ylabel('거래 건수')
st.pyplot(fig)

