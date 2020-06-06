# GooglePlayStoreScrape

Codes to scrape reviews about any Android App on [Google Play Store](https://play.google.com/store/apps/)

## Modules:
- __GooglePlayStoreScrape.py__ : Extracts all information about reviews of any app
    <br /> - _[get_reviews](#get_reviews)_
 
## Requirements
```python
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time  
```

### *get_reviews*
Extracts detailed reviews and ratings given to particular android app on play store

###### Information extracted:
- Detailed Review
- Shortened Review
- Date of Reivew
- Name of Reviewer
- Reply by Developers
- Date of Developer's reply (if any) 
- Rating

```python
import get_reviews from GooglePlayStoreScrape

#define app id and path of chrome driver
app_id = 'com.appname.extension' #example in the app url
chromedriver_path ="C:\\Users\\<insert actual path>\\chromedriver.exe"

get_reviews(app_id,chromedriver_path)
```

###### Arguments for get_reviews:
- **app_id**: App ID of the application given in the play store page url (Example: com.appname.extension )
- **chromedriver_path**: path of chromedriver (align the version with your chrome version, see [Resources](#resources))

## Resources
 
- **[Google Play Store](https://play.google.com/store/apps/)**
- **[Selenium](https://www.selenium.dev/)**
- **[Chrome Driver](https://chromedriver.chromium.org/)**
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[HTML Parser](https://docs.python.org/3/library/html.parser.html)**
    
