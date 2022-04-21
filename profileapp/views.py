from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def home(request):
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ProfileForm()
    img=Profile.objects.all()
    return render(request,'home.html',{'form':form})


def update(request):
    return render(request,"updated.html")

# def updateview(request, id):
#     data = Breath_timeset.objects.get(id=id)
#     if request.method == 'POST':
#         data.time = request.POST.get('time', data.time)
#         data.title = request.POST.get('title', data.title)
#         data.save()
#         return redirect('ts-home')
#     return render(request, 'AAdmin/edit-breathtime.html', {'data': data})

# def user_profile(request, id):
#     data = MyUser.objects.get(id=id)
#     return render(request, 'AAdmin/my-profile.html', {'i': data})


# def update_User(request, pk):
#     print(pk, request.POST)

#     data = MyUser.objects.get(id=pk)
#     s = str(data.date_of_birth)  # 'April 24, 2020'
#     # print(parser.parse(s))
#     data.date_of_birth = s

#     if request.method == 'POST':
#         data.full_name = request.POST.get('full_name', data.full_name)

#         data.date_of_birth = request.POST.get('date_of_birth', data.date_of_birth)
#         print(request.POST['date_of_birth'])
#         data.email = request.POST.get('email', data.email)
#         data.phone = request.POST.get('phone', data.phone)
#         data.profile_pic = request.FILES.get('file', data.profile_pic)
#         old_password = request.POST.get('old-password', None)
#         print(old_password)

        
#         data.save()
#         messages.success(request, "Profile Successfully Updated")
#         return redirect('adminuser:my-profile', data.id)
#     return render(request, 'AAdmin/edit-my-profile.html', {"data": data})
