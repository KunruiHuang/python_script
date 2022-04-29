import matplotlib.pyplot as plt
import numpy as np
#设置字体
# plt.rcParams["font.family"]="SimHei"
app=[78,80,79,81,91,95,96]
ban=[70,80,81,82,75,90,89]
x=np.arange(1,8)
#创建画布
fig=plt.figure(num=1,figsize=(6,4))
#创建子图
ax=fig.add_subplot(111)

# format_string：主要来控制我们画的曲线的格式：颜色，风格，标记，可取三者的组合如：“g-o”,"r-.D",如果不用组合，则用color,marker,linestyle,三个参数分别指定。
# label： 添加图例的类标。
ax.plot(x,app,"r-.d",label="train_loss")
ax.plot(x,ban,"c-d",label="test_loss")

ax.set_xlim([1,7.1])
ax.set_ylim([40,100])
#设置标刻点
ax.set_xticks(np.linspace(1,7,7))
ax.set_yticks(np.linspace(50,100,6))#可调控字体大小，样式，
#设置标刻点标识
# ax.set_xticklabels(["星期一","星期二","星期三","星期四","星期五","星期六","星期日"],fontproperties="SimHei",fontsize=12)
# ax.set_yticklabels(["50kg","60kg","70kg","80kg","90kg","100kg"])

ax.tick_params(left=False,pad=8,direction="in",length=2,width=3,color="b",labelsize=12)
ax.tick_params("x",labelrotation=10)#类标旋转

ax.set_xlabel("epoch")#添加x轴坐标标签，后面看来没必要会删除它，这里只是为了演示一下。
ax.set_ylabel("loss",fontsize=16)#添加y轴标签，设置字体大小为16，这里也可以设字体样式与颜色

ax.set_title("loss",fontsize=12,backgroundcolor='#3c7f90',\
fontweight='bold',color='white',verticalalignment="baseline")

#ax.spines["left"].set_color("darkblue")#设置左轴的颜色
#ax.spines["bottom"].set_linewidth(2)#底轴线条宽度设置

ax.spines["top"].set_visible(False)#上轴不显示
ax.spines["right"].set_visible(False)
# ax.spines["left"].set_visible(False)
#x坐标，y坐标,"文本文件"，fontsize字体尺寸，color颜色，alpha透明度
# ax.text(7,97,"max:96",fontsize=14,color="g",alpha=1)
# ax.text(6,86,"max:90",fontsize=12,alpha=1)
#箭头
# ax.annotate(text="min:70",xy=(1,70),xytext=(1.3,66),arrowprops=dict(facecolor="y",shrink=0.05,\
#                                                               headwidth=12,headlength=6,width=4\
#                                                                 ),fontsize=12)
# ax.annotate(text="min:70",xy=(1,70),xytext=(1.3,66),arrowprops=dict(facecolor="y",shrink=0.05,\
#                                                               headwidth=12,headlength=6,width=4\
#                                                                 ),fontsize=12)

ax.legend(loc=3,labelspacing=1,handlelength=3,fontsize=8,shadow=True)

# plt.show()
#保存为jpg文件
plt.savefig("./1.jpg")#我这里填的是相对路径，如果想保存在指定文件夹下，填写绝对路径。
#保存为png文件
plt.savefig("./1.png")