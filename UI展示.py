# 这里写UI展示的代码
import streamlit as st
import openai
from 脚本生成器 import generate_script

st.title("🎬 视频脚本生成器！！")
st.divider()

with st.sidebar:
    openai_apikey = st.text_input("请输入您的OpenAI API密钥：", type='password')
    st.markdown("[获取OpenAI API密钥地址 🔑](https://platform.openai.com/account/api_keys)")

subject = st.text_input("🌼 请输入视频的主题：")
st.markdown("<br>", unsafe_allow_html=True)
video_time = st.number_input("⏳ 请输入视频的大致时长（单位：分钟）：", min_value=0.1, step=0.1)
st.markdown("<br>", unsafe_allow_html=True)
creativity = st.slider("💡 请输入视频脚本的创造力（数字越小说明越严谨，数字越大说明越多样）", min_value=0.0, max_value=1.0, step=0.1, value=0.3)

submit = st.button("生成脚本")

# 判断逻辑
if submit and not openai_apikey:
    st.info('请输入您的OpenAI API密钥！！')
    st.stop()
if submit and not subject:
    st.info('请输入您的视频主题！！')
    st.stop()
if submit and not video_time >= 0.1:
    st.info('视频时长需要大于等于0.1！！')
    st.stop()
if submit:
    try:
        with st.spinner("💦 脚本正在路上..."):
            search_result, title, script = generate_script(subject,video_time,creativity,openai_apikey)
        st.success('视频脚本已生成！！')

        st.subheader('🔥 标题：')
        st.write(title)
        st.divider()

        st.subheader('📋 脚本：')
        st.write(script)
        st.divider()

        with st.expander("📂 维基百科搜索结果："):
            st.info(search_result)

    except openai.AuthenticationError:
        st.error('OpenAI API密钥无效，请检查您的输入！！')
    except Exception as e:
        st.error(f'生成脚本时发生未知错误：{e}')


