# This app is vulnerable to reflected XSS

## How to run:
- git clone https://github.com/ScottNeaves/refl-xss-vuln
- cd refl-xss-vuln
- docker-compose build
- docker-compose up
- curl 127.0.0.1:5000/hello?greeting=your_greeting

### spoiler!
The attack string is "PHM8c2NyaXB0PmNyaXB0PmFsZXJ0KDEpPC9zPC9zY3JpcHQ%2BY3JpcHQ%2B", which is the url-encoded b64-encoded version of this: "<s<script>cript>alert(1)</s</script>cript>"

Note: another way to bypass chrome's XSS protections would have been just to pass the X-XSS-Protection header with a value of 0: https://stackoverflow.com/questions/43249998/chrome-err-blocked-by-xss-auditor-details
