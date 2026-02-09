# Today I Learned (TIL) - Django Social Platform

A modern social media platform built with Django where users can share their knowledge through short posts, follow other users, and manage their profiles. This project is part of the Django-201 tutorial series, demonstrating advanced Django concepts and best practices.

## 🚀 Features

### User Authentication
- User registration and login with **django-allauth**
- Email-based authentication
- Password reset functionality
- Session management with "Remember me" option
- Styled authentication pages with modern UI

### Posts & Feed
- Create short posts (max 240 characters) via AJAX modal
- Real-time post creation without page reload
- Chronological feed of posts from all users
- View individual post details
- Author attribution with timestamps

### User Profiles
- Customizable user profiles with:
  - Profile picture upload with thumbnail generation
  - Cover image upload
  - First name and last name
  - Username customization
- Profile statistics:
  - Total posts count
  - Followers count
  - Following count
- View other users' profiles

### Profile Management
- Edit profile information
- Update profile and cover images with preview
- Change password (with old password verification)
- Separate forms for profile data and password changes
- Image processing with **sorl-thumbnail**

### Social Features
- Follow/Unfollow other users
- AJAX-powered follow actions without page reload
- Visual follow/unfollow button states
- Follower/Following relationship tracking
- Prevention of self-following

### UI/UX
- Modern, responsive design with **TailwindCSS**
- Sidebar navigation with context-aware menu items
- Toast notifications with auto-dismiss
- Icon integration with **Boxicons**
- Modal-based post creation
- Smooth transitions and hover effects

## Screenshots

### Login
<img width="1918" height="867" alt="login" src="https://github.com/user-attachments/assets/57a7ed08-b30b-4b9b-896e-b572f60f62c2" />


### Homepage
<img width="1897" height="868" alt="homepage" src="https://github.com/user-attachments/assets/f4e3c748-be6e-4eb4-8829-337011731e9c" />


### Create Post
<img width="1915" height="870" alt="create_post" src="https://github.com/user-attachments/assets/a0801a05-0b42-4f07-b933-b275d817ec56" />


### My Profile
<img width="1918" height="862" alt="my_profile" src="https://github.com/user-attachments/assets/f133f5c1-29e1-491f-bd61-563278c867de" />


### User Profile
<img width="1918" height="866" alt="user_profile" src="https://github.com/user-attachments/assets/12bd3c89-e5ba-4a50-a778-0ba6bce3ed69" />


### Edit Profile
<img width="1898" height="862" alt="edit_profile_1" src="https://github.com/user-attachments/assets/b0055a85-a057-4c1b-9635-487a5999d28d" />
<img width="1897" height="866" alt="edit_profile_2" src="https://github.com/user-attachments/assets/5a755836-3325-4bd5-9bf0-72aca4649177" />


## 🛠️ Tech Stack

### Backend
- **Django 5.2.7** - High-level Python web framework
- **Python 3.12** - Programming language
- **SQLite** - Database (development)
- **Pillow** - Image processing library

### Frontend
- **TailwindCSS** - Utility-first CSS framework
- **jQuery 3.7.1** - JavaScript library for DOM manipulation and AJAX
- **Boxicons** - Icon library

### Third-Party Packages
- **django-allauth** - Authentication, registration, and account management
- **sorl-thumbnail** - Image thumbnail generation and caching

### Environment Management
- **Pipenv** - Python dependency and virtual environment management

## 📋 Prerequisites

- Python 3.12 or higher
- Pipenv (recommended) or pip
- SQLite (included with Python)

## 🔧 Installation

### 1. Clone the Repository
```bash
cd Django-201
```

### 2. Install Dependencies

Using Pipenv (recommended):
```bash
pipenv install
pipenv shell
```

Or using pip:
```bash
pip install django django-allauth sorl-thumbnail pillow
```

