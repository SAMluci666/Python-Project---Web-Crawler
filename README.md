# Python Web Crawler/Scraper Project for Semester VI Python Workshop (14-02-2024) - Samar Singla  
## This is a guide/tutorial and my experience in building this project

## Table of Contents

- [Introduction](#introduction)
- [Steps](#steps)
- [Use Cases](#scraping-use-cases")
- [Challenges](#challenges-in-web-scraping)
- [Process](#web-scraping-process)
- [Examples](#examples)
- [Contributing](#contributing)
- [License][def]

# Introduction: 

### What is a Web Crawler?
Web crawling is a technique that refers to visiting pages and discovering URLs on a site. It enables the collection of large amounts of data from many pages.

### What is Web Scraping? 
the process of retrieving data from the web. Even copying and pasting content from a page is a form of scraping! But it usually refers to the task performed by an automated software (script, bot, crawler, spider etc...) that visits a website and extracts the data of interest from its pages

### Is there a difference between Web Crawling and Web Scraping?
web scraping is about extracting data from one or more websites. While crawling is about finding or discovering URLs or links on the web

### Why Python? Can we use another language?    
Python is easy-to-use with a large community and a vast library bank. Python has become the most popular language for AI/ML and web scraping puropose. We can also use other languages (It will be a future project)

---
# Steps: 

### Steps involved in Scraping Process: -
1. **Inspect the target site:**
            - Get an idea of what information is to be extracted from the site. 
            - Study about the HTML elements position on the pages.
            - Study about the data to be extracted 
2. **Get the page's HTML code:** 
            - Access the HTML content by downloading the page's documents. To accomplish that:
            - Use an HTTP client library, like Requests, to connect to your target website.
            - HTTP GET requests to the server with the URLs of the pages to scrape.
            - Verify that the server returned the HTML document successfully.
3. **Extract your data from the HTML document:**  Obtain the information you're after, usually a specific piece of data or a list of items. To achieve this:
            - Parse the HTML content with a data parsing library, like Beautiful Soup.
            - Select the HTML content of interest with the same library.
            - Write the scraping logic to extract information from these elements. 
            - If the website consists of many pages and you want to scrape them all:
            - Extract the links to follow from the current page and add them to a queue.
            - Follow the first link and go back until the queue is empty.
4. **Store the extracted data:** Once extracted, transform and store it in a format that makes it easier to use. To reach this:
            - Convert the scraped content to CSV, JSON, or similar formats and export them to a file.
            - Write it to a database.

# Scraping Use Cases
- **Competitor Analysis:** Gather data from your competitors' sites about their products/services, features, and marketing approaches, to monitor them and gain a competitive edge.

- **Price Comparison:** Collect prices from several e-commerce platforms to compare them and find the best deals.

- **Lead Generation:** Extract contact information from websites, such as names, email addresses, and phone numbers, to create targeted marketing lists for businesses. But be aware of your national laws when personal information is involved.

- **Sentiment Analysis:** Retrieve news and posts from social media to track public opinion about a topic or a brand.

- **Social Media Analytics:** Recover data from social platforms, such as Twitter, Instagram, Facebook, and Reddit, to track the popularity and engagement of specific hashtags, keywords, or influencers.

- **Competitive Pricing Analysis:** Our web scraping tool can be used to gather pricing data from competitor websites, allowing businesses to compare prices and adjust their own pricing strategies accordingly. By regularly scraping competitor sites, businesses can stay competitive in the market and attract more customers with competitive pricing.

- **Social Media Monitoring:** Our tool enables users to scrape data from various social media platforms to monitor public sentiment, track trends, and analyze user engagement. For example, businesses can track mentions of their brand or products on social media to gauge customer satisfaction and identify areas for improvement in their marketing strategies.

# Challenges in Web Scraping: 

- **Variety:** The diversity in website layouts, styles, and data structures necessitates custom-built scraping scripts for each target.
  
- **Longevity:** Web pages frequently change their structure and content, causing scraping scripts to stop working and requiring adaptation.
  
- **Scalability:** Increasing data volume raises concerns about spider performance. Solutions like distributed systems, parallel scraping, and code optimization can enhance scalability.

- **Anti-bot technologies**: These are the measures that sites take to protect against malicious or unwanted bots and include scrapers by default. pose obstacles to scraping efforts: 
- **IP Blocking:** Websites may block IP addresses used by scrapers.
- **JavaScript Challenges:** Sites may employ JavaScript-based challenges to deter scrapers.  
- **CAPTCHAs:** CAPTCHAs hinder automated scraping by requiring human interaction.

Future Idea: To overcome these challenges, techniques such as rotating proxies and headless browsers can be employed, or services like ZenRows can simplify the process.

# Web Scraping Process

## Setting up the Environment

- **Python** : I have installed Python 3.12.2
- **pip** : The Python Package Index (PyPi) used to install libraries.
- **Python IDE**: I will be using VSCode

- Create a python-scrapper.py file in the directory.

## Inspecting the Target Website: 

First analyze the target website to study the site structure and understand how to scrape data from it. (sounds tedious but is crucial)

- For this project, I will be scraping the website: [scrapeme](https://scrapeme.live/shop/)

- Interact/ Browse the Website like a normal user and study how the site reacts.
  - Explore different list pages 
  - Try Search Feature
  - Open product pages
  - **Focus how the URL changes.**
  
### Analyze the URL Structure: -
A web server returns an HTML document based on the request URL, each one is associated with a specific page. Typically, URLs of same-type pages share a similar format overall.

*Ex*: - https://scrapeme.live/shop/Raticate/

- This URL can be divided into two parts 
1. **Base URL**: The path to the shop section of the website.
2. **Specific Page Location**: The path to the specific product. *The URL may end with .html, .php, or have no extension at all.*
   
- The URL can also contain additional information: - 
  - **Path Parameters:** These are used to capture specific values in a RESTful approach 
  Example: In https://www.example.com/users/14, 14 is the path param.
  - **Query parameters:** Added to the end of a URL after a question mark (?). They generally encode filter values to send to the server when performing a search.
  Example: In https://www.example.com/search?search=blabla&sort=newest, search=blabla and sort=newest are the query parameters.

Any query parameter string consists of :-
`?`: Marks the beginning. and A list of `key=value` parameters separated by `&`

**Analysis Result**: All products listed on the website have the same base URL and only the latter part of the URL (string) changes for each specific product.

For Example: https://scrapeme.live/page/3/?s=bla

This URL corresponds to the third page of search result for "bla" query. where *3 is the path parameter* and *bla is the value of s key/parameter*

Thus, the above  URL will instruct the server to run a paginated search query and get all that contain the string bla and return only the results of page number three.

### Use Developer Tools to Inspect the Site: - Inspecting the HTML Code

Every modern web browser includes a powerful suite of developer tools. These tools do a range of things, from inspecting currently-loaded HTML, CSS and JavaScript to showing which assets the page has requested and how long they took to load.

Developer Tools let us inspect the structure of **Document Object Model (DOM)** of a web page. (Open the `Elements` tab) This helps in deeper insight into website's structure. 

#### DOM vs HTML
- The HTML code represents the content of a web page document written by a developer.

- The DOM is a dynamic, in-memory representation of HTML code created by the browser.
  
## Download HTML Pages: - [Using `request` library]

- To scrape data from any website, first we need to download the HTML document.

- Intall request library using pip
```py
pip install requests
```
- Now, using the below code: -

```py
import requests

#download the HTML document with an HTTP GET request
response = requests.get("https://scrapme.live/shop/")

print(response.text)
```
- The above code imports the dependencies.
- Then uses, requests get() function to perform **HTTP GET request** to the target HTML Page URL
- It returns the python representation of the response containing the HTML document.
- Using the `print(response.text)` statement, we get the HTML code of the page.
- The GET request to the server may fail for several reasons. The server may be temporarily unavailable, the URL may be wrong, or your IP might have been blocked. 

**Error Handling Code: -**
```py 
# If response is 2xx (i.e. 200 OK), the request was successful. 
if response.ok:
    #scraping Logic
else:
    # in case of 4xx or 5xx response, log the error response
print(response) #This line prints the HTML content of the webpage to the console    
```
