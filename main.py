import csv
import requests as rq
from bs4 import BeautifulSoup

# names = open("names.txt", "w")
# phones = open("phones.txt", "w")
# address = open("address.txt", "w")
web = open("sites.txt", "w")

# restaurant name - Done
# address - Done
# phone - Done
# email
# description
# excel file e save kora lagbo

site = "https://www.yellowpages.com/search?search_terms=Indian+Restaurants&geo_location_terms=Los+Angeles%2C+CA&page="

all_data = ["Name", "Phone", "Website", "Address"]

sheet_data = []

try:
  for i in range(1, 100):
    page = rq.get(f"{site}{i}")
    bs = BeautifulSoup(page.text, "html.parser")
    name = bs.find_all('a', {"class": "business-name"})
    phone = bs.find_all('div', {"class": "phones"})
    addr1 = bs.find_all('div', {"class": "street-address"})
    addr2 = bs.find_all('div', {"class": "locality"})
    wb = bs.find_all('a', {"class": "track-visit-website"})

    for n, p, a1, a2, lnk in zip(name, phone, addr1, addr2, wb):
      # names.write(n.find('span').text + "\n")
      # phones.write(p.text + "\n")
      # address.write(f"{a1.text}, {a2.text}\n")
      # web.write(lnk["href"] + "\n")
      dct = {
        "Name": n.find('span').text,
        "Phone": p.text,
        "Website": lnk["href"],
        "Address": f"{a1.text}, {a2.text}"
      }
      sheet_data.append(dct)
except:
  print("Limit reached")

with open("data.csv", "w") as csv_data:
  sheet = csv.DictWriter(csv_data, restval=",", fieldnames=all_data)
  sheet.writeheader()
  sheet.writerows(sheet_data)

# names.close()
# phones.close()
# address.close()
# web.close()