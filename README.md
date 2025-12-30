# FitTrack Aura 💪⚡

![FitTrack Aura Logo](static/images/og-image.png)

**Live Site:** [FitTrack Aura](https://fit-track-aura.onrender.com)

**GitHub Repository:** [GitHub - FitTrack Aura](https://github.com/dannykadoshi/fit-track-aura)

---

## Table of Contents

- [Project Overview](#project-overview)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Wireframes](#wireframes)
- [Features](#features)
- [Database Design](#database-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Admin Access](#admin-access)
- [Credits](#credits)

---

## Project Overview

FitTrack Aura is a comprehensive full-stack fitness tracking web application built with Django and Python. It allows users to log workouts, set fitness goals, track progress, and maintain workout streaks. The application provides an intuitive dashboard with real-time statistics and a modern, responsive user interface.

This project was developed as Portfolio Project 4 (Full-Stack Toolkit) for Code Institute's Diploma in Full Stack Software Development.

### Project Goals

- Provide users with an easy-to-use platform to track their fitness journey
- Enable goal setting and progress monitoring
- Motivate users through streak tracking and achievement badges
- Demonstrate proficiency in full-stack web development using Django
- Implement CRUD (Create, Read, Update, Delete) functionality
- Apply Agile methodology throughout the development process

---

## User Experience (UX)

### Target Audience

- Fitness enthusiasts who want to track their workouts
- Individuals setting and working toward fitness goals
- Gym-goers looking to monitor their progress over time
- People who need motivation through streak tracking

### User Stories

All user stories were managed using GitHub Projects with Agile methodology. User stories were organized into Epics and tracked through a Kanban board.

**GitHub Projects Board:** [https://github.com/users/dannykadoshi/projects/4](https://github.com/users/dannykadoshi/projects/4)

#### Epic 1: User Authentication & Profile Management

- **User Story #1:** As a new user, I want to register for an account so that I can start tracking my fitness journey
- **User Story #2:** As a registered user, I want to log in securely so that I can access my personal workout data
- **User Story #3:** As a logged-in user, I want to log out easily so that my data remains secure

#### Epic 2: Workout Management (CRUD)

- **User Story #4:** As a user, I want to create new workout entries so that I can log my training sessions
- **User Story #5:** As a user, I want to view all my workouts so that I can review my training history
- **User Story #6:** As a user, I want to edit my workouts so that I can correct mistakes or add details
- **User Story #7:** As a user, I want to delete workouts so that I can remove incorrect entries
- **User Story #8:** As a user, I want to add multiple exercises to a workout so that I can track complete training sessions

#### Epic 3: Goal Management (CRUD)

- **User Story #9:** As a user, I want to create fitness goals so that I have targets to work toward
- **User Story #10:** As a user, I want to view my goals so that I can track my progress
- **User Story #11:** As a user, I want to update my goals so that I can adjust targets as needed
- **User Story #12:** As a user, I want to delete goals so that I can remove outdated objectives
- **User Story #18:** As a user, I want to mark goals as complete so that I can celebrate achievements

#### Epic 4: Dashboard & Analytics

- **User Story #15:** As a user, I want to see a workout streak counter so that I stay motivated to exercise consistently
- **User Story #20:** As a user, I want to see a dashboard with my fitness statistics so that I can monitor my progress at a glance

#### Epic 5: User Experience Enhancements

- **User Story #5:** As a user, I want a searchable exercise library so that I can quickly find exercises when logging workouts
- **User Story #6:** As a user, I want custom branding and favicon so that the app has a professional appearance
- **User Story #7:** As a user, I want social media preview images so that sharing the app looks professional

#### Epic 6: Testing & Quality Assurance

- **User Story #3:** As a developer, I want comprehensive automated tests so that I can ensure code quality and prevent bugs
- **User Story #17:** As a developer, I want detailed manual testing documentation so that all features are verified to work correctly

#### Epic 7: Deployment & Documentation

- **User Story #16:** As a developer, I want to deploy the application to a cloud platform so that users can access it online
- **User Story #1:** As a developer, I want comprehensive README documentation so that others can understand and use the project

### Design

#### Color Scheme

The application uses a modern purple gradient theme that conveys energy, motivation, and premium quality:

- **Primary Purple:** `#a855f7` - Main brand color
- **Secondary Pink:** `#ec4899` - Accent and gradients
- **Dark Background:** `#0f172a` - Professional dark mode
- **Deep Purple:** `#581c87` - Rich depth in gradients
- **Success Green:** `#10b981` - Positive actions
- **Warning Orange:** `#f59e0b` - Streak indicators

#### Typography

- **Primary Font:** System fonts (Segoe UI, -apple-system, BlinkMacSystemFont)
- **Headings:** Bold weights (600-700) for emphasis
- **Body Text:** Regular weight (400) for readability
- **Gradient Text:** Used for branding and emphasis

#### UI/UX Principles

- **Glassmorphism:** Semi-transparent cards with backdrop blur effects
- **Gradient Backgrounds:** Purple to dark gradient creates depth
- **Responsive Design:** Mobile-first approach using Bootstrap 5
- **Consistent Spacing:** Using Bootstrap's spacing utilities
- **Visual Feedback:** Success messages, hover effects, loading states
- **Accessibility:** Semantic HTML, ARIA labels, color contrast compliance

### Wireframes

Low-fidelity wireframes were created during the planning phase to establish the layout and user flow.

#### Dashboard Wireframe
![Dashboard Wireframe](docs/wireframes/wireframe-dashboard.png)

The dashboard wireframe shows the main layout with welcome message, statistics cards (workouts count, streak counter, training time, goals progress), recent workouts list, active goals with progress bars, and streak statistics.

#### Create Workout Wireframe
![Create Workout Wireframe](docs/wireframes/wireframe-workout-create.png)

The workout creation form wireframe demonstrates the structured input layout with workout title, date/duration fields, notes section, exercise selection with sets/reps/weight inputs, and action buttons.

#### Goals List Wireframe
![Goals List Wireframe](docs/wireframes/wireframe-goals-list.png)

The goals list wireframe displays active goals with progress indicators and action buttons (Edit, Complete, Delete), as well as completed goals section showing achieved objectives.

---

## Features

### Existing Features

#### 1. User Authentication & Authorization
- **User Registration:** Sign up with username, email, and password
- **Secure Login:** Django Allauth integration for authentication
- **User Isolation:** Users can only access their own data
- **Session Management:** Secure session handling with Django

![Sign Up Page](docs/screenshots/02-signup.png)
![Login Page](docs/screenshots/03-login.png)

#### 2. Dashboard
- **Statistics Overview:** Workouts this month, total training time, goals progress
- **Current Streak Counter:** Displays consecutive workout days with fire emoji
- **Best Streak Badge:** Shows all-time longest streak with achievement emojis
- **Recent Workouts:** Quick access to latest 5 workouts
- **Active Goals:** Progress bars for up to 3 active goals
- **Streak Stats Card:** Detailed breakdown of current streak, best streak, and total workouts

![Dashboard](docs/screenshots/04-dashboard.png)

#### 3. Workout Management (Full CRUD)
- **Create Workouts:** Log workouts with title, date, duration, and notes
- **Add Exercises:** Multiple exercises per workout with sets, reps, weight, and distance
- **Exercise Library:** 60+ predefined exercises across all categories
- **Searchable Dropdown:** Select2 autocomplete for finding exercises quickly
- **View Workouts:** List view with search functionality
- **Edit Workouts:** Update workout details and exercises
- **Delete Workouts:** Remove workouts with confirmation

![Workout List](docs/screenshots/05-workout-list.png)
![Create Workout](docs/screenshots/06-workout-create.png)
![Workout Detail](docs/screenshots/07-workout-detail.png)
![Exercise Autocomplete](docs/screenshots/12-autocomplete.png)

#### 4. Goal Management (Full CRUD)
- **Create Goals:** Set targets with title, description, category, target value, and date
- **Track Progress:** Visual progress bars showing completion percentage
- **Update Goals:** Edit goal details and current progress
- **Complete Goals:** Mark goals as achieved
- **Delete Goals:** Remove goals with confirmation
- **Goal Categories:** Organize by weight loss, muscle gain, endurance, etc.

![Goals List](docs/screenshots/08-goals-list.png)
![Create Goal](docs/screenshots/09-goal-create.png)

#### 5. Workout Streak System
- **Automatic Calculation:** Streak updates based on workout dates
- **Current Streak:** Shows consecutive days with workouts
- **Best Streak:** Tracks all-time longest streak
- **Motivation System:** Dynamic emojis based on streak length (🔥 for active, 🏆 for milestones)
- **Achievement Badges:** Unlock badges at 3, 7, 14, and 30+ day streaks

#### 6. User Interface Features
- **Responsive Design:** Works on desktop, tablet, and mobile devices
- **Dark Theme:** Modern purple gradient dark mode
- **Success Messages:** Toast notifications for all user actions
- **Form Validation:** Client and server-side validation
- **Loading States:** Visual feedback during data operations
- **Error Handling:** Custom 404 and 500 error pages

![Mobile Responsiveness](docs/screenshots/mobile-homepage..jpeg)
![404 Error Page](docs/screenshots/10-404-error.png)

#### 7. Security Features
- **CSRF Protection:** All forms protected against Cross-Site Request Forgery
- **Password Hashing:** Django's built-in password hashing (PBKDF2)
- **User Data Isolation:** Users can only access their own workouts and goals
- **Login Required:** Protected views require authentication
- **Environment Variables:** Sensitive data stored in .env file
- **SQL Injection Protection:** Django ORM prevents SQL injection

#### 8. Additional Features
- **Custom Favicon:** Professional branding across all pages
- **Open Graph Tags:** Social media sharing preview images
- **Semantic HTML:** Proper HTML5 structure for accessibility
- **Progressive Enhancement:** Core functionality works without JavaScript

### Features Left to Implement

These features were identified during development but moved to "Future Enhancements" due to time constraints:

1. **Visual Progress Charts:** Interactive charts showing workout trends over time using Chart.js
2. **Custom Exercises:** Allow users to create and save their own exercises
3. **Workout Templates:** Save frequent workouts as templates for quick logging
4. **Social Features:** Share workouts and compete with friends
5. **Mobile App:** Native iOS/Android applications
6. **Nutrition Tracking:** Log meals and track calorie intake
7. **Photo Progress:** Upload and compare progress photos
8. **Export Data:** Download workout history as CSV/PDF

---

## Database Design

### Database Schema

FitTrack Aura uses a **relational database** (SQLite in development, PostgreSQL in production) with the following models:

#### Entity Relationship Diagram

```
┌─────────────────┐
│      User       │
│  (Django Auth)  │
└────────┬────────┘
         │
         │ 1:N
         │
    ┌────┴─────────────────────┬──────────────────┐
    │                          │                  │
    ▼                          ▼                  ▼
┌─────────┐              ┌──────────┐      ┌──────────┐
│ Workout │              │   Goal   │      │ Exercise │
└────┬────┘              └──────────┘      └────┬─────┘
     │                                           │
     │ 1:N                                       │
     │                                           │
     └────────────────┬──────────────────────────┘
                      │ N:1
                      ▼
              ┌──────────────────┐
              │ WorkoutExercise  │
              │  (Through Model) │
              └──────────────────┘
```

### Models

#### 1. User Model (Django's built-in)
- Handles authentication and user management
- Fields: username, email, password, etc.

#### 2. Workout Model
```python
class Workout(models.Model):
    user = ForeignKey(User)           # Owner of the workout
    title = CharField(max_length=200)  # Workout name
    date = DateField()                 # When workout occurred
    duration = PositiveIntegerField()  # Duration in minutes
    notes = TextField()                # Optional notes
    created_at = DateTimeField()       # Record creation timestamp
    updated_at = DateTimeField()       # Last modification timestamp
```

#### 3. Exercise Model
```python
class Exercise(models.Model):
    name = CharField(max_length=100)   # Exercise name
    category = CharField(max_length=50) # Category (upper_body, legs, etc.)
    
    CATEGORY_CHOICES = [
        ('upper_body', 'Upper Body'),
        ('lower_body', 'Lower Body'),
        ('cardio', 'Cardio'),
        ('core', 'Core'),
        ('full_body', 'Full Body'),
    ]
```

#### 4. WorkoutExercise Model (Through Model)
```python
class WorkoutExercise(models.Model):
    workout = ForeignKey(Workout)      # Related workout
    exercise = ForeignKey(Exercise)    # Exercise performed
    sets = PositiveIntegerField()      # Number of sets
    reps = PositiveIntegerField()      # Repetitions per set
    weight = DecimalField()            # Weight used
    unit = CharField()                 # kg or lbs
    distance = DecimalField()          # For cardio exercises
    duration = PositiveIntegerField()  # For cardio exercises
```

#### 5. Goal Model
```python
class Goal(models.Model):
    user = ForeignKey(User)            # Owner of the goal
    title = CharField(max_length=200)  # Goal name
    description = TextField()          # Goal description
    category = CharField(max_length=50) # Goal category
    target_value = CharField()         # Target to achieve
    current_value = CharField()        # Current progress
    target_date = DateField()          # Deadline
    is_completed = BooleanField()      # Completion status
    completed_date = DateField()       # When completed
    created_at = DateTimeField()       # Record creation timestamp
    updated_at = DateTimeField()       # Last modification timestamp
```

### Database Relationships

- **One-to-Many:** User → Workouts (one user has many workouts)
- **One-to-Many:** User → Goals (one user has many goals)
- **Many-to-Many:** Workout ↔ Exercise (through WorkoutExercise model)

---

## Technologies Used

### Languages

- **Python 3.14** - Backend programming language
- **HTML5** - Structure and content
- **CSS3** - Styling and layout
- **JavaScript** - Interactive functionality

### Frameworks & Libraries

#### Backend
- **Django 6.0** - Python web framework
- **Django Allauth 65.13.1** - User authentication
- **Python Decouple 3.8** - Environment variable management
- **dj-database-url 3.0.1** - Database configuration
- **Whitenoise 6.11.0** - Static file serving
- **Gunicorn 23.0.0** - WSGI HTTP Server (production)
- **psycopg2-binary 2.9.11** - PostgreSQL adapter

#### Frontend
- **Bootstrap 5.3** - Responsive CSS framework
- **Select2 4.1** - Searchable dropdown component
- **jQuery 3.6** - JavaScript library (for Select2)

### Database

- **SQLite** - Development database
- **PostgreSQL 17** - Production database (Render)

### Tools & Services

- **Git** - Version control
- **GitHub** - Code repository and project management
- **VS Code** - Code editor
- **Chrome DevTools** - Testing and debugging
- **Render** - Cloud deployment platform
- **Coverage.py 7.13.0** - Code coverage analysis

### Python Packages

```txt
asgiref==3.11.0
coverage==7.13.0
dj-database-url==3.0.1
Django==6.0
django-allauth==65.13.1
gunicorn==23.0.0
packaging==25.0
pillow==12.0.0
psycopg2-binary==2.9.11
python-decouple==3.8
sqlparse==0.5.5
whitenoise==6.11.0
```

---

## Testing

### Automated Testing

FitTrack Aura includes a comprehensive automated test suite with **30+ tests** achieving **88% code coverage**.

#### Test Coverage Summary

- **Workout App Tests:** 15 tests
  - Model tests (Workout, Exercise, WorkoutExercise)
  - View tests (CRUD operations)
  - Form tests (validation)
  
- **Goal App Tests:** 12 tests
  - Model tests (Goal)
  - View tests (CRUD operations)
  - Form tests (validation)
  
- **Integration Tests:** 5 tests
  - Dashboard functionality
  - User authentication flow
  - Streak calculation

#### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests with coverage report
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

#### Test Results

```
Found 32 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
................................
----------------------------------------------------------------------
Ran 32 tests in 2.456s

OK
Destroying test database for alias 'default'...

Code Coverage: 88%
```

### Manual Testing

Comprehensive manual testing was performed and documented in [TESTING.md](TESTING.md).

#### Testing Areas Covered

1. **User Authentication**
   - Registration with valid/invalid data
   - Login with correct/incorrect credentials
   - Logout functionality
   - Session persistence

2. **Workout CRUD Operations**
   - Create workout with exercises, sets, reps, and weight
   - View workout list and details
   - Edit workout information
   - Delete workout with confirmation
   - Form validation (required fields, date format)
   - Dynamic exercise form with add/remove functionality
   - Autocomplete exercise selection (72 pre-loaded exercises)
   - Search and filter workouts

3. **Goal CRUD Operations**
   - Create and track fitness goals with target dates and values
   - Visual progress tracking with animated gradient progress bars
   - Real-time progress percentage calculation
   - Mark goals as complete when achieved
   - View completed goals history with completion dates

4. **Dashboard Functionality**
   - Statistics accuracy (workouts count, training time)
   - Streak counter calculation
   - Recent workouts display
   - Active goals display
   - Progress bar accuracy

5. **Responsive Design**
   - Mobile devices (320px - 480px)
   - Tablets (768px - 1024px)
   - Desktop (1280px+)
   - Cross-browser testing (Chrome, Firefox, Safari, Edge)

6. **Security Testing**
   - User data isolation (cannot access other users' data)
   - CSRF protection on all forms
   - SQL injection prevention
   - XSS protection
   - Unauthorized access redirects to login

7. **Usability Testing**
   - Navigation flow
   - Form feedback (success/error messages)
   - Button states (hover, active, disabled)
   - Loading indicators
   - Error page functionality (404, 500)

### Validation

#### HTML Validation
- Passed [W3C Markup Validation Service](https://validator.w3.org/)
- No errors or warnings

#### CSS Validation
- Passed [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- No errors found

#### Python Code Quality
- Follows PEP 8 style guide
- Checked with `flake8` and `pylint`
- No major issues

#### Accessibility
- Semantic HTML5 elements used throughout
- ARIA labels on interactive elements
- Color contrast meets WCAG AA standards
- Keyboard navigation supported

### Known Bugs

No known bugs at the time of submission. All identified issues during testing were resolved.

---

## Deployment

### Live Deployment

The application is deployed on Render and can be accessed at:
**[https://fit-track-aura.onrender.com](https://fit-track-aura.onrender.com)**

### Local Development Setup

#### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)

#### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/dannykadoshi/fit-track-aura.git
cd fit-track-aura
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```bash
touch .env
```

Add the following to `.env`:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Load exercise data**
```bash
python add_exercises.py
```

8. **Collect static files**
```bash
python manage.py collectstatic
```

9. **Run development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

### Production Deployment to Render

#### Prerequisites
- Render account (free tier available)
- GitHub repository

#### Deployment Steps

1. **Prepare project for deployment**

Create `build.sh` in project root:
```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python create_superuser.py
python add_exercises.py
```

Make it executable:
```bash
chmod +x build.sh
```

2. **Update settings.py for production**

Add at the top:
```python
import dj_database_url
```

Update DATABASES:
```python
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600
    )
}
```

Update ALLOWED_HOSTS:
```python
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.onrender.com',
]
```

Add WhiteNoise to MIDDLEWARE (after SecurityMiddleware):
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]
```

Add at bottom of settings.py:
```python
# Static files configuration for production
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
```

3. **Create Render Web Service**

- Go to [https://render.com/](https://render.com/)
- Sign in with GitHub
- Click "New +" → "Web Service"
- Connect your repository
- Configure:
  - **Name:** fit-track-aura
  - **Region:** Oregon (or closest)
  - **Branch:** main
  - **Runtime:** Python 3
  - **Build Command:** `./build.sh`
  - **Start Command:** `gunicorn fittrack_project.wsgi:application`
  - **Instance Type:** Free

4. **Add Environment Variables**

In Render dashboard, add Secret File:
- **Filename:** `.env`
- **Contents:**
```
SECRET_KEY=your-production-secret-key
DEBUG=False
PYTHON_VERSION=3.14.0
```

5. **Create PostgreSQL Database**

- Click "New +" → "PostgreSQL"
- **Name:** fit-track-aura-db
- **Region:** Same as web service
- **PostgreSQL Version:** 17
- **Instance Type:** Free

6. **Connect Database to Web Service**

- In web service Environment tab
- Click "Add Environment Variable"
- Key: `DATABASE_URL`
- Value: Copy from PostgreSQL "Internal Database URL"

7. **Deploy**

- Click "Manual Deploy" → "Deploy latest commit"
- Wait 3-5 minutes for build to complete
- Visit your live site: `https://fit-track-aura.onrender.com`

### Environment Variables

Required environment variables for production:

| Variable | Description | Example |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | `django-insecure-abc123...` |
| DEBUG | Debug mode (False in production) | `False` |
| DATABASE_URL | PostgreSQL connection string | `postgres://user:pass@host/db` |
| PYTHON_VERSION | Python version for Render | `3.14.0` |

### Security Considerations

- ✅ `DEBUG = False` in production
- ✅ Secret key stored in environment variable
- ✅ Database credentials not in version control
- ✅ HTTPS enforced with SSL redirect
- ✅ Secure cookies enabled
- ✅ CSRF and XSS protection enabled
- ✅ `.env` file in `.gitignore`
- ✅ No hardcoded passwords in code

### Important Notes

**Render Free Tier Limitations:**
- Services spin down after 15 minutes of inactivity
- First load after inactivity may take 30-60 seconds
- No persistent disk storage (use PostgreSQL for data)
- Suitable for student projects and portfolios

---

## Admin Access

### For Code Institute Assessors

To access the Django admin panel for assessment purposes:

**Admin Panel URL:** [https://fit-track-aura.onrender.com/admin/](https://fit-track-aura.onrender.com/admin/)

**Admin Credentials:**
- **Username:** `admin`
- **Password:** Provided in LMS submission form

**What you can access:**
- View all user accounts and data
- Full CRUD operations on all models (Workouts, Goals, Exercises)
- User management and permissions
- Database administration
- View all workout exercises and relationships

**Note:** For security reasons, the admin password is provided separately in the project submission form, not in this public README.

### Test User Account

You can create your own test account by visiting:
**[https://fit-track-aura.onrender.com/accounts/signup/](https://fit-track-aura.onrender.com/accounts/signup/)**

Or use the admin panel to view existing user data and workouts.

### Important Note for Assessors

**First Load Delay:** The application uses Render's free tier, which spins down after 15 minutes of inactivity. If the service is asleep, the first page load may take 30-60 seconds. Subsequent page loads will be instant.

**Database Limitation:** This project uses Render's free tier PostgreSQL database, which expires after 30 days. If you encounter a database connection error:

1. The database may have expired (free tier limitation)
2. Please contact me at dannykadoshi@me.com
3. I can recreate the database within 10 minutes
4. All data automatically reloads via build scripts

**Current Database Expiration:** January 27, 2025

This is a known limitation of free tier hosting and does not affect the project's code quality or functionality.

---

## Credits

### Code & Resources

- **Django Documentation:** [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **Bootstrap 5 Documentation:** [https://getbootstrap.com/docs/5.3/](https://getbootstrap.com/docs/5.3/)
- **Django Allauth:** [https://django-allauth.readthedocs.io/](https://django-allauth.readthedocs.io/)
- **Select2 Documentation:** [https://select2.org/](https://select2.org/)
- **Render Documentation:** [https://render.com/docs](https://render.com/docs)
- **Code Institute Learning Materials:** Django walkthrough projects and course content
- **Stack Overflow:** Various solutions for specific implementation challenges

### Design Inspiration

- **Color Palette:** Inspired by modern fitness app designs
- **Glassmorphism Effects:** CSS-Tricks and contemporary UI trends
- **Dashboard Layout:** Influenced by popular fitness tracking apps (Strava, MyFitnessPal)

### Content

- **Exercise Library:** Compiled from standard fitness resources and exercise databases
- **Icons & Emojis:** Unicode emoji characters
- **Wireframes:** Created using Adobe Firefly AI
- **Favicon & OG Images:** Generated using Pillow (Python Imaging Library)

### Acknowledgments

- **Code Institute:** For providing the comprehensive learning platform and project guidance
- **Slack Community:** For assistance with debugging, deployment issues, and best practices
- **Family & Friends:** For testing the application and providing valuable user feedback
- **Render:** For providing free cloud hosting for student projects

---

## Contact

**Developer:** Danny Kadoshi  
**Email:** dannykadoshi@me.com  
**GitHub:** [@dannykadoshi](https://github.com/dannykadoshi)

---

## License

This project was created for educational purposes as part of Code Institute's Full Stack Software Development Diploma. 

© 2025 FitTrack Aura | Portfolio Project 4 - Code Institute

---

**[Back to Top](#fittrack-aura-)**
