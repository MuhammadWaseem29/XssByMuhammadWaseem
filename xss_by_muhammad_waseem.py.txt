import argparse
import requests
from concurrent.futures import ThreadPoolExecutor
from utils import load_payloads, extract_forms, submit_form, extract_links

def scan_url(url, payloads, headers):
    forms = extract_forms(url)
    vulnerabilities = []
    for form in forms:
        for payload in payloads:
            response = submit_form(form, url, payload, headers)
            if payload in response.text:
                vulnerabilities.append((url, payload))
                print(f"Vulnerability found at {url} with payload: {payload}")
    return vulnerabilities

def scan_urls(urls, payloads, headers, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda url: scan_url(url, payloads, headers), urls)
    return [item for sublist in results for item in sublist]

def crawl_and_scan(url, payloads, headers, threads):
    links = extract_links(url)
    return scan_urls(links, payloads, headers, threads)

def main():
    parser = argparse.ArgumentParser(description='XSS By Muhammad Waseem')
    parser.add_argument('-f', '--file', type=str, help='Filename that contains bunch of links')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output filename in which all the vulnerable endpoints are stored')
    parser.add_argument('-t', '--threads', type=int, default=1, help='Number of threads (Max: 10)')
    parser.add_argument('-u', '--url', type=str, help='Single URL to scan')
    parser.add_argument('-H', '--headers', type=str, help='Custom headers (Use "," within "" to add multiple headers)')
    parser.add_argument('--crawl', action='store_true', help='Crawl the links first and then find XSS')
    parser.add_argument('--pipe', action='store_true', help='Use PIPE to input URLs')

    args = parser.parse_args()

    headers = {}
    if args.headers:
        headers_list = args.headers.split(',')
        for header in headers_list:
            key, value = header.split(':')
            headers[key.strip()] = value.strip()

    payloads = load_payloads('payloads.txt')
    vulnerabilities = []

    if args.url:
        if args.crawl:
            vulnerabilities = crawl_and_scan(args.url, payloads, headers, args.threads)
        else:
            vulnerabilities = scan_url(args.url, payloads, headers)
    elif args.file:
        with open(args.file, 'r') as file:
            urls = [line.strip() for line in file]
        vulnerabilities = scan_urls(urls, payloads, headers, args.threads)
    elif args.pipe:
        import sys
        urls = [line.strip() for line in sys.stdin]
        vulnerabilities = scan_urls(urls, payloads, headers, args.threads)

    with open(args.output, 'w') as output_file:
        for url, payload in vulnerabilities:
            output_file.write(f"{url} is vulnerable with payload: {payload}\n")

if __name__ == "__main__":
    main()
