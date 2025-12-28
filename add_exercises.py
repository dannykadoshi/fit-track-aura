import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fittrack_project.settings')
django.setup()

from workouts.models import Exercise

exercises = [
    # Strength - Upper Body
    ('Bench Press', 'strength'),
    ('Incline Bench Press', 'strength'),
    ('Decline Bench Press', 'strength'),
    ('Dumbbell Press', 'strength'),
    ('Dumbbell Flyes', 'strength'),
    ('Push-Ups', 'strength'),
    ('Dips', 'strength'),
    ('Tricep Dips', 'strength'),
    ('Overhead Press', 'strength'),
    ('Arnold Press', 'strength'),
    ('Lateral Raises', 'strength'),
    ('Front Raises', 'strength'),
    ('Shrugs', 'strength'),
    ('Bicep Curls', 'strength'),
    ('Hammer Curls', 'strength'),
    ('Skull Crushers', 'strength'),
    ('Cable Crossovers', 'strength'),
    ('Chest Press Machine', 'strength'),
    
    # Strength - Back
    ('Pull-Ups', 'strength'),
    ('Chin-Ups', 'strength'),
    ('Lat Pulldown', 'strength'),
    ('Barbell Row', 'strength'),
    ('Dumbbell Row', 'strength'),
    ('T-Bar Row', 'strength'),
    ('Cable Rows', 'strength'),
    ('Face Pulls', 'strength'),
    ('Reverse Flyes', 'strength'),
    ('Deadlift', 'strength'),
    ('Romanian Deadlift', 'strength'),
    
    # Strength - Legs
    ('Squats', 'strength'),
    ('Front Squats', 'strength'),
    ('Leg Press', 'strength'),
    ('Lunges', 'strength'),
    ('Walking Lunges', 'strength'),
    ('Bulgarian Split Squats', 'strength'),
    ('Leg Extensions', 'strength'),
    ('Leg Curls', 'strength'),
    ('Calf Raises', 'strength'),
    ('Hip Thrusts', 'strength'),
    ('Glute Bridges', 'strength'),
    ('Step-Ups', 'strength'),
    
    # Strength - Core
    ('Plank', 'strength'),
    ('Side Plank', 'strength'),
    ('Crunches', 'strength'),
    ('Bicycle Crunches', 'strength'),
    ('Russian Twists', 'strength'),
    ('Leg Raises', 'strength'),
    ('Hanging Knee Raises', 'strength'),
    ('Ab Wheel', 'strength'),
    ('Mountain Climbers', 'strength'),
    ('Flutter Kicks', 'strength'),
    ('Dead Bug', 'strength'),
    
    # Cardio
    ('Treadmill', 'cardio'),
    ('Running', 'cardio'),
    ('Cycling', 'cardio'),
    ('Stationary Bike', 'cardio'),
    ('Rowing Machine', 'cardio'),
    ('Elliptical', 'cardio'),
    ('Stair Climber', 'cardio'),
    ('Jump Rope', 'cardio'),
    ('Jumping Jacks', 'cardio'),
    ('Burpees', 'cardio'),
    ('High Knees', 'cardio'),
    ('Box Jumps', 'cardio'),
    ('Battle Ropes', 'cardio'),
    ('Swimming', 'cardio'),
    
    # Flexibility
    ('Stretching', 'flexibility'),
    ('Yoga', 'flexibility'),
    ('Pilates', 'flexibility'),
    
    # Sports
    ('Basketball', 'sports'),
    ('Soccer', 'sports'),
    ('Tennis', 'sports'),
]

print("Adding/updating exercises...")
for name, category in exercises:
    obj, created = Exercise.objects.get_or_create(name=name, defaults={'category': category})
    if created:
        print(f"✅ Added {name} ({category})")
    else:
        # Update category if it's different
        if obj.category != category:
            obj.category = category
            obj.save()
            print(f"🔄 Updated {name} → {category}")
        else:
            print(f"⏭️  Skipped {name} (already correct)")

print(f"\n🎉 Total exercises in database: {Exercise.objects.count()}")