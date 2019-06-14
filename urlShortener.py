from pyshorteners import Shortener

class Shortening: 
    def __init__(self):
        self.shortener = Shortener('Tinyurl')

    def shortenURL(self):
        self.url = input("Enter URL to shorten: ")
        shortURL = self.shortener.short(self.url)
        print("The shortened URL is: " + shortURL)

    def decodeURL(self):
        self.url = input("Enter URL to expand: ")
        expandURL = self.shortener.expand(self.url)
        print("The expanded URL is: " + expandURL)

app = Shortening()
app.shortenURL()
app.decodeURL()