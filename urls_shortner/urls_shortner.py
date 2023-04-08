import pyshorteners

# urls = input("")
#
# short_urls = pyshorteners.Shortener()
#
# short_url = short_urls.tinyurl.short(urls)
# print("The Shortened URL is: " + short_url)


original_url = input("Enter the URL to shorten: ")
#Bitly shortener
type_bitly = pyshorteners.Shortener(api_key='bb6148cfc329e4a0d3c1445064e4743ae8057a3c')
short_url = type_bitly.bitly.short(original_url)
print("The Shortened URL is: " + short_url)