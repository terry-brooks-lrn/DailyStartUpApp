from agenda.models import WIN_OOPS, Agenda, Item
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column
from crispy_forms.layout import HTML
from crispy_forms.layout import Layout, Div
from crispy_forms.layout import Row, Field, Button
from crispy_forms.bootstrap import FormActions
from django import forms


class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "create-item-form"
        self.helper.form_method = "post"
        self.helper.form_action = "/api/items/"
        self.helper.layout = Layout(
            Row(
                Column("title", css_class="form-group col-md-8 mb-0"),
                Column("link_to_ticket", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("creator", css_class="form-group col-md-6 mb-0"),
                Column("section", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("description", css_class="form-group col-md-12 mb-0"),
                css_class="form-row",
            ),
            HTML(
                """<hr/>
            <h3 class="application-text">Stand-Up Meeting Notes</h3>"""
            ),
            Row(
                Column("notes", css_class="form-group col-md-12 mb-0"),
                css_class="form-row",
            ),
            Div(
                FormActions(
                    Button(
                        "submit",
                        "Create Item",
                        onclick="createItem()",
                        css_class="btn btn-success",
                    ),
                    Button(
                        "cancel",
                        "Cancel",
                        css_class="btn btn-danger",
                        css_id="cancel-add-item",
                    ),
                ),
                css_class="modal-footer",
            ),
        )

    class Meta:
        model = Item

        fields = (
            "section",
            "title",
            "link_to_ticket",
            "description",
            "notes",
            "owner_of_next_task_needed_to_resolve",
            "next_task_needed_to_resolve",
        )
