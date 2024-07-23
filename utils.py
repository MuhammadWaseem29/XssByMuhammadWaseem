import requests
from bs4 import BeautifulSoup

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        payloads = [line.strip() for line in file]
    return payloads

def extract_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    return forms

def submit_form(form, url, payload, headers=None):
    action = form.get('action')
    method = form.get('method', 'get').lower()
    inputs = form.find_all('input')

    data = {}
    for input_tag in inputs:
        name = input_tag.get('name')
        if name:
            data[name] = payload

    if method == 'post':
        return requests.post(url + action, data=data, headers=headers)
    else:
        return requests.get(url + action, params=data, headers=headers)

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links
