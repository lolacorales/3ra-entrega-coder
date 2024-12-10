from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50, blank=True, null=True, help_text="Ejemplo: Vegetal, Carne, Lácteo, etc.")

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name="recetas")
    ingredientes = models.ManyToManyField(Ingrediente, related_name="recetas")
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    instrucciones = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
