from django import forms
from django.core import validators


class contactform(forms.Form):
    name = forms.CharField(label="User Name: ",
                           help_text="Enter your name here", required=False)

    # file=forms.FileField()
    # email=forms.EmailField(label="User email")
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    # check=forms.BooleanField()


# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput,required=False)

#     # def clean_name(self):
#     #     valname= self.cleaned_data["name"]
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with atleast 10 characters")
#     #     return valname

#     # #validate email

#     # def clean_email(self):
#     #     valmail=self.cleaned_data["email"]
#     #     if ".com" not in valmail:
#     #         raise forms.ValidationError("Enter a correct mail which contain .com ")
#     #     return valmail

#     def clean(self):
#         cleaned_data=super().clean()
#         valname=self.cleaned_data["name"]
#         valmail=self.cleaned_data["email"]
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with atleast 10 characters")
#         if ".com" not in valmail:
#             raise forms.ValidationError("Enter a correct mail which contain .com ")


class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[
                           validators.MinLengthValidator(2, message="10 word r kom dea jabe na!!!")])
    email = forms.CharField(widget=forms.EmailInput, required=False, validators=[
                            validators.EmailValidator(message="enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(
        34, message="age must be smaller than 34"), validators.MinValueValidator(24, message="age must be bigger than 24")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=["pdf"])])


class passwordValidation(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data["password"]
        val_confrm_pass=self.cleaned_data["confirm_password"]
        if val_pass != val_confrm_pass :
            raise forms.ValidationError(message="Password aren't matched!!")
    