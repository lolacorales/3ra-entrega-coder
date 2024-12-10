from django.db import models

class libro(models.Model):
    titulo = models.CharField(max_length=100, unique=False)
    año = models.PositiveIntegerField(help_text="2020")
    autor = models.CharField(max_length=100, unique=False)
    
    def __str__(self):
        return self.titulo

class critico(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.nombre

class reseña(models.Model):
    texto = models.TextField()
    libro = models.ForeignKey(libro, on_delete=models.CASCADE, related_name="reseñas")
    critico = models.ForeignKey(critico, on_delete=models.CASCADE, related_name="reseñas")

    def __str__(self):
        return f"Review del crítico {self.critico.nombre} para el libro {self.libro.titulo}"
