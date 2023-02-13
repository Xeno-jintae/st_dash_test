import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout="wide")

# Data import
data_depth = pd.read_csv("./data/manual_by_depth_2depth.csv", index_col=0)
data_2depth = pd.read_csv("./data/statics_2depth.csv", index_col=0)
data_2depth_10years = pd.read_csv("./data/statics_2depth_10years.csv", index_col=0)
data_2depth_5years = pd.read_csv("./data/statics_2depth_5years.csv", index_col=0)

data_2depth_pv = pd.read_csv("./data/statics_2depth_pv.csv", index_col=0)
data_2depth_pv_10years = pd.read_csv("./data/statics_2depth_pv_10years.csv", index_col=0)
data_2depth_pv_5years = pd.read_csv("./data/statics_2depth_pv_5years.csv", index_col=0)

data_2depth_pv_fillna_5years = pd.read_csv("./data/statics_2depth_pv_fillna_5years.csv", index_col=0)
data_2depth_pv_fillna_5years2 = pd.read_csv("./data/statics_2depth_pv_fillna_5years2.csv", index_col=0)

st.title("2-Depth Data를 이용한 그래프")
st.write("CPI(소비자물가지수)를 이용하여 물가상승률이 적용된 임금에 대한 결과입니다.")
st.write("두 그래프 모두 5년 단위로 그룹화 되었습니다.")
st.write("기본적인 나이에 대한 범위는 20~64세 이며, 이후의 나이 범위에 데이터가 존재하는 경우에만 그래프는 보여집니다.")

# Dropdown Menu
dropdown = st.selectbox("*직종을 선택해주세요.*", data_depth["definition2"])

col1, col2 = st.columns(2)

filtered_data_count = data_2depth[data_2depth["depth"] == int(dropdown[:2])]

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig.add_trace(go.Bar(x=filtered_data_count[filtered_data_count["p_sex"] == 1]["p_age"].values,
                     y=filtered_data_count[filtered_data_count["p_sex"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2')), secondary_y=False)
fig.add_trace(go.Scatter(x=filtered_data_count[filtered_data_count["p_sex"] == 1]["p_age"].values,
                         y=filtered_data_count[filtered_data_count["p_sex"] == 1]["median_growth"].values, name="man_growth", marker=dict(color='#4ebafc')),secondary_y=True)
fig.add_trace(go.Bar(x=filtered_data_count[filtered_data_count["p_sex"] == 2]["p_age"].values,
                     y=filtered_data_count[filtered_data_count["p_sex"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a")), secondary_y=False)
fig.add_trace(go.Scatter(x=filtered_data_count[filtered_data_count["p_sex"] == 2]["p_age"].values,
                         y=filtered_data_count[filtered_data_count["p_sex"] == 2]["median_growth"].values, name="woman_growth", marker=dict(color="#fa5282"), ), secondary_y=True)
fig.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) 및 임금상승률(Line) by 2-Depth 데이터 (중간값 사용)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"),
    yaxis2=dict(
        title=dict(text="Growth(%)"),
        side="right",
        overlaying="y"))

# pv 반영된 중간값 그래프
filtered_data_count_pv = data_2depth_pv[data_2depth_pv["depth"] == int(dropdown[:2])]

# Create figure with secondary y-axis
fig_pv = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig_pv.add_trace(go.Bar(x=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 1]["p_age"].values,
                     y=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2')), secondary_y=False)
fig_pv.add_trace(go.Scatter(x=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 1]["p_age"].values,
                         y=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 1]["median_growth"].values, name="man_growth", marker=dict(color='#4ebafc')),secondary_y=True)
fig_pv.add_trace(go.Bar(x=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 2]["p_age"].values,
                     y=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a")), secondary_y=False)
fig_pv.add_trace(go.Scatter(x=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 2]["p_age"].values,
                         y=filtered_data_count_pv[filtered_data_count_pv["p_sex"] == 2]["median_growth"].values, name="woman_growth", marker=dict(color="#fa5282"), ), secondary_y=True)
fig_pv.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) 및 임금상승률(Line) by 2-Depth 데이터 물가상승률 적용됨 (중간값 사용)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"),
    yaxis2=dict(
        title=dict(text="Growth(%)"),
        side="right",
        overlaying="y"))

filtered_data_count_10years = data_2depth_10years[data_2depth_10years["depth2"] == int(dropdown[:2])]

# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig2.add_trace(go.Bar(x=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 1]["p_age_range"].values,
                     y=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2'), text=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 1]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig2.add_trace(go.Scatter(x=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 1]["p_age_range"].values,
                         y=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 1]["median_growth"].values, name="man_growth", marker=dict(color='#4ebafc'), line=dict(width=4)),secondary_y=True)
