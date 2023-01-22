from django.db import models

class Inventory(models.Model):
    CATEGORY_CHOICES = [
        ('Consumable', 'consumable'),
        ('Non-Consumable', 'non_consumable'),
    ]
    inventoryId = models.AutoField(primary_key=True,max_length=11,null=False)
    inventoryName = models.CharField(max_length=150, null=False, blank=False)
    category =  models.CharField(max_length=150, null=False, choices=CATEGORY_CHOICES, default='consumable')
    inventoryType=models.CharField(max_length=100)
    inventoryQuantity=models.IntegerField( blank=True)
    inventoryUnit=models.CharField(max_length=15)
    inventoryTotal=models.IntegerField(blank=True)
    quantityLevel=models.FloatField(null=True)
    inventoryDate=models.DateTimeField()
    inventoryStatus=models.IntegerField(default=1)
    inventoryComment=models.CharField(max_length=500,blank=True)
    inventoryExpiryDate=models.DateTimeField()
    inventoryLastUpdatedDate=models.DateTimeField()
    emailFlag=models.IntegerField(default=1)
    inventoryStatusFlag=models.IntegerField(default=1)
    alternateEmail = models.CharField(max_length=100, blank=True)
    referenceInventoryID = models.IntegerField(blank=True)
    isDisable = models.IntegerField(default=0)
    purchaseUnit = models.CharField(max_length=100, blank=True, null=True)
    materialCode = models.CharField(max_length=100, default='')
    unitQuantity = models.FloatField(default=1)
    tax = models.FloatField(default=0)
    hsn_code = models.CharField(max_length=100, null=True, blank=True)
    catalog_code = models.CharField(max_length=100, null=True, blank=True)
    department=models.CharField(max_length=100,blank=True,null=True)
