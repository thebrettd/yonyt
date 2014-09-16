from flask import Flask, request

import requests

import os

app = Flask(__name__)

base_nyt_url = 'http://api.nytimes.com'

@app.route('/subscribe/')
def subscribe():
    results = retrieve_most_popular()
    username = request.args.get('username')
    yo_user_with_link(results, username)
    return 'Subscribed %s' % username


def retrieve_most_popular(resource_type='mostviewed', sections='all-sections', interval=30,
                          nyt_api_key=os.environ.get('NYT_API_KEY')):

    request_string = '%s/svc/mostpopular/v2/%s/%s/%s/?api-key=%s' % (base_nyt_url, resource_type, sections, interval, nyt_api_key)

    requests_get = requests.get(request_string)
    return 'http://www.google.com'


def yoall_with_link(link):
    payload = {'api_token': os.environ.get('YO_API_KEY'), 'link': link}
    requests.post("http://api.justyo.co/yoall/", data=payload)


def yo_user_with_link(link, username):
    print 'Will yo %s' % username
    payload = {'api_token': os.environ.get('YO_API_KEY'), 'username': username, 'link': link}
    requests.post("http://api.justyo.co/yo/", data=payload)


def schedule():
    popular_link = retrieve_most_popular()
    yoall_with_link(popular_link)

if __name__ == '__main__':
    app.run()
