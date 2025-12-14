import json, re, os, requests
from bs4 import BeautifulSoup

def Mercatoria(start, end, file):
    products = []

    for page in range(start, end):
        url = f'https://www.mercatoria.store/catalog?query=salchichas&page={page}&sort=popularity'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        for i in soup.select("div.MuiCardContent-root"):
            h3 = i.select_one("h3.MuiTypography-root.MuiTypography-h3.css-p9dpgq")
            p = i.select_one("p.MuiTypography-root.MuiTypography-body1.css-m6tgpv")

            if not h3 or not p:
                continue
            heading = h3.get_text(strip=True)
            paragraph = p.get_text(strip=True)
            paragraph = paragraph.replace("\xa0", " ").replace("\u00A0", " ")

            match_h = re.match(r"^(.*?)\s*\((.*?)\)$", heading)
            match_p = re.match(r"^([\d\.,]+)\s*([A-Za-z]+)$", paragraph)
            if match_h:
                name = match_h.group(1)
                weight = match_h.group(2)

                price = match_p.group(1).replace(",", ".")
                price = float(price)
                currency = match_p.group(2)

            if "x" in weight:
                continue
            data = {
                "name": name,
                "count": weight,
                "price": price,
                "currency": currency
            }

            products.append(data)

    save = f'./datasets/mercatoria/{file}.json'
    if os.path.exists(save):
        with open(save, "r", encoding="utf-8") as f:
            exist = json.load(f)
        if isinstance(exist, list):
            final = exist + products
        else:
            final = [exist] + products
    else:
        final = products

    with open(save, "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=4)
    print(f"Archivo '{save}' actualizado con {len(final)} productos.")

Mercatoria(1, 6, 'salchichas.json')