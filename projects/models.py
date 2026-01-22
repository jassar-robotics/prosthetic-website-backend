# from cloudinary.uploader import destroy, upload
from django.db import models
from tinymce.models import HTMLField


from core.mixins import HomeImageProcessingMixin
from core.models import  BaseSlugModel, BaseModel
from projects.manager import AllManager, NonHiddenManager, HiddenManager
from components.models import Component






class Project(BaseSlugModel, HomeImageProcessingMixin):
    # Choice Definitions
    class HandChoices(models.TextChoices):
        LEFT = 'LEFT', 'Left'
        RIGHT = 'RIGHT', 'Right'

    class StatusChoices(models.TextChoices):
        UPCOMING = 'UPCOMING', 'Upcoming'
        ONGOING = 'ONGOING', 'Ongoing'
        FINAL = 'FINAL', 'Final'

    # Basic Info
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    which_hand = models.CharField(max_length=10, choices=HandChoices.choices, default=HandChoices.RIGHT)
    circuit_diagram = models.FileField(upload_to='projects/circuits/', blank=True, null=True) # .sch
    manuals = models.FileField(upload_to='projects/manuals/', blank=True, null=True) # .pdf
    video_url = models.URLField(blank=True, null=True)

    # Meta & Description
    software_github_link = models.URLField(blank=True, null=True)
    video_description_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default=StatusChoices.UPCOMING)
    version = models.CharField(max_length=20, blank=True)
    description = HTMLField()

    # Relations & Visibility
    # stories = models.ManyToManyField('Stories', blank=True)
    is_hidden = models.BooleanField(default=False)

    # Contributor URLs
    mechanical_github_repo_folder = models.URLField(blank=True, null=True)
    electrical_github_repo = models.URLField(blank=True, null=True)
    software_github_repo = models.URLField(blank=True, null=True)
    vision = HTMLField(blank=True, null=True)

    # Contributor Files
    readme_mechanical = models.FileField(upload_to='projects/readmes/', blank=True, null=True)
    readme_electrical = models.FileField(upload_to='projects/readmes/', blank=True, null=True)
    readme_software = models.FileField(upload_to='projects/readmes/', blank=True, null=True)

    # Existing components and managers
    components = models.ManyToManyField(
        "components.Component",
        through="ComponentQuantityPerProject",
        related_name="projects",
        blank=True
    )


    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()
    
    class Meta:
        db_table = "projects"

    def __str__(self):
        return f"{self.id}: {self.name}"

    # def delete(self, *args, **kwargs):
    #     if self.image:
    #         try:
    #             destroy(self.image.public_id)
    #         except:
    #             pass 
    #     super().delete(*args, **kwargs)






        
class Story(BaseModel):
    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
        ('NP', 'Nepal'),
        ('DE', 'Germany'),
        ('IN', 'India'),
    ]

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='US')
    story_content = HTMLField()
    is_accepted = models.BooleanField(default=False)
    projects = models.ManyToManyField('Project', related_name='project_stories')

    class Meta:
        db_table = "stories"
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.name




class UseCase(BaseModel):
    heading = models.CharField(max_length=50)
    description = HTMLField()
    
    # Relationships
    projects = models.ManyToManyField(
        'Project', 
        related_name='use_cases'
    )

    class Meta:
        db_table = "use_cases"
        verbose_name = "Use Case"
        verbose_name_plural = "Use Cases"

    def __str__(self):
        return self.heading



class Stage(BaseModel):
    project = models.ForeignKey(
        'Project', 
        related_name="stages", 
        on_delete=models.CASCADE
    )
    stage_no = models.IntegerField()
    heading = models.CharField(max_length=100)
    description = HTMLField()
    image = models.ImageField(upload_to="stages/", null=True, blank=True)
    
    class Meta:
        db_table = "stages"
        ordering = ['project', 'stage_no']
        # Ensures Project A cannot have two "Stage 1" entries
        constraints = [
            models.UniqueConstraint(fields=['project', 'stage_no'], name='unique_stage_per_project')
        ]
        verbose_name = "Project Stage"
        verbose_name_plural = "Project Stages"

    def __str__(self):
        return f"{self.project.name} - Stage {self.stage_no}: {self.heading}"


        
class ComponentQuantityPerProject(BaseModel):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="component_quantities"
    )
    component = models.ForeignKey(
        "components.Component",
        on_delete=models.CASCADE,
        related_name="project_quantities"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "component_quantity_per_project"
        unique_together = ("project", "component")
        verbose_name = "Component Quantity per Project"
        verbose_name_plural = "Component Quantities per Project"

    def __str__(self):
        return f"{self.project.name} - {self.component.name} (x{self.quantity})"
    
    







class Statusboard(BaseSlugModel, HomeImageProcessingMixin):
    class StatusChoices(models.TextChoices):
        TODO = 'TODO', 'To Do'
        ONGOING = 'ONGOING', 'Ongoing'
        TESTING = 'TESTING', 'Testing'
        REVIEW = 'REVIEW', 'Review'
        ACCEPTED = 'ACCEPTED', 'Accepted'

    # New Fields
    projects = models.ManyToManyField(
        'projects.Project', 
        related_name='statusboards',
    )
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = models.CharField(
        max_length=20, 
        choices=StatusChoices.choices, 
        default=StatusChoices.TODO
    )

    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()

    class Meta:
        db_table = "statusboards"

    def __str__(self):
        return f"{self.heading} - {self.status}"
    