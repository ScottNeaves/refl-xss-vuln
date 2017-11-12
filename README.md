# This app is vulnerable to reflected XSS

## How to run:
- git clone https://github.com/ScottNeaves/refl-xss-vuln
- cd refl-xss-vuln
- docker-compose build
- docker-compose up
- curl 127.0.0.1:5000/hello?greeting=your_greeting
