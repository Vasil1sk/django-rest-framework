from django.db import models


class Sensor(models.Model):
    """Объект на котором проводят измерения."""

    name = models.CharField(max_length=60, null=False)
    description = models.CharField(max_length=60, null=False)

class Measurement(models.Model):
    """Измерение температуры на объекте."""

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', default=1)
    temperature = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)