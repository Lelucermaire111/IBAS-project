# 语音播报模块
from email import contentmanager
import pyttsx3 
 
# aiff文件转换成mp3编码文件模块
from pydub import AudioSegment
 
# 模块初始化
engine = pyttsx3.init() 
 
# 语音播报内容
with open("export.txt",encoding = "utf-8") as f:
    content=f.read().splitlines()
    #print(content)
    p=content.index('文本内容:')

list_without_head=content[p+1:-1]
content_str=''.join(list_without_head)
#print(content_str)
#print(content.read())

# 输出文件格式
# outFile = 'out.aiff' 
 
print('准备开始语音播报...')
 
# 设置要播报的Unicode字符串
engine.say(content_str) 
 
# 等待语音播报完毕 
engine.runAndWait()
 
# 将文字输出为 aiff 格式的文件
# engine.save_to_file(content, outFile)
 
# 将文件转换为mp3格式
# AudioSegment.from_file(outFile).export("Python.mp3", format="mp3")