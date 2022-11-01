import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import glob

"""Request on this sites"""
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.maximize_window()
#
# try:
#     for i in range(1, 20):
#         driver.get(url=f"https://www.turpravda.ua/uc/top-hotels.html?rte%5B0%5D=9&rte%5B1%5D=8&p={i}")
#         time.sleep(3)
#         with open(f"all_pages/index{i}.html", 'w') as file:
#             file.write(driver.page_source)
# except Exception as _ex:
#     print(_ex)
# finally:
#     driver.close()
#     driver.quit()

"""PARSING INFORMATION"""
# for i in range(1, 20):
#     with open(f"all_pages/index{i}.html") as file:
#         src = file.read()
#     soup = BeautifulSoup(src, 'lxml')
#     hotels_name_hrefs = soup.find_all(class_="hotel-name-title")
#     hotels_rating = soup.find_all(class_="value fl")
#     hotels_city = soup.find_all(class_="hotel-breadcr")
#     hotels_services = soup.find_all(class_="service-list")
#     all_categories_dict = {}
#
#     for hrefs in hotels_name_hrefs:
#         hotel_name = hrefs.text.replace(" ", "").strip()
#         hotel_url = 'https://www.turpravda.ua' + hrefs.get("href").replace(" ", "").strip()
#         for rating in hotels_rating:
#             rating_text = rating.text.replace(" ", "").strip()
#         for city in hotels_city:
#             city_text = city.text.replace(" ", "").strip()
#         for services in hotels_services:
#             services_text = services.text.replace(" ", "").strip()
#
#         all_categories_dict[hotel_name] = {"name":hotel_name, "url": hotel_url, "rate": rating_text, "city": city_text,
#                                            "service": services_text}
#
#     with open(f"all_jsons/{i}page.json", 'w') as file:
#         json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


'''UNION IN ONE FILE'''
# result = []
# for f in glob.glob("all_jsons/*.json"):
#     with open(f) as infile:
#         result.append(json.load(infile))
#
# with open("merged_file.json", "w") as outfile:
#      json.dump(result, outfile,indent=4, ensure_ascii=False)
