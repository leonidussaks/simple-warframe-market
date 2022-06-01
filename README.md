# simple-warframe-market
this script is aimed at getting data from the warframe market. can do almost nothing at the moment.

<details> 
  <summary>🇺🇸 Open to example</summary>

```python
// best_price() function for output best price for items in platinum
// where is 'crimson dervish' is the item u need it.
// if u add 'True'  it will only output who is in the game at the moment
x = siwam.best_price("crimson dervish", True, 'en')
// Output: {'username': 7}
  

// best_sell() function for output best buyers for items in platinum  
// where is 'Inaros Prime Set' is the item u need it.
// if u add 'False'  it will output all players who want to buy this item
y = siwam.best_sell("Inaros Prime Set", False, 'en')
// Output: {'username': 600}
  
x = siwam.info_items("crimson dervish", 'en')  
// Output: {'item_name': 'Crimson Dervish', 'description': 'Strong whirlwind attacks.', 'wiki_link': 'https://warframe.fandom.com/wiki/Crimson_Dervish', 'drop': []}

```

  </details>

<details> 
  <summary>🇷🇺 Открой для описания</summary>

```python
// best_price() функция выводящая лучшую цену продавцов
// где 'кровавый дервиш' это предмет который вам нужен.
// если поставить значение True - покажет тех кто находится в игре (можно не ставить)
x = siwam.best_price("кровавый дервиш", True, 'ru')
// Вывод: {'username': 7}
  

// best_sell() функция выводящая лучших покупателей по платине
// где 'Инарос Прайм: комплект' это то что вам нужно.
// если добавить значение 'False', то выведет всех игроков, которые хотят купить это (онлайн,оффлайн,онлайн в игре)
y = siwam.best_sell("Inaros Prime Set", False, 'ru')
// Вывод: {'username': 600}
  
x = siwam.info_items("кровавый дервиш", 'ru')  
// Вывод: {'item_name': 'Кровавый Дервиш', 'description': 'Сильные ураганные атаки.', 'wiki_link': 'https://warframe.fandom.com/ru/wiki/...', 'icon': 'icons/ru/Crimson_Dervish.12f1451d9ba47c437c239a650d613525.png', 'thumb': 'icons/ru/thumbs/Crimson_Dervish.12f1451d9ba47c437c239a650d613525.128x128.png', 'drop': []}

```

  </details>
