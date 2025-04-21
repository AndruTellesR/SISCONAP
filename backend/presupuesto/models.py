from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Rubro(models.Model):
    codigo = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código del Rubro",
        help_text="Código único identificador del rubro (ej. 2111)"
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre del Rubro",
        help_text="Nombre descriptivo del rubro presupuestal"
    )
    monto_inicial = models.DecimalField(
        max_digits=15,             # Suficiente para manejar montos grandes
        decimal_places=2,          # Precisión estándar para moneda
        default=Decimal('0.00'),   # Valor por defecto
        validators=[MinValueValidator(Decimal('0.00'))], # No permitir montos negativos
        verbose_name="Monto Inicial",
        help_text="Presupuesto inicial asignado al rubro"
    )
    # Campos calculados (se definirán más adelante como propiedades o métodos)
    # saldo_actual = ...

    class Meta:
        verbose_name = "Rubro Presupuestal"
        verbose_name_plural = "Rubros Presupuestales"
        ordering = ['codigo'] # Ordenar por código por defecto

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
