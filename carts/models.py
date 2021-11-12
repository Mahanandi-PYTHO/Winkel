from django.db import models
from Store.models import product,Variation

# Create your models here.
from Accounts.models import Account


class Cart(models.Model):
    cart_id = models.CharField(blank=True, max_length=250)
    date_added = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation,blank=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity


    def __unicode__(self):
        return self.product
