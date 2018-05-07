from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # 并集
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.hashers import make_password

from .models import UserMessage, VerifyRecord
from .forms import ModifyPwdForm, RegisterForm, LoginForm, ForgetForm, VerifyForm, ModifyMessageForm
from utils.verifycode_send import send_verify_code


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserMessage.objects.get(Q(username=username) | Q(email=username) | Q(user_mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 验证
class VerifyView(View):
    def post(self, request):
        verify_form = VerifyForm(request.POST)
        if verify_form.is_valid():
            dict1 = dict(request.POST)
            for i in dict1.keys():
                dict1[i] = dict1[i][0]
            all_records = VerifyRecord.objects.filter(code=dict1['code'])
            if all_records:  # 用户存在
                for record in all_records:
                    emailormobile = record.email_or_mobile
                    if 'email' in record.send_type:
                        user = UserMessage.objects.get(email=emailormobile)
                    else:
                        user = UserMessage.objects.get(user_mobile=emailormobile)
                    user.password = make_password(dict1['password'])
                    user.is_active = True
                    user.save()
                    result = {'result': 'Successful!'}
            else:
                result = {'result': 'Activecode is wrong'}
        else:
            result = {'result': 'Message is wrong'}
        return JsonResponse(result)


# {'password':'','code':''}


# 注册
class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            dict1 = dict(request.POST)
            for i in dict1.keys():
                dict1[i] = dict1[i][0]
            if 'email' in dict1.keys():
                email_or_mobile = dict1['email']
                type1 = 'email'
            else:
                email_or_mobile = dict1['user_mobile']
                type1 = 'mobile'
            if UserMessage.objects.filter(email=email_or_mobile) or UserMessage.objects.filter(
                    user_mobile=email_or_mobile):
                result = {'result': "用户已经存在"}
            else:
                UserMessage.objects.create(**dict1)
                send_verify_code(type1, email_or_mobile, type1 + 'register')
        else:
            result = {'result': '信息错误！'}

        return JsonResponse(result)


# {'username':'','email':''}
# {'username':'','user_mobile':''}


# 登录
class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 验证登录信息是否填写错误
            dict1 = dict(request.POST)
            for i in dict1.keys():
                dict1[i] = dict1[i][0]
            user_name = dict1['username']
            pass_word = dict1['password']
            user = authenticate(username=user_name, password=pass_word)  # 验证用户名密码
            if user is not None:
                if user.is_active:
                    login(request, user)
                    result = {'result': 'login success'}
                else:
                    result = {'result': 'unverified'}
            else:
                result = {'result': 'username or password is false'}
        else:
            result = {'result': 'message is unvalid'}
        return JsonResponse(result)


# {'username':'','password':''}


# 忘记密码
class ForgetPwdView(View):
    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            dict1 = dict(request.POST)
            for i in dict1.keys():
                dict1[i] = dict1[i][0]
            if 'email' in dict1.keys():
                email_or_mobile = dict1['email']
                type1 = 'email'
            else:
                email_or_mobile = dict1['user_mobile']
                type1 = 'mobile'
            if UserMessage.objects.filter(email=email_or_mobile) or UserMessage.objects.filter(
                    user_mobile=email_or_mobile):
                send_verify_code(type1, email_or_mobile, type1 + 'forget')
                result = {'result': '已向{}发送验证码，请注意查收'.format(email_or_mobile)}
            else:
                result = {'result': "user is None"}

        else:
            result = {'result': '信息错误！'}
        return JsonResponse(result)


# {'email':''}
# {'user_mobile':''}

# 个人中心
class PersonalCenterView(View):
    def post(self, request):
        if request.user.is_authenticated():
            user = request.user
            image = user.user_img
            signature = user.user_signature
            username = user.username
            result = {'image': str(image), 'signature': signature, 'username': username}
        else:
            result = {'result': 'user is none'}
        return JsonResponse(result)


# 修改密码
class ModifyPwdView(View):
    def post(self, request):
        modifypwd_form = ModifyPwdForm(request.POST)
        if modifypwd_form.is_valid():
            if request.user.is_authenticated():
                user = request.user
                oldpwd = request.POST.get("oldpwd", "")
                pwd1 = request.POST.get("password1", "")
                pwd2 = request.POST.get("password2", "")
                # UserMessage.objects.get(username=user.username)
                if user is not None:
                    if not user.check_password(oldpwd):
                        result = {'result': 'Password is false'}
                        return JsonResponse(result)
                    if pwd1 != pwd2:
                        result = {'result': 'Entered password differ'}
                    else:

                        user.password = make_password(pwd2)
                        user.save()
                        result = {'result': 'Modify successfully!'}

                else:
                    result = {'result': 'user is none'}
            else:
                result = {'result': 'user is none'}
        else:
            result = {'result': 'Message is invalid'}
        return JsonResponse(result)


# {'oldpwd':'','pwd1':'','pwd2':''}

class PersonalMessageView(View):
    def post(self, request):
        if request.user.is_authenticated():
            user = request.user
            dict1 = {}
            dict1['username'] = user.username
            dict1['email'] = user.email
            dict1['birday'] = user.user_birday
            dict1['gender'] = user.user_gender
            dict1['mobile'] = user.user_mobile
            dict1['address'] = user.user_address
            dict1['signature'] = user.user_signature
            dict1['department'] = user.user_department
            dict1['desc'] = user.user_desc
            result = dict1
            return JsonResponse(result)
# {
#   "username": "111",
#   "email": "1625449339@qq.com",
#   "birday": "1998-10-12",
#   "gender": "male",
#   "mobile": "18834198432",
#   "address": "xxxx",
#   "signature": "23333",
#   "department": "Python",
#   "desc": "啦啦啦"
# }

# 修改信息
class ModifyMessageView(View):

    def post(self, request):
        modifymessage_form = ModifyMessageForm(request.POST)
        if modifymessage_form.is_valid():
            if request.user.is_authenticated():
                user = request.user
                username = request.POST.get("username", "")
                email = request.POST.get("email", "")
                address = request.POST.get("user_address", "")
                birday = request.POST.get("user_birday", "")
                gender = request.POST.get("user_gender", "")
                mobile = request.POST.get("user_mobile", "")
                desc = request.POST.get("user_desc", "")
                signature = request.POST.get("user_signature", "")
                department = request.POST.get("user_department", "")

                user.username = username
                user.email = email
                user.user_birday = birday
                user.user_gender = gender
                user.user_mobile = mobile
                user.user_address = address
                user.user_signature = signature
                user.user_department = department
                user.user_desc = desc
                user.save()
                result = {'result': 'success'}
            else:
                result = {'result': 'user is none'}
        else:
            result = {'result': 'message is invalid'}
        return JsonResponse(result)


# {'user_address':'','username':'','email':'','user_birday':'','user_gender':'','user_mobile':'','user_desc':'','user_signature':'','user_department':''}


# 注销
class LogoutView(View):
    def post(self, request):
        logout(request)
        result = {'result': 'successful'}
        return JsonResponse(result)