fig2.add_trace(go.Bar(x=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 2]["p_age_range"].values,
                     y=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a"), text=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 2]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig2.add_trace(go.Scatter(x=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 2]["p_age_range"].values,
                         y=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 2]["median_growth"].values, name="woman_growth", marker=dict(color="#fa5282"), line=dict(width=4)), secondary_y=True)
fig2.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) 및 임금상승률(Line) by 2-Depth 데이터 and 10년 그룹화 (중간값의 평균)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"),
    yaxis2=dict(
        title=dict(text="Growth(%)"),
        side="right",
        overlaying="y"))

# pv_10년치 그래프
filtered_data_count_pv_10years = data_2depth_pv_10years[data_2depth_pv_10years["depth2"] == int(dropdown[:2])]

# Create figure with secondary y-axis
fig2_pv = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig2_pv.add_trace(go.Bar(x=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 1]["p_age_range"].values,
                     y=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2'), text=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 1]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig2_pv.add_trace(go.Scatter(x=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 1]["p_age_range"].values,
                         y=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 1]["median_growth"].values, name="man_growth", marker=dict(color='#4ebafc'), line=dict(width=4)),secondary_y=True)
fig2_pv.add_trace(go.Bar(x=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 2]["p_age_range"].values,
                     y=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a"), text=filtered_data_count_10years[filtered_data_count_10years["p_sex2"] == 2]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig2_pv.add_trace(go.Scatter(x=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 2]["p_age_range"].values,
                         y=filtered_data_count_pv_10years[filtered_data_count_pv_10years["p_sex2"] == 2]["median_growth"].values, name="woman_growth", marker=dict(color="#fa5282"), line=dict(width=4)), secondary_y=True)
fig2_pv.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) 및 임금상승률(Line) by 2-Depth 데이터 and 10년 그룹화 물가상승률 적용됨 (중간값의 평균)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"),
    yaxis2=dict(
        title=dict(text="Growth(%)"),
        side="right",
        overlaying="y"))

filtered_data_count_5years = data_2depth_5years[data_2depth_5years["depth2"] == int(dropdown[:2])]

# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig3.add_trace(go.Bar(x=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 1]["p_age_range"].values,
                     y=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2'), text=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 1]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig3.add_trace(go.Scatter(x=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 1]["p_age_range"].values,
                         y=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 1]["median_growth"].values, name="man_growth", marker=dict(color='#4ebafc'), line=dict(width=4)),secondary_y=True)
fig3.add_trace(go.Bar(x=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 2]["p_age_range"].values,
                     y=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a"), text=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 2]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig3.add_trace(go.Scatter(x=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 2]["p_age_range"].values,
                         y=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 2]["median_growth"].values, name="woman_growth", marker=dict(color="#fa5282"), line=dict(width=4)), secondary_y=True)
fig3.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) 및 임금상승률(Line) by 2-Depth 데이터 and 5년 그룹화 (중간값의 평균)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"),
    yaxis2=dict(
        title=dict(text="Growth(%)"),
        side="right",
        overlaying="y"))

filtered_data_count_pv_5years = data_2depth_pv_5years[data_2depth_pv_5years["depth2"] == int(dropdown[:2])]

# Create figure with secondary y-axis
fig3_pv = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig3_pv.add_trace(go.Bar(x=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 1]["p_age_range"].values,
                     y=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2'), text=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 1]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig3_pv.add_trace(go.Scatter(x=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 1]["p_age_range"].values,
                         y=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 1]["median_growth"].values, name="man_growth", marker=dict(color='#4ebafc'), line=dict(width=4)),secondary_y=True)
