# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.conf import settings

# 조건이 만족하면 자동으로 코드가 실행됨
# 인증이 완료되면 자동으로 토큰이 부여됨

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
