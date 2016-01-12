from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core import exceptions
from deals.models import STATE_CHOICES


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    user_state = models.SmallIntegerField(choices=STATE_CHOICES,
                                          default=25)
    occupation = models.TextField(blank=True, default='')
    phonenumber = models.CharField(blank=True, default='', max_length=20)
    intlnumber = models.CharField(blank=True, default='', max_length=20)

    def check_diff(self, request_value):

        for field in request_value:
            if getattr(self, field, False) != False and getattr(self, field) != request_value[field] and \
                    request_value[field] != '':
                    setattr(self, field, request_value[field])
        self.save()
        return {
            u'user_state': self.user_state,
            u'phonenumber': self.phonenumber,
            u'intlnumber': self.intlnumber,
            u'occupation': self.occupation
        }

    def is_complete(self):
        """Checks if a user's profile is completed"""
        for field in self._meta.get_all_field_names():
            try:
                fieldattr = getattr(self, field)
                if fieldattr == '':
                    return False
                if type(fieldattr) == User:
                    if fieldattr.first_name == '' or fieldattr.last_name == '':
                        return False
            except:
                pass
        return True

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User,
                      dispatch_uid=create_user_profile)
