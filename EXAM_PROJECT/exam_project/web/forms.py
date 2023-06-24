from django import forms
from exam_project.web.models import Profile, Fruit


class ProfileCreateModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['image_url', 'age']


class AddFruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        exclude = ["profile"]


class EditFruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"


class DeleteFruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"


class ProfileEditModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['image_url', 'age']
