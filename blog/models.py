from django.db import models
from django.utils import timezone
import ast
from ckeditor_uploader.fields import RichTextUploadingField

#自定義list field 提供儲存使用者我的收藏和我的閱讀 List
class ListField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='標題')
    keyword = ListField(blank=True, verbose_name='關鍵字')
    slug = models.SlugField(max_length=100, verbose_name='連結',unique=True)
    body = RichTextUploadingField(verbose_name='文章內容')
    readcount = models.IntegerField(verbose_name='閱讀次數', default = 0)
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='發布日期')

    class Meta:
        verbose_name = '部落格文章'
        verbose_name_plural = '部落格'  # 指定模型複數名稱
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title