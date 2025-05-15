from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from decimal import Decimal

# Create your models here.

class RubroPrincipal(models.Model):
    codigo = models.CharField(
        max_length=4,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{4}$', message='El código debe tener 4 dígitos.')],
        verbose_name="Código del Rubro Principal",
        help_text="Código único de 4 dígitos para el rubro principal (ej. 2112)."
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre del Rubro Principal",
        help_text="Nombre descriptivo del rubro principal."
    )

    class Meta:
        verbose_name = "Rubro Principal"
        verbose_name_plural = "Rubros Principales"
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class RubroAuxiliar(models.Model):
    rubro_principal = models.ForeignKey(
        RubroPrincipal,
        on_delete=models.CASCADE,
        related_name='auxiliares',
        verbose_name="Rubro Principal Asociado"
    )
    codigo_auxiliar = models.CharField(
        max_length=10, # Suficiente para sub-códigos como "01", "01.01", etc.
        verbose_name="Código Auxiliar",
        help_text="Código del rubro auxiliar dentro del principal (ej. 01, A, 1.1)."
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre del Rubro Auxiliar",
        help_text="Nombre descriptivo del rubro auxiliar."
    )
    # El presupuesto se manejará a través del modelo AsignacionPresupuesto.

    class Meta:
        verbose_name = "Rubro Auxiliar"
        verbose_name_plural = "Rubros Auxiliares"
        ordering = ['rubro_principal__codigo', 'codigo_auxiliar']
        # Asegura que el codigo_auxiliar sea único para cada rubro_principal
        unique_together = ('rubro_principal', 'codigo_auxiliar')

    def __str__(self):
        return f"{self.rubro_principal.codigo}-{self.codigo_auxiliar} - {self.nombre}"

    @property
    def codigo_completo(self):
        return f"{self.rubro_principal.codigo}-{self.codigo_auxiliar}"

class AsignacionPresupuesto(models.Model):
    rubro_auxiliar = models.ForeignKey(
        RubroAuxiliar,
        on_delete=models.CASCADE, # Si se borra el rubro, se borran sus asignaciones
        related_name="asignaciones_presupuestarias",
        verbose_name="Rubro Auxiliar"
    )
    monto = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))], # Una asignación debe tener un monto positivo
        verbose_name="Monto Asignado"
    )
    documento_soporte = models.FileField(
        upload_to='soportes_asignaciones/', # Asegúrate que MEDIA_ROOT y MEDIA_URL estén configurados
        verbose_name="Documento Soporte de Asignación"
    )
    fecha_asignacion = models.DateField(
        auto_now_add=True, # Se establece automáticamente al crear el registro
        verbose_name="Fecha de Asignación"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción Adicional"
    )

    class Meta:
        verbose_name = "Asignación de Presupuesto"
        verbose_name_plural = "Asignaciones de Presupuesto"
        ordering = ['-fecha_asignacion', 'rubro_auxiliar__codigo_completo']

    def __str__(self):
        return f"Asignación de {self.monto} a {self.rubro_auxiliar.codigo_completo} el {self.fecha_asignacion}"
