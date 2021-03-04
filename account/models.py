from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CatkinUser(AbstractBaseUser):
    class Used(models.TextChoices):
        Y = 'Y'
        N = 'N'

    class Status(models.TextChoices):
        ACT = 'act', '사용중'
        DEL = 'del', '탈퇴'
        REST = 'rest', '휴면'
        STOP = 'stop', '중지'

    email = models.EmailField(max_length=255, verbose_name='이메일')
    date_of_birth = models.DateField(default=None, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, verbose_name='매니저')
    is_superuser = models.BooleanField(default=False, verbose_name='관리자')
    username = models.CharField(max_length=30, unique=True, verbose_name='아이디')
    name = models.CharField(max_length=40, verbose_name='이름')
    post_code = models.CharField(max_length=50, null=True, blank=True,
                                 verbose_name='우편번호')
    address1 = models.CharField(max_length=150, null=True, blank=True,
                                verbose_name='주소1')
    address2 = models.CharField(max_length=150, null=True, blank=True,
                                verbose_name='주소2')
    phone = models.CharField(max_length=50, verbose_name='전화번호')
    status = models.CharField(max_length=10, choices=Status.choices,
                              verbose_name='사용자상태')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='로그인')
    password_at = models.DateTimeField(null=True, blank=True,
                                       verbose_name='비밀번호 수정일')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = '회원정보'
        verbose_name_plural = verbose_name
        ordering = ('-id',)
