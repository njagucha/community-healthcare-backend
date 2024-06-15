from django import forms
from .models import KiharuHealthFacilitiesCleaned


class MultiChoiceField(forms.MultipleChoiceField):
    def to_python(self, value):
        if not value:
            return ""
        return ",".join(value)

    def validate(self, value):
        choices = [choice[0] for choice in self.choices]
        for item in value.split(","):
            if item not in choices:
                raise forms.ValidationError(f"{item} is not a valid choice.")


class HealthFacilityForm(forms.ModelForm):
    services_offered = MultiChoiceField(
        choices=KiharuHealthFacilitiesCleaned.Services.choices,
        widget=forms.CheckboxSelectMultiple,
    )
    amenities_available = MultiChoiceField(
        choices=KiharuHealthFacilitiesCleaned.Amenities.choices,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = KiharuHealthFacilitiesCleaned
        fields = "__all__"
