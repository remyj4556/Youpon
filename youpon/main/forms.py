from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(
                            label = "", 
                            max_length = 200,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New Shopping List'})
                          )
    check = forms.BooleanField(required = False)


