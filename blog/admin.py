from django.contrib import admin
from .models import Post,Comment,Accounts
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {
        'slug':('title',)
    }



admin.site.register(Post,PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on','active')
    list_filter = ('active','created_on')
    search_fields = ('name','email','body')
    actions = ['approve_comments','disapprove_comments']
    
    def approve_comments(self,request,queryset):
        queryset.update(active=True)
    def disapprove_comments(self,request,queryset):
        queryset.update(active=False)
        

        
@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('name','username','created_on')
    list_filter = ('account_status','created_on')
    search_fields = ('name','username')
    actions = ['activate','deactivate']
    
    def activate(self,request,queryset):
        queryset.update(account_status=True)
        
    def deactivate(self,request,queryset):
        queryset.update(account_status=False)
        