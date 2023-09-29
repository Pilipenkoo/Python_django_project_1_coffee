from django.db import models
    
    
    
    
class Product_K(models.Model):
    name = models.CharField( "Название",max_length=255,db_index=True)
    weight = models.PositiveIntegerField("Вес,г")
    price = models.DecimalField("Цена",max_digits=10, decimal_places=2)
    composition = models.TextField("Описание")
    image = models.ImageField("Изображение",upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Ассортимент на Краснознаменской"
        
        
class Product_B(models.Model):
    name = models.CharField( "Название",max_length=255)
    weight = models.PositiveIntegerField("Вес,г")
    price = models.DecimalField("Цена",max_digits=10, decimal_places=2)
    composition = models.TextField("Описание")
    image = models.ImageField("Изображение",upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Ассортимент на Бульваре"
        
class Product_C(models.Model):
    name = models.CharField( "Название",max_length=255)
    weight = models.PositiveIntegerField("Вес,г")
    price = models.DecimalField("Цена",max_digits=10, decimal_places=2)
    composition = models.TextField("Описание")
    image = models.ImageField("Изображение",upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Ассортимент на Черёмушках"
    