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

## Dependencies and Supporting Libraries
Uses Selenium and BeautifulSoup, on calling the functions it opens a chrom window using selenium and scrolls down to open all reviews, till the last page. Window will automatically close when action is completed. 

## Modules:
- __GooglePlayStoreScrape.py__ : Extracts all information about the app and all reviews
    <br /> - _[get_reviews](#get_reviews)_
    <br /> - _[get_info](#get_info)_
 
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
- Number of People who found the review helpful

## Usage:

```python
import GooglePlayStoreScrape as gpss

#define app id and path of chrome driver
app_id = 'com.appname.extension' #example in the app url
country = 'IN'
language = 'en'

gpss.get_reviews(app_id,language,country)
```

###### Arguments for get_reviews:
- **app_id**: App ID of the application given in the play store page url (Example: com.appname.extension )
- **language**: Language of the application given in the play store page url (Example: en ), Optional Argument Default value = 'en'
- **country**: Coutry of the application given in the play store page url (Example: IN ), Optional Argument Default value = 'IN'

### *get_info*
Extracts details of particular android app on play store

###### Information extracted:
- Name
- Genre
- Total Number of Ratings
- Average Rating
- Last Updated Date
- Size
- Number of Installs
- Current Version
- Content Rating
- In-app Products
- Offered by
- Developer Website
- Developer Email
- Privacy Policy
- New Features in Latest Update
- Decription of the App

## Usage:

```python
import GooglePlayStoreScrape as gpss

#define app id and path of chrome driver
app_id = 'com.appname.extension' #example in the app url
country = 'IN'
language = 'en'

gpss.get_info(app_id,language,country)
```

###### Arguments for get_info:
- **app_id**: App ID of the application given in the play store page url (Example: com.appname.extension )
- **language**: Language of the application given in the play store page url (Example: en ), Default value = 'en'
- **country**: Coutry of the application given in the play store page url (Example: IN ), Default value = 'IN'

## Resources
 
- **[Google Play Store](https://play.google.com/store/apps/)**
- **[Selenium](https://www.selenium.dev/)**
- **[Chrome Driver](https://chromedriver.chromium.org/)**
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[HTML Parser](https://docs.python.org/3/library/html.parser.html)**
    
## Project Links:
- **[PyPI](https://pypi.org/project/GooglePlayStoreScrape)**
- **[GitHub](https://github.com/apurvasijaria/GooglePlayStoreScrape/)**
