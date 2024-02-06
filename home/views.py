from django.contrib.auth.models import User
from django.shortcuts import render, reverse, Http404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from home.models import BmiMeasurement
from home.forms import BmiForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def bmi(request):
#     return render(request, "base.html")


@login_required
def bmiuserlist(request):
    userlist = BmiMeasurement.objects.filter(user=request.user)
    # userlist = BmiMeasurement.objects.all()
    context = {"userlist": userlist}
    return render(request, "bmiuserlist.html", context)

@login_required
def bmiform(request):
    form = BmiForm(request.POST or None)
   
    if  request.POST:
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))

        bmi = round((weight/(height**2)), 2)

        if bmi < 18:
            message = "Underweight. Eat a variety of foods that give you the nutrition that your body needs."
        elif bmi > 18 and bmi < 24.9:
            message = "Congratulation! Your weight is normal.Keep it up."
        elif bmi > 25 and bmi < 29.9:
            message = "Overweight. Avoid junk food and do exercise regularly."
        elif bmi > 30:
            message = "Obese. Consult with doctor, avoid junk food and increase physical activities."
        
        if form.is_valid():
            bmis = form.save(commit=False)
            bmis.user = request.user
            bmis.bmi = bmi
            bmis.message = message
            bmis.save()
        context = {'bmi':bmi, 'message':message}
        return render(request, "form.html", context)
    context = {"form":form}
    return render(request, "form.html", context)



@login_required
def bmi_edit(request, id):
    # try:
    #     bmis = BmiMeasurement.objects.get(id=id)
    # except BmiMeasurement.DoesNotExist:
    #     raise Http404("No object found.")
    bmi = get_object_or_404(BmiMeasurement, id=id)
    form = BmiForm(request.POST or None, instance=bmi)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("home:bmiuserlist"))
    context = {"form": form}
    return render(request, "form.html", context)

@login_required
def bmi_delete(request, id):
    bmi = get_object_or_404(BmiMeasurement, id=id)
    bmi.delete()
    return HttpResponseRedirect(reverse("home:bmiuserlist"))

@login_required
def send_confirm_email(request):
    send_bmi = round(BmiMeasurement.objects.filter(user=request.user).last().bmi, 2)
    send_mgs = BmiMeasurement.objects.filter(user=request.user).last().message
    subject = "Bmi Message"
    message = "Your Bmi is " + str(send_bmi)+"kg/m2 ." + str(send_mgs) 
    from_email = "herotamang245@gmail.com"
    recipient_list = [
                    request.user.profile.email,
        ]
    res = send_mail(subject, message, from_email, recipient_list)
    return render(request, "success.html")
    # return HttpResponse(res)
