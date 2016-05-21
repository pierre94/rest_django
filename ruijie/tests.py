from django.test import TestCase
from ruijie.models import RuijieUser
from ruijie.serializers import RuijieUserSerializer
from dev.token import token_auth, key_from_token
from dev.models import devuser_auth
from ruijie.crypt import aes_encrypt, aes_decrypt

def handle():
    ruijie_user = RuijieUser.objects.all()
    serializer = RuijieUserSerializer(ruijie_user, many=True)
    data = serializer.data
    for user in data:
        user['flow_used'] = aes_encrypt(user['flow_used'], '0123456789123456')
        user['money'] = aes_encrypt(user['money'], '0123456789123456')
    print serializer.data