#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhutongtong time:2020/10/16

from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from lxml import etree
import os
import time
import re
#import wget

##传参
link="http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&qid=1&SID=8FGF7CfXVMHYxC53XTo&&page=1"
number=11
zongyeshu=12
#定义输出文件
output_wos1 = open('D:/output_wos1.txt','w',encoding='utf-8')
output_wos2 = open('D:/output_wos2.txt','w',encoding='utf-8')
# 实例化一个WOS浏览器，并添加chromedriver路径
chromedriver_path = "D:/exe/谷歌浏览器/MyChrome_64bit/Chrome/chromedriver.exe"
driver_WOS = webdriver.Chrome(chromedriver_path)

#循环页码

for zp in range(1,zongyeshu+1):
    link = "http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&qid=1&SID=8FGF7CfXVMHYxC53XTo&&page="+str(zp)
    # 发送请求
    driver_WOS.get(link)
    #获取网页代码
    source = driver_WOS.page_source
    #将返回的网页进行修正
    source = etree.HTML(source)

    #循环每一篇文章
    for i in range(1,number):
        wosid="RECORD_"+str((zp-1)*10+i)
        print((zp-1)*10+i)
        print(wosid)
        #初始化
        title="-"
        chubanshang="-"
        juan="-"
        qi="-"
        ye="-"
        chubannian="-"
        citeScore_WOS="-"
        driver_WOS.get(link)
        # 获取网页代码
        source = driver_WOS.page_source
        # 将返回的网页进行修正
        source = etree.HTML(source)
        # 定位元素并获取元素信息
        title=source.xpath('//*[@id='+"\""+wosid+"\""+']/div[3]/div/div[1]/div/a/value/text()')
        chubanshang=source.xpath('//*[@id="show_journal_overlay_link_'+str((zp-1)*10+i)+"\""+']/a/span/value/span/text()')
        juan=source.xpath('//*[@id='+"\""+wosid+"\""+']/div[3]/div/div[3]/span[6]/value/text()')
        qi=source.xpath('//*[@id='+"\""+wosid+"\""+']/div[3]/div/div[3]/span[8]/value/text()')
        ye=source.xpath('//*[@id='+"\""+wosid+"\""+']/div[3]/div/div[3]/span[9]/span[2]/value/text()')
        chubannian=source.xpath('//*[@id='+"\""+wosid+"\""+']/div[3]/div/div[3]/span[11]/value/text()')
        citeScore_WOS=source.xpath('//*[@id='+"\""+wosid+"\""+']/div[4]/div[1]/a/text()')
        #输出结果
        # print(title)
        # print(chubanshang)
        # print(juan)
        # print(qi)
        # print(ye)
        main_paper=str(title)+"\t"+str(chubanshang)+"\t"+str(juan)+"\t"+str(qi)+"\t"+str(ye)+"\t"+str(chubannian)+"\t"+str(citeScore_WOS)+"\n"
        if len(title) !=0:
            output_wos1.write(main_paper)
            print(main_paper)
            #获得每篇文章的施引文章信息
            #模拟点击
            ac = driver_WOS.find_element_by_xpath('//*[@id='+"\""+wosid+"\""+']/div[4]/div[1]/a')
            ActionChains(driver_WOS).move_to_element(ac).click(ac).perform()
            #子页面信息获取
            source_new2 = driver_WOS.page_source
            source_new = etree.HTML(source_new2)
            #获取子页面所有文章信息
            # 获取施引文献页数
            yeshu = int(source_new.xpath('//*[@id ="pageCount.bottom"]/text()')[0])
            print(yeshu)
            #按页循环
            for p in range(1,yeshu+1):
                for j in range(1,number):
                    wosid_new = "RECORD_" + str((p-1)*10+j)
                    print(wosid_new)
                    # 定位元素并获取元素信息
                    # 初始化
                    title2 = "-"
                    chubanshang2 = "-"
                    juan2 = "-"
                    qi2 = "-"
                    ye2 = "-"
                    chubannian2 = "-"
                    citeScore_WOS2 = "-"
                    # 定位元素并获取元素信息
                    title2 = source_new.xpath('//*[@id='+"\""+ wosid_new + "\"" + ']/div[3]/div/div[1]/div/a/value/text()')
                    chubanshang2 = source_new.xpath('//*[@id="show_journal_overlay_link_' + str((p-1)*10+j) + "\"" + ']/a/span/value/text()')
                    juan2 = source_new.xpath('//*[@id=' + "\"" + wosid_new + "\"" + ']/div[3]/div/div[3]/span[6]/value/text()')
                    qi2 = source_new.xpath('//*[@id=' + "\"" + wosid_new + "\"" + ']/div[3]/div/div[3]/span[8]/value/text()')
                    ye2 = source_new.xpath('//*[@id=' + "\"" + wosid_new + "\"" + ']/div[3]/div/div[3]/span[9]/span[2]/value/text()')
                    chubannian2 = source_new.xpath('//*[@id=' + "\"" + wosid_new + "\"" + ']/div[3]/div/div[3]/span[11]/value/text()')
                    citeScore_WOS2 = source_new.xpath('//*[@id=' + "\"" + wosid_new + "\"" + ']/div[4]/div[1]/a/text()')
                    # 输出结果
                    main_paper2 = str(title)+"\t"+str(title2)+"\t"+str(chubanshang2)+"\t"+str(juan2)+"\t"+str(qi2)+"\t"+str(ye2)+"\t"+str(chubannian2)+"\t"+str(citeScore_WOS2)+"\n"
                    if len(title2) !=0:
                        output_wos2.write(main_paper2)
                        # print(title2)
                        # print(chubanshang2)
                        # print(juan2)
                        # print(qi2)
                        # print(ye2)
                        print(main_paper2)
                    # 模拟点击至下一页
                bc = driver_WOS.find_element_by_xpath('//*[@id="summary_navigation"]/nav/table/tbody/tr/td[3]/a')
                ActionChains(driver_WOS).move_to_element(bc).click(bc).perform()
                source_new2 = driver_WOS.page_source
                source_new = etree.HTML(source_new2)

            ##传参
            ##NOTE： Scopus只有一页，每页上限展示200篇；如超出需修改脚本
            link = "https://www.scopus.com/results/results.uri?numberOfFields=0&src=s&clickedLink=&edit=&editSaveSearch=&origin=searchbasic&authorTab=&affiliationTab=&advancedTab=&scint=1&menu=search&tablin=&searchterm1=Genomics+proteomics+bioinformatics&field1=SRCTITLE&dateType=Publication_Date_Type&yearFrom=2018&yearTo=2019&loadDate=7&documenttype=All&accessTypes=All&resetFormLink=&st1=Genomics+proteomics+bioinformatics&st2=&sot=b&sdt=b&sl=44&s=SRCTITLE%28Genomics+proteomics+bioinformatics%29&sid=70cf118e97e519e7acf90168c2f65564&searchId=70cf118e97e519e7acf90168c2f65564&txGid=112d982834202ed2204476ab1ea36ad3&sort=cp-f&originationType=b&rr="
            number = 93
            zongyeshu = 1
            # 定义输出文件
            output_scopus1 = open('D:/output_scopus1.txt', 'w', encoding='utf-8')
            output_scopus2 = open('D:/output_scopus2.txt', 'w', encoding='utf-8')
            # 实例化一个WOS浏览器，并添加chromedriver路径
            chromedriver_path = "D:/exe/谷歌浏览器/MyChrome_64bit/Chrome/chromedriver.exe"
            driver_scopus = webdriver.Chrome(chromedriver_path)

            # 循环页码

            for zp in range(1, zongyeshu + 1):
                # link = "http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&qid=1&SID=8FGF7CfXVMHYxC53XTo&&page="+str(zp)
                # 发送请求
                driver_scopus.get(link)
                # 获取网页代码
                source = driver_scopus.page_source
                # 将返回的网页进行修正
                source = etree.HTML(source)

                # 循环每一篇文章
                for i in range(number):
                    scopusid = "resultDataRow" + str((zp - 1) * 10 + i)
                    print((zp - 1) * 10 + i)
                    print(scopusid)
                    # 初始化
                    title = "-"
                    chubanshang = "-"
                    juan = "-"
                    qi = "-"
                    ye = "-"
                    chubannian = "-"
                    citeScore_WOS = "-"
                    driver_scopus.get(link)
                    # 二次点击修改每页展示文献数（最大200篇）
                    be = driver_scopus.find_element_by_xpath('//*[@id="resultsPerPage-button"]/span[1]')
                    ActionChains(driver_scopus).move_to_element(be).click(be).perform()
                    ee = driver_scopus.find_element_by_xpath('//*[@id="ui-id-4"]')
                    ActionChains(driver_scopus).move_to_element(ee).click(ee).perform()
                    source = driver_scopus.page_source
                    source = etree.HTML(source)
                    # 定位元素并获取元素信息
                    title = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[1]/a/text()')
                    chubanshang = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[4]/a/text()')
                    juan = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[4]/div/span[1]/text()')
                    qi = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[4]/div/span[2]/text()')
                    ye = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[4]/div/span[3]/text()')
                    chubannian = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[3]/span/text()')
                    citeScore_WOS = source.xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[5]/a/text()')
                    # 输出结果
                    # print(title)
                    # print(chubanshang)
                    # print(juan)
                    # print(qi)
                    # print(ye)
                    main_paper = str(title) + "\t" + str(chubanshang) + "\t" + str(juan) + "\t" + str(qi) + "\t" + str(
                        ye) + "\t" + str(chubannian) + "\t" + str(citeScore_WOS) + "\n"
                    if len(title) != 0:
                        output_scopus1.write(main_paper)
                        print(main_paper)
                        # 获得每篇文章的施引文章信息
                        # 模拟点击
                        ae = driver_scopus.find_element_by_xpath('//*[@id=' + "\"" + scopusid + "\"" + ']/td[5]/a')
                        ActionChains(driver_scopus).move_to_element(ae).click(ae).perform()
                        # 二次点击修改每页展示文献数（最大200篇）
                        be = driver_scopus.find_element_by_xpath('//*[@id="resultsPerPage-button"]/span[1]')
                        ActionChains(driver_scopus).move_to_element(be).click(be).perform()
                        ee = driver_scopus.find_element_by_xpath('//*[@id="ui-id-4"]')
                        ActionChains(driver_scopus).move_to_element(ee).click(ee).perform()
                        # 子页面信息获取
                        source_new2 = driver_scopus.page_source
                        source_new = etree.HTML(source_new2)
                        # 获取子页面所有文章信息
                        # 获取施引文献数
                        yinyongshu = int(
                            source_new.xpath('//*[@id="searchResFormId"]/div[1]/div/header/h1/span[1]/text()')[0])
                        print(yinyongshu)
                        for j in range(yinyongshu):
                            scopusid_new = "resultDataRow" + str(j)
                            print(scopusid_new)
                            # 定位元素并获取元素信息
                            # 初始化
                            title2 = "-"
                            chubanshang2 = "-"
                            juan2 = "-"
                            qi2 = "-"
                            ye2 = "-"
                            chubannian2 = "-"
                            citeScore_WOS2 = "-"
                            # 定位元素并获取元素信息
                            title2 = source_new.xpath('//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[1]/a/text()')
                            chubanshang2 = source_new.xpath(
                                '//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[4]/a/text()')
                            juan2 = source_new.xpath(
                                '//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[4]/div/span[1]/text()')
                            qi2 = source_new.xpath(
                                '//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[4]/div/span[2]/text()')
                            ye2 = source_new.xpath(
                                '//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[4]/div/span[3]/text()')
                            chubannian2 = source_new.xpath(
                                '//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[3]/span/text()')
                            citeScore_WOS2 = source_new.xpath(
                                '//*[@id=' + "\"" + scopusid_new + "\"" + ']/td[5]/a/text()')
                            # 输出结果
                            main_paper2 = str(title) + "\t" + str(title2) + "\t" + str(chubanshang2) + "\t" + str(
                                juan2) + "\t" + str(qi2) + "\t" + str(ye2) + "\t" + str(chubannian2) + "\t" + str(
                                citeScore_WOS2) + "\n"
                            if len(title2) != 0:
                                output_scopus2.write(main_paper2)
                                # print(title2)
                                # print(chubanshang2)
                                # print(juan2)
                                # print(qi2)
                                # print(ye2)
                                print(main_paper2)
#结果比较(need install R software)
os.system('D:/Compare_information.R')

#NOTE
#由于title字母大小写及其它格式错误难以避免会导致数据冗余，请手动删除此类行
#示例：['Relevant Applications of Generative Adversarial Networks in Drug Design and Discovery: MolecularDe NovoDesign, Dimensionality Reduction, andDe NovoPeptide and Protein Design']
#['Relevant applications of generative adversarial networks in drug design and discovery: Molecular de novo design, dimensionality reduction, and de novo peptide and protein design']

