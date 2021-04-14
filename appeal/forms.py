from django import forms

class AppealForm(forms.Form):
    appeal_num = forms.CharField(label='appeal_num', max_length=100)
    bsk_number = forms.CharField(label='bsk_number', max_length=100)
    appeal_create_date = forms.DateField(label='appeal_create_date')
    appeal_owner_name = forms.CharField(label='appeal_owner_name', max_length=100)

class AppealAnswerForm(forms.Form):
    answer = forms.CharField(label='answer', max_length=1500, widget=forms.Textarea)
    answer.widget.attrs.update({'class':'form-control', 'required':'required'})
