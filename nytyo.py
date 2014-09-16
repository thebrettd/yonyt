from flask import Flask, request

import requests

import os

app = Flask(__name__)

base_nyt_url = 'http://api.nytimes.com'
nyt_api_key = os.environ.get('NYT_API_KEY')
yo_api_key = os.environ.get('YO_API_KEY')


@app.route('/subscribe/')
def subscribe():
    results = retrieve_most_popular()
    username = request.args.get('username')
    yo_user_with_link(results, username)
    return 'Subscribed %s' % username


def retrieve_most_popular(resource_type='mostviewed', sections='all-sections', interval=1):

    request_string = '%s/svc/mostpopular/v2/%s/%s/%s/?api-key=%s' % (
        base_nyt_url, resource_type, sections, interval, nyt_api_key)

    popular_url = requests.get(request_string).json().get('results')[0].get('url')
    print 'Most popular story: %s ' % popular_url
    return popular_url


def yoall_with_link(link):
    payload = {'api_token': yo_api_key, 'link': link}
    print 'Will yoall with %s using api_key %s' % (link, yo_api_key)
    r = requests.post("http://api.justyo.co/yoall/", data=payload)
    print r.text


def yo_user_with_link(link, username):
    payload = {'api_token': yo_api_key, 'username': username, 'link': link}
    print 'Will yo %s with %s using api_key %s' % (username, link, yo_api_key)
    r = requests.post("http://api.justyo.co/yo/", data=payload)
    print r.text


@app.route('/schedule/')
def schedule():
    popular_link = retrieve_most_popular()
    yoall_with_link(popular_link)
    return 'Yoed Everyone!', 200


@app.route('/ping/')
def ping():
    return 'Pong'


if __name__ == '__main__':
    app.run()
