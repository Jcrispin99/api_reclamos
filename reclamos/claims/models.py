from django.db import models
from django.utils import timezone

# Create your models here.
class Claim(models.Model):
    # Datos personales del reclamante
    nombre = models.CharField('Nombres', max_length=100)
    apellido = models.CharField('Apellidos', max_length=100)
    tipo_documento = models.CharField(
        'Tipo de documento',
        choices=[
            ('DNI', 'DNI'),
            ('RUC', 'RUC'),
            ('Pasaporte', 'Pasaporte'),
            ('Carnet de extranjería', 'Carnet de extranjería'),
        ],
        default='DNI'
    )
    numero_documento = models.CharField('Número de documento', max_length=20)
    telefono = models.CharField('Teléfono/Celular', max_length=20)
    domicilio = models.CharField('Dirección', max_length=255, blank=True, default='')
    email = models.EmailField('Correo electrónico')

    # Detalles del producto/servicio
    tipo_producto_servicio = models.CharField(
        'Producto / Servicio',
        max_length=20,
        choices=[
            ('PRODUCTO', 'Producto'),
            ('SERVICIO', 'Servicio'),
        ],
        default='PRODUCTO'
    )
    descripcion_producto_servicio = models.CharField(
        'Descripción del Producto / Servicio',
        max_length=255
    )
    monto_reclamo = models.DecimalField(
        'Monto del bien objeto de Reclamo',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    numero_pedido = models.CharField(
        'Número de Pedido (Opcional)',
        max_length=50,
        blank=True,
        default=''
    )

    # Detalles de la reclamación
    tipo_reclamacion = models.CharField(
        'Tipo de reclamación',
        max_length=20,
        choices=[
            ('RECLAMO', 'Reclamo'),
            ('QUEJA', 'Queja'),
        ],
        default='RECLAMO'
    )
    detalle_reclamo = models.TextField('Detalle del Reclamo')
    mensaje = models.TextField('Mensaje adicional', blank=True, default='')

    # Metadata
    created_at = models.DateTimeField('Creado el', default=timezone.now)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True)
    status = models.CharField(
        'Estado',
        max_length=20,
        default='pendiente',
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En proceso'),
            ('resuelto', 'Resuelto'),
            ('rechazado', 'Rechazado'),
        ]
    )

    class Meta:
        verbose_name = 'Reclamación'
        verbose_name_plural = 'Reclamaciones'
        ordering = ['-created_at']

    def __str__(self):
        return f"Reclamación {self.id} - {self.nombre} {self.apellido} - {self.tipo_reclamacion}"

