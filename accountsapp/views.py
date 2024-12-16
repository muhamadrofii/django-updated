from django.shortcuts import render, redirect
from .models import ProfileParent
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, detailForm
import os
# from django.shortcuts import render
from subscriptionsapp.decoratos import subscription_required

from django.conf import settings
# ProfileForm
from .models import ProfileParent, ProfileChild

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'signUp.html')

# @login_required
# def profil(request):



#     user = request.user
#     try:
#         profil = ProfileParent.objects.get(user=user) 
#         profil_child = ProfileChild.objects.get(parent=profil)  # Menarik data anak dari orang tua
 
#         fullname = f"{profil.user.first_name} {profil.user.last_name}".strip()
#         current_avatar = profil.avatar if profil else None
#     except ProfileParent.DoesNotExist:
#         ()

#     if request.method == 'POST':
#         # Form untuk User dan Profile
#         user_form = UserForm(request.POST, instance=user)
#         profile_form = ProfileForm(request.POST, request.FILES, instance=profil)

#         fullname = request.POST.get('fullname', '')
#         if fullname:
#             first_name, last_name = fullname.split(' ', 1) if ' ' in fullname else (fullname, '')
#             user.first_name = first_name
#             user.last_name = last_name
#             user.save()  # Save the updated user info


#             if profil:
#                 profil.save()

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()  # Simpan data User
#             profile = profile_form.save()


#             if profile.avatar:
#                 print(f"Avatar berhasil di-upload: {profile.avatar.url}")
            
#             return redirect('profil') 
#     else:

#         user_form = UserForm(instance=user)


#         profile_form = ProfileForm(instance=profil)


#     avatar_dir = os.path.join(settings.MEDIA_ROOT, 'avatar')
#     avatars = []
#     if os.path.exists(avatar_dir):
#         avatars = [f for f in os.listdir(avatar_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

#     if request.method == 'POST':

#         avatar_name = request.POST.get('avatar')
#         if avatar_name:

#             if profil:
#                 profil.avatar = 'avatar/' + avatar_name  # Pastikan atribut avatar sesuai dengan model Anda
#                 profil.save()
#                 print(f"Avatar berhasil diperbarui: {profil.avatar}")
#             else:

#                 profil = ProfileParent.objects.create(user=user, avatar='avatar/' + avatar_name)
#             return redirect('profil')  # Redirect setelah avatar disimpan



#     return render(request, 'profil.html', {
#         'user_form': user_form,
#         'fullname': fullname,
#         'profil_child': profil_child,
#         'profil': profil,
#         'avatars': avatars,
#         'current_avatar': current_avatar,
#     })

@login_required
def profil(request):
    user = request.user

    # Ambil atau buat profil orang tua
    profil, created = ProfileParent.objects.get_or_create(user=user)
    profil_child = ProfileChild.objects.filter(parent=profil).first()  # Ambil anak pertama jika ada

    # Default untuk avatar dan nama lengkap
    fullname = f"{profil.user.first_name} {profil.user.last_name}".strip()
    current_avatar = profil.avatar if profil.avatar else None

    if request.method == 'POST':
        # Form untuk User dan Profile
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profil)

        # Update nama lengkap (fullname)
        fullname = request.POST.get('fullname', '')
        if fullname:
            first_name, last_name = fullname.split(' ', 1) if ' ' in fullname else (fullname, '')
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        # Simpan data form jika valid
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save()

            # Log avatar jika ada
            if profile.avatar:
                print(f"Avatar berhasil di-upload: {profile.avatar.url}")
            
            return redirect('profil')

        # Perbarui avatar berdasarkan pilihan
        avatar_name = request.POST.get('avatar')
        if avatar_name:
            profil.avatar = f'avatar/{avatar_name}'  # Pastikan path sesuai
            profil.save()
            print(f"Avatar berhasil diperbarui: {profil.avatar}")
            return redirect('profil')

    else:
        # GET request: inisialisasi form dengan instance
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profil)

    # Ambil daftar avatar yang tersedia
    avatar_dir = os.path.join(settings.MEDIA_ROOT, 'avatar')
    avatars = [f for f in os.listdir(avatar_dir) if f.endswith(('.png', '.jpg', '.jpeg'))] if os.path.exists(avatar_dir) else []

    # Render halaman profil
    return render(request, 'profil.html', {
        'user_form': user_form,
        'fullname': fullname,
        'profil_child': profil_child,
        'profil': profil,
        'avatars': avatars,
        'current_avatar': current_avatar,
    })

    # context = {
    #     'user_form': user_form,
    #     'profile_form': profile_form,
    #     'fullname': fullname,
    #     'profil': profil,
    #     'profil_child': profil_child,
    #     'current_avatar': current_avatar,
    # }

    # return render(request, 'profil.html', context)


    # try:
    #     profile = ProfileParent.objects.get(user=request.user)
    # except ProfileParent.DoesNotExist:
    #     raise Http404("Profil tidak ditemukan")
    # return render(request, 'profile.html', {'profile': profile})

# from .decorators import redirect_based_on_subscription
@subscription_required
def beranda(request):
    return render(request, 'beranda.html')

@subscription_required
def landingPage(request):
    return render(request, 'landingPage.html')