import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

class SeabornPlots:
    def __init__(self) -> None:
        pass

    def boxplot(self, df):
        st.header("boxplot")
        col1, col2, col3 = st.columns(3)
        with col1:
            x = st.selectbox(label="X-axis", options=df.columns, index=4)
        with col2:
            y = st.selectbox(label="Y-axis", options=df.columns, index=0)
        with col3:
            hue = st.selectbox(label="hue(w.r.t)", options=df.columns, index=3)
        sns.boxplot(x=x, y=y, data=df, hue=hue)
        plot_line_text = f"sns.boxplot(x='{x}', y='{y}', hue='{hue}')"

        return plt, plot_line_text
    
    def violinplot(self, df):
        st.header("violinplot")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            x = st.selectbox(label="X-axis", options=df.columns, index=4)
        with col2:
            y = st.selectbox(label="Y-axis", options=df.columns, index=0)
        with col3:
            hue = st.selectbox(label="hue(w.r.t)", options=df.columns, index=3)
        with col4:
            split = st.selectbox(label="split", options=[True, False], index=0)
        sns.violinplot(x=x, y=y, data=df, hue=hue, split=split)
        plot_line_text = f"sns.violinplot(x='{x}', y='{y}', data=df, hue='{hue}', split={split})"

        return plt, plot_line_text

    def stripplot(self, df):
        st.header("stripplot")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            x = st.selectbox(label="X-axis", options=df.columns, index=4)
        with col2:
            y = st.selectbox(label="Y-axis", options=df.columns, index=0)
        with col3:
            hue = st.selectbox(label="hue(w.r.t)", options=df.columns, index=3)
        with col4:
            jitter = st.selectbox(label="jitter", options=[True, False], index=0)
        with col5:
            dodge = st.selectbox(label="dodge", options=[True, False], index=0)
        sns.stripplot(x=x, y=y, data=df, hue=hue, jitter=jitter, dodge=dodge)
        plot_line_text = f"sns.stripplot(x='{x}', y='{y}', data=df, hue='{hue}', jitter={jitter}, dodge={dodge})"

        return plt, plot_line_text

    def countplot(self, df):
        st.header("countplot")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            x = st.selectbox(label="X-axis", options=df.columns, index=4)
        sns.countplot(x=x, data=df)
        plot_line_text = f"sns.countplot(x='{x}', data=df)"

        return plt, plot_line_text

    def lmplot(self, df):
        st.header("lmplot")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            x = st.selectbox(label="X-axis", options=df.columns, index=0)
        with col2:
            y = st.selectbox(label="Y-axis", options=df.columns, index=1)
        with col3:
            size = st.text_input(label="size", value=2)
        with col4:
            aspect = st.text_input(label="aspect", value=2)
        sns.lmplot(x=x, y=y, data=df)
        plot_line_text = f"sns.lmplot(x='{x}', y='{y}', data=df)"

        return plt, plot_line_text