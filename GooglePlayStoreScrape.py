# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:10:22 2019

@author: a.sijaria
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time  


def get_reviews(app_id,chromedriver_path):

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path = chromedriver_path)
    link = ''.join(["https://play.google.com/store/apps/details?id=",app_id,"&hl=en_IN&showAllReviews=true"])
    driver.get(link)

    number_review =  int(int(BeautifulSoup(driver.find_element_by_xpath("//span[@class='AYi5wd TBRnV']").get_attribute('innerHTML'), "html.parser").text.replace(',', ''))/100)

    for j in range(0,number_review):
        for i in range(0,5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        if(j == 0):
            show_more_button = driver.find_element_by_xpath("//div[@class='U26fgb O0WRkf oG5Srb C0oVfc n9lfJ']")
        else:
            show_more_button = driver.find_element_by_xpath("//div[@class='U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d']")
        time.sleep(2)
        show_more_button.click()

        

    full_review_list =[]
    review_list = []
    date = []
    name = []
    reply = []
    reply_date =[]
    rating =[]
       
    
    reviews_all = driver.find_elements_by_xpath("//div[@class='d15Mdf bAhLNe']")
    for review_i in reviews_all:
        review_content = review_i.get_attribute('innerHTML')
        page_content = BeautifulSoup(review_content, "html.parser") 
        try:
            date.append(page_content.findAll('span', attrs = {"class":"p2TkOb"})[0].string)
        except:
            date.append(0)
        try:
            full_review_list.append(page_content.findAll('span', attrs = {"jsname":"fbQN7e"})) 
        except:
            full_review_list.append(0) 
        try:
            review_list.append(page_content.findAll('span', attrs = {"jsname":"bN97Pc"}))
        except:
            review_list.append(0)
        try:
            name.append(page_content.findAll('span', attrs = {"class":"X43Kjb"})[0].string)
        except:
            name.append(0)
        try:
            reply.append(page_content.findAll('div', attrs = {"class":"LVQB0b"})) 
        except:
            reply.append(0) 
        try:
            rating.append(len(page_content.findAll('div', attrs = {"class":"vQHuPe bUWb7c"})))
        except:
            rating.append(0)                  
        if(len(page_content.findAll('span', attrs = {"class":"p2TkOb"})) == 2):
            reply_date.append(page_content.findAll('span', attrs = {"class":"p2TkOb"})[1].string)
        else:
            reply_date.append("")
        
        
    review_data = pd.DataFrame({
        'full reviews': full_review_list,
        'reviews': review_list ,
        'name': name ,
        'reply': reply ,
        'reply_date': reply_date ,
        'date': date,
        'rating':rating })

    review_data.to_csv(''.join(["Reviews_",app_id,".csv"]))
    print (''.join(["Reviews Extracted ",number_review,"Reviews Found"]))
