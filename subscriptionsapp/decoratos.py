from django.shortcuts import redirect
from django.utils.timezone import now
from django.urls import reverse
from functools import wraps
from subscriptionsapp.models import Subscription

def subscription_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Jika pengguna tidak login, redirect ke halaman login
        if not request.user.is_authenticated:
            return redirect('account_login')
        
        try:
            # Periksa apakah pengguna memiliki langganan aktif
            subscription = Subscription.objects.filter(
                user=request.user, 
                status='active', 
                end_date__gt=now()
            ).first()

            if subscription:
                # Langganan aktif ditemukan
                if request.path == reverse('landingPage'):  # Cek jika pengguna berada di landingPage
                    return redirect('beranda')  # Redirect ke beranda
                return view_func(request, *args, **kwargs)  # Lanjutkan ke view aslinya
            else:
                # Tidak ada langganan aktif
                if request.path == reverse('landingPage'):
                    return view_func(request, *args, **kwargs)  # Izinkan akses ke landingPage
                return redirect('landingPage')  # Redirect ke landingPage
        except Exception as e:
            print(f"Error: {e}")
        
        # Redirect default jika terjadi kesalahan
        return redirect('landingPage')
    return wrapper
