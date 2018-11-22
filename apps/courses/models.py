from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self,form):
        errors=[]
        if len(form['name'])<5:
            errors.append("Name must be at least 5 characters length")
        if len(form['description'])<15:
            errors.append("Description must be at least 15 characters length")
        course_list=self.filter(name=form['name'])
        if len(course_list)>0:
            errors.append('The course already exists!')
        return errors
    def create_course(self,form):
        course=self.create(
            name=form['name'],
            description=form['description']
            )
        return course
    def LoadAll(self):
        list=self.all()
        return list
    def delete(self,cid):
        self.get(id=cid).delete()
    def Load(self,cid):
        course=self.get(id=cid)
        return course
class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    objects=CourseManager()
