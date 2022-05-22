import requests.utils

# url = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(url, currency_code):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding = encodings)
    list1 = content.split('CharCode')
    cur_names = []
    for i in list1:
        if i.startswith('>'):
            cur_names.append(i[1:4])
    for n in cur_names:
        cur_names.remove('<No')
    cur_value = []
    list2 = content.split('<Value')
    for k in list2:
        if k.startswith('>') and k[1:2].isdigit():
            cur_value.append(k[1:8].replace(',', '.'))
    cor_val_float = [float(x) for x in cur_value]
    mut_list = dict(zip(cur_names,cur_value))
    for code in mut_list:
        if code == currency_code.upper():
            return float(mut_list[code.replace('.', ',')])
    
if __name__ == '__main__':
    currency_rates('http://www.cbr.ru/scripts/XML_daily.asp','DKK')
