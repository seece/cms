from django import template
from cms.templatetags import cms_tags
from ..models import SiteInstance
from ..helpers import get_current_site

register = template.Library()


@register.inclusion_tag('djangocms_siteselector/sitepicker.html')
def available_sites():
    current_site = get_current_site()
    sites = SiteInstance.objects.all()
    return {'currentSite': current_site.id, 'sites': sites}


@register.tag()
class SitePageUrl(cms_tags.PageUrl):

    def render_tag(self, context, **kwargs):
        return super(SitePageUrl, self)

    def get_value(self, context, page_lookup, lang, site):
        url = super(SitePageUrl, self).get_value(context, page_lookup, lang, site)
        current_site = get_current_site()
        if current_site is not None and not current_site.default:
                return '/{0}{1}'.format(current_site.slug, url)
        return url
