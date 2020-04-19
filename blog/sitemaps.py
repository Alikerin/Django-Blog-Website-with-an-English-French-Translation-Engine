# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-03-21T12:48:26+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-03-21T12:48:28+02:00
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on
