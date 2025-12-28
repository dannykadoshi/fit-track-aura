import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fittrack_project.settings')
django.setup()

from workouts.models import Exercise

# Map ALL exercises with their correct categories
exercise_categories = {
    'Ab Wheel': 'strength',
    'Arnold Press': 'strength',
    'Barbell Row': 'strength',
    'Basketball': 'sports',
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
    'Soccer': 'sports',
    'Squats': 'strength',
    'Stair Climber': 'cardio',
    'Stationary Bike': 'cardio',
    'Step-Ups': 'strength',
    'Stretching': 'flexibility',
    'Swimming': 'cardio',
    'T-Bar Row': 'strength',
    'Tennis': 'sports',
    'Treadmill': 'cardio',
    'Tricep Dips': 'strength',
    'Walking Lunges': 'strength',
    'Yoga': 'flexibility',
}

print("FORCE UPDATING ALL EXERCISES...")
updated_count = 0

# Update EVERY exercise, no checking
for exercise in Exercise.objects.all():
    if exercise.name in exercise_categories:
        old_category = exercise.category
        new_category = exercise_categories[exercise.name]
        exercise.category = new_category
        exercise.save()  # FORCE SAVE EVERY TIME
        
        if old_category:
            if old_category == new_category:
                print(f"✅ {exercise.name}: {old_category} (no change needed)")
            else:
                print(f"🔄 {exercise.name}: {old_category} → {new_category}")
                updated_count += 1
        else:
            print(f"🆕 {exercise.name}: BLANK → {new_category}")
            updated_count += 1
    else:
        print(f"⚠️  {exercise.name}: NOT IN LIST")

print(f"\n{'='*60}")
print(f"✅ UPDATED: {updated_count} exercises")
print(f"🎉 TOTAL: {Exercise.objects.count()} exercises")
print(f"{'='*60}")