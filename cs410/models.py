# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from simple_history.models import HistoricalRecords


class Main(models.Model):
    vehicle_id = models.IntegerField(db_column='Vehicle_ID', primary_key=True)  # Field name made lowercase.
    make = models.ForeignKey('Makes', models.DO_NOTHING, db_column='Make_ID')  # Field name made lowercase.
    model = models.ForeignKey('Models', models.DO_NOTHING, db_column='Model_ID')  # Field name made lowercase.
    make_name = models.CharField(db_column='Make_Name', max_length=255)  # Field name made lowercase.
    model_name = models.CharField(db_column='Model_Name', max_length=255)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=255)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    history = HistoricalRecords()

    class Meta:
        managed  = False
        db_table = 'Main'


class Makes(models.Model):
    make_id = models.IntegerField(db_column='Make_ID', primary_key=True)  # Field name made lowercase.
    make_name = models.CharField(db_column='Make_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Makes'


class Models(models.Model):
    model_id = models.IntegerField(db_column='Model_ID', primary_key=True)  # Field name made lowercase.
    model_name = models.CharField(db_column='Model_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    make = models.ForeignKey(Makes, models.DO_NOTHING, db_column='Make_ID')  # Field name made lowercase.
    rfid = models.ForeignKey('Ratings', models.DO_NOTHING, db_column='RFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Models'


class Ratings(models.Model):
    ratingid = models.IntegerField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=255)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    overallfrontcrashrating = models.IntegerField(db_column='OverallFrontCrashRating', blank=True, null=True)  # Field name made lowercase.
    frontcrashdriversiderating = models.IntegerField(db_column='FrontCrashDriversideRating', blank=True, null=True)  # Field name made lowercase.
    frontcrashpassengersiderating = models.IntegerField(db_column='FrontCrashPassengersideRating', blank=True, null=True)  # Field name made lowercase.
    overallsidecrashrating = models.IntegerField(db_column='OverallSideCrashRating', blank=True, null=True)  # Field name made lowercase.
    sidecrashdriversiderating = models.IntegerField(db_column='SideCrashDriversideRating', blank=True, null=True)  # Field name made lowercase.
    sidecrashpassengersiderating = models.IntegerField(db_column='SideCrashPassengersideRating', blank=True, null=True)  # Field name made lowercase.
    combinedsidebarrierandpoleratingfront = models.IntegerField(db_column='combinedSideBarrierAndPoleRatingFront', blank=True, null=True)  # Field name made lowercase.
    combinedsidebarrierandpoleratingrear = models.IntegerField(db_column='combinedSideBarrierAndPoleRatingRear', blank=True, null=True)  # Field name made lowercase.
    sidebarrierratingoverall = models.IntegerField(db_column='sideBarrierRatingOverall', blank=True, null=True)  # Field name made lowercase.
    rolloverrating = models.IntegerField(db_column='RolloverRating', blank=True, null=True)  # Field name made lowercase.
    rolloverrating2 = models.IntegerField(db_column='RolloverRating2', blank=True, null=True)  # Field name made lowercase.
    rolloverpossibility = models.IntegerField(db_column='RolloverPossibility', blank=True, null=True)  # Field name made lowercase.
    rolloverpossibility2 = models.IntegerField(db_column='RolloverPossibility2', blank=True, null=True)  # Field name made lowercase.
    dynamictipresult = models.IntegerField(db_column='dynamicTipResult', blank=True, null=True)  # Field name made lowercase.
    sidepolecrashrating = models.IntegerField(db_column='SidePoleCrashRating', blank=True, null=True)  # Field name made lowercase.
    vehicle_id = models.ForeignKey('Main', models.DO_NOTHING, db_column='Vehicle_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ratings'


class States(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    rfid = models.ForeignKey(Ratings, models.DO_NOTHING, db_column='RFID', blank=True, null=True)  # Field name made lowercase.
    premium = models.IntegerField(db_column='Premium', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'States'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cs410Historicalplaceholder(models.Model):
    id = models.BigIntegerField()
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs410_historicalplaceholder'


class Cs410Placeholder(models.Model):
    id = models.BigAutoField(primary_key=True)
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cs410_placeholder'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
