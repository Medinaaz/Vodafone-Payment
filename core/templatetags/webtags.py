from django import template

register = template.Library()


@register.filter
def replace_language(path: str, lang: str) -> str:
    """Replace language in the url.
    Usage: {{ request.path|replace_language:language }}
    """
    try:
        language = path.split("/")[1]
    except IndexError:
        return path
    if not language:
        return path
    return path.replace(language, lang, 1)
