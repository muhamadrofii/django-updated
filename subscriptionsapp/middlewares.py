from django.shortcuts import redirect
from django.utils.timezone import now

class RedirectOnSubscriptionMiddleware:
    """
    Middleware untuk mengarahkan pengguna ke beranda jika langganan aktif,
    atau ke landing page jika belum berlangganan.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Periksa apakah pengguna sudah login
        if request.user.is_authenticated:
            try:
                # Ambil langganan pengguna
                subscription = request.user.subscription  # Asumsikan ada relasi OneToOneField
                if subscription.is_active():  # Langganan aktif
                    # Jika pengguna mencoba mengakses landing page, arahkan ke beranda
                    if request.path == '/landingpage/':
                        return redirect('beranda')  # Ganti 'home' dengan nama URL beranda
                else:
                    # Jika langganan tidak aktif, arahkan ke landing page
                    if request.path != '/landing/':
                        return redirect('landingPage')  # Ganti 'landing' dengan nama URL landing page
            except:
                # Jika pengguna tidak memiliki langganan, arahkan ke landing page
                if request.path != '/landing/':
                    return redirect('landingPage')

        # Jika pengguna belum login atau tidak perlu diarahkan
        response = self.get_response(request)
        return response
