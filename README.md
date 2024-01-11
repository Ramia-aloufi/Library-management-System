# 📚 DRFBookshelf - Library Management System

Bookshelf - a sophisticated Library Management System meticulously crafted using the Django REST Framework (DRF). Developed as the final project of the REST API using Python and Django program at **[Tuwaiq Academy](https://tuwaiq.edu.sa/)**, Bookshelf sets a new standard for elegance and efficiency in book management.

## Key Features

**🌟 [Jazzmin-Themed](https://django-jazzmin.readthedocs.io/) Admin Dashboard:** Elevate your administrative experience with a visually captivating and functionally rich dashboard.

**🛡️ Secure User Authentication:** Seamlessly manage user profiles, encompassing cities, semesters, deposits, and a robust authentication system.

**📚 Comprehensive Book Management:** Revolutionize how you organize and track your book inventory with features for authors, publishers, faculties, languages, and more.

**📰 Timely News Updates:** Stay ahead of the curve with a dedicated news section for adding, editing, and displaying articles, ensuring your users are well-informed.

**🚀 Django Rest Framework Integration:** Experience efficient API integration, enabling fluid data exchange and seamless communication.

### Prerequisites 📦

- Python 3.x
- Django
- Django REST Framework

### Quick Start 🚀

1. **🖇️ Clone the Repository:**

   ```bash
   git clone https://github.com/FMashi/DRFBookshelf.git
   cd DRFBookshelf
   ```

2. **🛠️ Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **♻️ Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Change Directory to 'app':**

   ```bash
   cd app
   ```

5. **⚙️ Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **👤 Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **🪄 Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **✨ Access the Admin Panel:**
   - Open your browser and go to [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Project Structure 🏷️

```plaintext
📁 app/
|-- 📁 app/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- 📁 authentication/
|   |-- 📁 migrations/
|   |   `-- ...
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- signals.py
|   |-- tests.py
|   `-- views.py
|-- 📁 book/
|   |-- 📁 migrations/
|   |   `-- ...
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   `-- views.py
-- 📁 news/
|   |-- 📁 migrations/
|   |   `-- ...
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   `-- views.py
|-- manage.py

```
