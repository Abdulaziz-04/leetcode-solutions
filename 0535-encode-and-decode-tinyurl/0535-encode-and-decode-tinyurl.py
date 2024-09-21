class Codec:
    def __init__(self):
        self.map={}

    def encode(self, longUrl: str) -> str:
        shortUrl=hash(longUrl)
        self.map[shortUrl]=longUrl
        return shortUrl
        """Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        return self.map[shortUrl]
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))