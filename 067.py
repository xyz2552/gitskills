import streamlit as st
import streamlit.components.v1 as components


df1 = [{"id":1,"name":"","scro1":0,"scro2":0,"scro3":0,"scro4":0},{"id":2,"name":"","scro1":0,"scro2":0,"scro3":0,"scro4":0},{"id":3,"name":"","scro1":0,"scro2":0,"scro3":0,"scro4":0}]
df2 = []
xue = {}
# ii = 0
button_clicked = False
st.warning("一定要在学校的网站上先把系数输入完毕，才能在这里输入成绩！")
zhanghao = st.text_input("输入信息门户的账号：", "",placeholder="输入信息门户的账号")

mima = st.text_input("输入信息门户的密码：", "",placeholder="输入信息门户的密码")

st.write('↓↓↓↓↓如果想录入名下第一个课的成绩就选择01，第二门课的成绩就选02，以此类推↓↓↓↓↓')
kxh = st.selectbox(
    "选择第几门课（针对名下有2门及以上的，如果名下只有一门课，选01就可以了）：",
    ["01","02","03","04","05","06","07","08","09",]
    )
st.write('把学生学号、姓名以及成绩复制到下面的表格（可以整列复制,鼠标选中每一列的第一个单元格然后Ctrl+V）')
edited_df = st.data_editor(df1,num_rows="dynamic",column_config={
        "id": "学号",
        "name": "姓名",
        "scro1": st.column_config.NumberColumn("成绩1"),
        "scro2": st.column_config.NumberColumn("成绩2"),
        "scro3": st.column_config.NumberColumn("成绩3"),
        "scro4": st.column_config.NumberColumn("成绩4")}
        )
message_placeholder = st.empty()
def input_grade(user,ppasswoed,k_xh):
    pass
def handle_button_click():
    global button_clicked
    if not button_clicked:
        button_clicked = True
        # 执行按钮点击后的操作
        input_grade(zhanghao, mima, kxh)
        # st.write("按钮被点击了！")
    else:
        pass
if st.button('开始录入成绩', on_click=handle_button_click):
    pass
    
# xue[edited_df[0]["id"]] = [edited_df[0]["scro1"],edited_df[0]["scro2"],edited_df[0]["scro3"],edited_df[0]["scro4"]]
# for i in edited_df:
#     if i["id"] != None:
        
#         xue[int(i["id"])] = [i["scro1"],i["scro2"],i["scro3"],i["scro4"]]
# st.write(xue)

