from django.shortcuts import render
from django.views import generic
from .models import Post,Comment
# Create your views here.

def comments(request):
   
    return render(request,'test.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    
    def get_object(self, queryset=None):
       obj = super().get_object(queryset)
       return obj

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['comments'] = self.object.comments.all()
       print(context['comments'])
       return context