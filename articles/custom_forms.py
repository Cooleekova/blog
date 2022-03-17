from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if title.lower().strip() == 'война':
            # raise
            raise forms.ValidationError("Нельзя говорить про войну")
        print(cleaned_data)
        return cleaned_data
