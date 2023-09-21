from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Image,offrefield,bangalo,Own_Message
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login

def home(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('second')
        else:
            return render(request, 'ocp.html')
    else:
        return render(request, 'ocp.html')
    

alba = 0
def second(request):
    try:
        user_profile = Image.objects.get(Image_RELATION=request.user)
    except Image.DoesNotExist:
        user_profile = None
    images_offres = offrefield.objects.all()
    image_bangalo = bangalo.objects.all()
    if request.method == 'POST':
        try:
            input = request.POST['input']  
            request.session['variable'] = input
        except:
            input = None     
        if input is not None:
            return redirect('Third')
        try:
            Home = request.POST['Home']
        except:
            Home = None
        try:
            Message =request.POST['Message']
        except:
            Message = None
        if Home is not None:
            return redirect('second')
        if Message is not None:
            return redirect('Message')
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            if user_profile:
                user_profile.delete()
            image = form.save(commit=False)
            image.Image_RELATION = request.user
            image.save()
            return redirect('second')
        
    else:
        form = ImageForm()
        image_bangalo_recherché="halla"
    return render(request, 'secondary.html', {'form': form, 'image': user_profile,'images_offres':images_offres,'image_bangalo':image_bangalo,'image_bangalo_recherch':image_bangalo_recherché})

def Message(request):
    Usere = User.objects.all() 
    Useres = User.objects.all()
    try:
        user_profile = Image.objects.get(Image_RELATION=request.user)
    except Image.DoesNotExist:
        user_profile = None
    chosen_user = None
    chosen_user = request.session.get('chosen_user')
    alba = "po"
    chosen = None
    ID = request.session.get('chosen')
    chosen = Image.objects.get(id=ID)
    for user in Useres:
        try:
            choosed = request.POST[user.username]
        except:
            choosed = None
        if choosed is not None:
            chosen_user = user.username
            chosen = Image.objects.get(Image_RELATION=user)
            request.session["chosen"] = chosen.id
            alba = user.username
            request.session["chosen_user"] = chosen_user
            request.session['alba'] = user.username
    try:
        messages = request.POST['messages']
    except:
        messages = None
    useer_destination = request.session.get('alba')
    if messages and useer_destination is not None:
        print("!!!!!!!!",useer_destination)
        message = Own_Message(Message_RELATION=request.user, Message=messages,lmoursil =str(request.user),lmousta9bil=useer_destination)
        message.save()
        print("!!!!!!!!!",message.Message)
    les_messagages = Own_Message.objects.all()
    l,B = [],[]
    dicsution = []
    for messag in les_messagages:
        if messag.lmoursil == str(request.user) and messag.lmousta9bil == useer_destination:
            dicsution.append(messag)
        if messag.lmoursil == useer_destination and messag.lmousta9bil == str(request.user):
            dicsution.append(messag)
    for dic in dicsution:
        print(dic.Message,dic.id)
    user_name = str(request.user)
    user_other = useer_destination
    return render(request,'message.html',{'chosen':chosen,'image': user_profile,'User':Usere,'chosen_user':chosen_user,'discution':dicsution,'user_name':user_name,'user_other':user_other})



def Third(request):
    image_bangalo = bangalo.objects.all()
    input = request.session.get('variable')
    print(input)
    image_bangalo_recherché = "dari"
    for img in image_bangalo:
        if img.ville == input:
            image_bangalo_recherché = img
            print(image_bangalo_recherché)  

    try:
        user_profile = Image.objects.get(Image_RELATION=request.user)
    except Image.DoesNotExist:
        user_profile = None
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            if user_profile:
                user_profile.delete()
            image = form.save(commit=False)
            image.Image_RELATION = request.user
            image.save()
    else:
        form = ImageForm()
    return render(request,'Third.html',{'form': form,'image': user_profile,'image_bangalo_recherch':image_bangalo_recherché})


# alba = input
            





# # Create your views here.
# class ArticleForm(forms.ModelForm):
#     image = forms.ImageField() 
#     class Meta:
#         model = Image
#         fields = '__all__'

# # # Create your views here.
# # def second(request):
# #     if request == 'POST':
# #         image = Image.objects.first()
# #         if image:
# #             image.delete()
# #         form = ArticleForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             return render(request, "secondary.html")
# #     else:
# #         images = Image.objects.first()
# #         print(images)
# #         form = ArticleForm()
# #     return render(request, 'secondary.html', {'form': form,'images':images})




