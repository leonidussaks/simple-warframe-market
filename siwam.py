import requests
import json

#init a config

with open('config.json') as config_file:
    data = json.load(config_file)
    url = data['url']
    version_info = data['version']

def all_items(lang='em'):
    headers = {'language': lang, 'accept': 'application/json'}
    r = requests.get(url, headers=headers)
    res = r.json()['payload']['items']
    return res

# используется чтобы можно было вводить текст на любом языке и получить результат на нем, не знаю как это лучше сделать
def check_items(item, lang='en'):
    r = all_items(lang)
    for i in r:
        if i['item_name'].lower() == item.lower():
            item_url = i["url_name"]
            break
        else:
            item_url = False
    return item_url
            
def info_items(item, lang='en'):
    # get the url of items 
    item_url = check_items(item, lang)
    headers = {'platform' : 'pc'}
    r = requests.get(url+"/"+item_url, headers=headers)
    res = r.json()["payload"]["item"]["items_in_set"]
    for i in res:
        item_info = i[lang]
        print(item_info)
    return item_info

def best_price(item, user_ingame_status=True):
    item_url = check_items(item)
    headers = {'platform' : 'pc'}
    r = requests.get(url+"/"+item_url+"/orders", headers=headers)
    res = r.json()["payload"]["orders"]
    orders = {}
    for i in res:
        platinum = i['platinum']
        user_username = i['user']['ingame_name']
        user_status = i['user']['status']
        user_shop = i['order_type']
        if user_status == "ingame" and user_shop == "sell" and user_ingame_status == True:
            orders[user_username]=platinum
        if user_shop == "sell" and user_ingame_status == False:
            orders[user_username]=platinum 
    if orders == {}:
        return f"no one wants to sell this item ({item})"
    k = min(orders, key=orders.get)
    platinum = orders.get(k)
    return {k : platinum}
    
def best_sell(item, user_ingame_status=True):
    item_url = check_items(item)
    headers = {'platform' : 'pc'}
    r = requests.get(url+"/"+item_url+"/orders", headers=headers)
    res = r.json()["payload"]["orders"]
    orders = {}
    for i in res:
        platinum = i['platinum']
        user_username = i['user']['ingame_name']
        user_status = i['user']['status']
        user_shop = i['order_type']
        if user_status == "ingame" and user_shop == "buy" and user_ingame_status == True:
            orders[user_username]=platinum
        if user_shop == "sell" and user_ingame_status == False:
            orders[user_username]=platinum 
    if orders == {}:
        return f"no one wants to buy this item ({item})"
    k = max(orders, key=orders.get)
    platinum = orders.get(k)
    return {k : platinum}


def version():
    return version_info