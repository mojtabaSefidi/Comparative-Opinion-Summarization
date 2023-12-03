from bs4 import BeautifulSoup
import pandas as pd 
import requests
import csv

def get_hotels_city(url):
    Hotels = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.findAll('a', attrs = {'class':"tile-card"})
    for row in table:
        if row.p != None and row.p.text != '\n':
            try:
                name = row['title']
                link = row['href']
                Hotels[name] = {}
                Hotels[name]['Link'] = link
            except:
                continue

    return Hotels

def add_details(dict_hotels):
  for hotel in dict_hotels.keys():
    url = dict_hotels[hotel]['Link']
    content = requests.get(url)
    soup = BeautifulSoup(content.content, 'lxml')
    dict_hotels[hotel]['Address'] = soup.findAll('span', attrs = {'itemprop':"streetAddress"})[0].text
    dict_hotels[hotel]['Star'] = soup.findAll('span', attrs = {'class':"hotel_grid"})[0].text.replace('(', '').replace(')', '').strip()
    scores = soup.findAll('div', attrs = {'class':['col-2 col-lg-1 body-1 text-end',"col-5 col-lg-4 body-2 text-secondary"]})
    avg_scores = {}
    for i in range(0, len(scores)-1, 2):
      avg_scores[scores[i].text] = float(scores[i+1].text)
    dict_hotels[hotel]['Average_Scores'] = avg_scores
    
    reviews = []
    all_reviews = soup.findAll('div', attrs = {'class':"card js-comment js-travel-goal-family mb-5"})
    for review in all_reviews:
      detail = {}
      detail['Name'] = review.findAll('div', attrs = {'class':"fw-semibold me-2 me-md-4"})[0].text.strip()
      detail['Date'] = review['data-e24-date']
      detail['Rate'] = review['data-e24-rate']
      detail['Purpose'] = review.findAll('div', attrs = {'class':"text-secondary"})[0].text.strip()
      comments = review.findAll('div', attrs = {'class':"property-comments__comment-text body-1"})
      merged_comments = ''
      for comment in comments:
        merged_comments += ' ' + comment.text.strip()
      detail['Comment'] = merged_comments.strip()
      reviews.append(detail)
    
    dict_hotels[hotel]['Reviews'] = reviews
  return dict_hotels
