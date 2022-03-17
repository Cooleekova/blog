from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'Title "{title}" us already in use')
        return cleaned_data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if title.lower().strip() == 'война':
            self.add_error('title', 'в теме не должно быть слова война')
        if 'война' in text or "война" in title:
            self.add_error('text', 'НЕЛЬЗЯ !')
            raise forms.ValidationError(f"Нельзя говорить про войну")
        print(cleaned_data)
        return cleaned_data
