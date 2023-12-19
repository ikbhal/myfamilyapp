# health/models.py

from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add other fields related to family members

    def __str__(self):
        return f"{self.name} (Age: {self.age})"

class Exercise(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.family_member.name} - {self.exercise_name} ({self.duration_minutes} minutes on {self.date})"

class Nutrition(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    meal_description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.family_member.name} - Nutrition ({self.date})"

class WaterDrinking(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    glasses_count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.family_member.name} - Water Drinking ({self.glasses_count} glasses on {self.date})"

class Bath(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f"{self.family_member.name} - Bath ({self.duration_minutes} minutes on {self.date})"

class Toilet(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    activities = models.TextField()

    def __str__(self):
        return f"{self.family_member.name} - Toilet ({self.date})"
    
class Namaz(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    fajr = models.BooleanField(default=False, verbose_name='Fajr')
    dhuhr = models.BooleanField(default=False, verbose_name='Dhuhr')
    asr = models.BooleanField(default=False, verbose_name='Asr')
    maghrib = models.BooleanField(default=False, verbose_name='Maghrib')
    isha = models.BooleanField(default=False, verbose_name='Isha')
    # You can add additional fields related to Namaz tracking

    def __str__(self):
        return f"{self.family_member.name} - Namaz on {self.date}"


class QuranReading(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    # You can add additional fields related to Quran Reading tracking

    def __str__(self):
        return f"{self.family_member.name} - Quran Reading on {self.date}"

class Zikir(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    # You can add additional fields related to Zikir tracking

    def __str__(self):
        return f"{self.family_member.name} - Zikir on {self.date}"

class Roja(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    # You can add additional fields related to Roja tracking

    def __str__(self):
        return f"{self.family_member.name} - Roja on {self.date}"

class Cycling(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    duration_minutes = models.IntegerField()
    # You can add additional fields related to Cycling tracking

    def __str__(self):
        return f"{self.family_member.name} - Cycling ({self.duration_minutes} minutes on {self.date})"

class Cooking(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    meal_description = models.TextField()
    # You can add additional fields related to Cooking tracking

    def __str__(self):
        return f"{self.family_member.name} - Cooking ({self.date})"
    
class Cooking(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    meal_description = models.TextField()
    # You can add additional fields related to Cooking tracking

    def __str__(self):
        return f"{self.family_member.name} - Cooking ({self.date})"
    

class TeachingKids(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    # You can add additional fields related to Teaching Kids tracking

    def __str__(self):
        return f"{self.family_member.name} - Teaching Kids ({self.subject} for {self.duration_minutes} minutes on {self.date})"

class PayLoans(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    # You can add additional fields related to Pay Loans tracking

    def __str__(self):
        return f"{self.family_member.name} - Pay Loans ({self.amount_paid} on {self.date})"

class EarnMoney(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    amount_earned = models.DecimalField(max_digits=10, decimal_places=2)
    # You can add additional fields related to Earn Money tracking

    def __str__(self):
        return f"{self.family_member.name} - Earn Money ({self.amount_earned} on {self.date})"
  
class CleanHouse(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    clean_floor = models.BooleanField(default=False, verbose_name='Clean Floor')
    clean_toilet = models.BooleanField(default=False, verbose_name='Clean Toilet')
    # You can add additional fields related to Clean House tracking

    def __str__(self):
        return f"{self.family_member.name} - Clean House on {self.date}"
    

class SchoolGoing(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    went_to_school = models.BooleanField(default=False, verbose_name='Went to School')
    # You can add additional fields related to SchoolGoing tracking

    def __str__(self):
        return f"{self.family_member.name} - School Going on {self.date}"

# health/models.py

class HomeItemsBuying(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    bought_milk = models.BooleanField(default=False, verbose_name='Bought Milk')
    bought_eggs = models.BooleanField(default=False, verbose_name='Bought Eggs')
    bought_curd = models.BooleanField(default=False, verbose_name='Bought Curd')
    bought_vegetables = models.BooleanField(default=False, verbose_name='Bought Vegetables')
    bought_fruits = models.BooleanField(default=False, verbose_name='Bought Fruits')
    # You can add additional fields related to Home Items Buying tracking

    def __str__(self):
        return f"{self.family_member.name} - Home Items Buying on {self.date}"

class EveningTeaBreak(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    duration_minutes = models.IntegerField()
    # You can add additional fields related to Evening Tea Break tracking

    def __str__(self):
        return f"{self.family_member.name} - Evening Tea Break ({self.duration_minutes} minutes on {self.date})"

class Walking(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    date = models.DateField()
    duration_minutes = models.IntegerField()
    # You can add additional fields related to Walking tracking

    def __str__(self):
        return f"{self.family_member.name} - Walking ({self.duration_minutes} minutes on {self.date})"