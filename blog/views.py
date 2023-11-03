from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
import bcrypt
from .models import Post,Accounts
from .forms import CommentForm,AccountsForm
from django.http import HttpResponse
import json
# Create your views here

def comments(request):
   
    return render(request,'test.html')



        
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    

def login(request):
    print(request)
    response = HttpResponse()
    if request.method == 'POST':
        account = Accounts.objects.get(username=request.POST['username'])
        #print(account.password.split("'")[1])
        #print(type(account.password))
        
        if bcrypt.checkpw(bytes(request.POST['password'],'utf-8'),bytes(account.password.split("'")[1],'utf-8')):
            print('Correct User')
            response.set_cookie('myblogapp',json.dumps({
                'username':account.username,
                'password':request.POST['password']
            }))
            
            #print(response.cookies)
        return render(request,'account.html',{})
    
    return render(request,'login.html',{})

def signup(request):
    if request.method == 'POST':
        password = bcrypt.hashpw( bytes(request.POST['password'],'utf-8'),bcrypt.gensalt(16))
        data = {
            'email':request.POST['email'],
            'username':request.POST['username'],
            'password':password,
            'name':request.POST['name']
        }
        account_form = AccountsForm(data)
        
        if account_form.is_valid():
            new_account = account_form.save(commit=False)
            new_account.save()
            return redirect('login')
        else:
            return render(request,'signup.html',{
                'error': 'Invalid form data'
            })
            
            
    return render(request,'signup.html',{})
    
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    print(request.POST)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        #------------------------
        if comment_form.is_valid():
            #---------------------
            new_comment = comment_form.save(commit=False)
            #---------------------
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request,template_name,{
        'post':post,
        'comments': comments,
        'new_comments': new_comment,
        'comment_form': comment_form
        })
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    
    def get_object(self, queryset=None):
       obj = super().get_object(queryset)
       return obj

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['comments'] = self.object.comments.all()
       #print(context['comments'])
       return context