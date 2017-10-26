# -*- coding: utf-8 -*-
__author__ = 'bobby'

from selenium import webdriver
from scrapy.selector import Selector


# browser.get("https://www.weibo.com")
#

# browser.find_element_by_css_selector(".qrcode-signin-step1 .signin-switch-password").click()
#
# browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("276027411@qq.com")
# browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("Lovesong1")
# #
# browser.find_element_by_css_selector(".view-signin button.sign-button").click()


# selenium 完成微博模拟登录

# browser.get("https://www.oschina.net/blog")
import time
time.sleep(5)
# browser.find_element_by_css_selector("#loginname").send_keys("13399285270")
# browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("Lovesong1020")
# browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()

# for i in range(3):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
# t_selector = Selector(text=browser.page_source)
# print(t_selector.css(".tm-promo-price .tm-price::text").extract())
# browser.quit()

# 设置chromedriver不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_opt.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(executable_path="D:/spider_test/ArticleSpider/chromedriver.exe", chrome_options=chrome_opt)
# browser.get('https://www.taobao.com')

# phantomjs, 无界面的浏览器， 多进程情况下phantomjs性能会下降很严重

browser = webdriver.PhantomJS(executable_path="D:/spider_test/ArticleSpider/phantomjs-2.1.1-windows/bin/phantomjs.exe")
browser.get(
    'https://detail.tmall.com/item.htm?id=546258631533&spm=a1z2k.6997417.0.0.rwAPIj&scm=12306.1.0.0&skuId=3300160104048')
#
print(browser.page_source)
browser.quit()
