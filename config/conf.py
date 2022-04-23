import configparser
import os

# 获取当前路径
currPath = os.path.split(os.path.realpath(__file__))[0]
#print(currPath)
#D:\Software\PycharmProjects\sccProjects\config

# 读配置文件获取项目路径
conf = configparser.ConfigParser()
ini = os.path.join(currPath,"config.ini")
conf.read(ini)
proPath = conf.get("project","project_path")
# print(proPath)
# D:\Software\PycharmProjects\sccProjects\

'''
computerWidth = conf.get("computer","width")
computerHeight = conf.get("computer","height")
'''
baseUrl = conf.get("url","baseUrl")

'''
seUrl = conf.get("url","seUrl")
hwUrl = conf.get("url","hwUrl")
'''

#数据库配置
host=conf.get("mysql","host")
port=conf.get("mysql","host")
user=conf.get("mysql","user")
passwd=conf.get("mysql","passwd")
db=conf.get("mysql","db")
charset=conf.get("mysql","charset")


# 获取测试数据路径
dataPath = os.path.join(proPath,"testData")
# print(dataPath)


# 获取日志路径
logPath = os.path.join(proPath,'log')
# print(logPath)
# D:\Software\PycharmProjects\sccProjects\report


# 保存截图路径
# 错误截图
failImagePath = os.path.join(proPath, 'report', 'image','fail')
# 成功截图
passImagePath = os.path.join(proPath, 'report', 'image','pass')



#获取测试报告路径
reportPath = os.path.join(proPath,'report')
#获取测试用例路径
casePath = os.path.join(proPath,'testCase')
