An implementation of scrapy spiders for web scraping and ntlk for keyword extraction 

## Installation:

- Install scrapy using this command:
```
pip install scrapy
```
- Install rake ntlk library using this command:
```
 pip install rake-nltk
```
- Idownload stopwords for rake-nltk using this command:
```
python3 -c "import nltk; nltk.download('stopwords')"
```


## Setting up and usage

- clone this repo 

```
git clone https://github.com/samuelayo/scrapy-example.git
```

- change directory to this repo 
```
cd scrapy-example
```
- run the spider that would crawl news from investopedia. after running this command, rake will download some files needed as first run. after that, the scraping will commence
```
scrapy crawl investopedia

```
**Verify the contents that have been scrapped by opening investopeida/investopedia.csv in an excel document**

## todo
- create unit tests

