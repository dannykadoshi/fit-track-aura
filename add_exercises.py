import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fittrack_project.settings')
django.setup()

from workouts.models import Exercise

# Map ALL exercises with their correct categories
exercise_categories = {
    # Strength - Upper Body
    'Ab Wheel': 'strength',
    'Arnold Press': 'strength',
    'Barbell Row': 'strength',
    'Battle Ropes': 'cardio',
    'Bench Press': 'strength',
    'Bicep Curls': 'strength',
    'Bicycle Crunches': 'strength',
    'Box Jumps': 'cardio',
    'Bulgarian Split Squats': 'strength',
    'Burpees': 'cardio',
    'Cable Crossovers': 'strength',
    'Cable Rows': 'strength',
    'Calf Raises': 'strength',
    'Chest Press Machine': 'strength',
    'Chin-Ups': 'strength',
    'Crunches': 'strength',
    'Cycling': 'cardio',
    'Dead Bug': 'strength',
    'Deadlift': 'strength',
    'Decline Bench Press': 'strength',
    'Dips': 'strength',
    'Dumbbell Flyes': 'strength',
    'Dumbbell Press': 'strength',
    'Dumbbell Row': 'strength',
    'Elliptical': 'cardio',
    'Face Pulls': 'strength',
    'Flutter Kicks': 'strength',
    'Front Raises': 'strength',
    'Front Squats': 'strength',
    'Glute Bridges': 'strength',
    'Hammer Curls': 'strength',
    'Hanging Knee Raises': 'strength',
    'High Knees': 'cardio',
    'Hip Thrusts': 'strength',
    'Incline Bench Press': 'strength',
    'Jump Rope': 'cardio',
    'Jumping Jacks': 'cardio',
    'Lat Pulldown': 'strength',
    'Lateral Raises': 'strength',
    'Leg Curls': 'strength',
    'Leg Extensions': 'strength',
    'Leg Press': 'strength',
    'Leg Raises': 'strength',
    'Lunges': 'strength',
    'Mountain Climbers': 'strength',
    'Overhead Press': 'strength',
    'Pilates': 'flexibility',
    'Plank': 'strength',
    'Pull-Ups': 'strength',
    'Push-Ups': 'strength',
    'Reverse Flyes': 'strength',
    'Romanian Deadlift': 'strength',
    'Rowing Machine': 'cardio',
    'Running': 'cardio',
    'Russian Twists': 'strength',
    'Shrugs': 'strength',
    'Side Plank': 'strength',
    'Skull Crushers': 'strength',
    'Squats': 'strength',
    'Stair Climber': 'cardio',
    'Stationary Bike': 'cardio',
    'Step-Ups': 'strength',
    'Stretching': 'flexibility',
    'Swimming': 'cardio',
    'T-Bar Row': 'strength',
    'Tennis': 'sports',
    'Basketball': 'sports',
    'Soccer': 'sports',
    'Treadmill': 'cardio',
    'Tricep Dips': 'strength',
    'Walking Lunges': 'strength',
    'Yoga': 'flexibility',
}

print("Fixing ALL exercise categories...")
updated_count = 0
created_count = 0
skipped_count = 0

# First, update ALL existing exercises
for exercise in Exercise.objects.all():
    if exercise.name in exercise_categories:
        correct_category = exercise_categories[exercise.name]
        if exercise.category != correct_category:
            exercise.category = correct_category
            exercise.save()
            print(f"🔄 FIXED: {exercise.name} → {correct_category}")
            updated_count += 1
        else:
            print(f"✅ OK: {exercise.name} ({correct_category})")
            skipped_count += 1
    else:
        print(f"⚠️  Unknown exercise (not in list): {exercise.name}")

# Then, create any missing exercises
for name, category in exercise_categories.items():
    obj, created = Exercise.objects.get_or_create(name=name, defaults={'category': category})
    if created:
        print(f"➕ CREATED: {name} ({category})")
        created_count += 1

print(f"\n" + "="*50)
print(f"🔄 Updated: {updated_count}")
print(f"➕ Created: {created_count}")
print(f"✅ Already OK: {skipped_count}")
print(f"🎉 Total exercises: {Exercise.objects.count()}")
print("="*50)