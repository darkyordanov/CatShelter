from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from cat_shelter.cats.models import \
    OurBoy, OurGirl, Kitten
    

class OurBoyForm(forms.ModelForm):
    class Meta:
        model = OurBoy
        fields = '__all__'  # Or specify the fields you want to include

    def __init__(self, *args, **kwargs):
        super(OurBoyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'photo',
            'name',
            'registration',
            'color',
            'date_of_birth',
            'blood_type',
            'research_genetic',
            'research_blood',
            'available',
            Submit('submit', 'Save', css_class='btn btn-primary')
        )
        
        
# form_class = OurBoysCreateForm
# form_class = OurGirlsCreateForm
# form_class = KittensCreateForm
