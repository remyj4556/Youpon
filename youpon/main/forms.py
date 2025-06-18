from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(
                            label = "", 
                            max_length = 200,
                            widget=forms.TextInput(attrs={'class': 'form-control flex-grow-1 text-start me-3', 'placeholder': 'New Shopping List'})
                          )
    check = forms.BooleanField(required = False)


