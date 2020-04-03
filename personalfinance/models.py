from django.db import models

# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length = 15, unique = True)
    description = models.CharField(max_length = 25)
    image = models.URLField(unique = True)
    
    def  __str__(self):
        return self.name


class RelationshipTag(models.Model):
    name = models.CharField(max_length = 15, unique = True)

    def __str__(self):
        return self.name


class AssociatedPerson(models.Model):
    name = models.CharField(max_length =  20, unique = True)
    relationship_tag = models.ForeignKey(RelationshipTag, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name


class Expense(models.Model):
    tags = models.ForeignKey(Tags, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 30)
    Date = models.DateField()
    amount = models.IntegerField()
    associatedPerson =  models.ForeignKey(AssociatedPerson, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name


class Budget(models.Model):
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    QUARTELY = 'QUARTELY'
    YEARLY = 'YEARLY'
    BUDGET_PERIOD = [
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (QUARTELY, 'Quartely'),
        (YEARLY, 'Yearly'),
    ]
    period = models.CharField(choices=BUDGET_PERIOD, default=MONTHLY, max_length= 8)
    amount = models.IntegerField()
    tag = models.ForeignKey(Tags, on_delete = models.DO_NOTHING)
    name = models.CharField(unique = True, max_length = 20)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.name