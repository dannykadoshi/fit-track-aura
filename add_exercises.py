import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fittrack_project.settings')
django.setup()

from workouts.models import Exercise

exercises = [
    # Upper Body
    ('Incline Bench Press', 'upper_body'),
    ('Dumbbell Flyes', 'upper_body'),
    ('Tricep Dips', 'upper_body'),
    ('Bicep Curls', 'upper_body'),
    ('Overhead Press', 'upper_body'),
    ('Lateral Raises', 'upper_body'),
    ('Front Raises', 'upper_body'),
    ('Skull Crushers', 'upper_body'),
    ('Hammer Curls', 'upper_body'),
    ('Cable Crossovers', 'upper_body'),
    ('Dips', 'upper_body'),
    ('Arnold Press', 'upper_body'),
    ('Chest Press Machine', 'upper_body'),
    
    # Back
    ('Pull-Ups', 'back'),
    ('Lat Pulldown', 'back'),
    ('Barbell Row', 'back'),
    ('Dumbbell Row', 'back'),
    ('Face Pulls', 'back'),
    ('Cable Rows', 'back'),
    ('T-Bar Row', 'back'),
    ('Chin-Ups', 'back'),
    ('Reverse Flyes', 'back'),
    
    # Legs
    ('Leg Press', 'legs'),
    ('Lunges', 'legs'),
    ('Leg Curls', 'legs'),
    ('Leg Extensions', 'legs'),
    ('Calf Raises', 'legs'),
    ('Bulgarian Split Squats', 'legs'),
    ('Romanian Deadlift', 'legs'),
    ('Hip Thrusts', 'legs'),
    ('Walking Lunges', 'legs'),
    ('Step-Ups', 'legs'),
    ('Glute Bridges', 'legs'),
    
    # Core
    ('Crunches', 'core'),
    ('Russian Twists', 'core'),
    ('Bicycle Crunches', 'core'),
    ('Leg Raises', 'core'),
    ('Side Plank', 'core'),
    ('Mountain Climbers', 'core'),
    ('Ab Wheel', 'core'),
    ('Hanging Knee Raises', 'core'),
    ('Flutter Kicks', 'core'),
    ('Dead Bug', 'core'),
    
    # Cardio
    ('Treadmill', 'cardio'),
    ('Rowing Machine', 'cardio'),
    ('Jump Rope', 'cardio'),
    ('Burpees', 'cardio'),
    ('High Knees', 'cardio'),
    ('Box Jumps', 'cardio'),
    ('Jumping Jacks', 'cardio'),
    ('Battle Ropes', 'cardio'),
    ('Stair Climber', 'cardio'),
    ('Elliptical', 'cardio'),
]

print("Adding exercises...")
for name, category in exercises:
    obj, created = Exercise.objects.get_or_create(name=name, category=category)
    if created:
        print(f"✅ Added {name}")
    else:
        print(f"⏭️  Skipped {name} (already exists)")

print(f"\n🎉 Total exercises in database: {Exercise.objects.count()}")