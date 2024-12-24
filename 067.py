import streamlit as st
import streamlit.components.v1 as components
 
# 自定义安装函数
@st.cache
def install_DrissionPage():
    import subprocess
    subprocess.run(["pip", "install", "DrissionPage"])
 
# 调用安装函数
install_DrissionPage()

from DrissionPage import WebPage
from DrissionPage import ChromiumOptions

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
    ii = 0
    button_clicked = True
    # 创建一个占位符，用于显示消息
    
    message_placeholder.info("1个人大概需要4秒左右，根据学生数量自己算吧，我就不算了！")
    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    co = ChromiumOptions().set_browser_path(path).set_argument('--start-maximized').auto_port()
    
    # 创建页面对象，初始d模式
    page = WebPage(mode = 'd',chromium_options = co )
    # 访问百度
    page.get('https://pt.tiangong.edu.cn/cas/login')
    # 定位输入框并输入工号
    page.ele('#username').input(user)  #''
    # 定位输入框并输入密码
    page.ele('#ppassword').input(ppasswoed) #''
    # print("标题为：",page.title)
    # 点击“登录”按钮
    page.ele('#dl').click()
    # 等待页面加载
    page.wait.load_start()

    if(page.ele('我的主页',timeout=4)):
        page.ele('我的主页').click()
        page.wait.load_start()
    # print("标题为：",page.title)
    page.ele('教务系统').click()
    # 等待页面加载
    page.wait.load_start()
    # print("标题为：",page.title)
    tab = page.latest_tab
    # print("标题为：",tab.title)
    message_placeholder.info("进入教务系统中...")
    tab.wait(1.5)
    if (tab.ele(".btn btn-sm btn-gray btn-round")):
        tab.ele(".btn btn-sm btn-gray btn-round").click()   #系统会提示一个修改密码的弹出，点取消用的，没有就跳过这句
    tab.wait(1)
    tab.ele("#2001000000").click()
    tab.wait(1)
    tab.ele("#2001007000").click()
    tab.wait(1)
    tab.ele("#2001007001").click()   #上面这3个点击是点左侧边拉栏进入输入成绩的页面
    tab.wait(3)
    tab.eles(".btn btn-xs btn-round btn-info")[int(k_xh)-1].click()   #

    # tab.wait(1)
    # tab.ele("text=自动暂存倒计时").click()
    message_placeholder.info("输入成绩中...")
    tab.wait(2)
    chirs = tab.ele("#scoreDetailtbody").children()      #获取所有的学生信息
    tab.wait(1)
    tab.ele(".ace-icon fa fa-cog bigger-130 purple").click()
    tab.wait(1)
    tab.ele("#spinner1").click()
    tab.wait(1)
    tab.ele("#spinner1").input("30",clear=True)
    tab.ele("#loading-btn").click()
    tab.wait(1)
    
    for i in edited_df:
        if i["id"] != None:       
            xue[int(i["id"])] = [i["scro1"],i["scro2"],i["scro3"],i["scro4"]]
    # chirs[0].child(7).click()
    # tab.wait(0.1)
    for ch in chirs:                 #遍历每个学生的四个成绩，并输入成绩
        chengji = xue.get(int(ch.child(3).text))
        if (chengji != None):           
            
            ch.child(7).click()
            # ch.child(7).input(Keys.CTRL_A)
            # tab.wait(0.1)           
            ch.child(7).input(chengji[0],clear=True)
            # print(xue)
            # tab.wait(0.1)
            ch.child(8).click()
            # ch.child(8).input(Keys.CTRL_A)
            # ch.child(7).input(Keys.TAB)
            # tab.wait(0.1)
            ch.child(8).input(chengji[1],clear=True)
            # tab.wait(0.1)
            ch.child(9).click()
            # ch.child(9).input(Keys.CTRL_A)
            # ch.child(8).input(Keys.TAB)
            # tab.wait(0.1)
            ch.child(9).input(chengji[2],clear=True)
            # tab.wait(0.1)
            ch.child(10).click()
            # ch.child(10).input(Keys.CTRL_A)
            # ch.child(9).input(Keys.TAB)
            # tab.wait(0.1)
            ch.child(10).input(chengji[3],clear=True)
            # tab.wait(0.1)
            # ch.child(10).input(Keys.TAB)
            # tab.wait(0.1)
            
            ii = ii + 1
        message_placeholder.info("进度："+str(ii)+"/"+str(len(chirs))+"---每一个人耗时大概需要4秒左右")
    tab.ele("#zancun").click()    #点暂存
    message_placeholder.info("暂存中...")
    tab.wait(10)
    message_placeholder.empty()
    tab.close()
    page.close()
    
    st.success("成绩输入完毕，可以关闭这个页面了！")
    button_clicked = False
    # chs[0].child(7).click()
    # tab.wait(1)
    # chs[0].child(8).click()
    # chs[0].child(8).input("90")
    # print(chs[0].child(3).text)
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

