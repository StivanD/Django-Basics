from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('bio', )


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = '__all__'
        exclude = None
