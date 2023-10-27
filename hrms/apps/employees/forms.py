from django import forms

from employees.models import KycDetail


class EmployeeKycForm(forms.ModelForm):
    document = forms.FileField(
        widget=forms.FileInput(attrs={"accept": "application/pdf"})
    )

    class Meta:
        model = KycDetail

        fields = [
            "document",
            "document_type",
        ]

    def clean_document(self):
        document = self.cleaned_data.get("document")
        if document.size <= 2000000:
            return document
        raise forms.ValidationError("accept only upto 2 mb file")
