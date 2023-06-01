from django.db import models

# Create your models here.

class CaseStudies(models.Model):
    casestudyname = models.CharField(db_column='CaseStudyName', max_length=200)  # Field name made lowercase.       
    account = models.CharField(db_column='Account', max_length=50)  # Field name made lowercase.
    vertical = models.CharField(db_column='Vertical', max_length=50)  # Field name made lowercase.
    spoc = models.CharField(max_length=50, blank=True, null=True)
    solutionname = models.CharField(db_column='SolutionName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    serviceofferingmapping = models.CharField(db_column='ServiceOfferingMapping', max_length=150, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    metadata = models.CharField(db_column='MetaData', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=255, blank=True, null=True)  # Field name made lowercase.  
    casestudypoc = models.CharField(db_column='CaseStudyPOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customerreferenceable = models.CharField(db_column='CustomerReferenceable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dependency = models.CharField(db_column='Dependency', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'case_studies'