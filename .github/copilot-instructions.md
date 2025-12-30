# FitTrack Aura - AI Agent Instructions

## Project Overview
FitTrack Aura is a Django-based full-stack fitness tracking web application. Users can log workouts, set fitness goals, and track progress with real-time statistics. The app uses a three-app Django structure: `workouts`, `goals`, and `users`, with django-allauth for authentication.

**Stack:** Django 6.0, PostgreSQL, WhiteNoise (static files), django-allauth, Render deployment

---

## Architecture & Core Patterns

### Three-App Structure
- **`workouts/`** - Workout logging with exercise library (Exercise → Workout → WorkoutExercise hierarchy)
- **`goals/`** - Fitness goal tracking with progress calculation and completion tracking
- **`users/`** - User authentication and profiles using django-allauth

### Key Design Patterns

**Model Relationships:**
- Workout is the central entity with ForeignKey(User) and reverse relation `user.workouts`
- WorkoutExercise is a through-model connecting Workout to Exercise (supports multiple exercise types: strength with sets/reps/weight, cardio with distance/duration)
- Exercise can be predefined (is_custom=False) or user-created (is_custom=True)

**View Pattern - Functional Views + Login Required:**
All app views use `@login_required` decorator. Views follow a consistent pattern:
```python
@login_required
def view_name(request):
    # Filter queryset by current user
    objects = Model.objects.filter(user=request.user)
    # Return with context
    return render(request, 'template.html', context)
```

**Dashboard Calculations:**
The dashboard in [workouts/views.py](workouts/views.py#L15) computes several metrics efficiently:
- Workout streak (current + best) by iterating through sorted dates
- Monthly totals using `aggregate(total=Sum('duration'))`
- Goal progress averages across active goals

---

## Critical Workflows & Commands

### Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser for admin
python create_superuser.py

# Load exercise library fixtures
python add_exercises.py

# Run tests with coverage
python manage.py test
coverage run --source='.' manage.py test
coverage report
```

### Deployment Build Script
[build.sh](build.sh) is Render-specific:
1. Install requirements
2. Collect static files (WhiteNoise handles serving)
3. Run migrations
4. Create superuser & load exercises
5. Database is PostgreSQL via environment variables

### Testing & QA
- Tests located in `apps/tests.py` and `apps/test_forms.py`
- Run specific app: `python manage.py test workouts` (or `goals`, `users`)
- Coverage report in `htmlcov/index.html`
- Manual testing documented in [TESTING.md](TESTING.md)

---

## Project-Specific Conventions

### Form Handling & Formsets
- Workout creation uses **inline formset** (WorkoutExerciseFormSet) for multiple exercises per workout
- FormSet key pattern: Check `request.POST.get('workout_exercises-TOTAL_FORMS')`
- Exercise selection is dynamic - can add predefined or create new exercises in-form

### Goal Progress Calculation
[goals/models.py#L43](goals/models.py#L43) - Beware of mixed-unit goals:
- Strips units (km, kg, lbs) from strings before converting to float
- Returns 0 on ValueError/AttributeError; caps at 100%
- This is intentionally flexible to support goals like "20 workouts" or "100km"

### Workout Streak Logic
[workouts/views.py#L25](workouts/views.py#L25) - Two separate calculations:
- **Current streak:** Iterate backwards from today checking if date exists in workout dates
- **Best streak:** Track consecutive date differences of 1 day
- Edge case: A single workout counts as streak=1

### User Isolation
All filtered querysets must use `user=request.user`. This prevents cross-user data leaks:
```python
# CORRECT: Filtered by user
workouts = Workout.objects.filter(user=request.user)

# WRONG: Would show all users' workouts
workouts = Workout.objects.all()
```

---

## Integration Points & External Dependencies

### Authentication (django-allauth)
- URL namespace: `accounts/` (configured in [fittrack_project/urls.py](fittrack_project/urls.py#L8))
- Provides login, signup, password reset, email verification
- Custom user profile extensions in [users/models.py](users/models.py)

### Static Files & Media
- WhiteNoise middleware (line 62, settings.py) handles static file serving in production
- Static files collected to `staticfiles/` directory
- CSS in `static/css/`, images in `static/images/`

### Database Configuration
- Uses `dj_database_url` to parse DATABASE_URL environment variable
- PostgreSQL in production (Render), SQLite in development
- Migrations auto-loaded from each app's `migrations/` folder

### Settings Management
- Environment variables via `python-decouple` config()
- DEBUG, SECRET_KEY, DATABASE_URL from environment
- ALLOWED_HOSTS includes 'localhost', '127.0.0.1', '.onrender.com', '.herokuapp.com'

---

## Common Pitfalls & Solutions

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| "Workouts not appearing" | User filtering missing | Add `filter(user=request.user)` to queryset |
| Formset validation fails silently | Not checking `formset.is_valid()` in POST | Always check `form.is_valid() and formset.is_valid()` |
| Streak calculation wrong | Using `-date` instead of sorting dates properly | Use `sorted(dates, reverse=True)` for best streak |
| Static files 404 in production | Missing `collectstatic` step | Ensure build script runs `python manage.py collectstatic --no-input` |
| Goal progress always 0 | Unit stripping doesn't handle format | Ensure target_value/current_value match expected format (e.g., "100km", "20") |

---

## File Structure Reference

```
workouts/          # Core workout tracking app
├── models.py      # Exercise, Workout, WorkoutExercise
├── views.py       # CRUD views + dashboard (streak/stats logic)
├── forms.py       # WorkoutForm + WorkoutExerciseFormSet
└── tests.py       # Model & view tests

goals/             # Goal tracking app
├── models.py      # Goal model (progress_percentage property)
├── views.py       # CRUD for goals
├── forms.py       # GoalForm
└── tests.py       # Goal tests

users/             # User profiles & auth
├── models.py      # Custom user profile (if extending User)
├── views.py       # Profile views
└── urls.py        # Auth URL patterns

fittrack_project/  # Django project settings
├── settings.py    # Database, apps, middleware, static files
├── urls.py        # URL routing (allauth, workouts, goals, users)
└── views.py       # Custom 404/500 handlers

templates/         # Template hierarchy
├── base.html      # Main layout
├── workouts/      # Workout templates
├── goals/         # Goal templates
└── users/         # Auth templates

static/            # CSS, images, JS
```

---

## Quick Reference: Key Model Methods

- `Goal.mark_complete()` - Sets `is_completed=True`, records `completed_date`
- `Goal.progress_percentage` - Property returning 0-100 int (handles unit stripping)
- `Workout.total_exercises()` - Returns count of related WorkoutExercise
- `Exercise.__str__()` - Returns exercise name
- `WorkoutExercise.__str__()` - Returns "{exercise} in {workout}"
