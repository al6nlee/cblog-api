from flask_smorest import Blueprint as _SmorestBlueprint


class Blueprint(_SmorestBlueprint):

    def add_resource(self, resource, *args, **kwargs):
        self.route(*args, **kwargs)(resource)

    def arguments(self, *args, **kwargs):
        kwargs.setdefault("as_kwargs", True)
        return super().arguments(*args, **kwargs)
