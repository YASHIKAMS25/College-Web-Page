from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock, CharBlock, RichTextBlock
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

class DemoStreamBlock(StreamBlock):
    title = CharBlock(required=True)
    paragraph = RichTextBlock(required=False)
    table = TypedTableBlock([
        ('text', CharBlock(required=False)),
        ('numeric', RichTextBlock(required=False)),
        ('rich_text', RichTextBlock(required=False)),
        ('image', ImageChooserBlock(required=False)),
        ('document', DocumentChooserBlock(required=False)),
    ], required=False)
    # ('document', DocumentChooserBlock(required=False)),

class CriteriaPage(Page):
    """
    A Wagtail Page model for Criteria, with support for rich text, StreamFields, and file uploads.
    """
    body = RichTextField(blank=True)
    content = StreamField(DemoStreamBlock(), blank=True, use_json_field=True)  # JSON-based storage for StreamField

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('content'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['all_criteria'] = CriteriaPage.objects.live().exclude(id=self.id)
        return context
