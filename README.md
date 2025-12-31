# FitTrack Aura 💪

A comprehensive Django fitness tracking web application that empowers users to log workouts, set goals, earn achievement badges, and maintain motivation through gamification.

![FitTrack Aura](static/images/og-image.png)

**Portfolio Project 4** - Full-Stack Toolkit  
**Code Institute Diploma** - Full Stack Software Development

---

## 🚀 Quick Start for Assessors

**Live Site:** [FitTrack Aura](https://fit-track-aura.onrender.com)  

**Admin Panel:** [Admin Panel - FitTrack Aura](https://fit-track-aura.onrender.com/admin/)  

**GitHub Projects Board:** [GitHub Repository - View User Stories & Agile Workflow](https://github.com/dannykadoshi/fit-track-aura)

**Full testing documentation:** [TESTING.md](TESTING.md)


**Test Accounts:**
- **Admin:** Username: `admin` / Password: *See LMS submission form*
- **Demo User:** Username: `create your own user` / Password: *Create a password*

**⏱️ Important:** Render free tier spins down after inactivity. First load may take 30-60 seconds (subsequent loads are instant).

**Key Metrics:**
- ✅ 41/41 User Stories Completed
- ✅ 157 Automated Tests (80% Coverage)
- ✅ Lighthouse: 100 Performance | 93 Accessibility | 100 Best Practices | 100 SEO
- ✅ WCAG AA Accessibility Compliant

---

## Table of Contents

- [Project Overview](#project-overview)
- [User Experience (UX)](#user-experience-ux)
- [Agile Development](#agile-development)
- [Features](#features)
- [Database Design](#database-design)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Project Overview

FitTrack Aura is a full-stack fitness tracking application built with Django, demonstrating proficiency in CRUD operations, user authentication, complex database relationships, and modern web development practices.

### Key Goals

![Home Page](docs/screenshots/home-page-1.png)
![Home Page](docs/screenshots/home-page-2.png)

- **Track Fitness:** Log detailed workouts with exercises, sets, reps, and weights
- **Set Goals:** Create fitness targets with visual progress tracking
- **Stay Motivated:** Earn achievement badges and maintain workout streaks
- **Analyze Progress:** View weekly activity charts and comprehensive statistics
- **Export Data:** Generate professional PDF reports of workouts and goals

### Target Audience

Fitness enthusiasts who want comprehensive workout tracking, goal-oriented individuals motivated by progress visualization, and gym-goers tracking strength training with progressive overload.

### Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~9,682 |
| **Git Commits** | 105 |
| **Test Coverage** | 80% |
| **Automated Tests** | 157 |
| **User Stories** | 41/41 completed |

---

## User Experience (UX)

### User Stories & Agile Development

Development followed Agile methodology using GitHub Projects with user stories organized into Epics, prioritized using MoSCoW method, and tracked through a Kanban board.

**GitHub Projects Board:** [View Full Board](https://github.com/users/dannykadoshi/projects/6)

#### Epic Summary

**Epic 1: Authentication & Profile** (5 stories - 100% complete)
- User registration and secure login
- Profile management with customizable settings
- Password change functionality

**Epic 2: Workout Management** (10 stories - 100% complete)
- Create workouts with multiple exercises
- View, edit, and delete workout history
- Search and filter workouts by date/category
- Export workouts to PDF
- Custom exercise library
- Workout templates for recurring routines
- Calendar visualization

**Epic 3: Goal Management** (6 stories - 100% complete)
- Create fitness goals with targets and deadlines
- Update progress with visual indicators
- Mark goals complete and track achievements
- Export goals to PDF

**Epic 4: Dashboard & Analytics** (3 stories - 100% complete)
- Real-time statistics dashboard
- Workout streak tracking (current and best)
- Weekly activity charts with Chart.js

**Epic 5: Gamification** (1 story - 100% complete)
- 7 achievement badges with auto-unlock system

**Epic 6: UX Enhancements** (2 stories - 100% complete)
- Dark/light mode toggle with persistence
- Social sharing (X, Facebook, WhatsApp)

**Epic 7: Testing & Quality** (2 stories - 100% complete)
- 157 automated tests with 80% coverage
- Comprehensive manual testing documentation

**Epic 8: Deployment** (2 stories - 100% complete)
- Production deployment to Render
- Complete project documentation

**Total:** 41/41 user stories completed ✅

#### Key User Stories (Examples)

**US-006: Create Workout**
> As a user, I want to create new workout entries so that I can log my training sessions

**Acceptance Criteria:**
- ✅ Form with title, date, duration, notes
- ✅ Add multiple exercises with dynamic formset
- ✅ Support strength (sets/reps/weight) and cardio (distance/duration)
- ✅ Form validation prevents empty submissions
- ✅ Badge unlock check (First Step badge)

**US-025: Achievement Badges**
> As a motivated user, I can earn achievement badges for reaching fitness milestones so that I feel recognized for my progress

**Acceptance Criteria:**
- ✅ 7 badge types with unlock conditions
- ✅ Automatic unlock when condition met
- ✅ Notification: "🎉 Achievement Unlocked!"
- ✅ Dashboard preview and dedicated badges page
- ✅ Cannot earn duplicate badges

---

### Design Decisions

#### Color Scheme

- **Primary:** Purple (#a855f7) - Energy and motivation
- **Secondary:** Pink (#ec4899) - Accent and gradients
- **Dark Mode:** Slate background (#0f172a) with purple gradients
- **Light Mode:** Soft blue-gray gradients for comfortable daytime viewing

#### Typography

- **Font Stack:** System fonts for performance (-apple-system, Segoe UI, Roboto)
- **Hierarchy:** Bold headings (700), regular body text (400), gradient logo text

#### UI/UX Principles

- **Glassmorphism:** Semi-transparent cards with backdrop blur for modern aesthetic

![Glassmorphism](docs/screenshots/Glassmorphism.png)

- **Mobile-First:** Responsive design using Bootstrap 5 grid system

![Mobile-First](docs/screenshots/responsive-mobile-dashboard.png)

- **Visual Feedback:** Success messages, progress bars, hover effects, loading states

![Success messages](docs/screenshots/user-feedback-message.png)

- **Accessibility:** Semantic HTML, ARIA labels, WCAG AA color contrast

---

### Wireframes

Low-fidelity wireframes guided the development process and ensured user-centered design:

![Dashboard Wireframe](docs/wireframes/wireframe-dashboard.png)
*Dashboard layout showing stat cards, activity chart, recent workouts, and goals sidebar*

![Workout Form Wireframe](docs/wireframes/wireframe-workout-create.png)
*Workout creation form with dynamic exercise formset and helpful tips*

![Goals Wireframe](docs/wireframes/wireframe-goals-list.png)
*Goals list with progress bars and active/completed sections*

---

## Agile Development

### Methodology

**Framework:** Scrum-inspired Agile with GitHub Projects

**Sprint Structure:**
- 5 sprints over 8 weeks
- 1-2 week sprint duration
- Daily progress tracking
- Sprint reviews and retrospectives

### GitHub Projects Board

**Columns:**
- **Backlog:** User stories awaiting prioritization
- **To Do:** Prioritized stories for current sprint
- **In Progress:** Actively being developed
- **Testing:** Under manual/automated testing
- **Done:** Completed and verified

**Labels:**
- `must-have` - Critical features (Epic 1, 2, 3)
- `should-have` - Important features (Epic 4, 5)
- `could-have` - Nice-to-have features (Epic 6)
- `wont-have` - Deferred to future releases

### User Story Template
```markdown
**As a** [user type]
**I want to** [action]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Priority:** Must Have / Should Have / Could Have
**Story Points:** 1-5 (complexity estimate)
```

### Development Workflow

1. **Story Selection:** Choose highest priority story from To Do
2. **Development:** Implement feature with TDD approach
3. **Testing:** Write/update automated tests
4. **Code Review:** Self-review against acceptance criteria
5. **Manual Testing:** User acceptance testing
6. **Done:** Move to Done column when all criteria met

### Sprint Retrospectives

**Sprint 1-2:** Authentication, core CRUD operations  
**Sprint 3:** Advanced features (templates, calendar, badges)  
**Sprint 4:** UX enhancements (dark mode, sharing, PDF)  
**Sprint 5:** Testing, documentation, deployment

---

## Features

### Core Features

#### 1. User Authentication & Authorization
- Django Allauth integration for registration, login, logout
- User data isolation (users can only access their own data)
- CSRF protection on all forms
- Secure password hashing (PBKDF2)

![Authentication](docs/screenshots/feature-signup.png)

---

#### 2. Dashboard
- **Statistics Overview:** Workouts this month, current streak, training minutes, goals progress
- **Streak Tracking:** Current and best streak with fire/trophy emojis
- **Weekly Activity Chart:** Chart.js visualization of workout duration (Mon-Sun)
- **Recent Workouts:** Quick access to last 5 workouts
- **Active Goals:** Top 3 goals with progress bars
- **Achievement Badges:** Preview of earned badges

![Dashboard](docs/screenshots/feature-dashboard-full.png)
![Dashboard](docs/screenshots/feature-dashboard-full-2.png)

---

#### 3. Workout Management (Full CRUD)

**Create:**
- Comprehensive form with title, date, duration, notes
- Dynamic exercise formset (add/remove exercises)
- Select2 autocomplete for 70+ exercises
- Support for strength (sets/reps/weight) and cardio (distance/duration)

![Create Workout](docs/screenshots/log-new-workout.png)

**Read:**
- Paginated workout list with search and filter
- Filter by date range or exercise category
- Detailed workout view with exercise table

**Update:**
- Pre-filled edit form with existing data
- Modify workouts and exercises

![Workout and Exercise filter](docs/screenshots/workout-and-exercise-filter.png)

**Delete:**
- Confirmation page before deletion
- Cascade delete related exercises

![Workout CRUD](docs/screenshots/feature-workout-list.png)

---

#### 4. Custom Exercise Library
- Create personal exercises for unique movements
- Custom exercises appear first in dropdowns (marked with ✨)
- Edit/delete own custom exercises
- 70+ default exercises protected (view-only)
- Categories: Strength, Cardio, Flexibility, Sports

![Exercise Library](docs/screenshots/feature-exercise-library.png)

---

#### 5. Workout Templates
- Save any workout as reusable template
- Templates preserve all exercises with sets/reps/weights
- "Use Template" creates new workout pre-filled with exercises
- Saves time for recurring routines (e.g., "Leg Day", "Upper Body Split")

![Templates](docs/screenshots/feature-templates-list.png)

---

#### 6. Goal Management (Full CRUD)
- Create goals with target number, unit, and deadline
- Visual progress bars with percentage calculation
- Update current progress and watch bars fill
- Mark goals complete (triggers badge check)
- Track completed goals with completion dates

![Goals](docs/screenshots/feature-goals-list.png)

---

#### 7. Achievement Badge System

**7 Badge Types:**
1. 🎯 **First Step** - Complete first workout
2. 💪 **Getting Strong** - Log 10 workouts
3. 🔥 **On Fire** - 7-day workout streak
4. ⭐ **Goal Crusher** - Complete first goal
5. ✨ **Innovator** - Create custom exercise
6. 🚀 **Dedicated** - Log 50 workouts
7. 👑 **Champion** - 30-day workout streak

**Features:**
- Automatic unlock when conditions met
- Notification: "🎉 Achievement Unlocked!"
- Badges page shows earned (color) and locked (grayscale)
- Dashboard preview (first 5 badges)

![Badges](docs/screenshots/feature-badges-page.png)

---

#### 8. Calendar View
- Monthly calendar grid (Mon-Sun) with workout visualization
- Days with workouts highlighted with purple gradient
- Today marked with pink badge
- Workout count badges (green circles)
- Clickable workout titles navigate to detail page
- Previous/Next month navigation
- Month statistics: Total workouts, total minutes

![Calendar](docs/screenshots/feature-calendar-full.png)

---

#### 9. Search & Filter
- **Search:** Find workouts by title or exercise name
- **Filter:** Date range (from/to dates)
- **Filter:** Exercise category (Strength, Cardio, Flexibility, Sports)
- **Clear Filters:** Reset to show all workouts
- Real-time results update

![Search & Filter](docs/screenshots/feature-workout-filters.png)

---

#### 10. PDF Export
- Professional PDF reports using ReportLab
- **Workouts PDF:** All workouts with dates, durations, exercises
- **Goals PDF:** All goals with progress percentages and status
- FitTrack Aura branding
- Automatic download with timestamped filename

![PDF Export](docs/screenshots/feature-workout-pdf-sample.png)

---

#### 11. Dark/Light Mode Toggle
- Toggle in user dropdown menu (☀️/🌙)
- Saved to user profile (persists across sessions/devices)
- Entire app theme changes instantly
- Frosted glass navbar effect in both modes
- Select2 dropdowns styled for both themes

**Dark Mode:** Purple gradients, dark cards, white text  
**Light Mode:** Blue-gray gradients, white cards, dark text

![Light Mode](docs/screenshots/feature-light-mode-dashboard.png)

---

#### 12. Social Sharing
- **Share from:** Workout detail pages, dashboard
- **Platforms:** X (Twitter), Facebook, WhatsApp, Copy Link
- Pre-filled messages with workout/progress data
- Share monthly progress from dashboard
- One-click sharing with friends and family

![Social Sharing](docs/screenshots/feature-share-workout.png)

---

#### 13. Additional Features

- **Form Validation:** Client and server-side validation with inline error messages
- **User Feedback:** Django messages framework with color-coded alerts

![User Feedback messages](docs/screenshots/user-feedback-message.png)

- **Error Handling:** Custom 404 and 500 error pages

![Error handling -404](docs/screenshots/404-error.png)

- **FAQ Page:** 13 comprehensive questions with accordion UI

![FAQ page](docs/screenshots/FAQ-page.png)

- **About Page:** Project overview, 14 feature cards, technology stack

![About Page](docs/screenshots/about-page-1.png)
![About Page](docs/screenshots/about-page-2.png)
![About Page](docs/screenshots/about-page-3.png)

- **Profile Management:** Edit bio, DOB, height, weight unit, theme preference, password change

![Profile Management](docs/screenshots/profile-management.png)

- **Security:** CSRF tokens, login required decorators, XSS protection, SQL injection protection

---

### Future Enhancements

**High Priority:**
- Workout analytics dashboard with personal records and volume tracking
- Nutrition tracking with calorie logging and macro goals
- Progress photos with timeline gallery

**Medium Priority:**
- Social features (follow users, workout feed, leaderboards)
- Mobile applications (iOS/Android) with offline mode
- Advanced goal types (body weight tracking, measurements)

**Lower Priority:**
- AI exercise form tips and workout recommendations
- Integration with MyFitnessPal, Strava, Garmin, Apple Health
- Shareable workout card images for Instagram

---

## Database Design

### Entity Relationship Diagram

![Database ERD](docs/database-erd.png)

### Database Schema Overview

FitTrack Aura uses a **relational database**:
- **Development:** SQLite3
- **Production:** PostgreSQL 17 (Render)

### Core Models

#### User (Django Built-in)
- Username, email, password (hashed)
- Django's `django.contrib.auth.models.User`

#### UserProfile (Extended User Model)
```python
user = OneToOneField(User, CASCADE)
bio = TextField(max_length=500, blank=True)
date_of_birth = DateField(null=True, blank=True)
height = DecimalField(max_digits=5, decimal_places=2)
weight_unit = CharField(choices=[('kg', 'KG'), ('lbs', 'LBS')])
theme = CharField(choices=[('dark', 'Dark'), ('light', 'Light')], default='dark')
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

**Key Features:**
- Auto-created on user signup (via signal)
- Stores preferences (weight unit, theme)
- One-to-one relationship with User

---

#### Workout
```python
user = ForeignKey(User, CASCADE)
title = CharField(max_length=200)
date = DateField()
duration = PositiveIntegerField(null=True, blank=True)  # minutes
notes = TextField(blank=True)
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

**Relationships:**
- ManyToMany with Exercise (through WorkoutExercise)
- OneToMany with WorkoutExercise

**Indexes:** `(user, date)` for performance

---

#### Exercise
```python
name = CharField(max_length=100, unique=True)
category = CharField(choices=CATEGORY_CHOICES)  # Strength, Cardio, Flexibility, Sports
description = TextField(blank=True)
is_custom = BooleanField(default=False)
created_by = ForeignKey(User, null=True, blank=True, SET_NULL)
created_at = DateTimeField(auto_now_add=True)
```

**Key Features:**
- 70+ default exercises (is_custom=False)
- Users can create custom exercises (is_custom=True)
- Custom exercises only visible to creator
- Cannot delete exercises used in workouts (PROTECT)

---

#### WorkoutExercise (Through Model)
```python
workout = ForeignKey(Workout, CASCADE)
exercise = ForeignKey(Exercise, PROTECT)
sets = PositiveIntegerField(null=True, blank=True)
reps = PositiveIntegerField(null=True, blank=True)
weight = DecimalField(max_digits=6, decimal_places=2, null=True)
unit = CharField(choices=[('kg', 'KG'), ('lbs', 'LBS')])
distance = DecimalField(max_digits=6, decimal_places=2, null=True)  # km
duration = PositiveIntegerField(null=True, blank=True)  # minutes
notes = TextField(blank=True)
```

**Usage:**
- **Strength exercises:** Use sets, reps, weight
- **Cardio exercises:** Use distance, duration

---

#### Goal
```python
user = ForeignKey(User, CASCADE)
title = CharField(max_length=200)
target_number = DecimalField(max_digits=10, decimal_places=2)
current_number = DecimalField(max_digits=10, decimal_places=2, default=0)
unit = CharField(choices=['workouts', 'kilograms', 'kilometers', 'minutes'])
target_date = DateField()
is_completed = BooleanField(default=False)
completed_date = DateField(null=True, blank=True)
```

**Properties:**
```python
@property
def progress(self):
    """Calculate progress percentage (0-100)"""
    if self.target_number > 0:
        return min(int((self.current_number / self.target_number) * 100), 100)
    return 0
```

---

#### WorkoutTemplate
```python
user = ForeignKey(User, CASCADE)
name = CharField(max_length=200)
description = TextField(blank=True)
created_at = DateTimeField(auto_now_add=True)
```

**Relationships:**
- ManyToMany with Exercise (through TemplateExercise)
- Unique together: (user, name)

---

#### TemplateExercise (Through Model)
```python
template = ForeignKey(WorkoutTemplate, CASCADE)
exercise = ForeignKey(Exercise, CASCADE)
sets, reps, weight, unit, distance, duration  # Same as WorkoutExercise
order = PositiveIntegerField(default=0)
```

---

#### Badge
```python
user = ForeignKey(User, CASCADE)
badge_type = CharField(choices=BADGE_CHOICES)  # 7 types
earned_date = DateTimeField(auto_now_add=True)
```

**Badge Types:**
- first_step, getting_strong, on_fire, goal_crusher, innovator, dedicated, champion

**Constraints:**
- Unique together: (user, badge_type) - prevents duplicates

---

### Database Relationships Summary

| Relationship | Type | Description |
|--------------|------|-------------|
| User → UserProfile | One-to-One | Extended user data |
| User → Workout | One-to-Many | User's workouts |
| User → Goal | One-to-Many | User's goals |
| User → Badge | One-to-Many | Earned badges |
| User → WorkoutTemplate | One-to-Many | Saved templates |
| User → Exercise | One-to-Many | Custom exercises |
| Workout ↔ Exercise | Many-to-Many | Through WorkoutExercise |
| WorkoutTemplate ↔ Exercise | Many-to-Many | Through TemplateExercise |

### Key Design Decisions

**Cascade Behavior:**
- Delete User → Deletes UserProfile, Workouts, Goals, Badges, Templates
- Delete Workout → Deletes WorkoutExercise entries
- Delete Exercise → PROTECT (cannot delete if used in workouts)

**Calculated Fields:**
- Goal progress percentage (calculated, not stored)
- Workout streak (calculated from workout dates)
- Best streak (calculated from all workout dates)

**Performance:**
- Indexed foreign keys (user, date)
- `select_related()` for single FK lookups
- `prefetch_related()` for ManyToMany relationships

---

## Technologies

### Core Technologies

**Backend:**
- Python 3.12
- Django 5.0
- PostgreSQL 17 (production)
- SQLite3 (development)

**Frontend:**
- HTML5, CSS3, JavaScript (ES6)
- Bootstrap 5.3
- Chart.js 4.4.0 (data visualization)
- Select2 4.1.0 (enhanced dropdowns)

**Deployment & Infrastructure:**
- Render (web service + PostgreSQL)
- WhiteNoise (static file serving)
- Gunicorn (WSGI server)
- Git & GitHub

### Python Packages

**Core:**
```
Django==5.0
django-allauth==65.13.1
python-decouple==3.8
dj-database-url==3.0.1
psycopg2-binary==2.9.11
```

**Production:**
```
gunicorn==23.0.0
whitenoise==6.11.0
```

**Features:**
```
reportlab==4.2.5      # PDF generation
Pillow==12.0.0        # Image processing
```

**Testing:**
```
coverage==7.13.0
```

**Full requirements:** [requirements.txt](requirements.txt)

### External Libraries (CDN)

- jQuery 3.6.0 (for Select2)
- Bootstrap 5.3 (CSS framework + JS)
- Select2 4.1.0 (enhanced dropdowns)
- Chart.js 4.4.0 (data visualization)

---

## Testing

Comprehensive testing was performed including automated unit tests, manual feature testing, validation, and browser compatibility testing.

### Testing Summary

| Test Type | Status | Details |
|-----------|--------|---------|
| **Automated Tests** | ✅ 157 passing | Unit tests for models, views, forms |
| **Code Coverage** | ✅ 80% | 1,589 of 1,839 statements covered |
| **HTML Validation** | ✅ Pass | W3C Markup Validation |
| **CSS Validation** | ✅ Pass | W3C CSS Validation |
| **Python (PEP 8)** | ✅ Pass | flake8 zero errors |
| **JavaScript** | ✅ Pass | JSHint validation |
| **Accessibility** | ✅ Pass | WCAG AA standards |
| **Performance** | ✅ 92-96/100 | Chrome Lighthouse |
| **Browser Compatibility** | ✅ Pass | Chrome, Safari, Firefox, Edge |
| **Responsiveness** | ✅ Pass | 375px - 2560px |

### Test Coverage by Module

**Goals App (84% coverage):**
- ✅ Goal CRUD operations
- ✅ Goal completion workflow
- ✅ Progress tracking
- ✅ Badge awarding system
- ✅ Authorization checks

**Workouts App (89% coverage):**
- ✅ Workout CRUD operations
- ✅ Workout streak calculations (100% coverage)
- ✅ Exercise library management
- ✅ Workout templates
- ✅ Calendar view
- ✅ Search and filter
- ✅ PDF generation

**Users App (91% coverage):**
- ✅ UserProfile creation
- ✅ Profile updates
- ✅ Password change
- ✅ Theme preference management

### Manual Testing Highlights

**Authentication:**
- ✅ User registration with validation
- ✅ Secure login/logout
- ✅ Password change

**Core Features:**
- ✅ Workout CRUD (create, read, update, delete)
- ✅ Goal CRUD with progress tracking
- ✅ Custom exercise management
- ✅ Workout template creation and usage
- ✅ Calendar view with navigation
- ✅ Search and filter workouts
- ✅ PDF export (workouts and goals)

**Gamification:**
- ✅ All 7 badges unlock correctly
- ✅ Streak calculations accurate
- ✅ Dashboard statistics real-time

**UX Features:**
- ✅ Dark/light mode toggle with persistence
- ✅ Social sharing (X, Facebook, WhatsApp)
- ✅ Responsive design on all devices

**Security:**
- ✅ User data isolation verified
- ✅ CSRF protection on all forms
- ✅ SQL injection prevention
- ✅ XSS protection

### Bugs Fixed

1. ✅ Select2 dropdown dark in light mode (CSS overrides)
2. ✅ Navbar transparency showing content (enhanced blur)
3. ✅ Social sharing missing URLs (production domain)
4. ✅ Workout dropdown background inconsistent (CSS)

**Known Limitations:**
- Native select dropdowns use OS styling (browser limitation)
- Render free tier: Database expires after 30 days (non-critical)

**Full testing documentation:** [TESTING.md](TESTING.md)

---

## Deployment

### Live Application

**URL:** [FitTrack Aura](https://fit-track-aura.onrender.com)

**Important Note for Assessors:**
- Render free tier spins down after 15 minutes of inactivity
- **First load may take 30-60 seconds** (subsequent loads are instant)
- Database expires after 30 days (build script reloads data automatically)

---

### Local Development

**Prerequisites:** Python 3.12+, Git

**Installation:**
```bash
# 1. Clone repository
git clone https://github.com/dannykadoshi/fit-track-aura.git
cd fit-track-aura

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
touch .env
# Add: SECRET_KEY, DEBUG=True, DATABASE_URL=sqlite:///db.sqlite3

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Load exercise data
python add_exercises.py

# 8. Run server
python manage.py runserver
```

Access at: http://127.0.0.1:8000/

---

### Environment Variables

**Required Variables:**
```bash
# .env file (local development)
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

# Production (Render Secret File)
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/database
PYTHON_VERSION=3.12.0
```

**Generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### Render Deployment

#### Step 1: Prepare Project

**Create `build.sh`:**
```bash
#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python create_superuser.py
python add_exercises.py
```

**Make executable:**
```bash
chmod +x build.sh
```

#### Step 2: Update settings.py
```python
import dj_database_url
from decouple import config

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600
    )
}

# Allowed hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']

# Middleware (add WhiteNoise)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security (production only)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

#### Step 3: Create Render Services

**Web Service:**
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect GitHub repository
4. Configure:
   - Name: `fit-track-aura`
   - Runtime: Python 3
   - Build Command: `./build.sh`
   - Start Command: `gunicorn fittrack_project.wsgi:application`
   - Instance Type: Free

**PostgreSQL Database:**
1. Click "New +" → "PostgreSQL"
2. Configure:
   - Name: `fit-track-aura-db`
   - PostgreSQL Version: 17
   - Instance Type: Free
3. Copy "Internal Database URL"

#### Step 4: Environment Variables

In Render web service, add **Secret File**:

**Filename:** `.env`

**Contents:**
```
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=postgres://...  # From PostgreSQL service
PYTHON_VERSION=3.12.0
```

#### Step 5: Deploy

1. Click "Manual Deploy" → "Deploy latest commit"
2. Wait 3-5 minutes for build
3. Service live at: `https://fit-track-aura.onrender.com`

---

### Deployment Troubleshooting

**Issue: Build Fails**
- Check build logs in Render dashboard
- Verify `requirements.txt` is up to date
- Ensure `build.sh` is executable

**Issue: Static Files Not Loading**
- Verify WhiteNoise in MIDDLEWARE
- Check STATIC_ROOT is set
- Run `python manage.py collectstatic` locally first

**Issue: Database Connection Error**
- Verify DATABASE_URL is set correctly
- Check PostgreSQL service is running
- Use Internal Database URL (not External)

**Issue: 500 Server Error**
- Set DEBUG=True temporarily to see error
- Check application logs in Render
- Verify all migrations ran successfully


## Credits

### Code & Learning Resources

- **Django Documentation:** Framework reference and best practices
- **Bootstrap 5 Documentation:** CSS framework and components
- **Code Institute:** Django walkthrough projects and course materials
- **Stack Overflow:** Problem-solving for specific implementation challenges
- **Real Python:** Python best practices and Django tutorials

### Design & Inspiration

- **Color Palette:** Modern fitness app designs (Strava, Nike Training Club)
- **Glassmorphism:** CSS-Tricks tutorials
- **UI/UX:** Dashboard layouts from MyFitnessPal and Strong app

### Content

- **Exercise Library:** Compiled from ExRx.net and standard fitness resources (70+ exercises)
- **Icons:** Unicode emoji characters (no external library)
- **Images:** Favicon and OG images generated using Pillow (Python Imaging Library)
- **Wireframes:** Created using Adobe Firefly AI

### Third-Party Libraries

- Django & Django Allauth (authentication)
- ReportLab (PDF generation)
- Chart.js (data visualization)
- Select2 (enhanced dropdowns)
- Coverage.py (testing)
- WhiteNoise (static file serving)

### Acknowledgments

- **Code Institute:** Comprehensive learning platform and project guidance
- **Family & Friends:** User testing and feedback
- **Render:** Free cloud hosting for student projects

---

## Contact

**Developer:** Danny Kadoshi  
**Email:** [dannykadoshi@me.com](dannykadoshi@me.com)
**GitHub:** [@dannykadoshi](https://github.com/dannykadoshi)

---

## License

Educational project for Code Institute Full Stack Software Development Diploma.

© 2025 Danny Kadoshi | Portfolio Project 4

---

**Last Updated:** December 31, 2025  
**Version:** 1.0.0  
**Status:** Grading Ready ✅

**[Back to Top](#fittrack-aura-)**