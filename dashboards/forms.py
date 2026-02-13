from django import forms
from blogs.models import Blog, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')



# EditUserForm is used to edit user details and permissions. It does not include password fields as we are not allowing password change from this form.
#we want that password change permission to be handled by the user not the management. So we will not include password fields in this form. We will create a separate form for password change if needed.
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')