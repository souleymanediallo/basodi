from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        TITLE_CHOICES = "TITLE_CHOICES"
        model = Article
        fields = ["main_category", "category", "subcategory", "name", "description", "price", "condition", "tag", "color", "size",
                  "change", "give", "photo_main", "photo_1", "photo_2", "photo_3", "photo_4", "photo_5", "photo_6"]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'tag': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            # Mettre à jour les attributs spécifiques pour le champ size en dehors de la boucle.
        self.fields['size'].widget.attrs.update({
            'class': 'form-control',
            'id': 'size_select',
            'placeholder': 'Pas de Taille'
        })

        # Mettre à jour les attributs pour les champs de téléchargement de photos.
        photo_fields = ['photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
        for photo_field in photo_fields:
            self.fields[photo_field].widget.attrs.update({'class': 'custom-file-upload'})

        # Mettre à jour les attributs pour les sélecteurs de catégories.
        self.fields['main_category'].widget.attrs.update({'id': 'main_category_select'})
        self.fields['category'].widget.attrs.update({'id': 'sub_category_select'})
        self.fields['subcategory'].widget.attrs.update({'id': 'third_sub_category_select'})

        # Mettre à jour les attributs pour le champ tag.
        self.fields['tag'].widget.attrs.update({'class': 'form-check-input-c'})


