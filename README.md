yonyt
=====

Yo Service which responds to any Yo with a popular link from the [New York Times API](http://developer.nytimes.com/docs/most_popular_api/#h2-requests).



Popular API query is executed using the following parameters:



- resource-type: mostviewed
- section: all-sections
- time-period: 1



Currently deployed and running on [Heroku](http://www.heroku.com)


Cronjobs
-------------
The following 2 cronjobs which are running on my personal VPS:

0 9 * * * curl http://yonyt.herokuapp.com/schedule/


This job initiates the 9am daily push to all subscribers.


0,30 * * * * curl http://yonyt.herokuapp.com/ping/


This job prevents Heroku from idling the Dyno

