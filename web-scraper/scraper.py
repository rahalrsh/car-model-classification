import requests
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

import time


def get_ad_links_from_truecar_page(soup, filter_model, filter_years):
    links = []

    divs = soup.find_all("div", {"data-qa": "Listings"})

    for d in divs:

        title = d.find("span", {"class": "vehicle-header-make-model"}).contents
        title = ' '.join(title).split()
        title = ' '.join(title)

        make_year = d.find("span", {"class": "vehicle-card-year"}).contents[0]

        a = d.find("div", {"data-qa": "Listing"}).find("a")
        link = a["href"]

        print(title, make_year, filter_model)

        if any(year in make_year for year in filter_years) and (filter_model.lower() in title.lower()):
            print(title, make_year)
            links.append(link)

    return links


def get_ad_links_from_kijiji_page(soup, filter_model, filter_years):
    links = []

    divs = soup.find_all("div")
    for d in divs:
        if d.has_attr("data-listing-id"):
            a = d.find("div", {"class": "title"}).find("a")

            title = a.contents[0]
            link = a["href"]

            if any(year in title for year in filter_years) and (filter_model.lower() in title.lower()):
                links.append(link)

    return links


def get_image_urls_from_kijiji(soup):
    urls = []

    div_vip_body = soup.find_all("div", attrs={"id": "vip-body"})[0]
    imgs = div_vip_body.find_all("img")

    for img in imgs:
        image_url = img["src"]

        if ".JPG" not in image_url:
            print("NOT AN IMAGE: ", image_url)
            continue

        image_url = image_url.replace("$_2.JPG", "$_27.JPG")

        urls.append(image_url)

    return urls


def get_image_urls_from_truecar(soup):
    urls = []

    try:
        div_data_qa = soup.find_all("div", attrs={"data-qa": "GalleryPreview"})[0]
        imgs = div_data_qa.find_all("img")
    except:
        print("COULD NOT FIND GalleryPreview")
        return []

    for img in imgs:
        image_url = img["src"]

        if ".jpg" not in image_url:
            print("NOT AN IMAGE: ", image_url)
            continue

        image_url = image_url.replace("-60.jpg", "-540.jpg")

        urls.append(image_url)

    return urls


def download_and_save_images_from_urls(urls, image_name_prefix, model_name):
    for url in urls:
        # i = image_name_prefix + " - " + "{0:0=5d}".format(i)

        millis = str(round(time.time() * 1000000000))
        i = millis + " - " + image_name_prefix

        filename = "downloads/" + model_name + "/" + i + ".jpg"

        print(filename, url)

        r = requests.get(url, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

        else:
            print('Image Couldn\'t be retreived')


def mkdir_if_not_exist(dir_name):
    Path("downloads/" + dir_name).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    make = "Toyota"
    model = "RAV4"

    model_name = make + " - " + model

    years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]

    mkdir_if_not_exist(model_name)

    # Kijiji.com
    KIJIJI = "https://www.kijiji.ca"

    kijiji_list_pages = [
        "https://www.kijiji.ca/b-canada/honda-civic/k0l0?rb=true&dc=true",
        "https://www.kijiji.ca/b-cars-trucks/canada/honda-civic/page-2/k0c174l0?rb=true",
        "https://www.kijiji.ca/b-cars-trucks/canada/honda-civic/page-3/k0c174l0?rb=true",
    ]

    for page in kijiji_list_pages:
        req = requests.get(page, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        kijiji_urls = get_ad_links_from_kijiji_page(soup, (make + " " + model), years)

        print(kijiji_urls)
        image_urls = []

        for url in kijiji_urls:
            req = requests.get(KIJIJI+url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')

            image_urls.extend(get_image_urls_from_kijiji(soup))

        if image_urls:
            download_and_save_images_from_urls(urls=image_urls, image_name_prefix="kijiji", model_name=model_name)


    # TruCar.com
    TRUECAR = "https://www.truecar.com/"

    truecar_list_pages = [
        # "https://www.truecar.com/used-cars-for-sale/listings/honda/civic/location-los-angeles-ca/?sort[]=best_match",
    ]

    for page in truecar_list_pages:
        req = requests.get(page, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        truecar_urls = get_ad_links_from_truecar_page(soup, (make + " " + model), years)

        print(truecar_urls)
        image_urls = []

        for url in truecar_urls:
            req = requests.get(TRUECAR+url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')

            image_urls.extend(get_image_urls_from_truecar(soup))

        if image_urls:
            download_and_save_images_from_urls(urls=image_urls, image_name_prefix="truecar", model_name=model_name)