fig3_pv.add_trace(go.Bar(x=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 2]["p_age_range"].values,
                     y=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a"), text=filtered_data_count_5years[filtered_data_count_5years["p_sex2"] == 2]["count2"].values, textposition="inside", textfont=dict(size=18)), secondary_y=False)
fig3_pv.add_trace(go.Scatter(x=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 2]["p_age_range"].values,
                         y=filtered_data_count_pv_5years[filtered_data_count_pv_5years["p_sex2"] == 2]["median_growth"].values, name="woman_growth", marker=dict(color="#fa5282"), line=dict(width=4)), secondary_y=True)
fig3_pv.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) 및 임금상승률(Line) by 2-Depth 데이터 and 5년 그룹화 물가상승률 적용됨 (중간값의 평균)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"),
    yaxis2=dict(
        title=dict(text="Growth(%)"),
        side="right",
        overlaying="y"))

filtered_data_count_pv_fillna_5years = data_2depth_pv_fillna_5years[data_2depth_pv_fillna_5years["depth2"] == int(dropdown[:2])]
# filtered_data_count_pv_fillna_5years = filtered_data_count_pv_fillna_5years.dropna()
# Create figure with secondary y-axis
fig3_pv_fillna = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig3_pv_fillna.add_trace(go.Bar(x=filtered_data_count_pv_fillna_5years[filtered_data_count_pv_fillna_5years["p_sex2"] == 1]["p_age_range"].values,
                     y=filtered_data_count_pv_fillna_5years[filtered_data_count_pv_fillna_5years["p_sex2"] == 1]["median_wage"].values, name="man_wage", marker=dict(color='#556ff2')))
fig3_pv_fillna.add_trace(go.Bar(x=filtered_data_count_pv_fillna_5years[filtered_data_count_pv_fillna_5years["p_sex2"] == 2]["p_age_range"].values,
                     y=filtered_data_count_pv_fillna_5years[filtered_data_count_pv_fillna_5years["p_sex2"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a")))
fig3_pv_fillna.update_layout(
    title_text="직종 별 - 나이 별 - 성별 임금(Bar) by 2-Depth 데이터 (중간값의 평균)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"))

filtered_data_count_pv_fillna_5years2 = data_2depth_pv_fillna_5years2[data_2depth_pv_fillna_5years2["depth2"] == int(dropdown[:2])]
# filtered_data_count_pv_fillna_5years = filtered_data_count_pv_fillna_5years.dropna()
# Create figure with secondary y-axis
fig3_pv_fillna2 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig3_pv_fillna2.add_trace(go.Bar(x=filtered_data_count_pv_fillna_5years2["p_age_range"].values,
                     y=filtered_data_count_pv_fillna_5years2["median_wage"].values, marker=dict(color='#5aeda6')))
# fig3_pv_fillna.add_trace(go.Bar(x=filtered_data_count_pv_fillna_5years2[filtered_data_count_pv_fillna_5years2["p_sex2"] == 2]["p_age_range"].values,
#                      y=filtered_data_count_pv_fillna_5years2[filtered_data_count_pv_fillna_5years2["p_sex2"] == 2]["median_wage"].values, name="woman_wage", marker=dict(color="#f57e7a")))
fig3_pv_fillna2.update_layout(
    title_text="직종 별 - 나이 별 임금(Bar) by 2-Depth 데이터 (중간값의 평균)",
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Wage(만원)"),
        side="left"))



with col1:
    st.header("성별 구분 O")
    st.plotly_chart(fig3_pv_fillna)
    # st.header("물가상승률 적용 X")
    # st.plotly_chart(fig)
    # st.plotly_chart(fig2)
    # st.plotly_chart(fig3)

with col2:
    st.header("성별 구분 X")
    st.plotly_chart(fig3_pv_fillna2)
    # st.header("물가상승률 적용 O")
    # st.plotly_chart(fig_pv)
    # st.plotly_chart(fig2_pv)
    # st.plotly_chart(fig3_pv)



# st.bar_chart(data_2depth[data_2depth["depth"]==int(dropdown[:2])][["p_age","median_growth"]])
# for i in dropdown :
    # st.write(i)
    # st.write(data_2depth[data_2depth["depth"]==int(i[:1])])