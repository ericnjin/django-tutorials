from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='검색할 단어 Word')