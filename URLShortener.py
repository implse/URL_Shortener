import random
import string

class URL_shortener:
  def __init__(self):
    self.short_to_url = {}
    self.url_to_short = {}

  def _generate_short(self):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

  def _generate_unused_short(self):
    t = self._generate_short()
    while t in self.short_to_url:
      t = self._generate_short()
    return t

  def shorten(self, url):
    if url in self.url_to_short:
      return self.url_to_short[url]
    else:
      short = self._generate_unused_short()
      self.short_to_url[short] = url
      self.url_to_short[url] = short
    return short

  def restore(self, short):
    return self.short_to_url.get(short, None)

# Test
url = URL_shortener()

# Shorten URL
url_short = url.shorten("https://github.com/implse")
print(url_short)

# Restore URL
url_restore = url.restore(url_short)
print(url_restore)

# Shorten same URL twice(re-use)
print(url.shorten("https://github.com/implse"))
