from django.db import models

# Modelo para la tabla 'roles'
class Rol(models.Model):
    # id: BIGSERIAL PRIMARY KEY -> Django lo crea automáticamente (BigAutoField por defecto)
    nombre = models.CharField(max_length=64, unique=True, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        # Opcional: Especifica el nombre de la tabla si quieres que coincida exactamente
        # con tu SQL (Django usaría 'app_rol' por defecto)
        db_table = 'roles'


# Modelo para la tabla 'usuarios'
class Usuario(models.Model):
    # id: BIGSERIAL PRIMARY KEY -> Django lo crea automáticamente (BigAutoField por defecto)
    nombre = models.CharField(max_length=64, null=False)
    # email: VARCHAR(64) NOT NULL UNIQUE -> EmailField valida formato de email
    email = models.EmailField(max_length=64, unique=True, null=False)

    # --- ¡ADVERTENCIA DE SEGURIDAD IMPORTANTE! ---
    # password: VARCHAR(128) NOT NULL
    # Almacenar contraseñas directamente como texto plano o incluso hasheadas manualmente
    # NO es seguro. Django tiene un sistema de autenticación robusto incorporado
    # que maneja el hashing seguro de contraseñas.
    #
    # Se RECOMIENDA ENCARECIDAMENTE usar o extender el modelo User de Django
    # (django.contrib.auth.models.User o AbstractUser/AbstractBaseUser)
    # en lugar de manejar la contraseña manualmente de esta forma.
    #
    # Si DEBES mapear este campo exactamente como está en tu SQL (NO RECOMENDADO):
    password = models.CharField(max_length=128, null=False)
    # ---------------------------------------------

    # imagen: BYTEA -> BinaryField para datos binarios
    imagen = models.BinaryField(null=True, blank=True) # null=True/blank=True si la imagen es opcional

    # Relación ManyToMany con Rol
    # Esto maneja automáticamente la tabla intermedia 'usuario_roles'
    # related_name permite acceder a los usuarios desde un objeto Rol (ej: mi_rol.usuarios.all())
    roles = models.ManyToManyField(Rol, related_name='usuarios', db_table='usuario_roles')
    # Django nombraría la tabla intermedia como 'app_usuario_roles' por defecto.
    # Usamos db_table='usuario_roles' para que coincida con tu SQL.

    def __str__(self):
        return self.nombre

    class Meta:
        # Opcional: Especifica el nombre de la tabla si quieres que coincida exactamente
        # con tu SQL (Django usaría 'app_usuario' por defecto)
        db_table = 'usuarios'
