from requests_html import HTMLSession

url = 'https://news.google.com/rss/search?q=lockdown'

s = HTMLSession()

r = s.get(url)

print(r.html.html)

