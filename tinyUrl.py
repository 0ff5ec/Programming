# _*_ coding = utf-8 _*_
'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''
import base64
class Codec:

    def encode(self, longUrl):
        return "http://tinyurl.com/" + base64.b32encode(longUrl)
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        return base64.b32decode(shortUrl.split('/')[-1])
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """

if __name__ == "__main__":
	codec = Codec()
	print(codec.decode(codec.encode('https://google.com')))
