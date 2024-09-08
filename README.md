<h1 align="center" id="title">StoryHub🖊️ - A django blog application</h1>

<p id="description">This Django-powered blog platform is designed for users to create and share their thoughts on topics they're passionate about. The platform provides a personalized blogging experience allowing users to register log in and manage their profiles. Users can create edit and delete their own posts and browse posts from other members of the community.</p>

<h2>Project Screenshots:</h2>

<img src="https://drive.google.com/file/d/1iJxSy9YWV8wfiaS7MmrQsgl1GoI1aC7n/view?usp=sharing" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1aXLAWWyq8eLpC6w7zFEHw_bN_-RJ3KVm/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1-_4ra87zU5conUO-o8vyg2UozkyCrj8_/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1G2AAWfEA4EyncFapNbI18Mv_O16B7xri/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1Kaa8ygZFehIeinxV1wEuyN_rJWQ6KIJO/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1uyhF4S_NpaPKbLhQ9zlYyOvsb1GAi0f0/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1NNbiVvCLAl0UJR5-ZKK8wdCzucqoL35b/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

<img src="https://drive.google.com/file/d/1ESj4XtCPOJe2MLU_g62U9oZdYIkRv8d5/view?usp=drive_link" alt="project-screenshot" width="1000" height="1000/">

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   User Registration and Authentication: Secure user account creation login and profile management.
*   Profile Management: Users can update their profile details including profile pictures and bios.
*   Post Creation and Management: Users can create edit and delete posts with ease.
*   Search Functionality: Easily search for posts or information on the site.
*   Comments: Engage with content by commenting on posts.
*   Email Notifications: Automated emails for password resets and account updates.
*   Pagination: Efficiently browse through large volumes of content with pagination.
*   Inspirational Quote: A "Inspirational Quote" section displaying quotes from an external API on every refresh.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Repository: First clone your project repository from GitHub (or wherever your project is hosted).</p>

```
git clone https://github.com/monisharavi729735/django_blog.git
```

<p>2. Change the directory:</p>

```
cd django_blog
```

<p>3. Set Up a Virtual Environment: Create a virtual environment to isolate your project dependencies.</p>

```
python3 -m venv env
```

<p>4. Activate the virtual environment.</p>

<p>* On Windows:</p>

```
env\Scripts\activate
```

<p>* On macOS/Linux:</p>

```
source env/bin/activate
```

<p>5. Install Dependencies: Install all the necessary packages using pip. The dependencies are listed in the requirements.txt file.</p>

```
pip install -r requirements.txt
```

<p>6. Set Up the Database: Apply the database migrations to set up your database schema.</p>

```
python manage.py migrate
```

<p>7. Create a Superuser: Create a superuser account to access the Django admin interface.</p>

```
python manage.py createsuperuser
```

<p>8. Run the Development Server: Start the Django development server to run your project locally.</p>

```
python manage.py runserver
```

<p>9. Visit http://127.0.0.1:8000/ in your web browser to see the blog.</p>

<p>10. Access the Admin Panel: Visit http://127.0.0.1:8000/admin/ to log in to the Django admin panel using the superuser account you created.</p>

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   **Django**: A high-level Python web framework that enables rapid development of secure and maintainable websites. It handles the backend including user authentication URL routing and database operations.
*   **Django Template Language (DTL)**: A templating system provided by Django to dynamically generate HTML pages by combining static templates with data from the backend.
*   **Django Admin**: A built-in feature of Django that provides a web-based interface for managing site content users and settings.
*   **HTML/CSS**: For structuring and styling the web pages. HTML provides the structure while CSS adds visual styling.
*   **Bootstrap**: A popular CSS framework that provides pre-designed components and utilities for building responsive and mobile-first web pages.
*   **Crispy Forms**: A Django package used to style forms in the frontend ensuring they are rendered beautifully and consistently.
*   **SQLite/PostgreSQL**: The database system used to store user data blog posts and other application data. SQLite is used for development while PostgreSQL can be used in production for better scalability.
*   **Git**: Version control system used to manage and track changes in the project code.
*   **Virtualenv**: A tool for creating isolated Python environments ensuring that dependencies are managed properly and do not interfere with other projects.