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
  - [Existing Features](#existing-features)
  - [Future Enhancements](#future-enhancements)
- [Database Design](#database-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Admin Access](#admin-access)
- [Credits](#credits)

---

## Project Overview

FitTrack Aura is a comprehensive full-stack fitness tracking web application built with Django and Python. It empowers users to log detailed workouts, set and achieve fitness goals, earn achievement badges, and maintain motivation through gamification features like workout streaks and visual progress tracking.

This application demonstrates advanced full-stack development capabilities including complex database relationships, dynamic forms, real-time statistics, data visualization, PDF generation, and modern UI/UX design with dark/light mode theming.

**Developed as Portfolio Project 4 (Full-Stack Toolkit) for Code Institute's Diploma in Full Stack Software Development.**

### Project Goals

#### Primary Goals
- Provide users with a comprehensive platform to track their complete fitness journey
- Enable detailed workout logging with multiple exercises, sets, reps, and weights
- Implement goal setting with visual progress tracking and completion milestones
- Motivate users through gamification (streaks, badges, achievements)
- Demonstrate proficiency in full-stack web development using Django
- Apply Agile methodology throughout the development process

#### Technical Goals
- Implement full CRUD (Create, Read, Update, Delete) functionality across all models
- Build complex database relationships (One-to-Many, Many-to-Many)
- Create dynamic forms with JavaScript-enhanced user experience
- Develop RESTful URL patterns and proper HTTP methods
- Ensure robust security (authentication, authorization, CSRF protection)
- Achieve high code quality (PEP 8 compliance, comprehensive testing)
- Deploy production-ready application to cloud platform

#### User Goals
- Track workout history with detailed exercise information
- Monitor progress toward fitness goals with visual indicators
- Stay motivated through achievement badges and streak tracking
- Export workout and goal data as professional PDF reports
- Customize experience with personal exercises and workout templates
- Access application on any device (responsive design)
- Choose preferred theme (dark/light mode)

**[⬆ Back to Top](#fittrack-aura-)**

---

## User Experience (UX)

### Target Audience

- **Fitness Enthusiasts**: Individuals committed to regular exercise who want comprehensive tracking
- **Goal-Oriented Users**: People who thrive on setting targets and measuring progress
- **Gym-Goers**: Athletes tracking strength training with sets, reps, and progressive overload
- **Cardio Enthusiasts**: Runners and cyclists logging distance and duration
- **Beginners**: New to fitness and want structure and motivation
- **Data-Driven Athletes**: Users who want analytics, charts, and exportable reports
- **Streak Builders**: People motivated by consistency and daily habits

### User Stories

All user stories were managed using **GitHub Projects** with Agile methodology. Stories were organized into Epics, assigned priority labels (Must Have, Should Have, Could Have), and tracked through a Kanban board from To Do → In Progress → Done.

**GitHub Projects Board:** [https://github.com/users/dannykadoshi/projects/4](https://github.com/users/dannykadoshi/projects/4)

#### Epic 1: User Authentication & Profile Management

**Must Have Features:**

- **US-001:** As a new user, I want to register for an account so that I can start tracking my fitness journey
  - **Acceptance Criteria:**
    - Registration form with username, email, password
    - Email validation
    - Password strength requirements
    - Successful registration redirects to dashboard
  - **Status:** ✅ Complete

- **US-002:** As a registered user, I want to log in securely so that I can access my personal workout data
  - **Acceptance Criteria:**
    - Login form with username/password
    - Session management with Django
    - "Remember me" functionality
    - Redirect to dashboard after login
  - **Status:** ✅ Complete

- **US-003:** As a logged-in user, I want to log out easily so that my data remains secure
  - **Acceptance Criteria:**
    - Logout button in navigation
    - Confirmation message
    - Session cleared
    - Redirect to homepage
  - **Status:** ✅ Complete

**Should Have Features:**

- **US-004:** As a user, I want to manage my profile so that I can personalize my account
  - **Acceptance Criteria:**
    - Edit bio, date of birth, height
    - Choose weight unit preference (kg/lbs)
    - Select theme preference (dark/light)
    - Update profile successfully
  - **Status:** ✅ Complete

- **US-005:** As a user, I want to change my password so that I can maintain account security
  - **Acceptance Criteria:**
    - Secure password change form
    - Current password verification
    - New password confirmation
    - Success message displayed
  - **Status:** ✅ Complete

---

#### Epic 2: Workout Management (CRUD)

**Must Have Features:**

- **US-006:** As a user, I want to create new workout entries so that I can log my training sessions
  - **Acceptance Criteria:**
    - Form with title, date, duration, notes
    - Add multiple exercises with sets/reps/weight
    - Dynamic formset (add/remove exercises)
    - Validation for required fields
    - Success message and redirect
  - **Status:** ✅ Complete

- **US-007:** As a user, I want to view all my workouts so that I can review my training history
  - **Acceptance Criteria:**
    - List view showing all workouts
    - Display title, date, duration, exercise count
    - Click to view full details
    - Responsive on mobile
  - **Status:** ✅ Complete

- **US-008:** As a user, I want to edit my workouts so that I can correct mistakes or add details
  - **Acceptance Criteria:**
    - Edit form pre-filled with existing data
    - Can modify all fields and exercises
    - Save updates successfully
    - Redirect to workout detail
  - **Status:** ✅ Complete

- **US-009:** As a user, I want to delete workouts so that I can remove incorrect entries
  - **Acceptance Criteria:**
    - Delete button on workout detail
    - Confirmation page before deletion
    - Cascade delete related exercises
    - Success message shown
  - **Status:** ✅ Complete

- **US-010:** As a user, I want to add multiple exercises to a workout so that I can track complete training sessions
  - **Acceptance Criteria:**
    - Exercise formset with add/remove buttons
    - Select from exercise library (70+ exercises)
    - Track sets, reps, weight, distance, duration
    - Support both strength and cardio exercises
  - **Status:** ✅ Complete

**Should Have Features:**

- **US-011:** As a user, I want to search and filter workouts so that I can find specific training sessions
  - **Acceptance Criteria:**
    - Search by title or exercise name
    - Filter by date range (from/to)
    - Filter by exercise category
    - Clear filters button
    - Results update dynamically
  - **Status:** ✅ Complete

- **US-012:** As a user, I want to export my workouts to PDF so that I can share or print my training log
  - **Acceptance Criteria:**
    - Export button on workout list
    - PDF includes all workouts with details
    - Professional formatting
    - Download triggers automatically
  - **Status:** ✅ Complete

**Could Have Features:**

- **US-013:** As a user with specific routines, I can add my own custom exercises so that I can track movements not in the default list
  - **Acceptance Criteria:**
    - Exercise library page
    - Create custom exercise (name, category, description)
    - Custom exercises appear in workout dropdown
    - Edit/delete own custom exercises
    - Default exercises protected
  - **Status:** ✅ Complete

- **US-014:** As a user with recurring workouts, I can save workouts as templates so that I can quickly log repeated routines
  - **Acceptance Criteria:**
    - "Save as Template" button on workout detail
    - Template list view
    - "Use Template" creates new workout
    - Pre-fills all exercises from template
    - Can edit before saving
  - **Status:** ✅ Complete

- **US-015:** As a user, I can view my workouts in a calendar so that I can see my training schedule visually
  - **Acceptance Criteria:**
    - Monthly calendar view
    - Days with workouts highlighted
    - Show workout count per day
    - Click workout to view details
    - Navigate between months
  - **Status:** ✅ Complete

---

#### Epic 3: Goal Management (CRUD)

**Must Have Features:**

- **US-016:** As a user, I want to create fitness goals so that I have targets to work toward
  - **Acceptance Criteria:**
    - Goal form with title, target, unit, date
    - Support multiple goal types (workouts, weight, distance)
    - Initial progress set to 0
    - Success message displayed
  - **Status:** ✅ Complete

- **US-017:** As a user, I want to view my goals so that I can track my progress
  - **Acceptance Criteria:**
    - List view with active and completed sections
    - Visual progress bars
    - Percentage calculation
    - Due date displayed
  - **Status:** ✅ Complete

- **US-018:** As a user, I want to update my goals so that I can adjust targets or progress
  - **Acceptance Criteria:**
    - Edit form with current values
    - Update target or current progress
    - Progress bar updates in real-time
    - Can change target date
  - **Status:** ✅ Complete

- **US-019:** As a user, I want to delete goals so that I can remove outdated objectives
  - **Acceptance Criteria:**
    - Delete button on goal detail
    - Confirmation required
    - Success message shown
  - **Status:** ✅ Complete

- **US-020:** As a user, I want to mark goals as complete so that I can celebrate achievements
  - **Acceptance Criteria:**
    - Complete button on active goals
    - Goal moves to completed section
    - Completion date recorded
    - Badge unlock check triggered
  - **Status:** ✅ Complete

**Should Have Features:**

- **US-021:** As a user, I want to export goals to PDF so that I can track my goal history
  - **Acceptance Criteria:**
    - Export button on goals page
    - PDF shows all goals (active + completed)
    - Includes progress percentages
    - Professional formatting
  - **Status:** ✅ Complete

---

#### Epic 4: Dashboard & Analytics

**Must Have Features:**

- **US-022:** As a user, I want to see a dashboard with my fitness statistics so that I can monitor progress at a glance
  - **Acceptance Criteria:**
    - Welcome message with username
    - Stat cards: workouts count, streak, training time, goals progress
    - Recent workouts list (last 5)
    - Active goals preview (top 3)
    - Streak statistics sidebar
  - **Status:** ✅ Complete

- **US-023:** As a user, I want to see a workout streak counter so that I stay motivated to exercise consistently
  - **Acceptance Criteria:**
    - Current streak calculation (consecutive days)
    - Best streak (all-time longest)
    - Streak badge on dashboard header
    - Fire emoji when streak is active
    - Trophy emoji for milestone streaks
  - **Status:** ✅ Complete

**Should Have Features:**

- **US-024:** As a user, I want to see weekly activity charts so that I can visualize my training patterns
  - **Acceptance Criteria:**
    - Chart.js bar chart
    - Shows Mon-Sun workout duration
    - Total minutes, average, most active day
    - Responsive on mobile
    - Animated bars
  - **Status:** ✅ Complete

---

#### Epic 5: Gamification & Achievements

**Could Have Features:**

- **US-025:** As a motivated user, I can earn achievement badges for reaching fitness milestones so that I feel recognized for my progress
  - **Acceptance Criteria:**
    - 7 badge types with unlock conditions
    - Badges unlock automatically
    - Notification when badge earned
    - Badges page showing earned/locked
    - Dashboard badge preview (first 5)
  - **Status:** ✅ Complete

**Badge Types Implemented:**
1. 🎯 **First Step** - Complete first workout
2. 💪 **Getting Strong** - Log 10 workouts
3. 🔥 **On Fire** - Maintain 7-day streak
4. ⭐ **Goal Crusher** - Complete first goal
5. ✨ **Innovator** - Create custom exercise
6. 🚀 **Dedicated** - Log 50 workouts
7. 👑 **Champion** - Maintain 30-day streak

---

#### Epic 6: User Experience Enhancements

**Could Have Features:**

- **US-026:** As a user who prefers different visual themes, I can switch between dark and light mode so that I can use the app comfortably in different lighting conditions
  - **Acceptance Criteria:**
    - Toggle button in user dropdown
    - Theme saves to user profile
    - Persists across sessions
    - All pages respect theme
    - Default is dark mode
  - **Status:** ✅ Complete
  - **Known Limitation:** Native browser select dropdowns use OS styling (documented)

- **US-027:** As a user who wants to share achievements, I can post my progress on social media so that I can celebrate with friends
  - **Acceptance Criteria:**
    - Share buttons on workout detail
    - Share monthly progress from dashboard
    - Support X (Twitter), Facebook, WhatsApp
    - Copy link to clipboard
    - Pre-filled messages with workout/goal data
  - **Status:** ✅ Complete

---

#### Epic 7: Testing & Quality Assurance

**Must Have Features:**

- **US-028:** As a developer, I want comprehensive automated tests so that I can ensure code quality and prevent bugs
  - **Acceptance Criteria:**
    - Unit tests for all models
    - View tests for CRUD operations
    - Form validation tests
    - 80%+ code coverage
    - All tests passing
  - **Status:** ✅ Complete (88% coverage)

- **US-029:** As a developer, I want detailed manual testing documentation so that all features are verified to work correctly
  - **Acceptance Criteria:**
    - TESTING.md with all test cases
    - Screenshots of key features
    - Browser compatibility testing
    - Responsive design testing
    - Security testing documented
  - **Status:** ✅ Complete

---

#### Epic 8: Deployment & Documentation

**Must Have Features:**

- **US-030:** As a developer, I want to deploy the application to a cloud platform so that users can access it online
  - **Acceptance Criteria:**
    - Deployed to Render
    - PostgreSQL database configured
    - Static files served correctly
    - Environment variables secured
    - HTTPS enabled
  - **Status:** ✅ Complete

- **US-031:** As a developer, I want comprehensive README documentation so that others can understand and use the project
  - **Acceptance Criteria:**
    - Clear project overview
    - Installation instructions
    - Database schema diagram
    - Features documentation
    - Testing summary
    - Deployment guide
  - **Status:** ✅ Complete

---

### Design

#### Color Scheme

FitTrack Aura uses a modern, energetic purple-to-pink gradient theme that conveys motivation, premium quality, and athletic energy:

**Primary Colors:**
- **Primary Purple:** `#a855f7` - Main brand color, buttons, gradients
- **Secondary Pink:** `#ec4899` - Accent color, hover states, gradients
- **Deep Purple:** `#581c87` - Rich depth in backgrounds

**Background Colors:**
- **Dark Background:** `#0f172a` - Professional dark slate
- **Card Background:** `rgba(255, 255, 255, 0.05)` - Semi-transparent glassmorphism

**Semantic Colors:**
- **Success Green:** `#10b981` - Completed goals, positive actions
- **Warning Orange:** `#f59e0b` - Streak indicators, important notices
- **Danger Red:** `#ef4444` - Delete actions, warnings
- **Info Blue:** `#3b82f6` - Informational messages

**Light Mode Palette:**
- **Light Background:** `linear-gradient(135deg, #f0f4f8, #d9e2ec)`
- **Card Background:** `rgba(255, 255, 255, 0.9)`
- **Text Color:** `#1e293b` - Dark slate for readability

**Gradients:**
- **Primary Gradient:** `linear-gradient(135deg, #a855f7, #ec4899)`
- **Background Gradient:** `linear-gradient(135deg, #0f172a 0%, #581c87 50%, #0f172a 100%)`

#### Typography

**Font Stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

**Font Weights:**
- **Regular (400):** Body text, descriptions, secondary content
- **Semibold (600):** Subheadings, labels, card titles
- **Bold (700):** Main headings, stats, emphasis

**Font Sizes:**
- **Display (2.5rem):** Hero headings, page titles
- **Heading 1 (2rem):** Section headings
- **Heading 2-4 (1.5-1.125rem):** Card titles, sub-sections
- **Body (1rem):** Standard text
- **Small (0.875rem):** Meta information, timestamps

**Special Typography:**
- **Gradient Text:** Used for "FitTrack Aura" logo
- **Emoji Integration:** Contextual emojis enhance visual communication
- **Icon Fonts:** Unicode emoji characters (no external icon library needed)

#### UI/UX Design Principles

**1. Glassmorphism:**
- Semi-transparent cards with `backdrop-filter: blur()`
- Creates depth and modern aesthetic
- Maintains readability with subtle backgrounds

**2. Gradient Backgrounds:**
- Purple-to-dark gradient creates visual interest
- Consistent theme across all pages
- Light mode uses soft blue-gray gradients

**3. Responsive Design:**
- Mobile-first approach using Bootstrap 5
- Breakpoints: 576px, 768px, 992px, 1200px
- Hamburger menu on mobile, full nav on desktop
- Touch-friendly button sizes (min 44x44px)

**4. Visual Hierarchy:**
- Clear distinction between headings, body text, metadata
- Stat cards use large numbers for emphasis
- Progress bars provide instant visual feedback

**5. Consistent Spacing:**
- Bootstrap spacing utilities (p-*, m-*, gap-*)
- 8px base unit for consistent rhythm
- Generous padding on cards (1.5-2rem)

**6. Interactive Feedback:**
- Hover effects on all interactive elements
- Success/error messages for user actions
- Loading states for async operations
- Button state changes (active, disabled)

**7. Accessibility:**
- Semantic HTML5 elements (`<nav>`, `<main>`, `<article>`)
- ARIA labels on interactive elements
- Color contrast meets WCAG AA standards (4.5:1 minimum)
- Keyboard navigation supported
- Skip to main content link

**8. Smooth Transitions:**
- CSS transitions on hover states
- Chart.js animations for data visualization
- Progress bar animations
- Theme switching smooth transition

#### Design Patterns

**Card-Based Layout:**
- Content organized in distinct cards
- Clear visual separation
- Consistent padding and border radius

**Dashboard Grid:**
- CSS Grid for stat cards (responsive columns)
- Flexbox for internal alignment
- Consistent aspect ratios

**Forms:**
- Clear labels above inputs
- Placeholder text for guidance
- Inline validation errors
- Submit buttons prominently placed

**Navigation:**
- Fixed navbar for easy access
- Dropdown menus for organization
- Active state indicators
- Breadcrumb trails where appropriate

**Empty States:**
- Friendly messages when no data exists
- Call-to-action buttons to guide users
- Visual icons for context

### Wireframes

Low-fidelity wireframes were created during the planning phase to establish layout, user flow, and information architecture before development began. These wireframes guided the development process and ensured user-centered design.

#### Dashboard Wireframe
![Dashboard Wireframe](docs/wireframes/wireframe-dashboard.png)

**Key Elements:**
- Welcome header with username
- Four stat cards (workouts, streak, time, goals)
- Weekly activity chart
- Recent workouts list
- Active goals sidebar with progress bars

**Layout Decisions:**
- Grid layout for stat cards (responsive)
- Chart prominently placed for data visualization
- Sidebar for goals keeps them visible without overwhelming

---

#### Create Workout Wireframe
![Create Workout Wireframe](docs/wireframes/wireframe-workout-create.png)

**Key Elements:**
- Workout details section (title, date, duration)
- Exercise formset with dynamic add/remove
- Exercise dropdown with search
- Sets/reps/weight inputs
- Pro tips sidebar

**UX Decisions:**
- Single-page form (no multi-step)
- Inline exercise management
- Clear visual separation between exercises
- Helpful tips alongside form

---

#### Goals List Wireframe
![Goals List Wireframe](docs/wireframes/wireframe-goals-list.png)

**Key Elements:**
- Active goals section with progress bars
- Completed goals section
- Create goal button prominently placed
- Progress percentage displayed

**Visual Hierarchy:**
- Active goals at top (primary focus)
- Completed goals collapsed or below
- Progress bars provide instant visual feedback

---

#### Mobile Wireframes
![Mobile Wireframes](docs/wireframes/wireframe-mobile.png)

**Mobile-Specific Considerations:**
- Hamburger menu navigation
- Stat cards stack vertically
- Touch-friendly button sizes
- Simplified tables with horizontal scroll
- Bottom navigation for key actions

**[⬆ Back to Top](#fittrack-aura-)**

---

## Features

### Existing Features

#### 1. User Authentication & Authorization

**Registration & Login:**
- Django Allauth integration for robust authentication
- Email and username registration
- Password strength validation
- "Remember me" functionality
- Password reset via email
- Session management with secure cookies

**Security Features:**
- CSRF protection on all forms
- Password hashing (PBKDF2 SHA256)
- User data isolation (query filtering by user)
- Login required decorators on protected views
- SQL injection protection (Django ORM)
- XSS protection (template escaping)

![Sign Up Page](docs/screenshots/feature-signup.png)
![Login Page](docs/screenshots/feature-login.png)

---

#### 2. Comprehensive Dashboard

**Statistics Overview:**
- **Workouts This Month:** Count of current month workouts
- **Current Streak:** Consecutive days with workouts
- **Minutes Trained:** Total duration this month
- **Goals Progress:** Average progress across active goals

**Visual Elements:**
- Streak badge with fire emoji (🔥) in header
- Color-coded stat cards with gradient icons
- Achievement badge milestone alerts (3, 7, 14, 30+ day streaks)

**Recent Activity:**
- Last 5 workouts with quick access to edit
- Workout title, date, duration, exercise count
- Click to view full details

**Active Goals Preview:**
- Top 3 active goals displayed
- Visual progress bars with percentage
- Color changes when goal reaches 100% (green)
- Due date countdown

**Streak Statistics Sidebar:**
- Current streak with fire emoji
- Best streak (all-time) with trophy emoji
- Total workouts lifetime count

**Weekly Activity Chart:**
- Chart.js bar chart visualization
- Monday-Sunday workout duration
- Hover tooltips showing exact minutes
- Statistics: Total minutes, daily average, most active day
- Smooth animations on page load

![Dashboard Overview](docs/screenshots/feature-dashboard-full.png)
![Dashboard Statistics](docs/screenshots/feature-dashboard-stats.png)
![Weekly Activity Chart](docs/screenshots/feature-dashboard-chart.png)

---

#### 3. Workout Management (Full CRUD)

**Create Workout:**
- Comprehensive workout form with validation
- Fields: Title, Date, Duration (minutes), Notes
- Dynamic exercise formset (add/remove exercises)
- Select2 autocomplete for exercise search
- Support for multiple exercises per workout
- Separate inputs for strength (sets/reps/weight) and cardio (distance/duration)
- Weight unit selection (kg/lbs)
- Form validation (required fields, positive numbers)
- Success message with badge unlock check

![Workout Create Form](docs/screenshots/feature-workout-create.png)
![Exercise Selection](docs/screenshots/feature-workout-exercise-select.png)

---

**View Workouts:**
- Paginated list of all workouts
- Display: Title, Date, Duration, Exercise count
- Quick action buttons: View, Edit, Delete
- Export to PDF button
- Search and filter section
- Responsive card layout on mobile

![Workout List](docs/screenshots/feature-workout-list.png)

---

**Workout Detail:**
- Full workout information display
- Exercise table with all details (sets, reps, weight, distance, duration)
- Notes section (if provided)
- Workout summary sidebar (exercise count, duration, creation date)
- Action buttons: Edit, Delete, Save as Template
- Social sharing buttons (X, Facebook, WhatsApp, Copy Link)

![Workout Detail](docs/screenshots/feature-workout-detail.png)

---

**Edit Workout:**
- Pre-filled form with existing data
- Modify any field or exercise
- Add/remove exercises dynamically
- Validation prevents data loss
- Success message on update

![Workout Edit](docs/screenshots/feature-workout-edit.png)

---

**Delete Workout:**
- Confirmation page before deletion
- Shows workout title for verification
- Warning about permanent deletion
- Cancel option to prevent accidental deletion
- Cascade delete related exercises
- Success message after deletion

![Workout Delete Confirmation](docs/screenshots/feature-workout-delete.png)

---

**Search & Filter Workouts:**
- **Search by:**
  - Workout title
  - Exercise name (searches through all exercises)
- **Filter by:**
  - Date range (From date, To date)
  - Exercise category (Strength, Cardio, Flexibility, Sports)
- Apply filters button
- Clear filters button to reset
- Filtered results update dynamically
- "No results" state with clear filters option

![Workout Search & Filter](docs/screenshots/feature-workout-filters.png)
![Filtered Results](docs/screenshots/feature-workout-filtered.png)

---

**Export Workouts to PDF:**
- Professional PDF report generation (ReportLab)
- Includes all workouts with full details
- Table format: Date, Title, Duration, Exercise Count
- FitTrack Aura branding
- Automatic download with timestamped filename
- Success message confirmation

![PDF Export Button](docs/screenshots/feature-workout-pdf-button.png)
![PDF Sample](docs/screenshots/feature-workout-pdf-sample.png)

---

#### 4. Custom Exercise Library

**Exercise Management:**
- View all exercises (default + custom)
- Create custom exercises for unique movements
- Edit/delete own custom exercises
- Default exercises protected (view-only)
- Exercise categories: Strength, Cardio, Flexibility, Sports

**Custom Exercise Features:**
- Custom exercises appear first in dropdowns
- Marked with ✨ star emoji
- Grouped under "My Custom Exercises"
- Only visible to creator (user-isolated)
- Badge unlock: "Innovator" badge for creating first custom exercise

**Exercise Library Interface:**
- Search exercises by name
- Filter by category
- Collapsible default exercises section (shows count)
- Expanded custom exercises section
- Add Exercise button prominently placed

![Exercise Library](docs/screenshots/feature-exercise-library.png)
![Create Custom Exercise](docs/screenshots/feature-exercise-create.png)
![Custom Exercise in Dropdown](docs/screenshots/feature-exercise-dropdown-custom.png)

---

#### 5. Workout Templates

**Save Workouts as Templates:**
- Convert any workout into reusable template
- Template stores: Name, Description, All exercises with details
- Templates preserve sets, reps, weights, distances
- Multiple templates supported

**Use Templates:**
- Template list view with cards
- Each card shows: Name, Description, Exercise count, Exercise preview
- "Use Template" creates new workout
- Pre-fills all exercises from template
- User can edit before saving
- Saves time for recurring workouts

**Template Management:**
- Create from existing workout
- View all templates
- Delete templates (workouts created from template remain)
- Template created date displayed

![Workout Templates List](docs/screenshots/feature-templates-list.png)
![Save as Template](docs/screenshots/feature-template-save.png)
![Use Template](docs/screenshots/feature-template-use.png)

---

#### 6. Goal Management (Full CRUD)

**Create Goals:**
- Comprehensive goal form
- Fields: Title, Target Number, Unit, Current Progress, Target Date
- Unit options: Workouts, Kilograms, Kilometers, etc.
- Initial progress starts at 0
- Validation: Required fields, positive numbers, logical dates
- Success message on creation

![Goal Create Form](docs/screenshots/feature-goal-create.png)

---

**View Goals:**
- Separate sections: Active Goals, Completed Goals
- Visual progress bars with gradient fill
- Progress percentage calculated automatically
- Color changes: Purple (in progress), Green (100%+)
- Due date displayed
- Quick actions: Edit, Complete, Delete

![Goals List](docs/screenshots/feature-goals-list.png)

---

**Update Goal Progress:**
- Edit form pre-filled with current values
- Update current progress or target
- Progress bar updates in real-time
- Can modify target date
- Readable progress text: "X out of Y Units"
- Success message on save

![Goal Edit Form](docs/screenshots/feature-goal-edit.png)

---

**Complete Goals:**
- One-click "Complete" button
- Goal moves to Completed section
- Completion date recorded
- Badge unlock check: "Goal Crusher" badge
- Success message: "Goal completed! 🎉"
- Goal visible in completed history

![Goal Complete Success](docs/screenshots/feature-goal-complete.png)

---

**Export Goals to PDF:**
- Professional PDF report (ReportLab)
- Includes all goals (active + completed)
- Table format: Title, Target, Progress %, Status, Due Date
- Summary statistics (total, completed, active count)
- FitTrack Aura branding
- Automatic download

![Goals PDF Export](docs/screenshots/feature-goals-pdf-sample.png)

---

#### 7. Achievement Badge System

**7 Badge Types:**

1. **🎯 First Step** - Complete your first workout
2. **💪 Getting Strong** - Log 10 workouts
3. **🔥 On Fire** - Maintain a 7-day workout streak
4. **⭐ Goal Crusher** - Complete your first goal
5. **✨ Innovator** - Create a custom exercise
6. **🚀 Dedicated** - Log 50 workouts
7. **👑 Champion** - Maintain a 30-day workout streak

**Badge Features:**
- Automatic unlock when conditions met
- Success notification: "🎉 Achievement Unlocked: [Badge Name]!"
- Badge persistence (unique_together constraint prevents duplicates)
- Badges page shows earned/locked status
- Earned badges: Full color, earned date shown
- Locked badges: Grayscale, motivational text ("Keep training!")

**Badge Display:**
- Dashboard preview: First 5 earned badges
- "+X More" link if more than 5 badges
- Dedicated badges page with all 7 types
- Progress counter: "X/7 badges earned"

![Badges Page](docs/screenshots/feature-badges-page.png)
![Badge Unlock Notification](docs/screenshots/feature-badge-unlock.png)
![Dashboard Badge Preview](docs/screenshots/feature-dashboard-badges.png)

---

#### 8. Calendar View

**Monthly Calendar Display:**
- Standard calendar grid (Monday-Sunday)
- Current month/year displayed prominently
- Previous/Next navigation buttons
- Month statistics: Total workouts, Total minutes

**Day Indicators:**
- **Today:** Pink badge with date number
- **Days with workouts:** Purple gradient background
- **Workout count:** Green circle badge with number
- **Workout titles:** Clickable, truncated to fit
- **Duration:** Displayed below title (e.g., "60min")

**Interactive Features:**
- Click workout title → Navigate to workout detail
- Navigate between months
- Legend at bottom explains indicators
- Responsive on mobile (smaller day cells)

**Visual Design:**
- Empty days: Minimal styling
- Workout days: Stand out with color
- Multiple workouts per day: Stacked list
- Overflow handling: "+X more" for many workouts

![Calendar View](docs/screenshots/feature-calendar-full.png)
![Calendar Day with Workouts](docs/screenshots/feature-calendar-workout-day.png)
![Calendar Navigation](docs/screenshots/feature-calendar-navigation.png)

---

#### 9. Dark/Light Mode Toggle

**Theme Switching:**
- Toggle in user dropdown menu
- Icons: ☀️ Light Mode, 🌙 Dark Mode
- One-click theme change
- Success message: "Switched to [Theme] Mode"
- Instant visual change across entire app

**Theme Persistence:**
- Saved to UserProfile model
- Persists across browser sessions
- Syncs across devices (user-based, not cookie-based)
- Default theme: Dark mode

**Theme Styling:**

**Dark Mode:**
- Purple-pink gradient background
- Dark cards with glassmorphism
- White text
- High contrast

**Light Mode:**
- Light blue-gray gradient background
- White cards with subtle borders
- Dark text (#1e293b)
- Soft shadows

**Components Themed:**
- Navbar with frosted glass effect
- All cards and forms
- Dropdowns and menus
- Progress bars
- Buttons and badges
- Footer

**Known Limitation:**
- Select2 dropdown options styled correctly
- Documented browser limitation with native select OS controls

![Light Mode Dashboard](docs/screenshots/feature-light-mode-dashboard.png)
![Light Mode Workout](docs/screenshots/feature-light-mode-workout.png)
![Theme Toggle Dropdown](docs/screenshots/feature-theme-toggle.png)

---

#### 10. Social Sharing

**Share Locations:**
- Workout detail page
- Dashboard (monthly progress)

**Share Platforms:**
- **X (Twitter):** Pre-filled tweet with workout/progress + hashtags
- **Facebook:** Share dialog with FitTrack Aura URL
- **WhatsApp:** Pre-filled message with workout/progress details
- **Copy Link:** Copies current page URL to clipboard

**Share Content:**

**From Workout:**
```
💪 Just completed '[Workout Title]' - [X]min of training!
#fitness #workout
https://fit-track-aura.onrender.com
```

**From Dashboard:**
```
📊 This month on FitTrack Aura: [X] workouts, [Y] minutes! 💪
#fitnessjourney
https://fit-track-aura.onrender.com
```

**Features:**
- Share buttons styled consistently
- Icons: 🐦 (X), 📘 (Facebook), 💬 (WhatsApp), 🔗 (Copy)
- Copy link shows success alert
- Opens in new tab
- Mobile-optimized (native share on mobile browsers)

![Share Buttons Workout](docs/screenshots/feature-share-workout.png)
![Share Dashboard](docs/screenshots/feature-share-dashboard.png)
![Share Preview Twitter](docs/screenshots/feature-share-twitter.png)
![Share Preview WhatsApp](docs/screenshots/feature-share-whatsapp.png)

---

#### 11. User Profile Management

**Profile Information:**
- Username display
- Email (from Django User model)
- Bio (text area)
- Date of birth
- Height (in cm)
- Weight unit preference (kg/lbs)
- Theme preference (dark/light)

**Profile Actions:**
- View profile information
- Edit profile details
- Change password (secure form)
- Account created date

**Profile Features:**
- Validation on all fields
- Success messages for updates
- Password change requires current password
- Profile automatically created on user registration

![Profile View](docs/screenshots/feature-profile-view.png)
![Profile Edit](docs/screenshots/feature-profile-edit.png)
![Change Password](docs/screenshots/feature-password-change.png)

---

#### 12. Responsive Navigation

**Desktop Navigation:**
- Fixed navbar at top
- Logo/brand on left
- Navigation links: Dashboard, Workouts (dropdown), Goals
- User menu on right with icon

**Mobile Navigation:**
- Hamburger menu icon
- Collapsible menu
- Touch-friendly button sizes
- Full-width dropdowns

**Workouts Dropdown:**
- My Workouts
- Log New Workout
- ─────────────
- 📅 Calendar View
- 📋 Workout Templates
- 💪 Exercise Library

**User Dropdown:**
- 👤 My Profile
- 🏆 Achievements
- ─────────────
- ☀️ Light Mode (or 🌙 Dark Mode)
- ─────────────
- 🚪 Logout

**Navigation Features:**
- Active page highlighted
- Hover effects
- Dropdown menus close on click outside
- Keyboard accessible

![Desktop Navigation](docs/screenshots/feature-nav-desktop.png)
![Mobile Navigation](docs/screenshots/feature-nav-mobile.png)
![Workouts Dropdown](docs/screenshots/feature-nav-workouts-dropdown.png)
![User Dropdown](docs/screenshots/feature-nav-user-dropdown.png)

---

#### 13. Additional Features

**Form Validation:**
- Client-side validation (HTML5)
- Server-side validation (Django forms)
- Inline error messages
- Required field indicators (*)
- Positive number validation
- Date validation

**User Feedback:**
- Django messages framework
- Color-coded messages: Success (green), Error (red), Info (blue), Warning (yellow)
- Auto-dismiss after 5 seconds
- Positioned at top of page
- Accessible close button

**Error Handling:**
- Custom 404 error page
- Custom 500 error page
- User-friendly error messages
- Redirect to appropriate pages

**FAQ Page:**
- Accordion-style questions
- 13 comprehensive FAQs
- Covers all major features
- Bootstrap collapse functionality
- Mobile-responsive

**About Page:**
- Project overview
- Feature showcase (14 feature cards)
- Technology stack details
- Developer information
- Links to Dashboard and FAQ

**Security Features:**
- CSRF tokens on all forms
- Login required decorators
- User query filtering
- Secure password hashing
- XSS protection (template escaping)
- SQL injection protection (ORM)
- Environment variables for secrets

![Success Message](docs/screenshots/feature-message-success.png)
![404 Error Page](docs/screenshots/feature-404-page.png)
![FAQ Page](docs/screenshots/feature-faq-page.png)
![About Page](docs/screenshots/feature-about-page.png)

---

### Future Enhancements

Features identified during development but deferred for future releases:

#### High Priority

1. **Workout Stats & Analytics Dashboard**
   - Personal records tracking (heaviest weight, longest run)
   - Body part frequency heatmap
   - Progressive overload charts
   - Volume tracking (sets × reps × weight)
   - Estimated 1RM calculations

2. **Nutrition Tracking**
   - Calorie logging
   - Macro tracking (protein, carbs, fats)
   - Meal planning
   - Food database integration
   - Daily nutrition goals

3. **Progress Photos**
   - Upload before/after photos
   - Photo timeline gallery
   - Side-by-side comparison tool
   - Privacy controls
   - Cloud storage integration

#### Medium Priority

4. **Social Features**
   - Follow other users
   - Public workout feed
   - Like and comment on workouts
   - Leaderboards and challenges
   - Friend workout streak comparisons

5. **Mobile Application**
   - Native iOS app (Swift/SwiftUI)
   - Native Android app (Kotlin)
   - Offline mode with sync
   - Push notifications for streaks
   - Wearable device integration (Apple Watch, Fitbit)

6. **Advanced Goal Types**
   - Body weight tracking graph
   - Body measurements (chest, waist, biceps)
   - Multi-phase goals (bulking/cutting cycles)
   - Auto-adjust goals based on progress
   - Goal templates library

7. **Workout Programs**
   - Pre-built workout programs (5x5, PPL, HIIT)
   - Program progress tracking
   - Rest day scheduling
   - Deload week recommendations
   - Program customization

#### Lower Priority

8. **AI Features**
   - Exercise form tips (ML video analysis)
   - Workout recommendations based on history
   - Predicted 1RM calculator
   - Recovery time estimation
   - Injury risk alerts

9. **Integration**
   - MyFitnessPal calorie sync
   - Strava activity import
   - Garmin/Polar heart rate data
   - Google Fit / Apple Health export
   - Spotify workout playlists

10. **Enhanced Sharing**
    - Generate shareable workout cards (images)
    - Instagram Stories integration
    - Monthly progress video compilation
    - Achievement celebration animations
    - Printable workout logs

---

## Database Design

### Database Schema

FitTrack Aura uses a **relational database** with the following structure:
- **Development:** SQLite3 (Django default)
- **Production:** PostgreSQL 17 (Render)

### Entity Relationship Diagram
```
┌──────────────────┐
│       User       │ (Django built-in)
│  (Authentication)│
└────────┬─────────┘
         │
         │ 1:1
         ▼
    ┌────────────────┐
    │  UserProfile   │
    │ - bio          │
    │ - dob          │
    │ - height       │
    │ - weight_unit  │
    │ - theme        │
    └────────────────┘
         │
         │ 1:N
         ├──────────────────────┬──────────────────┬──────────────────┬───────────────────┐
         ▼                      ▼                  ▼                  ▼                   ▼
    ┌──────────┐         ┌──────────┐       ┌──────────┐       ┌──────────────┐   ┌──────────┐
    │ Workout  │         │   Goal   │       │  Badge   │       │WorkoutTemplate│   │ Exercise │
    │          │         │          │       │          │       │              │   │(is_custom│
    │- title   │         │- title   │       │- type    │       │- name        │   │created_by)│
    │- date    │         │- target  │       │- earned  │       │- description │   │          │
    │- duration│         │- current │       │  _date   │       │              │   │- name    │
    │- notes   │         │- unit    │       │          │       │              │   │- category│
    └────┬─────┘         │- date    │       └──────────┘       └──────┬───────┘   └────┬─────┘
         │               │- complete│                                  │                │
         │ 1:N           └──────────┘                                  │ 1:N            │
         │                                                              │                │
         ▼                                                              ▼                │
 ┌────────────────┐                                            ┌────────────────┐       │
 │WorkoutExercise │                                            │TemplateExercise│       │
 │(Through Model) │◄───────────────────────────────────────────┤(Through Model) │       │
 │- sets          │                     N:1                    │- sets          │       │
 │- reps          │                                            │- reps          │       │
 │- weight        │                                            │- weight        │       │
 │- unit          │                                            │- unit          │       │
 │- distance      │                                            │- distance      │       │
 │- duration      │                                            │- duration      │       │
 └────────┬───────┘                                            └────────┬───────┘       │
          │                                                             │                │
          │ N:1                                                         │ N:1            │
          └─────────────────────────────────────────────────────────────┴────────────────┘
```

### Model Descriptions

#### 1. User (Django Built-in)
Django's `django.contrib.auth.models.User`

**Fields:**
- `username` (CharField, unique)
- `email` (EmailField)
- `password` (CharField, hashed)
- `first_name` (CharField)
- `last_name` (CharField)
- `is_active` (BooleanField)
- `is_staff` (BooleanField)
- `date_joined` (DateTimeField)

**Relationships:**
- OneToOne → UserProfile
- OneToMany → Workout
- OneToMany → Goal
- OneToMany → Badge
- OneToMany → WorkoutTemplate
- OneToMany → Exercise (custom exercises)

---

#### 2. UserProfile (Extended User Model)

**Purpose:** Store additional user information beyond Django's default User model

**Fields:**
```python
user = OneToOneField(User, on_delete=CASCADE)
bio = TextField(max_length=500, blank=True)
date_of_birth = DateField(null=True, blank=True)
height = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # in cm
weight_unit = CharField(max_length=3, choices=[('kg', 'Kilograms'), ('lbs', 'Pounds')])
theme = CharField(max_length=10, choices=[('dark', 'Dark'), ('light', 'Light')], default='dark')
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

**Meta:**
- `verbose_name = "User Profile"`

**Methods:**
- `__str__()` → Returns "{username}'s profile"

**Signals:**
- `post_save` on User → Automatically creates UserProfile

---

#### 3. Workout

**Purpose:** Store workout sessions

**Fields:**
```python
user = ForeignKey(User, on_delete=CASCADE, related_name='workouts')
title = CharField(max_length=200)
date = DateField()
duration = PositiveIntegerField(null=True, blank=True)  # minutes
notes = TextField(blank=True)
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

**Meta:**
- `ordering = ['-date', '-created_at']`
- `indexes = [('user', 'date')]` (for performance)

**Methods:**
- `__str__()` → Returns "{title} - {date}"
- `@property total_exercises` → Count of related WorkoutExercise objects

**Relationships:**
- ManyToOne → User
- OneToMany → WorkoutExercise
- ManyToMany → Exercise (through WorkoutExercise)

---

#### 4. Exercise

**Purpose:** Library of exercises (default + user-created)

**Fields:**
```python
name = CharField(max_length=100, unique=True)
category = CharField(max_length=50, choices=CATEGORY_CHOICES)
description = TextField(blank=True)
is_custom = BooleanField(default=False)
created_by = ForeignKey(User, null=True, blank=True, on_delete=SET_NULL)
created_at = DateTimeField(auto_now_add=True)

CATEGORY_CHOICES = [
    ('strength', 'Strength'),
    ('cardio', 'Cardio'),
    ('flexibility', 'Flexibility'),
    ('sports', 'Sports'),
]
```

**Meta:**
- `ordering = ['name']`
- `indexes = [('category',), ('is_custom',)]`

**Methods:**
- `__str__()` → Returns "{name}"

**Validation:**
- Custom exercises must have `created_by` set
- Default exercises have `is_custom=False` and `created_by=None`

---

#### 5. WorkoutExercise (Through Model)

**Purpose:** Junction table linking Workouts to Exercises with additional data

**Fields:**
```python
workout = ForeignKey(Workout, on_delete=CASCADE, related_name='workout_exercises')
exercise = ForeignKey(Exercise, on_delete=PROTECT)
sets = PositiveIntegerField(null=True, blank=True)
reps = PositiveIntegerField(null=True, blank=True)
weight = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
unit = CharField(max_length=3, choices=[('kg', 'KG'), ('lbs', 'LBS')], default='kg')
distance = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # km
duration = PositiveIntegerField(null=True, blank=True)  # minutes
notes = TextField(blank=True)
```

**Meta:**
- `ordering = ['id']`

**Methods:**
- `__str__()` → Returns "{exercise.name} in {workout.title}"

**Business Logic:**
- Strength exercises: Use sets, reps, weight
- Cardio exercises: Use distance, duration
- PROTECT on Exercise prevents deletion if used in workouts

---

#### 6. Goal

**Purpose:** Track fitness goals and progress

**Fields:**
```python
user = ForeignKey(User, on_delete=CASCADE, related_name='goals')
title = CharField(max_length=200)
target_number = DecimalField(max_digits=10, decimal_places=2)
current_number = DecimalField(max_digits=10, decimal_places=2, default=0)
unit = CharField(max_length=50, choices=UNIT_CHOICES)
target_date = DateField()
is_completed = BooleanField(default=False)
completed_date = DateField(null=True, blank=True)
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)

UNIT_CHOICES = [
    ('workouts', 'Workouts'),
    ('kilograms', 'Kilograms'),
    ('kilometers', 'Kilometers'),
    ('minutes', 'Minutes'),
]
```

**Meta:**
- `ordering = ['-created_at']`

**Properties:**
```python
@property
def progress_percentage(self):
    if self.target_number > 0:
        return min(int((self.current_number / self.target_number) * 100), 100)
    return 0

@property
def target_display(self):
    return f"{int(self.target_number)}" if self.target_number % 1 == 0 else str(self.target_number)

@property
def current_display(self):
    return f"{int(self.current_number)}" if self.current_number % 1 == 0 else str(self.current_number)
```

**Methods:**
```python
def mark_complete(self):
    self.is_completed = True
    self.completed_date = timezone.now().date()
    self.save()

def __str__(self):
    return self.title
```

---

#### 7. WorkoutTemplate

**Purpose:** Store reusable workout templates

**Fields:**
```python
user = ForeignKey(User, on_delete=CASCADE, related_name='workout_templates')
name = CharField(max_length=200)
description = TextField(blank=True)
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

**Meta:**
- `ordering = ['-created_at']`
- `unique_together = ['user', 'name']`

**Methods:**
- `__str__()` → Returns "{name} - {user.username}"

---

#### 8. TemplateExercise (Through Model)

**Purpose:** Store exercises within workout templates

**Fields:**
```python
template = ForeignKey(WorkoutTemplate, on_delete=CASCADE, related_name='exercises')
exercise = ForeignKey(Exercise, on_delete=CASCADE)
sets = PositiveIntegerField(null=True, blank=True)
reps = PositiveIntegerField(null=True, blank=True)
weight = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
unit = CharField(max_length=3, choices=[('kg', 'KG'), ('lbs', 'LBS')], default='kg')
distance = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
duration = PositiveIntegerField(null=True, blank=True)
notes = TextField(blank=True)
order = PositiveIntegerField(default=0)
```

**Meta:**
- `ordering = ['order', 'id']`

**Methods:**
- `__str__()` → Returns "{exercise.name} in {template.name}"

---

#### 9. Badge

**Purpose:** Achievement badges earned by users

**Fields:**
```python
user = ForeignKey(User, on_delete=CASCADE, related_name='badges')
badge_type = CharField(max_length=50, choices=BADGE_CHOICES)
earned_date = DateTimeField(auto_now_add=True)

BADGE_CHOICES = [
    ('first_step', '🎯 First Step'),
    ('getting_strong', '💪 Getting Strong'),
    ('on_fire', '🔥 On Fire'),
    ('goal_crusher', '⭐ Goal Crusher'),
    ('innovator', '✨ Innovator'),
    ('dedicated', '🚀 Dedicated'),
    ('champion', '👑 Champion'),
]
```

**Meta:**
- `ordering = ['-earned_date']`
- `unique_together = ['user', 'badge_type']`

**Properties:**
```python
@property
def badge_icon(self):
    return dict(self.BADGE_CHOICES)[self.badge_type].split()[0]

@property
def badge_name(self):
    return ' '.join(dict(self.BADGE_CHOICES)[self.badge_type].split()[1:])

@property
def badge_description(self):
    descriptions = {
        'first_step': 'Complete your first workout',
        'getting_strong': 'Log 10 workouts',
        # ... etc
    }
    return descriptions[self.badge_type]
```

**Methods:**
- `__str__()` → Returns "{badge_name} - {user.username}"

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

---

### Database Migrations

All database changes tracked through Django migrations:
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# View migration status
python manage.py showmigrations
```

**Initial Migrations:**
- `0001_initial.py` - Created User, Workout, Exercise, WorkoutExercise
- `0002_goal.py` - Added Goal model
- `0003_userprofile.py` - Added UserProfile
- `0004_badge.py` - Added Badge model
- `0005_workouttemplate.py` - Added WorkoutTemplate, TemplateExercise
- `0006_userprofile_theme.py` - Added theme field to UserProfile

**[⬆ Back to Top](#fittrack-aura-)**

---

## Technologies Used

### Languages

- **Python 3.12** - Backend logic, Django framework
- **HTML5** - Structure and semantic markup
- **CSS3** - Styling, animations, responsive design
- **JavaScript (ES6)** - Interactive features, DOM manipulation
- **SQL** - Database queries (via Django ORM)

---

### Frameworks & Libraries

#### Backend Frameworks
- **Django 5.0** - High-level Python web framework
  - Model-View-Template (MVT) architecture
  - ORM for database abstraction
  - Built-in admin interface
  - Security features (CSRF, XSS protection)
  - Form handling and validation
  
- **Django Allauth 65.13.1** - Authentication system
  - User registration and login
  - Email verification
  - Password reset
  - Session management
  - Social authentication support (unused but available)

#### Frontend Frameworks
- **Bootstrap 5.3** - CSS framework
  - Responsive grid system
  - Pre-built components (navbar, cards, modals)
  - Utility classes for spacing/typography
  - Mobile-first approach
  - Customizable with CSS variables

- **Select2 4.1.0** - Enhanced select dropdowns
  - Searchable exercise selection
  - Keyboard navigation
  - Custom styling
  - Mobile-friendly

- **Chart.js 4.4.0** - Data visualization
  - Weekly activity bar chart
  - Smooth animations
  - Responsive canvas rendering
  - Customizable colors and tooltips

#### Python Packages

**Core Django:**
```txt
Django==5.0
asgiref==3.11.0
sqlparse==0.5.5
```

**Authentication:**
```txt
django-allauth==65.13.1
```

**Configuration:**
```txt
python-decouple==3.8        # Environment variables
dj-database-url==3.0.1      # Database URL parsing
```

**Production Server:**
```txt
gunicorn==23.0.0            # WSGI HTTP server
whitenoise==6.11.0          # Static file serving
psycopg2-binary==2.9.11     # PostgreSQL adapter
```

**PDF Generation:**
```txt
reportlab==4.2.5            # PDF creation library
Pillow==12.0.0              # Image processing (for PDFs)
```

**Testing:**
```txt
coverage==7.13.0            # Code coverage analysis
```

**Other:**
```txt
packaging==25.0             # Version string parsing
```

---

### Database

**Development:**
- **SQLite3** - Django default, file-based database
- Simple setup, no configuration needed
- Perfect for development and testing
- File location: `db.sqlite3`

**Production:**
- **PostgreSQL 17** - Robust relational database
- Hosted on Render
- Supports complex queries and relationships
- ACID compliant
- Better performance at scale
- Connection via `DATABASE_URL` environment variable

---

### Tools & Services

#### Development Tools
- **Git 2.x** - Version control
  - Commit history tracking
  - Branch management
  - Collaboration
  
- **GitHub** - Code repository
  - Remote repository hosting
  - GitHub Projects (Agile board)
  - Issue tracking
  - README and documentation

- **VS Code** - Code editor
  - Python extension
  - Django extension
  - Linting (flake8)
  - Git integration
  - Debugger

- **Chrome DevTools** - Testing and debugging
  - Element inspector
  - Network tab
  - Console for JavaScript
  - Responsive design mode
  - Lighthouse audits

#### Cloud Services
- **Render** - Cloud deployment platform
  - Web service hosting
  - PostgreSQL database
  - Automatic deploys from GitHub
  - SSL/HTTPS included
  - Environment variable management
  - Build scripts support

- **Cloudinary** (Optional, configured but unused)
  - Image and media storage
  - CDN for fast delivery
  - Image transformations
  - Available for future profile photos feature

#### External Libraries (CDN)
- **jQuery 3.6.0** - JavaScript library (for Select2)
- **Bootstrap 5.3** - CSS framework
- **Select2 4.1.0** - Enhanced dropdowns
- **Chart.js 4.4.0** - Data visualization
- **Bootstrap Icons** - Icon fonts (unused, using emoji instead)

---

### Testing Tools

- **Coverage.py 7.13.0** - Code coverage measurement
  - Track which code is tested
  - Generate HTML coverage reports
  - 88% coverage achieved

- **Django TestCase** - Unit testing framework
  - Model testing
  - View testing
  - Form validation testing
  - 32 tests written

- **W3C Validators**
  - HTML Markup Validation
  - CSS Validation
  - Accessibility checks

- **Chrome Lighthouse** - Performance auditing
  - Performance scores
  - Accessibility audits
  - Best practices checks
  - SEO analysis

- **flake8** - Python linting
  - PEP 8 compliance
  - Code quality checks
  - Unused imports detection

---

### Version Control
```bash
# Git workflow
git add .
git commit -m "Descriptive message"
git push origin main

# Branching (for features)
git checkout -b feature-name
git merge feature-name

# View history
git log --oneline --graph
```

**Commit Message Convention:**
- Feature: `Add workout template functionality`
- Fix: `Fix Select2 dropdown light mode styling`
- Docs: `Update README with deployment instructions`
- Style: `Improve navbar frosted glass effect`
- Test: `Add tests for goal completion`

**[⬆ Back to Top](#fittrack-aura-)**

---

## Testing

Comprehensive testing was performed across all features. Full testing documentation is available in **[TESTING.md](TESTING.md)**.

### Testing Summary

#### Automated Testing

**Test Suite:**
- 32 unit tests
- 88% code coverage
- All tests passing ✅

**Coverage Breakdown:**
- Models: 95-96% coverage
- Forms: 100% coverage
- Views: 58-59% coverage (lower due to error handling branches)

**Run Tests:**
```bash
python manage.py test
coverage run --source='.' manage.py test
coverage report
```

---

#### Manual Testing

**Features Tested:**
- ✅ User authentication (registration, login, logout)
- ✅ Workout CRUD operations
- ✅ Custom exercise management
- ✅ Workout template creation and usage
- ✅ Goal CRUD operations
- ✅ Achievement badge system
- ✅ Calendar view
- ✅ Search and filter
- ✅ PDF export (workouts and goals)
- ✅ Dark/light mode toggle
- ✅ Social sharing
- ✅ Profile management
- ✅ Form validation
- ✅ Security (authorization, CSRF protection)

---

#### Validation

**HTML Validation:**
- ✅ All pages pass W3C Markup Validation
- No errors or warnings

**CSS Validation:**
- ✅ `static/css/style.css` passes W3C CSS Validation
- Vendor prefixes intentional for compatibility

**Python Code Quality:**
- ✅ PEP 8 compliant (flake8)
- Zero errors, zero warnings
- Clean, readable code

**Accessibility:**
- ✅ WCAG AA color contrast
- ✅ Semantic HTML
- ✅ ARIA labels
- ✅ Keyboard navigation

---

#### Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 131+ | ✅ Fully functional |
| Safari | 17+ | ✅ Fully functional |
| Firefox | 133+ | ✅ Fully functional |
| Edge | 131+ | ✅ Fully functional |

---

#### Responsiveness

**Tested Devices:**
- ✅ iPhone SE (375px)
- ✅ iPhone 12/13 (390px)
- ✅ iPhone 14 Pro Max (430px)
- ✅ iPad Mini (768px)
- ✅ iPad Pro (1024px)
- ✅ Desktop (1920px+)

**All features responsive and functional on all screen sizes.**

---

#### Performance

**Lighthouse Scores (Desktop):**
- Performance: 92-96/100
- Accessibility: 100/100
- Best Practices: 100/100
- SEO: 100/100

---

### Known Issues

#### Resolved Issues
- ✅ Select2 dropdown dark in light mode (fixed with CSS overrides)
- ✅ Navbar transparency showing content (fixed with frosted glass effect)
- ✅ Social sharing missing URLs (fixed with production domain)
- ✅ Workout dropdown background inconsistent (fixed with CSS)

#### Known Limitations
- **Browser Limitation:** Native select dropdown options use OS-level styling on some browsers (documented, using Select2 instead)
- **Render Free Tier:** PostgreSQL database expires after 90 days (non-critical, build script reloads data)

**No critical bugs or issues at time of submission.**

**[⬆ Back to Top](#fittrack-aura-)**

---

## Deployment

### Live Deployment

**Production URL:** [https://fit-track-aura.onrender.com](https://fit-track-aura.onrender.com)

**Platform:** Render (free tier)
**Database:** PostgreSQL 17
**Static Files:** WhiteNoise

---

### Local Development Setup

#### Prerequisites
- Python 3.12 or higher
- Git
- pip (Python package manager)
- Virtual environment tool (venv)

#### Step-by-Step Installation

**1. Clone Repository**
```bash
git clone https://github.com/dannykadoshi/fit-track-aura.git
cd fit-track-aura
```

**2. Create Virtual Environment**
```bash
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Create Environment Variables**
```bash
# Create .env file
touch .env

# Add to .env:
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

**Generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**5. Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Create Superuser**
```bash
python manage.py createsuperuser
# Enter username, email, password when prompted
```

**7. Load Exercise Data**
```bash
python add_exercises.py
# Loads 70+ default exercises into database
```

**8. Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

**9. Run Development Server**
```bash
python manage.py runserver
```

**10. Access Application**
- **Homepage:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- Login with superuser credentials

---

### Production Deployment to Render

#### Prerequisites
- Render account (free tier available)
- GitHub account with repository

#### Deployment Steps

**1. Prepare Project**

Create `build.sh` in project root:
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python create_superuser.py
python add_exercises.py
```

Make executable:
```bash
chmod +x build.sh
```

**2. Update `settings.py`**

Add at top:
```python
import dj_database_url
from decouple import config
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
    # ... rest
]
```

Configure static files (bottom of settings.py):
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

**3. Create Render Web Service**

- Go to [Render Dashboard](https://dashboard.render.com/)
- Click "New +" → "Web Service"
- Connect GitHub repository
- Configure:
  - **Name:** fit-track-aura
  - **Region:** Oregon (or nearest)
  - **Branch:** main
  - **Runtime:** Python 3
  - **Build Command:** `./build.sh`
  - **Start Command:** `gunicorn fittrack_project.wsgi:application`
  - **Instance Type:** Free

**4. Add Environment Variables**

In Render service settings, add **Secret File**:

**Filename:** `.env`

**Contents:**
```
SECRET_KEY=your-production-secret-key
DEBUG=False
PYTHON_VERSION=3.12.0
```

**5. Create PostgreSQL Database**

- Click "New +" → "PostgreSQL"
- **Name:** fit-track-aura-db
- **Region:** Same as web service
- **PostgreSQL Version:** 17
- **Instance Type:** Free

**6. Connect Database**

- In web service, go to "Environment" tab
- Add variable:
  - **Key:** `DATABASE_URL`
  - **Value:** Copy from PostgreSQL "Internal Database URL"

**7. Deploy**

- Click "Manual Deploy" → "Deploy latest commit"
- Wait 3-5 minutes for build
- Service will be live at: `https://fit-track-aura.onrender.com`

---

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| SECRET_KEY | Django secret key | `django-insecure-...` |
| DEBUG | Debug mode (False in prod) | `False` |
| DATABASE_URL | PostgreSQL connection | `postgres://user:pass@host/db` |
| PYTHON_VERSION | Python version for Render | `3.12.0` |
| CLOUDINARY_URL | Media storage (optional) | `cloudinary://...` |

---

### Security Considerations

**Production Security:**
- ✅ `DEBUG = False`
- ✅ SECRET_KEY in environment variable
- ✅ Database credentials secured
- ✅ HTTPS enforced (SSL redirect)
- ✅ Secure cookies enabled
- ✅ CSRF tokens on all forms
- ✅ `.env` file in `.gitignore`
- ✅ No hardcoded secrets in code
- ✅ XSS protection (template escaping)
- ✅ SQL injection protection (Django ORM)

**What's NOT in Version Control:**
- `.env` file
- `db.sqlite3` (local database)
- `__pycache__/`
- `.venv/`
- `staticfiles/` (generated)
- `*.pyc` files

---

### Render Free Tier Notes

**Limitations:**
- Services spin down after 15 minutes of inactivity
- First load after idle: 30-60 seconds
- No persistent disk storage (use PostgreSQL)
- 750 hours/month free (enough for student projects)

**Benefits:**
- Automatic deploys from GitHub
- Free SSL certificate
- PostgreSQL database included
- Environment variable management
- Perfect for portfolios and MVPs

**[⬆ Back to Top](#fittrack-aura-)**

---

## Admin Access

### For Code Institute Assessors

**Admin Panel URL:** [https://fit-track-aura.onrender.com/admin/](https://fit-track-aura.onrender.com/admin/)

**Admin Credentials:**
- **Username:** `admin`
- **Password:** *Provided separately in LMS submission form*

**Admin Capabilities:**
- View all users and their data
- Full CRUD on all models (Workouts, Goals, Exercises, Badges, Templates)
- User management
- Database administration
- View relationship data (WorkoutExercise, TemplateExercise)

---

### Test User Account

**Option 1: Create Your Own**
- Visit: [https://fit-track-aura.onrender.com/accounts/signup/](https://fit-track-aura.onrender.com/accounts/signup/)
- Register new account
- Start logging workouts and goals

**Option 2: Use Admin Panel**
- Login as admin
- View existing user data
- Explore all features

---

### Important Note for Assessors

**First Load Delay:**
Render's free tier spins down after 15 minutes of inactivity. If the service is asleep, the **first page load may take 30-60 seconds**. Subsequent loads will be instant.

**Database Limitation:**
The free PostgreSQL database expires after 90 days. If you encounter a database connection error:
1. Database may have expired (free tier constraint)
2. Contact me at dannykadoshi@me.com
3. I can recreate it within 10 minutes
4. Build script automatically reloads all data

**Current Database Expiry:** March 31, 2026

*This is a known limitation of free hosting and does not affect code quality or functionality.*

**[⬆ Back to Top](#fittrack-aura-)**

---

## Credits

### Code & Resources

**Official Documentation:**
- [Django Documentation](https://docs.djangoproject.com/) - Framework reference
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/) - CSS framework
- [Chart.js Documentation](https://www.chartjs.org/docs/) - Data visualization
- [Select2 Documentation](https://select2.org/) - Enhanced dropdowns
- [Render Documentation](https://render.com/docs) - Deployment platform

**Learning Resources:**
- Code Institute Django Walkthrough Projects
- Code Institute LMS lessons on full-stack development
- Django for Beginners (William S. Vincent)
- MDN Web Docs - HTML/CSS/JavaScript reference

**Problem Solving:**
- Stack Overflow - Various implementation challenges
- Django Forum - ORM queries and relationships
- Real Python - Python best practices
- CSS-Tricks - Glassmorphism and modern CSS

---

### Design Inspiration

**Color Palette:**
- Modern fitness app designs (Strava, Nike Training Club)
- Purple-pink gradient trend in 2024/2025 design

**UI/UX Patterns:**
- Dashboard layouts from MyFitnessPal and Strong app
- Glassmorphism effects from CSS-Tricks tutorials
- Card-based layouts from Bootstrap examples

**Typography:**
- System font stack for performance
- Bootstrap default typography with custom weights

---

### Content

**Exercise Library:**
- Compiled from:
  - ExRx.net (exercise database)
  - Bodybuilding.com exercise guides
  - Standard fitness resources
- 70+ exercises across 4 categories

**Icons & Emoji:**
- Unicode emoji characters (no external library)
- Contextual use for visual communication

**Images:**
- **Favicon:** Generated using Pillow (Python Imaging Library)
- **OG Image:** Created with Pillow for social media previews
- **Wireframes:** Created using Adobe Firefly AI

---

### Third-Party Libraries

**Python Packages:**
- Django and Django Allauth (backend framework)
- ReportLab (PDF generation)
- Coverage.py (testing)
- python-decouple (environment variables)
- All listed in `requirements.txt`

**JavaScript Libraries (CDN):**
- jQuery 3.6.0 - Dependency for Select2
- Select2 4.1.0 - Enhanced dropdowns
- Chart.js 4.4.0 - Data visualization
- Bootstrap 5.3 - CSS framework and JS components

---

### Acknowledgments

**Code Institute:**
- Comprehensive learning platform
- Project guidance and assessment criteria
- Walkthrough projects (I Think Therefore I Blog, Task Manager)
- Mentor support and feedback

**Slack Community:**
- Debugging assistance
- Deployment troubleshooting
- Best practice discussions
- Peer code reviews

**Family & Friends:**
- User acceptance testing
- Feature feedback
- Bug discovery
- Usability insights

**Render:**
- Free cloud hosting for student projects
- Excellent documentation
- Reliable platform for portfolio work

---

### Special Thanks

- **My Mentor** - For code reviews and professional guidance
- **Code Institute Tutors** - For technical support
- **Fellow Students** - For collaboration and motivation
- **Open Source Community** - For Django, Python, and countless libraries

**[⬆ Back to Top](#fittrack-aura-)**

---

## Contact

**Developer:** Danny Kadoshi  
**Email:** dannykadoshi@me.com  
**GitHub:** [@dannykadoshi](https://github.com/dannykadoshi)  
**LinkedIn:** [Danny Kadoshi](https://www.linkedin.com/in/dannykadoshi)

**Project Repository:** [https://github.com/dannykadoshi/fit-track-aura](https://github.com/dannykadoshi/fit-track-aura)  
**Live Application:** [https://fit-track-aura.onrender.com](https://fit-track-aura.onrender.com)

---

## License

This project was created for educational purposes as part of Code Institute's Full Stack Software Development Diploma.

**Educational Use:** Free to view and learn from
**Commercial Use:** Not permitted without permission
**Attribution:** Required if used for learning purposes

© 2025 Danny Kadoshi | Portfolio Project 4 - Code Institute

---

**[⬆ Back to Top](#fittrack-aura-)**

---

**Last Updated:** December 31, 2025  
**Version:** 1.0.0  
**Status:** Production Ready ✅
