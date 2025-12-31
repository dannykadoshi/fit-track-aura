# Test Coverage Guide - Reaching 100%

Current Coverage: **58%** → Target: **100%**

## Quick Start

```bash
# Run tests with coverage
coverage run --source='.' manage.py test

# View coverage report
coverage report

# Generate HTML report to see exactly what lines are missing
coverage html
# Then open htmlcov/index.html in browser
```

## Priority Test Files to Create/Expand

### 1. Workouts App Tests (Biggest Impact)

#### Create: `workouts/test_views.py`
```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from .models import Workout, Exercise, WorkoutExercise


class WorkoutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # Create test exercise
        self.exercise = Exercise.objects.create(
            name='Push-ups',
            category='strength',
            muscle_group='chest'
        )
        
    def test_home_view(self):
        """Test landing page loads"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
    
    def test_dashboard_view_authenticated(self):
        """Test dashboard shows for authenticated user"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/dashboard.html')
        
    def test_dashboard_view_unauthenticated(self):
        """Test dashboard redirects for unauthenticated user"""
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/dashboard/')
        
    def test_workout_list_view(self):
        """Test workout list displays user's workouts"""
        Workout.objects.create(
            user=self.user,
            title='Morning Run',
            workout_type='cardio',
            date=date.today(),
            duration=30
        )
        
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Morning Run')
        
    def test_workout_create_get(self):
        """Test workout create form loads"""
        response = self.client.get(reverse('workout_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workout_form.html')
        
    def test_workout_create_post(self):
        """Test creating a new workout"""
        workout_data = {
            'title': 'Evening Workout',
            'workout_type': 'strength',
            'date': date.today(),
            'duration': 45,
            'notes': 'Felt strong'
        }
        
        response = self.client.post(reverse('workout_create'), data=workout_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Workout.objects.filter(title='Evening Workout').exists())
        
    def test_workout_update_get(self):
        """Test workout update form loads"""
        workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            workout_type='cardio',
            date=date.today(),
            duration=30
        )
        
        response = self.client.get(reverse('workout_update', args=[workout.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')
        
    def test_workout_update_post(self):
        """Test updating a workout"""
        workout = Workout.objects.create(
            user=self.user,
            title='Old Title',
            workout_type='cardio',
            date=date.today(),
            duration=30
        )
        
        updated_data = {
            'title': 'New Title',
            'workout_type': 'strength',
            'date': date.today(),
            'duration': 45
        }
        
        response = self.client.post(
            reverse('workout_update', args=[workout.pk]),
            data=updated_data
        )
        
        self.assertEqual(response.status_code, 302)
        workout.refresh_from_db()
        self.assertEqual(workout.title, 'New Title')
        
    def test_workout_delete(self):
        """Test deleting a workout"""
        workout = Workout.objects.create(
            user=self.user,
            title='To Delete',
            workout_type='cardio',
            date=date.today(),
            duration=30
        )
        
        response = self.client.post(reverse('workout_delete', args=[workout.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Workout.objects.filter(pk=workout.pk).exists())
        
    def test_workout_detail_view(self):
        """Test workout detail page displays correctly"""
        workout = Workout.objects.create(
            user=self.user,
            title='Detailed Workout',
            workout_type='strength',
            date=date.today(),
            duration=60
        )
        
        response = self.client.get(reverse('workout_detail', args=[workout.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detailed Workout')
        
    def test_user_can_only_access_own_workouts(self):
        """Test users can't access other users' workouts"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        
        workout = Workout.objects.create(
            user=other_user,
            title='Other User Workout',
            workout_type='cardio',
            date=date.today(),
            duration=30
        )
        
        response = self.client.get(reverse('workout_detail', args=[workout.pk]))
        self.assertEqual(response.status_code, 404)
```

#### Create: `workouts/test_utils.py`
```python
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Workout
from .utils import calculate_calories, generate_workout_stats
from datetime import date


class UtilsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_calculate_calories_cardio(self):
        """Test calorie calculation for cardio workout"""
        # Add your actual utility function tests here
        # Example:
        calories = calculate_calories('cardio', 30)
        self.assertIsInstance(calories, (int, float))
        self.assertGreater(calories, 0)
        
    def test_generate_workout_stats(self):
        """Test workout statistics generation"""
        Workout.objects.create(
            user=self.user,
            title='Test',
            workout_type='cardio',
            date=date.today(),
            duration=30
        )
        
        stats = generate_workout_stats(self.user)
        self.assertIn('total_workouts', stats)
        self.assertEqual(stats['total_workouts'], 1)
```

