from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import path
import os
from PIL import Image
#from selenium.webdriver.chrome.options import Options
timer = time.perf_counter
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# chrome_options = Options()
# chrome_options.page_load_strategy = 'none'
# driver = webdriver.Chrome(options=chrome_options)

def convertimg(picfile, outdir):
    '''调整图片大小,对于过大的图片进行压缩
    picfile:    图片路径
    outdir:    图片输出路径
    '''
    img = Image.open(picfile)
    width, height = img.size
    while (width * height > 4000000):  # 该数值压缩后的图片大约 两百多k
        width = width // 2
        height = height // 2
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(path.join(outdir, os.path.basename(picfile)))

def post(path):

    begin = timer()
    #driver.set_page_load_timeout(10)
    driver.get("http://srijan-ds-intelligent-image-captioning.s3-website.us-east-2.amazonaws.com/")
    print(timer() - begin)
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".imgInp")))
    driver.find_element_by_css_selector(".imgInp").send_keys(path)
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".btn.btn-caption.btn-margin")))
    driver.find_element_by_css_selector(".btn.btn-caption.btn-margin").click()
    element = driver.find_element_by_class_name( 'caption-text').text
    element = element[8:-6]
    print(element)
    driver.quit()

begin = timer()
picfile = r"C:\Users\Dell\Pictures\classroom.jpg"
outdir = r"D:\IBAS project\Request\tmp"

convertimg(picfile,outdir)
post(r"D:\IBAS project\Request\tmp\classroom.jpg")
print(timer()-begin)