import requests
from bs4 import BeautifulSoup

main_url = "https://hypertire.com"
page_number = 1
url = f"{main_url}/tires/?carsBrands=115&carsModels=0&carsTips=0&carsYears=0&carsSizes=0&page={page_number}"

tire_list = []
for page_number in range(1, 10):
    url = f"{main_url}/tires/?carsBrands=115&carsModels=0&carsTips=0&carsYears=0&carsSizes=0&page={page_number}"

    response = requests.get(url)

    if response.status_code == 200:
        contents = response.text
        
        # print(contents)

        soup = BeautifulSoup(contents, "html.parser")
        
        tires_soup = soup.find_all("neo-component-products-card", class_="shadow") # {"calss": "shadow"}
        print(len(tires_soup))
        

        headers = ["size", "year", "price", "tire_url"]
        for tire in tires_soup:
            size = tire.find("h4").text.strip()
            year = tire.find("b").text.strip()
            # price = tire.find("p", class_="price").text.strip()
            price = tire.find("p", class_="price")["price"]
            tire_url = main_url + tire.find("a", request="dynamic")["href"]
            print(f"{size:10}, {year:6}, {price:20}, {tire_url}")
            
            tire_list.append([size, year, price, tire_url])
            
        
        
        # ADD ro CSV
        
    else:
        print(f"Can not open url, status code= {response.status_code}")



