from copy import deepcopy


def realize_site(base_site: dict, name_company):
    for key, value in base_site.items():
        if not isinstance(value, dict):
            if 'телефон' in value:
                base_site[key] = value.replace('телефон', name_company)

        else:
            realize_site(value, name_company)


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

iphone_site = deepcopy(site)
realize_site(iphone_site, 'Iphone')
print(iphone_site)
android_site = deepcopy(site)
realize_site(android_site, 'Android')
print(android_site)


