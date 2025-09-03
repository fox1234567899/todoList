from django.views.generic import DeleteView,CreateView,UpdateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib import messages

from .models import MyPost
from django.shortcuts import render


class PostList(LoginRequiredMixin,ListView):
    model=MyPost
    context_object_name='posts'
    template_name = 'Post/postList.html'


    def get_queryset(self):
       return MyPost.objects.filter(user=self.request.user).order_by('-id')
    

class PostDetail(LoginRequiredMixin,DetailView):
    http_method_names=["get"]
    model=MyPost
    context_object_name='posts'
    template_name="Post/detail.html"

    def get_queryset(self):

        myQuery= super().get_queryset()
        return myQuery.filter(user=self.request.user)






class UpdatePost(LoginRequiredMixin,UpdateView):
    model=MyPost
    success_url=reverse_lazy('Post:list')
    fields=['title','description','image','time','checked']
    context_object_name = 'post'
    template_name="Post/edit.html" 


    def form_valid(self, form):
        messages.success(self.request,"The post was successfully updated")
        return super().form_valid(form)
    
    def get_queryset(self):

        myQuery= super().get_queryset()
        return myQuery.filter(user=self.request.user)


class CreatePost(LoginRequiredMixin,CreateView):
    model=MyPost
    fields=['title','description','image','time','checked']
    template_name="Post/postForm.html" 
    success_url=reverse_lazy('Post:list')
    

    def dispatch(self, request, *args, **kwargs):
        self.request=request
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        obj.save()
       
        
        return super().form_valid(form)
    
    def post(self,request,*args,**kwargs):
        from datetime import datetime
        checked_str = request.POST.get("checked")
        checked = True if checked_str in ["on", "1", "true"] else False
        time_str = request.POST.get("time", "").strip()
        time = None
        if time_str:
            time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M")
        post=MyPost.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            time=time,
            user=request.user,
            checked=checked,
        )
        return render(request, "Post/postList.html", {"posts": [post]},content_type="text/html",)



class DeletePost(LoginRequiredMixin,DeleteView):
    model=MyPost
    context_object_name='posts'
    success_url=reverse_lazy('Post:list')
    template_name="Post/delete.html"

    def form_valid(self, form):
        messages.success(self.request,"the Post deleted successfully")
        return super().form_valid(form)
    
    def get_queryset(self):
        myQuery=super().get_queryset()
        return myQuery.filter(user=self.request.user)
    

