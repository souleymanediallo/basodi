from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        TITLE_CHOICES = "TITLE_CHOICES"
        model = Article
        fields = ["category", "subcategory", "name", "description", "price", "condition", "tag", "color", "size",
                  "give", "photo_main", "photo_1", "photo_2", "photo_3", "photo_4", "photo_5", "photo_6"]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'tag': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            self.fields['size'].widget.attrs.update({'placeholder': 'Pas de Taille'})
            self.fields['photo_main'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_1'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_2'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_3'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_4'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_5'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_6'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['tag'].widget.attrs.update({'class': 'form-check-input-c'})