#### Create: `workouts/test_pdf_utils.py`
```python
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Workout
from .pdf_utils import generate_workout_pdf
from datetime import date
import io


class PDFUtilsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            workout_type='strength',
            date=date.today(),
            duration=45
        )
        
    def test_generate_workout_pdf(self):
        """Test PDF generation returns buffer"""
        pdf_buffer = generate_workout_pdf(self.workout)
        self.assertIsInstance(pdf_buffer, io.BytesIO)
        self.assertGreater(pdf_buffer.getbuffer().nbytes, 0)
        
    def test_pdf_contains_workout_title(self):
        """Test PDF contains workout information"""
        pdf_buffer = generate_workout_pdf(self.workout)
        # You can use PyPDF2 or similar to read and verify content
        # This is a basic check that PDF was created
        self.assertIsNotNone(pdf_buffer)
```

#### Create: `workouts/test_share_utils.py`
```python
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Workout
from .share_utils import generate_share_token, validate_share_token
from datetime import date


class ShareUtilsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            user=self.user,
            title='Shareable Workout',
            workout_type='strength',
            date=date.today(),
            duration=45
        )
        
    def test_generate_share_token(self):
        """Test share token generation"""
        token = generate_share_token(self.workout)
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 0)
        
    def test_validate_share_token(self):
        """Test share token validation"""
        token = generate_share_token(self.workout)
        workout_id = validate_share_token(token)
        self.assertEqual(workout_id, self.workout.id)
        
    def test_invalid_share_token(self):
        """Test invalid token returns None"""
        result = validate_share_token('invalid_token_12345')
        self.assertIsNone(result)
```

### 2. Users App Tests

#### Expand: `users/tests.py`
```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile


class UserViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
    def test_profile_view_get(self):
        """Test profile page loads"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        
    def test_profile_view_post_update(self):
        """Test updating profile"""
        profile_data = {
            'username': 'testuser',
            'email': 'newemail@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'height': 180,
            'weight': 75,
            'date_of_birth': '1990-01-01'
        }
        
        response = self.client.post(reverse('profile'), data=profile_data)
        self.assertEqual(response.status_code, 302)
        
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'newemail@example.com')
        
    def test_change_password_view_get(self):
        """Test password change form loads"""
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        
    def test_change_password_view_post(self):
        """Test changing password"""
        password_data = {
            'old_password': 'testpass123',
            'new_password1': 'newpass456',
            'new_password2': 'newpass456'
        }
        
        response = self.client.post(reverse('change_password'), data=password_data)
        self.assertEqual(response.status_code, 302)
        
        # Verify password was changed
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpass456'))
        
    def test_profile_unauthenticated_redirect(self):
        """Test profile redirects if not logged in"""
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        
    def test_user_profile_created_on_signup(self):
        """Test UserProfile is created when user signs up"""
        new_user = User.objects.create_user(
            username='newuser',
            password='pass123'
        )
        self.assertTrue(hasattr(new_user, 'profile'))
        self.assertIsInstance(new_user.profile, UserProfile)


class UserModelTests(TestCase):
    def test_userprofile_str(self):
        """Test UserProfile string representation"""
        user = User.objects.create_user(
            username='testuser',
            password='pass123'
        )
        self.assertEqual(str(user.profile), 'testuser Profile')
        
    def test_userprofile_defaults(self):
        """Test UserProfile default values"""
        user = User.objects.create_user(
            username='testuser',
            password='pass123'
        )
        profile = user.profile
        self.assertIsNotNone(profile.created_at)
        self.assertIsNotNone(profile.updated_at)
```

### 3. Goals App Tests

