# Generated by Django 4.0.7 on 2022-11-02 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0003_alter_nowbr_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ComMlist',
            new_name='ComMuseumList',
        ),
        migrations.RenameModel(
            old_name='NowTuBound',
            new_name='NowTimeUnitBoundary',
        ),
        migrations.RenameModel(
            old_name='NowTuSequence',
            new_name='NowTimeUnitSequence',
        ),
        migrations.RenameModel(
            old_name='NowBau',
            new_name='NowTimeUnitBoundaryUpdate',
        ),
        migrations.RenameModel(
            old_name='RefRefType',
            new_name='RefReferenceType',
        ),
        migrations.RenameModel(
            old_name='RefRef',
            new_name='RefReference',
        ),
        migrations.RenameModel(
            old_name='NowBr',
            new_name='NowTimeUnitBoundaryUpdateReference',
        ),
        migrations.RenameModel(
            old_name='NowCollMethValues',
            new_name='NowCollectingMethodValue',
        ),
        migrations.RenameModel(
            old_name='NowLoc',
            new_name='NowLocality',
        ),
        migrations.RenameModel(
            old_name='NowCollMeth',
            new_name='NowCollectingMethod',
        ),
        migrations.RenameModel(
            old_name='NowLau',
            new_name='NowLocalityUpdate',
        ),
        migrations.RenameModel(
            old_name='NowLr',
            new_name='NowLocalityUpdateReference',
        ),
        migrations.RenameModel(
            old_name='NowLs',
            new_name='NowLocalitySpecies',
        ),
        migrations.RenameModel(
            old_name='NowLsCopy',
            new_name='NowLocalitySpeciesCopy',
        ),
        migrations.RenameModel(
            old_name='NowMus',
            new_name='NowMuseum',
        ),
        migrations.RenameModel(
            old_name='NowProj',
            new_name='NowProject',
        ),
        migrations.RenameModel(
            old_name='NowProjPeople',
            new_name='NowProjectPeople',
        ),
        migrations.RenameModel(
            old_name='NowPlr',
            new_name='NowProjectLocality',
        ),
        migrations.RenameModel(
            old_name='NowPsr',
            new_name='NowProjectSpecies',
        ),
        migrations.RenameModel(
            old_name='NowSau',
            new_name='NowSpeciesUpdate',
        ),
        migrations.RenameModel(
            old_name='NowSr',
            new_name='NowSpeciesUpdateReference',
        ),
        migrations.RenameModel(
            old_name='NowSs',
            new_name='NowSedimentaryStructure',
        ),
        migrations.RenameModel(
            old_name='NowSsValues',
            new_name='NowSedimentaryStructureValue',
        ),
        migrations.RenameModel(
            old_name='NowSynLoc',
            new_name='NowLocalitySynonym',
        ),
        migrations.RenameModel(
            old_name='NowTau',
            new_name='NowTimeUnitUpdate',
        ),
        migrations.RenameModel(
            old_name='NowTur',
            new_name='NowTimeUnitBoundaryReference',
        ),
        migrations.RenameModel(
            old_name='NowTr',
            new_name='NowTimeUnitUpdateReference',
        ),
    ]
