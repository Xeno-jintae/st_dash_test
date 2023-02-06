import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data import
data_depth = pd.read_csv("./data/manual_by_depth_2depth.csv", index_col=0)
data_2depth = pd.read_csv("./data/statics_2depth.csv", index_col=0)
data_2depth_10years = pd.read_csv("./data/statics_2depth_10years.csv", index_col=0)

st.title("2-Depth Data를 이용한 그래프")
# st.write(data_depth)

# Dropdown Menu
dropdown = st.selectbox("select", data_depth["definition2"])

# st.write(data_2depth[data_2depth["depth"]==int(dropdown[:2])])

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


filtered_data_count_10years = data_2depth_10years[data_2depth_10years["depth"] == int(dropdown[:2])]
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
# fig2.update_traces(hovertemplate="%{x: s}세<br>%{y:.2f}%<extra></extra>")
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


st.plotly_chart(fig)
st.plotly_chart(fig2)

# st.bar_chart(data_2depth[data_2depth["depth"]==int(dropdown[:2])][["p_age","median_growth"]])
# for i in dropdown :
    # st.write(i)
    # st.write(data_2depth[data_2depth["depth"]==int(i[:1])])