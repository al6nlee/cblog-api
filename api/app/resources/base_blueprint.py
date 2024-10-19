from flask_smorest import Blueprint as _SmorestBlueprint


class Blueprint(_SmorestBlueprint):

    def add_resource(self, resource, *args, **kwargs):
        self.route(*args, **kwargs)(resource)
