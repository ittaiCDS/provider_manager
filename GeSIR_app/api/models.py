from django.db import models

# Create your models here.--

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = "Categoria"
    def __str__(self):
        return self.name

class Proveedor(models.Model):
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT)
    clave = models.IntegerField(null=False)
    nombre = models.CharField(max_length=250, blank=True)
    estado = models.CharField(max_length=250)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = "Proveedor"
    def __str__(self):
        return self.name
    
class Cordenadas(models.Model):
    id_proveedor = models.IntegerField(null=False)
    id_plano_proveedor = models.IntegerField(null=False)
    id_poly = models.IntegerField(null=False)
    coords = models.CharField(max_length=21800)
    class Meta:
        db_table = "Cordenadas"
    def __str__(self):
        return self.name

class Pais(models.Model):
    nombre = models.CharField(max_length=250)
    lenguaje = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=50)
    class Meta:
        db_table = "Pais"
    def __str__(self):
        return self.name
    
class Estado(models.Model):
    pais = models.ForeignKey("Pais", on_delete=models.PROTECT)
    nombre = models.CharField(max_length=250)
    clave = models.CharField(max_length=50)
    class Meta:
        db_table = "Estado"
    def __str__(self):
        return self.name
    
class Municipio(models.Model):
    estado = models.ForeignKey("Estado", on_delete=models.PROTECT)
    nombre = models.CharField(max_length=250)
    clave = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = "Municipio"
    def __str__(self):
        return self.name

class Lugar(models.Model):
    estado = models.ForeignKey("Estado", on_delete=models.PROTECT)
    calle = models.CharField(max_length=250)
    colonia = models.CharField(max_length=250)
    cp = models.CharField(max_length=50)
    referencia = models.CharField(max_length=250)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = "Lugar"
    def __str__(self):
        return self.name
    
    
class Incidente(models.Model):
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT)
    cliente = models.CharField(max_length=250)
    fecha_publicado = models.DateTimeField()
    fecha_aceptado = models.DateTimeField()
    fecha_tomado = models.DateTimeField()
    fecha_atendido = models.DateTimeField()
    estatus = models.IntegerField(null=False)
    class Meta:
        db_table = "Incidente"
    def __str__(self):
        return self.name

class Tipo_Lugar(models.Model):    
    descripcion = models.CharField(max_length=250)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = "Tipo_Lugar"
    def __str__(self):
        return self.name
    
class Rel_Incidente_Lugar(models.Model):
    incidente = models.ForeignKey("Incidente", on_delete=models.PROTECT)
    lugar = models.ForeignKey("Lugar", on_delete=models.PROTECT)
    tipo = models.ForeignKey("Tipo_Lugar", on_delete=models.PROTECT)
    class Meta:
        db_table = "Rel_Incidente_Lugar"
    def __str__(self):
        return self.name
    
    
class Cobertura(models.Model):
    proveedor = models.ForeignKey("Proveedor", on_delete=models.PROTECT)
    municipio = models.ForeignKey("Municipio", on_delete=models.PROTECT)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = "Cobertura"
    def __str__(self):
        return self.name