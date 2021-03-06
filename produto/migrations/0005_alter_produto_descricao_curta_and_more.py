# Generated by Django 4.0.3 on 2022-04-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_curta',
            field=models.TextField(max_length=255, verbose_name='Descrição Curta'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(verbose_name='Descrição Longa'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço Marketing'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Marketing Promocional'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promocional'),
        ),
    ]
