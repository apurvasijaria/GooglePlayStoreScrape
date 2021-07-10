# Project Description

GooglePlayStoreScrape is a python module to scrape reviews and other data about any Android App on [Google Play Store](https://play.google.com/store/apps/)

## Installation

```python
pip install GooglePlayStoreScrape
```

## Requirements
```python
pip install -r requirements.txt
```

If you receive errors related to Chrome Driver package, look at the chrome version installed in your machine and install the compatible version. This package uses 91.0.4472.101.0 


## Modules:
- __GooglePlayStoreScrape.py__ : Extracts all information about reviews of any app
    <br /> - _[get_reviews](#get_reviews)_
 
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

## Usage:

```python
import GooglePlayStoreScrape as gpss

#define app id and path of chrome driver
app_id = 'com.appname.extension' #example in the app url

gpss.get_reviews(app_id)
```

###### Arguments for get_reviews:
- **app_id**: App ID of the application given in the play store page url (Example: com.appname.extension )

## Resources
 
- **[Google Play Store](https://play.google.com/store/apps/)**
- **[Selenium](https://www.selenium.dev/)**
- **[Chrome Driver](https://chromedriver.chromium.org/)**
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[HTML Parser](https://docs.python.org/3/library/html.parser.html)**
    
## Project Links:
- **[PyPI](https://pypi.python.org/)**
- **[GitHub](https://github.com/apurvasijaria/GooglePlayStoreScrape/)**
