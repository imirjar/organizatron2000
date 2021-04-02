from django import forms

class AppealForm(forms.Form):
    appeal_num = forms.CharField(label='appeal_num', max_length=100)
    bsk_number = forms.CharField(label='bsk_number', max_length=100)
    appeal_create_date = forms.DateField(label='appeal_create_date')
    appeal_owner_name = forms.CharField(label='appeal_owner_name', max_length=100)

