from django.db import models


# Custom Manager do model Cource
class CourseManager(models.Manager):
    def search(self, query):
        # Lista os cursos que contem <query> no nome e na descrição
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )


# Model Course
class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    # substitui o Manager pelo Custom Manager
    objects = CourseManager()

    def __str__(self):
        return self.name

    ## Cria a url para acessar os detalhes do curso
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('courses:details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        # ordering = ['name']   # Ascending
        ordering = ['-name']  # Descending
