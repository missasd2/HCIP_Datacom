"""
Mysql8测试
"""

import random
import pymysql

db = pymysql.connect(
    user="root",
    password="Asd@159357",
    host="192.168.25.136",
    database="school",
    charset="utf8"
)

cursor = db.cursor()
last_name = list("赵钱孙李周吴郑王")
str1 = "苏宇轩 苏雨扬 苏雨璇 苏宇璇 苏苏 苏真真 苏雨熙 苏雨萱 苏雨轩 苏黎民 苏忠民 苏嘉毅 苏红 苏瀛 苏远航 苏伟祺 苏宸逸 苏益漫 苏卿尧 苏启尧 苏艺潇 苏绾铎 苏悠然 苏幽然 苏钰 苏俊喜 苏玲珑 苏毅尧 苏妍 苏元礤 苏子又 苏宇童 苏宇童 苏哇滕 苏云瑞 苏熙羟 苏博睿 苏紫菡 苏紫涵 苏文萱 苏雅然 苏佳晨 苏语晨 苏雨晨 苏贝晨 苏诗晗 苏欣妍 苏子萱 苏诗涵 苏依辰 苏依晨 苏晨萱 苏晨菲 苏晨希 苏晨曦 苏喧莹 苏喧妍 苏喧婷 苏昕雨 苏昕月 苏煜云 苏瑾琳 苏瑾 苏仁辙 苏湃濡 苏金月 苏金昌 苏文斌 苏煜轩 苏影 苏尚梅 苏锦曦 苏格格 苏昕靓 苏施雅 苏熙宸 苏冀彦 苏倩 苏袁 苏能 苏晓 苏焕迪 苏治诚 苏珍 苏乙祗 苏乙桓 苏姵莹 苏一员 苏眧臣 苏稔涵 苏广溢 苏子默 苏至朗 苏城朗 苏佳朗 苏圣朗 苏佩 苏钰涵 苏美琪 苏麒午 苏亚斌 苏宦安 苏凤菊 苏煜森 苏春喜 苏一涵 苏子生 苏一铭 苏铭铭 苏昕铭 苏智铭 苏鑫铭 苏学铭 苏跃铭 苏岳铭 苏越铭 苏壹铭 苏二铭 苏毅铭 苏子铭 苏康铭 苏亦铭 苏威铭 苏守铭 苏世铭 苏金铭 苏晓铭 苏珊 苏烨 苏琪 苏梦琪 苏欣悦 苏炘悦 苏刚 苏丽君 苏丽鑫 苏晶晶 苏婉灵 苏廷婷 苏怡婷 苏剑婷 苏醒 苏晨醒 苏婷婷 苏雯婷 苏恒运 苏君怡 苏文娟 苏文涓 苏建坤 苏宇杰 苏娅菲 苏子依 苏子怡 苏拉琪 苏子琪 苏子衡 苏子恒 苏子坤 苏子趟 苏子禾".replace(
    "苏", "").split(" ")

pro = ["python", "c", "java", "php", "linux"]

for i in range(100):
    name = random.choice(last_name) + random.choice(str1)
    gender = random.choice("男女")
    age = random.randint(20, 40)
    project = random.choice(pro)
    sql = "insert into teacher(name,gender,age,project) value('%s','%s',%s,'%s')" % (name, gender, age, project)
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    else:
        print(sql)

db.commit()
cursor.close()
db.close()
