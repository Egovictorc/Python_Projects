from tkinter import *
import bs4
import requests

#response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#response.raise_for_status
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html. Let’s first download the page and create a BeautifulSoup",
                        "html.parser")
response = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168", "html.parser")
#response = requests.get("https://techclinic.com.ng")
content = response.content
soup = bs4.BeautifulSoup(content, "html.parser")
seven_day = soup.find(id="seven-day-forecast")

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]
# img = tonight.find("img")
# desc = img["title"]
# print(desc)

# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)
#p = soup.find_all("a", target="_blank")
#p = soup.select("a[href='/blog/']")
#print(p)
#print(type)
#print(content)

#links = soup.select("a")
# for link in links:
#     print(link["href"])


