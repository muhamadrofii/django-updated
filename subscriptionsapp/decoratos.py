from django.shortcuts import redirect
from django.utils.timezone import now
from django.urls import reverse
from functools import wraps
from subscriptionsapp.models import Subscription

def subscription_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect ke login jika belum login
        
        try:
            # Query langsung ke tabel Subscription
            subscription = Subscription.objects.filter(
                user=request.user, 
                status='active', 
                end_date__gt=now()  # Langganan harus belum kedaluwarsa
            ).first()

            if subscription:
                # Langganan aktif ditemukan, redirect ke beranda jika sedang mencoba akses `landingPage`
                print(f"User: {request.user}, Subscription Plan: {subscription.plan}, Status: {subscription.status}")
                # if request.path == '/landingpage/':  # Pastikan ini sesuai URL `landingPage`
                if request.path == reverse('landingPage'):
                    return redirect('beranda')
                return view_func(request, *args, **kwargs)
            else:
                print(f"User: {request.user}, Subscription: None or Inactive")
        except Exception as e:
            print(f"Error: {e}")
        
        # Redirect ke landing page jika tidak ada langganan aktif
        return redirect('landingPage')
    return wrapper
