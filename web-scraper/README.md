# Overview
- This is used to scrap and download car images from kijiji.ca and truecar.com
- You can download images for any car make, model and year you specify as below
- When you run the scraper, will create a downloads directory
- It will also create sub directories as \<make> - \<model>
- Example: Acura - RDX
- NOTE: For now you can only scrape one make-model at a time
- If you want to scrape for multiple models, you need to to run the below steps for each make-model

# How to Run
- Update the 2 variables 'make' and 'model' to the model you want to download
- By default these are set to 'Toyota' and 'RAV4'
- Then navigate to kijiji.com and/or truecar.com
- Search for the car model you want to download images of
- Copy the url and append them to kijiji_list_pages and/or truecar_list_pages
- If you want to download from multiple pages, then you need to copy all page indexes
- Now append the built years you want in the 'years' variable 
- Example: To download Honda civic 2018, 2019 & 2020 images from the first 3 pages of kijiji.com
    ```
    make = "Honda"
    model = "Civic"
  
    years = ["2018, "2019", "2020"]
  
    kijiji_list_pages = [
            "https://www.kijiji.ca/b-canada/honda-civic/k0l0?rb=true&dc=true",
            "https://www.kijiji.ca/b-cars-trucks/canada/honda-civic/page-2/k0c174l0?rb=true",
            "https://www.kijiji.ca/b-cars-trucks/canada/honda-civic/page-3/k0c174l0?rb=true",
        ]
    ```
- run scrapper with python scraper.py

