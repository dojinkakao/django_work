from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import BlogPost

class IndexView(ListView):
  # index.htmlをレンダリングする
  template_name = 'index.html'
  # object_listキーの別名を設定
  context_object_name = 'orderby_records'
  # モデルBlogPostのオブジェクトにorder_by()を適用して
  # BlogPostのレコードを投稿日時の降順で並べ替える
  queryset = BlogPost.objects.order_by('-posted_at')
  # 1ページに表示するレコード件数を設定
  paginate_by = 4


class BlogDetail(DetailView):
  template_name = 'post.html'
  
  model = BlogPost