import requests #The requests library is a popular Python library used for making HTTP requests.
import csv

from bs4 import BeautifulSoup

# the list of dictionaries containing the scrape data
pokemon_products = []

# loop through each page and scrape the data

for page in range(1, 48):  # List of page numbers

    # download the HTML document with an HTTP GET request
    response = requests.get(f"https://scrapeme.live/shop/page/{page}/") 
    

    # Error-Handling Code   
    # If response is 2xx (i.e. 200 OK), the request was successful. 
    if response.ok:
        # parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        product_elements = soup.select("li.product")

        for product_element in product_elements:
            name = product_element.find("h2").get_text()
            url = product_element.find("a")["href"]
            image = product_element.find("img")["src"]
            price = product_element.select_one(".amount").get_text()

            # define a dictionary with the scraped data
            new_pokemon_product = {
                "name": name,
                "url": url,
                # "image": image,
                # "price": price
            }

            # add the new product dictionary to the list
            pokemon_products.append(new_pokemon_product)
    else:
        # in case of 4xx or 5xx response, log the error response

        print(response.text) 

# create the "products.csv" file
        
csv_file = open('products.csv', 'w', encoding='utf-8', newline='')

# initialize a writer object for CSV data
writer = csv.writer(csv_file)

# convert each element of pokemon_products
# to CSV and add it to the output file

for pokemon_product in pokemon_products:
    writer.writerow(pokemon_product.values())

# release the file resources
csv_file.close()