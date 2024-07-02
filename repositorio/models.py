from django.db import models

# Modelo de negocio de la aplicación.

#modelo de alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    #numero_legajo = models.IntegerField(unique=True)
    materias = models.ManyToManyField('Materia', through='AlumnoMateria')
    profesores = models.ManyToManyField('Profesor', through='AlumnoProfesor')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#modelo profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    materias = models.ManyToManyField('Materia', through='MateriaProfesor')
    mail= models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#modelo materia
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

#modelo curso
class Curso(models.Model):
#opcones de turnos   
    Turnos = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('vespertino', 'Vespertino'),
    ]

    nombre = models.CharField(max_length=100)
    division = models.CharField(max_length=10)
    turno = models.CharField(max_length=50, choices=Turnos)
    alumnos = models.ManyToManyField(Alumno, through='AlumnoCurso')
    profesores = models.ManyToManyField(Profesor, through='CursoProfesor')
    materias = models.ManyToManyField(Materia, through='CursoMateria')

    def __str__(self):
        return f"{self.nombre} - {self.division} ({self.get_turno_display()})"

#modelo relación alumno materia
class AlumnoMateria(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relación alumno profesor
class AlumnoProfesor(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relación alumno curso
class AlumnoCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

#modelo relación curso profesor
class CursoProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relación curso materia
class CursoMateria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relacion materia profesor
class MateriaProfesor(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)