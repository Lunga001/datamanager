from django.conf import settings


def google_analytics(request):
    """
    Add the Google Analytics tracking ID and domain to the context for use when
    rendering tracking code.
    """
    ga_tracking_id = getattr(settings, "GOOGLE_ANALYTICS_ID", False)
    if not settings.DEBUG and ga_tracking_id:
        return {"GOOGLE_ANALYTICS_ID": ga_tracking_id}
    return {}


def debug(request):
    return {"debug": settings.DEBUG}


def ckan_url(request):
    return {"CKAN_URL": settings.CKAN_URL}
