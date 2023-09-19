import requests
import json
import cityfinder as cf
import datefinder as df

def return_news(lat, long):
    news_api_key = "bf02e45c28064b52b5bd1eb88e75c741"
    news_url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy=popularity&apiKey={}"
    city = cf.get_city_from_lat_lng(lat, long)
    searchquery = city + " criminal activity"
    print(searchquery)

    dateslist = df.return_dates()
    today = dateslist[1]
    one_month_ago = dateslist[0]

    news_url = news_url.format(searchquery, one_month_ago, today, news_api_key)

    response = requests.get(news_url)
    data = response.json()

    return data

# for i in data['articles']:
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['urlToImage'])
#     print(i['publishedAt'])
#     print(i['content'])
#     print(
#         "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
