from django.db import models

# Create your models here.
class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    '''site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE, blank=True, null=True,
        default=None, related_name='menu'
    )'''

    def __str__(self):
        return self.text