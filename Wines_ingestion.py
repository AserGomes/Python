
import pandas as pd
import numpy as np
import bs4 as soup
import requests
import pandablob
from azure.storage.blob import ContainerClient

disp = []
clubPrice = []
listPrice = []
salePrice = []

page = 1
url = f'http://www.wine.com.br/browse.ep?cID=100851&exibirEsgotados=false&pn={page}&listagem=horizontal&sorter=price-asc&filters=cVINHOS%20atTIPO_TINTO'
r = requests.get(url)
soup = soup.BeautifulSoup(r.content.decode('utf=8'), 'html.parser')

boxSite = soup.findAll(class_='ProductDisplay ProductDisplay--horizontal')


for i in range(len(boxSite)):
    boxItems = str(boxSite[i].find(class_="vue-price-box")).split()

    for n in boxItems:

        if(n == "'available':"):
            disp.append(boxItems[int(boxItems.index(n)) + 1])

        if (n == "'clubPrice':"):
            clubPrice.append(boxItems[int(boxItems.index(n)) + 1])

        if (n == "'listPrice':"):
            listPrice.append(boxItems[int(boxItems.index(n)) + 1])

        if (n == "'salePrice':"):
            salePrice.append(boxItems[int(boxItems.index(n)) + 1])


df = pd.DataFrame({'Disponibilidade':disp,
                    'clubPrice': clubPrice,
                    'listPrice': listPrice,
                    'salePrice': salePrice})


account_url = "https://aserzin.blob.core.windows.net/"
token = "ioLV70V8qERvjBdpEEKK9x4xlXOMFDai2bCeu91DW8/Cu4OamUq5l2GZGxiUuxUTvxoX0kplB6rX+AStF2NrkA=="
container = "ingestion/wines"
blobname = "wines_ingestion.csv"

container_client = ContainerClient(account_url, container, credential=token)
blob_client = container_client.get_blob_client(blob=blobname)

pandablob.df_to_blob(df,blob_client,overwrite=True)
#DefaultEndpointsProtocol=https;AccountName=aserzin;
#AccountKey=ioLV70V8qERvjBdpEEKK9x4xlXOMFDai2bCeu91DW8/Cu4OamUq5l2GZGxiUuxUTvxoX0kplB6rX+AStF2NrkA==;
#EndpointSuffix=core.windows.net
"""
print(disp)
print(clubPrice)
print(listPrice)
print(salePrice)

#ProductDisplay ProductDisplay--horizontal

src="https://www.wine.com.br/cdn-cgi/image/f=png,h=238,q=99/assets-images/produtos/24552-01.png"
            class="CartItem-image lazy-img"
            data-sku="24552"
            data-seo="/vinhos/ja-pias-375-ml/prod24552.html"
            data-type="tinto"
            data-fullprice="47.90"
            data-member="19.90"
            data-saleprice="23.41"
            data-country="Portugal"
            alt="J&aacute; Pias 375 mL

"""




