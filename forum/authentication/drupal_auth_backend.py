from django.conf import settings

from forum.models import User
from forum.models import drupal
from django.contrib.auth.models import check_password, get_hexdigest


DRUPAL_DB = 'drupal_users'


class DrupalAuthBackend:
    """
    Authenticate against existing drupal user accounts.

    See example configuration at settings_local.py.dist. Take a look at the
    following links for documentation:
    * http://docs.djangoproject.com/en/dev/topics/auth/#writing-an-authentication-backend
    * http://docs.djangoproject.com/en/1.2/topics/db/multi-db/
    * http://docs.djangoproject.com/en/1.2/howto/legacy-databases/
    * http://blog.eval.ca/files/migration.py
    """

    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        try:
            drupal_user = drupal.Users.objects.using(DRUPAL_DB).get(name=username)
        except drupal.Users.DoesNotExist:
            return None
        if User.objects.filter(username=drupal_user.name):
            # Only authenticates users that have not being migrated to the django database.
            return None
        user = User(username=username)
        pwd_valid = self.check_password(drupal_user, user, password)
        if pwd_valid:
            DrupalAuthBackend.get_user_data(drupal_user, user)
            if User.objects.all().count() == 0:
                user.is_superuser = True
                user.is_staff = True
            user.save()
            return user
        else:
            return None

    def check_password(self, drupal_user, user, password):
        if '$' not in drupal_user.pass_field:
            is_correct = (drupal_user.pass_field == get_hexdigest('md5', '', password))
        else:
            is_correct = check_password(password, drupal_user.pass_field)
        if is_correct:
            user.set_password(password)
        return is_correct

    @classmethod
    def get_user_data(cls, drupal_user, user):
        user.email = drupal_user.mail
        drupal_realname = drupal.Realname.objects.using(DRUPAL_DB).get(uid=drupal_user.uid)
        user.real_name = drupal_realname.realname

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    @classmethod
    def get_openid_user(cls, assoc_key):
        try:
            authmap = drupal.Authmap.objects.using(DRUPAL_DB).get(authname=assoc_key)
            drupal_user = drupal.Users.objects.using(DRUPAL_DB).get(uid=authmap.uid)
            try:
                user = User.objects.get(username=drupal_user.name)
            except User.DoesNotExist:
                user = User(username=drupal_user.name)
                cls.get_user_data(drupal_user, user)
                user.save()
            return user
        except drupal.Authmap.DoesNotExist, drupal.Users.DoesNotExist:
            return None


