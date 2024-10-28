class ReadOnlyMixin:

    def make_fields_readonly(self):
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()