### 3. Configure Environment
The project uses default Django settings for development. For production, update `til/settings.py`:
- Set `DEBUG = False`
- Update `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Set up a production database (PostgreSQL recommended)

### 4. Run Migrations
```bash
pipenv run python manage.py migrate
```

Or:
```bash
python manage.py migrate
```

### 5. Create a Superuser
```bash
pipenv run python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
pipenv run python manage.py collectstatic
```

### 7. Run the Development Server
```bash
pipenv run python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 📁 Project Structure

```
Django-201/
├── feed/                          # Posts and feed functionality
│   ├── models.py                  # Post model
│   ├── views.py                   # Feed views (ListView, DetailView, CreateView)
│   ├── urls.py                    # Feed URL patterns
│   ├── templates/feed/            # Feed templates
│   └── migrations/
├── profiles/                      # User profiles
│   ├── models.py                  # Profile model with images
│   ├── views.py                   # Profile views (detail, edit, follow)
│   ├── forms.py                   # Profile and password change forms
│   ├── urls.py                    # Profile URL patterns
│   ├── templates/profiles/        # Profile templates
│   └── migrations/
├── followers/                     # Follow/Unfollow system
│   ├── models.py                  # Follower relationship model
│   ├── admin.py                   # Admin configuration
│   └── migrations/
├── til/                           # Main project directory
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Root URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── templates/                 # Base templates
│       ├── base.html              # Main layout with sidebar
│       ├── account/               # Allauth template overrides
│       └── includes/              # Reusable components
├── frontend/                      # Frontend assets
│   └── js/
│       └── main.js                # AJAX logic and interactions
├── static/                        # Collected static files
├── media/                         # User-uploaded files
│   ├── profile_images/            # Profile pictures
│   └── profile_images/covers/     # Cover images
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
├── Pipfile                        # Pipenv dependencies
└── README.md                      # This file
```

## 💾 Database Models

### Post (feed app)
- `text` - Post content (max 240 characters)
- `date` - Auto-generated timestamp
- `author` - ForeignKey to User

### Profile (profiles app)
- `user` - OneToOne relationship with User
- `image` - Profile picture (ImageField)
- `cover_image` - Profile cover image (ImageField)

### Follower (followers app)
- `followed_by` - User who initiates the follow
- `following` - User being followed
- Unique constraint preventing duplicate follows
- Self-follow validation

## 🎯 Usage

### For Users

1. **Sign Up**: Create an account from the sidebar
2. **Create Posts**: Click "Create Post" or use the + icon, write your post in the modal
3. **View Feed**: Browse posts on the homepage
4. **Profile Management**: 
   - Click "My Profile" to view your profile
   - Click "Edit Profile" to update your information and images
5. **Social Interaction**: 
   - Click on usernames to view profiles
   - Use Follow/Unfollow buttons to connect with users

### For Developers

#### Creating Migrations
```bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```

#### Running Tests
```bash
pipenv run python manage.py test
```

#### Accessing Admin Panel
Navigate to `http://localhost:8000/admin` and login with your superuser credentials.

#### Updating Static Files
After making changes to CSS/JS:
```bash
pipenv run python manage.py collectstatic --noinput
```

## 🔑 Key Features Implementation

### AJAX Post Creation
Posts are created without page reload using jQuery AJAX with CSRF token handling. The modal closes automatically and the new post appears at the top of the feed.

### Follow System
The follow/unfollow functionality uses AJAX to update relationships in real-time. The button text toggles between "Follow" and "Unfollow" based on the current state.

### Image Handling
Profile and cover images are processed using sorl-thumbnail for efficient storage and display. Images are automatically cropped and resized to maintain consistent dimensions.

### Toast Notifications
User feedback is provided through styled toast notifications that auto-dismiss after 5 seconds. Messages support multiple types: success, error, warning, and info.

### Authentication Flow
django-allauth handles user authentication with customized templates matching the application's design. Email verification is optional, and users are automatically logged in after email confirmation.
