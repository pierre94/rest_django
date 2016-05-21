from django.test import TestCase
from dev.models import DevUser

def handle():
    # Create your tests here.
    dev_list = DevUser.objects .all()

    for dev_user in dev_list:
        print dev_user.app_id