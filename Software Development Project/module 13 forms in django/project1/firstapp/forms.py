from django import forms

class contactform(forms.Form):
    name=forms.CharField(label="User Name: ",help_text="Enter your name here",required=False)
    
    
    
    # file=forms.FileField()
    # email=forms.EmailField(label="User email")
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    # check=forms.BooleanField()
    
    
class StudentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput,required=False)
     
    # def clean_name(self):
    #     valname= self.cleaned_data["name"]
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with atleast 10 characters")
    #     return valname

    # #validate email
    
    # def clean_email(self):
    #     valmail=self.cleaned_data["email"]
    #     if ".com" not in valmail:
    #         raise forms.ValidationError("Enter a correct mail which contain .com ")
    #     return valmail
    
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data["name"]
        valmail=self.cleaned_data["email"]
        if len(valname) < 10:
            raise forms.ValidationError("Enter a name with atleast 10 characters")
        if ".com" not in valmail:
            raise forms.ValidationError("Enter a correct mail which contain .com ")
    