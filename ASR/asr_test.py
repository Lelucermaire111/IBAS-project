from aip import AipSpeech
import time
timer = time.perf_counter
""" 你的 APPID AK SK """
APP_ID = '	26192494'
API_KEY = 'fUGAcScmUzG0mokHYKDd2eGi'
SECRET_KEY = 'GdgbeOcPI5S1Zr6D8xhNXWw9dOiBMllf'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

# 识别本地文件
def asr():
    begin = timer()
    result = client.asr(get_file_content('./audio/16k.pcm'), 'pcm', 16000, {
        'dev_pid': 1537,  # 默认1537（普通话 输入法模型），dev_pid参数见本节开头的表格
    })
    return result
