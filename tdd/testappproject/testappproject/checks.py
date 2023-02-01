from django.apps import apps
from django.core.checks import Tags, Warning, register

@register(Tags.models)
def check_model_str(app_configs=None, **kwargs):
    configs = (app_configs if app_configs else apps.get_app_configs())
    problem_models = [
        model
        for app in configs
        if not app.name.startswith("django.contrib")
        for model in app.get_models()
        if "__str__" not in model.__dict__
    ]
    return [
        Warning(
            "All models must mave a __str__ method.",
            hint=("See docs"),
        obj = model,
        id="suorganizer.W001",
        ) for model in problem_models
    ]