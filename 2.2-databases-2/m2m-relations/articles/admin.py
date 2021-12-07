from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    counter += 1
                    print(counter)

        if counter != 1:
            raise ValidationError('Обязательно нужно указать один основной раздел')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

admin.site.register(Tag)
