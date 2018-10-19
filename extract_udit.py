# -*- coding: utf-8 -*-
"""
Created on Fri May  4 01:23:11 2018

@author: Udit
"""
inception = input("Please input CP number:" )
inception = int(inception)
value_dict = {}
import selenium
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver',chrome_options=options)
fetchUrl = "https://www.icsi.in/student/Members/MemberSearch.aspx"
driver.get(fetchUrl)
input_element = driver.find_element_by_name('dnn$ctr410$MemberSearch$txtCpNumber')
input_element.send_keys(inception)
input_elemnt2 = driver.find_element_by_class_name('dnnPrimaryAction').click()
Organization = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblOrganizationName').text
Designation = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblDesignation').text
Mobile = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblMobileNumber').text
Address = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblAddress').text
Email = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblEmail').text
Membership_Number = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblMembershipNumber').text
city = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblCity').text
name = driver.find_element_by_css_selector('span#dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl04_lblFullName').text
value_dict = {'Name':name,'City':city,'Organization':Organization,'Designation':Designation,'Mobile':Mobile,'Address':Address,'Email':Email,'Membership no.':Membership_Number}
print(value_dict)
import json
print(json.dumps(value_dict))
driver.close





