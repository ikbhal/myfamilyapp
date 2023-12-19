# health/admin.py

# health/admin.py

from django.contrib import admin
from .models import FamilyMember, Exercise, Nutrition, WaterDrinking

# @admin.register(FamilyMember)
# class FamilyMemberAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age',)  # Add other fields you want to display in the list

# admin.site.register(Exercise)
# admin.site.register(Nutrition)
# admin.site.register(WaterDrinking)

# health/admin.py

from django.contrib import admin
# from .models import FamilyMember, Exercise, Nutrition, WaterDrinking, Bath, Toilet
# from .models import Namaz, QuranReading, Zikir, Roja, Cycling
# from .models import Cooking, CleanHouse, TeachingKids, PayLoans, EarnMoney

from .models import (
    FamilyMember, Exercise, Nutrition, WaterDrinking, Bath, Toilet,
    Namaz, QuranReading, Zikir, Roja, Cycling,
    Cooking, CleanHouse, TeachingKids, PayLoans, EarnMoney,
    SchoolGoing, HomeItemsBuying, EveningTeaBreak, Walking
)

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)

@admin.register(Exercise, Nutrition, WaterDrinking, Bath, Toilet)
class HealthActivityAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date',)

@admin.register(Namaz, QuranReading, Zikir, Roja, Cycling)
class SpiritualActivityAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date',)

@admin.register(Cooking, CleanHouse, TeachingKids, PayLoans, EarnMoney)
class DailyActivitiesAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date',)

@admin.register(SchoolGoing, HomeItemsBuying, EveningTeaBreak, Walking)
class OtherActivitiesAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date',)