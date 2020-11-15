import re

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    RegexValidator,
    EmailValidator, validate_email,
    URLValidator, validate_slug, validate_unicode_slug,
    validate_ipv4_address, validate_ipv6_address, validate_ipv46_address,
    validate_comma_separated_integer_list, int_list_validator,
    MaxValueValidator, MinValueValidator,
    MinLengthValidator, MaxLengthValidator,
    DecimalValidator,
    FileExtensionValidator, validate_image_file_extension
)
from django.utils.timezone import now
from django.core.exceptions import ValidationError


def validate_date_of_birth(date_of_birth):
    today = now()
    if (today.year - date_of_birth.year) < 18:
        raise ValidationError('Вы слишком молоды!')


class Post(models.Model):

    date_of_birth = models.DateField(_("date of birth"), null=True, validators=[
        validate_date_of_birth
    ])

    file = models.FileField(_("file"), upload_to='file/', max_length=100, null=True, validators=[
        validate_image_file_extension,
        # FileExtensionValidator(
        #     allowed_extensions=['xlsx', 'jpg'],
        #     message='Не тот файл!'
        # )
    ])

    number = models.DecimalField(_("number"), max_digits=9, decimal_places=3, null=True, validators=[
        DecimalValidator(
            max_digits=5,
            decimal_places=2
        )
    ])

    interval_length = models.CharField(_("interval length"), max_length=50, null=True, validators=[
        MinLengthValidator(
            limit_value=9,
            message='9'
        ),
        MaxLengthValidator(
            limit_value=42,
            message='42'
        )
    ])

    interval_value = models.IntegerField(_("interval"), null=True, validators=[
        MaxValueValidator(
            limit_value=42,
            message='Не более 42'
        ),
        MinValueValidator(
            limit_value=9,
            message='Не менее 9'
        )
    ])

    int_list_sep = models.CharField(_("list sep"), max_length=50, null=True, validators=[
        int_list_validator(
            sep=':',
            allow_negative=True,
            message='Используйте двоетечие!'
        )
    ])

    int_list_comma = models.CharField(_("list comma"), max_length=50, null=True, validators=[
        validate_comma_separated_integer_list
    ])

    # ip = models.GenericIPAddressField(_("ip"), protocol="both", unpack_ipv4=False)
    ip = models.CharField(_("ip"), max_length=50, null=True, validators=[
        # validate_ipv4_address,
        # validate_ipv6_address,
        validate_ipv46_address
    ])

    # url = models.SlugField(_("url"), allow_unicode=True)  # validate_slug | validate_unicode_slug
    # url = models.URLField(_("url"), max_length=200)  # URLValidator
    url = models.CharField(_("url"), max_length=50, null=True, validators=[
        # validate_slug,
        # validate_unicode_slug,
        URLValidator(
            message='Введите корректный URL',
            schemes=['https']
        )
    ])

    # email = models.EmailField(_("email"), max_length=254) validate_email
    email = models.CharField(_("email"), max_length=50, null=True, validators=[
        # validate_email,
        EmailValidator(
            message='Введите корректный email',
            whitelist=['localhost', 'my_local']
        )
    ])

    title = models.CharField(_("title"), max_length=50, validators=[
        RegexValidator(
            regex=r'\.$',
            # regex=re.compile()
            message='Поставьте точку в конце!',
            code='invalid',  # required
            inverse_match=True,
            flags=re.IGNORECASE
            # https://docs.python.org/3/library/re.html#contents-of-module-re
        )
    ])

    name = models.CharField(_("name"), max_length=150)
    slug = models.SlugField(_("url"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        db_table = 'posts'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
