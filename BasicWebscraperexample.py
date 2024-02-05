import requests
from bs4 import BeautifulSoup



#URL THAT YOU ARE TARGETING TO SCRAPE FROM 
URL = "https://realpython.github.io/fake-jobs/"
#REQUESTING FROM URL
page = requests.get(URL)

#UTILIZE BEAUTIFUL SOUP WITH HTML PARSER
soup = BeautifulSoup(page.content, "html.parser")

#DECLARE AND FIND THE ID RESULTS CONTAINER
results = soup.find(id="ResultsContainer")

# DECLARE A JOB ELEMENTS VARIABLE THAT GETS ALL ELEMENTS UNDER THE DIV CLASS card-content
job_elements = results.find_all("div", class_="card-content")

#ITERATE FOR THE TITLE, COMPANY< AND LOCATION, THIS WILL PRINT OUT THE TEXT AND REMOVE ANY WHITESPACE
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print("Job_Title: ", title_element.text.strip())
    print("Company_Name: ", company_element.text.strip())
    print("Location: ", location_element.text.strip())
    print()
