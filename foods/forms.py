from django import forms


class SearchForm(forms.Form):
	product_name = forms.CharField(
		max_length=50,
		label="Produit",
		widget=forms.TextInput(
			attrs={
				"placeholder": "Entrer un nom de produit",
				"type": "text",
				"name": "searched",
			}
		),
	)
