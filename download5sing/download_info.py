# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 09:42
# @Author  : Azrael.Bai
# @File    : download_info.py
# 使用selenium+ffmpeg下载5sing歌曲

from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import time
import io

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


url_cover = 'http://5sing.kugou.com/5811103/fc/{count}.html'
url_covers = []
ffsave = 'music_save'
isSave = False

download_save = '5sing_download'
if not os.path.isdir("/Users/suyeye/{}".format(download_save)):
    os.mkdir("/Users/suyeye/{}".format(download_save))


def save(filename, contents):
    fh = io.open(filename, 'w+', encoding='utf-8')
    fh.write(unicode(contents))
    fh.close()


def save_append(filename, contents):
    fh = io.open(filename, 'a+', encoding='utf-8')
    fh.write(unicode(contents))
    fh.close()


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_experimental_option("prefs",
                                      {'profile.default_content_settings.popups': 0, 'download.default_directory': '.'})
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.set_page_load_timeout(5)

for i in range(1, 5):
    url_current = url_cover.format(count=i)
    browser.get(url_current)
    WebDriverWait(browser, 2)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    links = soup.select('a')
    for link in links:
        href = link.get('href')
        if (href.startswith('http://5sing.kugou.com/fc/')) and href.endswith('html'):
            title = link.get('title')
            url_covers.append(href)
            print title, href
    print ''

if not os.path.isdir(ffsave):
    os.mkdir(ffsave)

for url in url_covers:
    try:
        browser.get(url)
        browser.set_page_load_timeout(10)
        WebDriverWait(browser, 5)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        title = soup.select('title')[0].get_text().replace('`', '')
        link = soup.select('audio')[0].get('src')
        cmd = 'ffmpeg -i "{url}" -c copy "/Users/suyeye/{download_save}/{filename}.mp3" -y'.format(url=link, download_save=download_save, filename=title)
        if isSave:
            subprocess.Popen(cmd)
        save_append('{ffsave}/music_url.sh'.format(ffsave=ffsave), cmd + '\n')
        print title, link
        print cmd
        print ''
    except:
        print('download {url} failed!'.format(url=url))
        save_append('{ffsave}/music_error.txt'.format(ffsave=ffsave), 'download {url} failed!'.format(url=url))

browser.quit()
