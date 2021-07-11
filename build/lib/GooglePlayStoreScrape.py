# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:10:22 2019

@author: a.sijaria
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time  
import chromedriver_binary
import sys,os


def get_reviews(app_id,language = 'en',country= 'IN'):

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    link = ''.join(["https://play.google.com/store/apps/details?id=",app_id,"&hl=",language,"_",country,"&showAllReviews=true"])
    print('--------------------')
    print('Opening Link: ',link)
    driver.get(link)

    number_review =  int(int(BeautifulSoup(driver.find_element_by_xpath("//span[@class='AYi5wd TBRnV']").get_attribute('innerHTML'), "html.parser").text.replace(',', '')))
    number_review_loop = int(number_review/100) +1

    for j in range(0,number_review_loop):
        for i in range(0,5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        try:
            if(j == 0):
                show_more_button = driver.find_element_by_xpath("//div[@class='U26fgb O0WRkf oG5Srb C0oVfc n9lfJ']")
            else:
                show_more_button = driver.find_element_by_xpath("//div[@class='U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d']")
            time.sleep(2)
            show_more_button.click()
        except:
            pass
    
    full_review_list =[]
    review_list = []
    date = []
    name = []
    reply = []
    reply_date =[]
    rating =[]
    votes =[]
       
    
    reviews_all = driver.find_elements_by_xpath("//div[@class='d15Mdf bAhLNe']")
    for review_i in reviews_all:
        review_content = review_i.get_attribute('innerHTML')
        page_content = BeautifulSoup(review_content, "html.parser") 
        try:
            date.append(page_content.findAll('span', attrs = {"class":"p2TkOb"})[0].string)
        except:
            date.append(0)
        try:
            full_review_list.append(page_content.findAll('span', attrs = {"jsname":"fbQN7e"})[0].string) 
        except:
            full_review_list.append(0) 
        try:
            review_list.append(page_content.findAll('span', attrs = {"jsname":"bN97Pc"})[0].string)
        except:
            review_list.append(0)
        try:
            name.append(page_content.findAll('span', attrs = {"class":"X43Kjb"})[0].string)
        except:
            name.append(0)
        try:
            reply_start = int(len(page_content.find('div', attrs = {"class":"LVQB0b"}).find('span', attrs = {"class":"X43Kjb"}).text)+len(page_content.findAll('span', attrs = {"class":"p2TkOb"})[1].string))
            reply.append(page_content.findAll('div', attrs = {"class":"LVQB0b"})[0].text[reply_start:]) 
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
        try:
            votes.append(page_content.find('div', attrs = {"class":"jUL89d y92BAb"}).string)
        except:
            votes.append(0) 
        
        
    review_data = pd.DataFrame({
        'full reviews': full_review_list,
        'reviews': review_list ,
        'name': name ,
        'reply': reply ,
        'reply_date': reply_date ,
        'date': date,
        'rating':rating,
        'helpful-votes':votes})

    review_data.to_csv(''.join(["Reviews_",app_id,".csv"]))
    print('Saving File at: ',os.getcwd() )
    print (''.join(["Reviews Extracted ",str(len(review_data)-1)," Reviews Found"]))

def get_info(app_id,language = 'en',country = 'IN'):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    link = ''.join(["https://play.google.com/store/apps/details?id=",app_id,"&hl=",language,"_",country])
    print('--------------------')
    print('Opening Link: ',link)
    driver.get(link)
  
    attr =[]
    att_value = []
       
    names = driver.find_elements_by_xpath("//div[@class='oQ6oV']")[0]
    name_content = names.get_attribute('innerHTML')
    page_content = BeautifulSoup(name_content, "html.parser")
    
    ##Add name
    attr.append('Name')
    att_value.append(page_content.find('h1', attrs = {"itemprop":"name"}).text)
    
    ##Add genre 
    attr.append('Genre')
    att_value.append(page_content.find('a', attrs = {"itemprop":"genre"}).text)
    
    ##Average Ratings
    attr.append('Number of Ratings')
    att_value.append(page_content.find('span', attrs = {"class":"AYi5wd TBRnV"}).text)
    
    ##Average rating
    attr.append('Average Rating')
    att_value.append(page_content.find('div', attrs = {"class":"pf5lIe"}).findAll('div')[0].get('aria-label'))
    
    add_info = driver.find_elements_by_xpath("//div[@class='hAyfc']")
    for i in add_info:
        info_content = i.get_attribute('innerHTML')
        page_content = BeautifulSoup(info_content, "html.parser") 
        try:
            attr.append(page_content.findAll('div', attrs = {"class":"BgcNfc"})[0].string)
        except:
            attr.append(0)
        try:
            att_value.append(page_content.findAll('span', attrs = {"class":"htlgb"})[0].text) 
        except:
            att_value.append(0)
        add_links = page_content.find('span', attrs = {"class":"htlgb"}).findAll('a')
        for l in add_links:
           attr.append(l.text)
           att_value.append(l.get('href'))
    new = driver.find_elements_by_xpath("//div[@class='W4P4ne ']")[2]
    new_content = new.get_attribute('innerHTML')
    page_content = BeautifulSoup(new_content, "html.parser")
    attr.append(page_content.find('h2',attrs={"class":"Rm6Gwb"}).text)
    att_value.append(page_content.find('div',attrs={"class":"DWPxHb"}).text)
   
    desc = driver.find_elements_by_xpath("//div[@class='DWPxHb']")[0]
    desc_content = desc.get_attribute('innerHTML')
    page_content = BeautifulSoup(desc_content , "html.parser").text
   
    attr.append('description')
    att_value.append(page_content)
            
    additional_info = pd.DataFrame({
        'Attributes': attr,
        'Value': att_value })

    additional_info.to_csv(''.join(["Info_",app_id,".csv"]))
    print('Saving File at: ',os.getcwd() )
    print (''.join(["Info Extracted ",str(len(additional_info))," Info found"]))
    
if __name__ == '__main__':
     globals()[sys.argv[1]](sys.argv[2],sys.argv[3],sys.argv[4])