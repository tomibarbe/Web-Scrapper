import requests

url = "https://huitru.com/templates/ajax/adicionales.php"

payload = "idProd=1569"
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'Origin': 'https://huitru.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://huitru.com/11-caminos/1607-yamani',
  'Accept-Language': 'es-ES,es;q=0.9',
  'Cookie': 'PHPSESSID=e2hb8lkfo2t9ehfs9etav5j0c6; _ga=GA1.2.243151964.1632087936; _gid=GA1.2.1153431520.1632087936; _gat=1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)