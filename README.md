# CloudFlare-IP

CloudFlare-IP is a tool which aims to gather origin IP of the website protected by Cloudflare from the website's favicon icon using Shodan api

## Installation
- `git clone https://github.com/karma9874/CloudFlare-IP.git`

- `pip3 install -r requirements.txt`

- Shodan CLI with API key (**not** the free one)

- To install shodan :
``python3 -m easy_install shodan``,
``shodan init API_KEY ``  


## Usage
- `python3 cloudFlare-IP.py https://website.com/favicon.ico`


## Dependencies
* Python3
* base64
* datetime
* requests
* shodan
* mmh3
* socket

## Example
![Example usage](https://github.com/karma9874/CloudFlare-IP/blob/master/example.JPG "Example usage")
