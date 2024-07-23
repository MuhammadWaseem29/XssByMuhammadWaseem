# XSS By Muhammad Waseem

A sophisticated XSS scanning tool to find cross-site scripting vulnerabilities, inspired by XSS-Strike.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/XssByMuhammadWaseem.git
    cd XssByMuhammadWaseem
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Scanning URLs from a file:
    ```bash
    python3 xss_by_muhammad_waseem.py -f <filename> -o <output>
    ```

### Scanning a single URL:
    ```bash
    python3 xss_by_muhammad_waseem.py -u http://example.com/hpp/?pp=12 -o out.txt
    ```

### Using custom headers:
    ```bash
    python3 xss_by_muhammad_waseem.py -f urls.txt -H "Cookies:test=123;id=asdasd, User-Agent: Mozilla/Firefox" -t 7 -o result.txt
    ```

### Using PIPE:
    ```bash
    cat katana.txt | python3 xss_by_muhammad_waseem.py --pipe -t 7 -o result.txt
    ```

### Crawl and Scan:
    ```bash
    python3 xss_by_muhammad_waseem.py -u http://example.com/hpp/?pp=12 -o out.txt --crawl
    ```

## Arguments

- `-f`, `--file`: Filename that contains a bunch of links.
- `-o`, `--output`: Output filename in which all the vulnerable endpoints are stored.
- `-t`, `--threads`: Number of threads (Max: 10).
- `-u`, `--url`: Single URL to scan.
- `-H`, `--headers`: Custom headers (Use "," within "" to add multiple headers).
- `--crawl`: Crawl the links first and then find XSS.
- `--pipe`: Use PIPE to input URLs.

## Examples

### Using multiple headers:
    ```bash
    python3 xss_by_muhammad_waseem.py -f urls.txt -H "Cookies:test=123;id=asdasd, User-Agent: Mozilla/Firefox" -t 7 -o result.txt
    ```

### Using a single header:
    ```bash
    python3 xss_by_muhammad_waseem.py -f urls.txt -H "Cookies:test=123;id=asdasd" -t 7 -o result.txt
    ```

### Scanning a single URL:
    ```bash
    python3 xss_by_muhammad_waseem.py -u http://example.com/hpp/?pp=12 -o out.txt
    ```

### Crawl and scan:
    ```bash
    python3 xss_by_muhammad_waseem.py -u http://example.com/hpp/?pp=12 -o out.txt --crawl
    ```

### Using PIPE:
    ```bash
    cat katana.txt | python3 xss_by_muhammad_waseem.py --pipe -t 7 -o result.txt
    ```

## License

This project is licensed under the MIT License.
