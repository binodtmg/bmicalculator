from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from useraccount.forms import CustomSignupForm, ProfileForm
from useraccount.models import Profile
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# def login_view(request):
#     form = AuthenticationForm(request.POST or None)
#     if request.POST:
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse("home:bmiform"))
#     context = {"form":form}
#     return render(request, "login.html", context)

class UserLogin(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["next"] = self.request.GET.get("next")
        return context
    
def user_profile(request):
    profilelist = Profile.objects.get(user=request.user)
    context = {"profile": profilelist }
    print(context)
    print(request.user.email)
    return render(request, "userprofile.html",context)
    




# def profile_create(request):
#     form = ProfileForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("user:profile"))
#     context = {"form":form}
#     return render(request, "profile_create.html", context)


def update_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile, )
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:profile"))
    context = {"form":form}
    return render(request, "updateprofile.html", context)

def signup_view(request):
    form = CustomSignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:login"))
    context = {"form":form}
    return render(request,"register.html", context)

def logout_request(request):
    logout(request)
    return HttpResponseRedirect("/user/login/")