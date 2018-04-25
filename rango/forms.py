from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ("name", )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ("category", )

    def clean_url(self):
        url = self.cleaned_data.get('url')

        if url.startswith("https://"):
            self.errors['url'] = "网址不能以https开头"
        return url


class UserForm(forms.ModelForm):
    username = forms.CharField(error_messages={'required': '用户名不能为空！', 'invalid': '用户名输入错误！'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': '密码不能为空！', 'invalid': '密码输入错误!'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

