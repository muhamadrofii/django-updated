from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ProfileParent, ProfileChild

# @receiver(post_save, sender=User)
# def create_or_update_profile(sender, instance, created, **kwargs):
#     if created:
#         # Jika user baru dibuat, buat ProfileParent yang terhubung
#         ProfileParent.objects.create(user=instance, email=instance.email)
#     else:
#         # Jika user diperbarui, sinkronkan data profil (opsional)
#         profile = ProfileParent.objects.filter(user=instance).first()
#         if profile:
#             profile.email = instance.email  # Sinkronisasi email jika diperbarui
#             profile.save()

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Jika user baru dibuat, buat ProfileParent yang terhubung
        profile_parent = ProfileParent.objects.create(user=instance, email=instance.email)
        
        # Buat ProfileChild kosong yang terhubung dengan ProfileParent yang baru
        ProfileChild.objects.create(parent=profile_parent)
    else:
        # Jika user diperbarui, sinkronkan data profil (opsional)
        profile_parent = ProfileParent.objects.filter(user=instance).first()
        if profile_parent:
            profile_parent.email = instance.email  # Sinkronisasi email jika diperbarui
            profile_parent.save()

            # Periksa atau perbarui ProfileChild yang terkait dengan ProfileParent
            profile_child = ProfileChild.objects.filter(parent=profile_parent).first()
            if profile_child:
                # Tidak ada perubahan pada ProfileChild karena data kosong
                profile_child.save()