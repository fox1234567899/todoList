from django.views.generic import TemplateView,FormView,View
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import SignUpForm,UpdateProfile,UserUpdate
from django.contrib.auth import login
from django.shortcuts import render,redirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile







class Homepage(TemplateView):

    template_name="home.html"



class SignUp(FormView):
    template_name="signup.html"
    form_class=SignUpForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('myapp:login')

    def form_valid(self, form):
        user=form.save()
        if user:
            login(self.request,user)
        return super(SignUp,self).form_valid(form)
    
    
    


  
class LoginPage(LoginView):
    template_name="login.html"
    redirect_authenticated_user=True

    def get_success_url(self):
        
        return "/"
    


    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return render(self.request,self.template_name,{"form":form})
        
        
    

class ProfilePage(LoginRequiredMixin,View):
    def get(self,request):
        userForm=UserUpdate(instance=request.user)
        profileForm=UpdateProfile(instance=request.user.profile)

        context={
            "userForm":userForm,
            "profileForm":profileForm,

        }

        return render(request,'profile.html',context)
    
    def post(self,request):
        userForm=UserUpdate(request.POST,instance=request.user)
        profileForm=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request,'Your profile has been changed successfully')
            return redirect('myapp:profile')
        else:
            context={
                    'userForm':userForm,
                    'profileForm':profileForm,
            }
            messages.error(request,'error cant update your profile')
            return render(request,'profile.html',context)