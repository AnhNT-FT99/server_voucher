from requests_html import HTMLSession
import database

URL = {
    "GRAB_FOOD": "https://chanhtuoi.com/ma-giam-gia-grab-c53.html?load=true&cate=14&order=hot",
    "GRAB_CAR": "https://chanhtuoi.com/ma-giam-gia-grab-c53.html?load=true&cate=15&order=hot",
    "GRAB_BIKE": "https://chanhtuoi.com/ma-giam-gia-grab-c53.html?load=true&cate=16&order=hot"
}


def crawler(url: str) -> list:
    id_division = None

    if url == URL["GRAB_FOOD"]:
        id_division = 1
    elif url == URL["GRAB_CAR"]:
        id_division = 2
    elif url == URL["GRAB_BIKE"]:
        id_division = 3

    session = HTMLSession()
    
    r = session.get(
    url=url,
    )
    article = r.html.find('div.chanhtuoi-code')

    item_list = article[0].find('div.item')

    vouchers = []

    for item in item_list:
        name = item.find('p', first=True).text
        item_desc = item.find('div.item-desc')
        des = item_desc[0].find('p', first=True).text
        dic = item.find('div.code')
        data = dic[0].attrs

        vouchers.append(
            {
                "id_division": id_division,
                "price_voucher": str(data['data-code']),
                "des_voucher": des,
                "name_voucher": name,
            }
        )  

    for voucher in vouchers:
        database.insert_voucher(voucher)
    


if __name__ == "__main__":
    crawler(URL["GRAB_FOOD"])
    crawler(URL["GRAB_CAR"])
    crawler(URL["GRAB_BIKE"])

