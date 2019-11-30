# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-24 10:43
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("budgetportal", "0036_auto_20191023_1343")]

    operations = [
        migrations.CreateModel(
            name="IRMSnapshot",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_taken", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "financial_year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="budgetportal.FinancialYear",
                    ),
                ),
            ],
            options={"ordering": ["financial_year", "quarter"]},
        ),
        migrations.CreateModel(
            name="ProvInfraProjectSnapshot",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "project_number",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                ("name", models.CharField(blank=True, max_length=1024, null=True)),
                ("province", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "department",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "local_municipality",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "district_municipality",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                ("latitude", models.CharField(blank=True, max_length=20, null=True)),
                ("longitude", models.CharField(blank=True, max_length=20, null=True)),
                ("status", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "budget_programme",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "primary_funding_source",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "nature_of_investment",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "funding_status",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "program_implementing_agent",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "principle_agent",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "main_contractor",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                ("other_parties", models.TextField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                (
                    "estimated_construction_start_date",
                    models.DateField(blank=True, null=True),
                ),
                ("estimated_completion_date", models.DateField(blank=True, null=True)),
                (
                    "contracted_construction_end_date",
                    models.DateField(blank=True, null=True),
                ),
                (
                    "estimated_construction_end_date",
                    models.DateField(blank=True, null=True),
                ),
                (
                    "total_professional_fees",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "total_construction_costs",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "variation_orders",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "total_project_cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "expenditure_from_previous_years_professional_fees",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "expenditure_from_previous_years_construction_costs",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "expenditure_from_previous_years_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "project_expenditure_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "main_appropriation_professional_fees",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "adjustment_appropriation_professional_fees",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "main_appropriation_construction_costs",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "adjustment_appropriation_construction_costs",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "main_appropriation_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "adjustment_appropriation_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "actual_expenditure_q1",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "actual_expenditure_q2",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "actual_expenditure_q3",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "actual_expenditure_q4",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "irm_snapshot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_snapshots",
                        to="budgetportal.IRMSnapshot",
                    ),
                ),
            ],
            options={
                "ordering": ["irm_snapshot"],
                "verbose_name": "Provincial infrastructure project snapshot",
            },
        ),
        migrations.CreateModel(
            name="Quarter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True)),
            ],
            options={"ordering": ["number"]},
        ),
        migrations.AlterModelOptions(
            name="provinfraproject",
            options={"verbose_name": "Provincial infrastructure project"},
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="actual_expenditure_q1"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="actual_expenditure_q2"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="actual_expenditure_q3"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="actual_expenditure_q4"
        ),
        migrations.RemoveField(
            model_name="provinfraproject",
            name="adjustment_appropriation_construction_costs",
        ),
        migrations.RemoveField(
            model_name="provinfraproject",
            name="adjustment_appropriation_professional_fees",
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="adjustment_appropriation_total"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="budget_programme"),
        migrations.RemoveField(
            model_name="provinfraproject", name="contracted_construction_end_date"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="department"),
        migrations.RemoveField(
            model_name="provinfraproject", name="district_municipality"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="estimated_completion_date"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="estimated_construction_end_date"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="estimated_construction_start_date"
        ),
        migrations.RemoveField(
            model_name="provinfraproject",
            name="expenditure_from_previous_years_construction_costs",
        ),
        migrations.RemoveField(
            model_name="provinfraproject",
            name="expenditure_from_previous_years_professional_fees",
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="expenditure_from_previous_years_total"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="financial_year"),
        migrations.RemoveField(model_name="provinfraproject", name="funding_status"),
        migrations.RemoveField(model_name="provinfraproject", name="latitude"),
        migrations.RemoveField(
            model_name="provinfraproject", name="local_municipality"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="longitude"),
        migrations.RemoveField(
            model_name="provinfraproject", name="main_appropriation_construction_costs"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="main_appropriation_professional_fees"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="main_appropriation_total"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="main_contractor"),
        migrations.RemoveField(model_name="provinfraproject", name="name"),
        migrations.RemoveField(
            model_name="provinfraproject", name="nature_of_investment"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="other_parties"),
        migrations.RemoveField(
            model_name="provinfraproject", name="primary_funding_source"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="principle_agent"),
        migrations.RemoveField(
            model_name="provinfraproject", name="program_implementing_agent"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="project_expenditure_total"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="project_number"),
        migrations.RemoveField(model_name="provinfraproject", name="province"),
        migrations.RemoveField(model_name="provinfraproject", name="start_date"),
        migrations.RemoveField(model_name="provinfraproject", name="status"),
        migrations.RemoveField(
            model_name="provinfraproject", name="total_construction_costs"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="total_professional_fees"
        ),
        migrations.RemoveField(
            model_name="provinfraproject", name="total_project_cost"
        ),
        migrations.RemoveField(model_name="provinfraproject", name="variation_orders"),
        migrations.AddField(
            model_name="provinfraprojectsnapshot",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project_snapshots",
                to="budgetportal.ProvInfraProject",
            ),
        ),
        migrations.AddField(
            model_name="irmsnapshot",
            name="quarter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="budgetportal.Quarter"
            ),
        ),
    ]
