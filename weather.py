import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier

def get_data(url):
    r = requests.get(url)
    return r.text

html_data = get_data("https://weather.com/weather/today/l/88ce48a2de7058a171621256c796cdae5c373d767e4ca0ecd12d2c55b46aa350")

soup = BeautifulSoup(html_data, 'html.parser')

current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))
temp_rain = str(chances_rain)

results = "current_temp" + temp[128:-9] + "in Fayetteville, NC" + "\n" + temp_rain[131:-14]
n.show_toast("Live Weather Update: \n ", results, duration = 10)
