from collective.plonetruegallery.utils import createSettingsFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.plonetruegallery.browser.views.display import BaseDisplayType
from collective.plonetruegallery.interfaces import IBaseSettings
from collective.plonetruegallery.browser.views.display import jsbool
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.ptg.pixelentity')

class IPixelentityDisplaySettings(IBaseSettings):
    pixelentity_imagewidth = schema.Int(
        title=_(u"label_pixelentity_imagewidth",
            default=u"Width"),
        default=400,
        min=50)
    pixelentity_imageheight = schema.Int(
        title=_(u"label_pixelentity_imageheight",
            default=u"Height"),
        default=260,
        min=50)

   

class PixelentityDisplayType(BaseDisplayType):
    name = u"pixelentity"
    schema = IPixelentityDisplaySettings
    description = _(u"label_pixelentity_display_type",
        default=u"Pixelentity")

    def javascript(self):
        return u"""
<script type="text/javascript">
$(document).ready(function() {
			$(".peKenBurns").peKenburnsSlider();
		})
</script>

""" % {
        'speed':        self.settings.duration,
	}

    def css(self):
        return u"""
        <style>
.peKenBurns {
    height: %(boxheight)ipx;
    width: %(boxwidth)ipx;
}

 

</style>
<link rel="stylesheet" type="text/css" href="+resource++ptg.pixelentity/style.css"/>
""" % {
        'boxheight': self.settings.pixelentity_imageheight,
        'boxwidth': self.settings.pixelentity_imagewidth,
       }
PixelentitySettings = createSettingsFactory(PixelentityDisplayType.schema)