#### Expand: `goals/tests.py` (add badge and utility tests)
```python
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Goal, Badge
from .badge_utils import check_and_award_badges, calculate_workout_streak
from datetime import date, timedelta


class BadgeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_badge_creation(self):
        """Test creating a badge"""
        badge = Badge.objects.create(
            user=self.user,
            name='First Workout',
            description='Complete your first workout',
            badge_type='workout_count'
        )
        self.assertEqual(str(badge), 'testuser - First Workout')
        
    def test_check_and_award_badges(self):
        """Test badge awarding system"""
        # Create conditions for badge
        badges_awarded = check_and_award_badges(self.user)
        self.assertIsInstance(badges_awarded, list)
        
    def test_calculate_workout_streak(self):
        """Test workout streak calculation"""
        from workouts.models import Workout
        
        # Create consecutive workouts
        for i in range(5):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                workout_type='cardio',
                date=date.today() - timedelta(days=i),
                duration=30
            )
        
        streak = calculate_workout_streak(self.user)
        self.assertEqual(streak, 5)


class BadgeViewTests(TestCase):
    def setUp(self):
        self.client.login(username='testuser', password='testpass123')
        
    def test_badge_list_view(self):
        """Test badge list displays correctly"""
        response = self.client.get(reverse('badge_list'))
        self.assertEqual(response.status_code, 200)


class GoalAchievementTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
    def test_goal_marked_complete_when_target_reached(self):
        """Test goal automatically marked complete"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            category='endurance',
            target_number=100,
            current_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )
        
        # Check if goal is marked complete
        goal.refresh_from_db()
        self.assertTrue(goal.is_completed)
```

## Key Testing Patterns

### 1. View Tests
- **GET requests**: Test page loads, correct template, authentication
- **POST requests**: Test form submission, database changes, redirects
- **Authorization**: Test users can only access their own data
- **Edge cases**: Empty data, invalid IDs, missing objects

### 2. Model Tests
- **String representation**: Test `__str__` methods
- **Methods**: Test custom model methods
- **Properties**: Test computed properties
- **Signals**: Test signal handlers (like auto-creating profiles)

### 3. Form Tests
- **Valid data**: Test form accepts correct data
- **Invalid data**: Test form rejects incorrect data
- **Required fields**: Test missing required fields
- **Validation**: Test custom validation logic

### 4. Utility Function Tests
- **Input/Output**: Test various inputs produce expected outputs
- **Edge cases**: Test with empty data, None, extremes
- **Error handling**: Test error conditions

## Running Specific Tests

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test workouts
python manage.py test goals
python manage.py test users

# Run specific test class
python manage.py test workouts.test_views.WorkoutViewTests

# Run specific test method
python manage.py test workouts.test_views.WorkoutViewTests.test_home_view

# With coverage for specific app
coverage run --source='workouts' manage.py test workouts
coverage report
```

## Tips for 100% Coverage

1. **Use coverage HTML report** to see exactly what lines are missing:
   ```bash
   coverage html
   open htmlcov/index.html
   ```

2. **Test error conditions** - exceptions, 404s, permission denials

3. **Test both branches** of if/else statements

4. **Test loop iterations** - empty lists, single item, multiple items

5. **Test authentication** - logged in and logged out states

6. **Mock external services** - use `unittest.mock` for emails, APIs, etc.

7. **Test edge cases**:
   - Empty strings, None values
   - Very large numbers
   - Past/future dates
   - Special characters in input

8. **Don't test Django internals** - focus on your custom code

## Current Test Files Structure

```
fit-track-aura/
├── goals/
│   ├── test_forms.py ✓ (exists)
│   └── tests.py ✓ (exists, needs expansion)
├── users/
│   └── tests.py ✓ (exists, needs expansion)
└── workouts/
    ├── test_forms.py ✓ (exists)
    ├── tests.py ✓ (exists, needs expansion)
    ├── test_views.py ✗ (create this)
    ├── test_utils.py ✗ (create this)
    ├── test_pdf_utils.py ✗ (create this)
    └── test_share_utils.py ✗ (create this)
```

## Next Steps

1. Start with **workouts/test_views.py** (biggest impact)
2. Add **utility function tests**
3. Expand **users/tests.py** with view tests
4. Add remaining **goals** tests for badges
5. Run coverage HTML report to find remaining gaps
6. Fill in missing lines iteratively

Remember: **100% coverage doesn't mean bug-free code**, but it does mean:
- All code paths are executed
- Edge cases are considered
- Regressions are caught early
- Code is more maintainable
