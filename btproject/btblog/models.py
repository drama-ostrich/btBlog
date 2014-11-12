from django.db import models

ENTRY_CHOICES = (
    ('IM', 'Image'),
    ('SI', 'Small Img'),
    ('TX', 'Text'),
    ('ST', 'Status'),
    ('AU', 'Audio'),
    ('VI', 'Video'),
    ('EV', 'Event'),
)

class Entry(models.Model):

    type = models.CharField(max_length=2, choices=ENTRY_CHOICES, default='TX')
    
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    
    text = models.TextField(blank=True)
    width = models.IntegerField(blank = True, null = True)
    height = models.IntegerField(blank = True, null = True)
    audio = models.FileField(blank = True, null = True, upload_to='upload')
    video = models.FileField(blank = True, null = True, upload_to='upload')
    image = models.ImageField(blank = True, null = True, upload_to='upload')
    
    order_manual = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
	    return self.title + ' - ' + self.type
    class Meta:
        ordering = ['-pk']
