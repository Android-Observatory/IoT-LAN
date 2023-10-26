import google_play_scraper
from google_play_scraper import app
import pandas as pd

with open('more_companion_apps.txt', 'r') as fp:
    dff = fp.readlines()
    
dff = [i.strip('\n') for i in dff ]
    
data = []
cols = ['pkg_name', 'app_name', 'version', 'description', 'category', 'category_id', 'content_rating', 'installs', 'content_rating_description', 'url']
df = pd.DataFrame(data, columns = cols, index=[0])

for pkg in dff:
    try:
        result = app(
            pkg,
            lang='en', # defaults to 'en'
            country='us' # defaults to 'us'
        )

        data = {'pkg_name': pkg, 
            'app_name': result['title'],
           'version': result['version'], 
           'description': result['description'],
            'category': result['genre'],
        'category_id': result['genreId'],
            'content_rating': result['contentRating'],
                'installs': result['installs'],
            'content_rating_description': result['contentRatingDescription'],
            'url': result['url']
           }

        print(data)
        df = df.append(data, ignore_index = True)
    except google_play_scraper.exceptions.NotFoundError:
        print("app not found")
        with open('com_app_not_found.txt', 'a') as fp:
            fp.write(pkg + '\n')
    

df.to_csv('more-iot-dataset.csv', index=False)
print('crawl complete......!')
