# Generated by Django 4.0.3 on 2022-04-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_itempedido_variacao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='Preço promocional'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='produto_id',
            field=models.PositiveIntegerField(verbose_name='Produto ID'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(max_length=255, verbose_name='Variação'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveIntegerField(verbose_name='Variação ID'),
        ),
    ]
