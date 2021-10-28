from django import forms

from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm

from mainapp.models import ProductCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = ('__all__')


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProductCategoryCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                field.widget.attrs['class'] = "form-check-input"
                field.widget.attrs['type'] = "checkbox"
            else:
                field.widget.attrs['class'] = 'form-control'
