import requests, json, os
from bs4 import BeautifulSoup
from datetime import datetime

def eltoque(url='https://eltoque.com', save='./datasets/eltoque.json'):
    sesion = requests.Session()
    response = sesion.get(url)

    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", attrs={"class": "sc-672dda73-2 eeMZSu table table-borderless"})
            tbody = table.find_next("tbody")
            tr = tbody.find_all_next("tr")
            
            price_eur = tr[0].find_next("span", attrs={"class": "price-text"})
            price_usd = tr[1].find_next("span", attrs={"class": "price-text"})
            price_mlc = tr[2].find_next("span", attrs={"class": "price-text"})
            
            converted_price_eur = float(price_eur.text.split(" ")[0])
            converted_price_usd = float(price_usd.text.split(" ")[0])
            converted_price_mlc = float(price_mlc.text.split(" ")[0])   
            
            data = {
                "USD": converted_price_usd,
                "MLC": converted_price_mlc,
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            
            if os.path.exists(save):
                with open(save, "r", encoding="utf-8") as f:
                    data_json = json.load(f)
            data_json.append(data)

            with open(save, "w", encoding="utf-8") as f:
                json.dump(data_json, f, ensure_ascii=False, indent=4)
            print(f'Datos actualizados: {data} \nGuardado en "{save}"')
            return data_json

    except Exception as e:
        print(e)

if __name__ == "__main__":
    eltoque()