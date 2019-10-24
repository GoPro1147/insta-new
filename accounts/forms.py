from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # model = setting.AUTH_USER_MODEL # 'accounts.user'(문자열 출력)
        model = get_user_model() # User (클래스 출력)
        fields = ('email', 'first_name', 'last_name', )
