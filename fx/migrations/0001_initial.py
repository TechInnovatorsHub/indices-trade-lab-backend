# Generated by Django 4.2.7 on 2023-11-18 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "payment_gateway",
                    models.CharField(
                        choices=[("S", "stripe"), ("P", "paypal"), ("M", "mpesa")],
                        max_length=50,
                    ),
                ),
                ("customer_id", models.CharField(max_length=50)),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("D", "deposit"), ("W", "withdrawal")], max_length=1
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("P", "pending"), ("C", "complete")], max_length=1
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("symbol", models.CharField(max_length=10, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "trade_type",
                    models.CharField(
                        choices=[("B", "buy"), ("S", "sell")], max_length=1
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("O", "open"), ("C", "complete")],
                        default="O",
                        max_length=1,
                    ),
                ),
                ("ref_code", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fx.payment"
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fx.stock"
                    ),
                ),
            ],
        ),
    ]
