import streamlit as st
import datetime

st.title("📊 Streamlit 示例应用")

st.sidebar.header("输入参数")

name = st.sidebar.text_input("请输入你的名字：", "海洋")
age = st.sidebar.number_input("请输入你的年龄：", min_value=1, max_value=120, value=25)
date = st.sidebar.date_input("请选择日期：", datetime.date.today())

st.write(f"你好，**{name}**！")
st.write(f"你今年 **{age}** 岁。")
st.write(f"今天是：{date.strftime('%Y-%m-%d')}")

st.subheader("交互式演示")
option = st.selectbox("请选择你喜欢的编程语言：", ["Python", "C++", "MATLAB", "Rust"])
st.success(f"你选择了 {option}！")

x = st.slider("选择一个数：", 0, 100, 50)
st.write(f"{x} 的平方是：{x**2}")
st.markdown("$$\int_0^\infty f(x)\mathbb{d}x 666$$")

