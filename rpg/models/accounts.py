from django.db import models
from django.db.models import Model
from django.db.models.fields import (
    CharField,
    IntegerField,
    EmailField,
    DateField,
    AutoField,
    DecimalField,
    TimeField,
    TextField,
    BooleanField,
    NullBooleanField,
    DateTimeField
)
from django.contrib.auth.models import (
    User,
    AbstractUser,
    PermissionsMixin,
    BaseUserManager
)


class Account(Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Accounts'

    id = AutoField(primary_key=True)
    label = CharField(max_length=25, null=False)
    active = BooleanField(default=True)

    @staticmethod
    def construct(label):
        return Account.objects.create(label=label)


class Profile(Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Profiles'

    user = models.ForeignKey(User, unique=True)
    account = models.ForeignKey(Account)
    token = CharField(max_length=32, blank=True, db_index=True, unique=True)
    token_expires = DateTimeField(auto_now=False, auto_now_add=False, null=True)


    # @staticmethod
    # def lookup(username, password=None):
    #     from django.contrib.auth import authenticate

    @staticmethod
    def construct(username, password, account=None):
        user = User()
        user.username = username
        user.set_password(password)
        user.save()

        if account is None:
            account = Account.construct("MY USER ACCOUNT")

        profile = Profile.objects.create(
            user=user,
            account=account
        )

        return profile



#
# # from django.utils import timezone
# # from django.utils.http import urlquote
# # from django.core.mail import send_mail
# # from django.contrib.auth.models import (
# #     BaseUserManager, PermissionsMixin, AbstractBaseUser
# # )
# # from django.utils.translation import ugettext_lazy as _
# # from django.conf import settings
# #
# # from Crypto.Cipher import Blowfish
# # import binascii
# #
# #
# # class BalanceUserManager(BaseUserManager):
# #
# #     def _create_user(self, email, password,
# #                      is_staff, is_superuser, **extra_fields
# #     ):
# #         now = timezone.now()
# #         if not email:
# #             raise ValueError("Users must have an email address")
# #         if not password:
# #             raise ValueError("Users must have a password")
# #         email = self.normalize_email(email)
# #         user = self.model(email=email,
# #                           is_staff=is_staff, is_active=True,
# #                           is_superuser=is_superuser, last_login=now,
# #                           date_joined=now, **extra_fields
# #         )
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
# #
# #     def create_user(self, email, password, **extra_fields):
# #         return self._create_user(email, password, False, False,
# #                                  **extra_fields
# #         )
# #
# #     def create_superuser(self, email, password, **extra_fields):
# #         return self._create_user(email, password, True, True,
# #                                  **extra_fields
# #         )
# #
# #
# # class BalanceUser(AbstractBaseUser, PermissionsMixin):
# #
# #     STATE_CHOICES = (
# #         ("UT", "Utah"),
# #     )
# #
# #     email = models.EmailField(
# #         _('email address'), max_length=255,
# #         unique=True, db_index=True
# #     )
# #     first_name = models.CharField(_('first name'), max_length=30, blank=True)
# #     last_name = models.CharField(_('last name'), max_length=30, blank=True)
# #     is_staff = models.BooleanField(_('staff status'), default=False,
# #                                    help_text=_('Designates whether the user can log into this admin '
# #                                                'site.'))
# #     is_active = models.BooleanField(_('active'), default=False,
# #                                     help_text=_('Designates whether this user should be treated as '
# #                                                 'active. Unselect this instead of deleting accounts.'))
# #     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
# #
# #     consent_to_email_contact = models.BooleanField(_("accepts email"),
# #                                                    default=False,
# #                                                    )
# #     consent_to_phone_contact = models.BooleanField(_("accepts phone calls"),
# #                                                    default=False,
# #                                                    )
# #     address_one = models.CharField(_("address line one"), max_length=255, blank=True)
# #     address_two = models.CharField(_("address line two"), max_length=255, blank=True)
# #     city = models.CharField(_("city"), max_length=50, blank=True)
# #     state = models.CharField(
# #         _("state"),
# #         max_length=2,
# #         choices=STATE_CHOICES,
# #         blank=True,
# #         )
# #     zip_code = models.CharField(_("zip code"), max_length=10, blank=True)
# #     home_phone = models.CharField(_("home phone"), max_length=14, blank=True)
# #     cell_phone = models.CharField(_("cell phone"), max_length=14, blank=True)
# #     ssn_last_four =models.CharField(max_length=32,
# #                                     verbose_name=_("Last 4 digits in social security nubmer"),
# #                                     blank=True,
# #                                     )
# #     dob = models.DateField(verbose_name=_("Date of Birth"), blank=True, null=True)
# #     dl_number = models.CharField(verbose_name=_("Driving license number"),
# #                                  max_length=32,
# #                                  blank=True,
# #                                  )
# #     dl_state = models.CharField(
# #         max_length=2,
# #         verbose_name=_("State that issued the driving license"),
# #         choices=STATE_CHOICES,
# #         blank=True,
# #         )
# #     activation_token = models.CharField(
# #         max_length=36,
# #         blank=True,
# #         )
# #     reset_token = models.CharField(
# #         max_length=36,
# #         blank=True,
# #         )
# #
# #     backend = "django.contrib.auth.backends.ModelBackend"
# #     USERNAME_FIELD = "email"
# #     REQUIRED_FIELDS = []
# #     objects = BalanceUserManager()
# #
# #     class Meta:
# #         verbose_name = _('user')
# #         verbose_name_plural = _('users')
# #
# #     def get_absolute_url(self):
# #         return "/users/%s/" % urlquote(self.email)
# #
# #     def get_full_name(self):
# #         """
# #         Returns the first_name plus the last_name, with a space in between.
# #         """
# #         full_name = '%s %s' % (self.first_name, self.last_name)
# #         return full_name.strip()
# #
# #     def get_short_name(self):
# #         "Returns the short name for the user."
# #         return self.first_name
# #
# #     def email_user(self, subject, message, from_email=None):
# #         """
# #         Sends an email to this User.
# #         """
# #         send_mail(subject, message, from_email, [self.email])
# #
# #     def _get_dl_number(self):
# #         enc_obj = Blowfish.new(settings.SECRET_KEY)
# #         return u"%s" % enc_obj.decrypt(binascii.a2b_hex(self.dl_number)).rstrip()
# #
# #     def _set_dl_number(self, value):
# #         enc_obj = Blowfish.new(settings.SECRET_KEY)
# #         repeat = 8 - (len(value) % 8)
# #         value += " " * repeat
# #         self.dl_number = binascii.b2a_hex(enc_obj.encrypt(value))
# #
# #     def _get_ssn(self):
# #         enc_obj = Blowfish.new(settings.SECRET_KEY)
# #         return u"%s" % enc_obj.decrypt(binascii.a2b_hex(self.ssn_last_four)).rstrip()
# #
# #     def _set_ssn(self, value):
# #         enc_obj = Blowfish.new(settings.SECRET_KEY)
# #         repeat = 8 - (len(value) % 8)
# #         value += " " * repeat
# #         self.ssn_last_four = binascii.b2a_hex(enc_obj.encrypt(value))
# #
# #     def get_activation_link(self):
# #         return "%s/accounts/activate/%s/" % (settings.BASE_URL, self.activation_token)
# #
# #     def get_reset_link(self):
# #         return "%s/accounts/reset/%s/" % (settings.BASE_URL, self.reset_token)
# #
# #     def get_forget_reset_link(self):
# #         return "%s/accounts/reset/%s/forget/" % (settings.BASE_URL, self.reset_token)
# #
# #
# #     full_name = property(get_full_name)
# #     activation_link = property(get_activation_link)
# #     reset_link = property(get_reset_link)
# #     reset_link_forget = property(get_forget_reset_link)
# #     ssn = property(_get_ssn, _set_ssn)
# #     driving_license_number = property(_get_dl_number, _set_dl_number)
# #
