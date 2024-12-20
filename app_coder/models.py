from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100, unique=False)
    año = models.PositiveIntegerField()
    autor = models.CharField(max_length=100, unique=False)
    
    def __str__(self):
        return self.titulo

class Critico(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.nombre

class Reseña(models.Model):
    texto = models.TextField()
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="reseñas")
    critico = models.ForeignKey(Critico, on_delete=models.CASCADE, related_name="reseñas")

    def __str__(self):
        return f"Review del crítico {self.critico.nombre} para el libro {self.libro.titulo}"
