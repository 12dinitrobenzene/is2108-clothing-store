IS2108 PAIR PROJECT - THE RENTAL RACK
=====================================

GROUP INFORMATION
-----------------
Group number: PP52

Member 1 (Group Leader)
Full name: FOO CHUAN KANG
Student number: A0322968R
Email:  e1525875@u.nus.edu
Contact number: +65 9759 0865

Member 2
Full name: ER TENG SHENG ELGIN
Student number: A0315640M
Email: e1512591@u.nus.edu
Contact number: +65 8101 7361


HOW TO RUN THE WEB APPLICATION
------------------------------
1. Open a terminal in the folder containing manage.py.

2. Create and activate a virtual environment.

   macOS:
   python -m venv .venv
   source .venv/bin/activate

   Windows:
   python -m venv .venv
   .venv\Scripts\activate

3. Install the required packages.

   pip install -r requirements.txt

4. Create the database tables and load the demonstration data.

   python manage.py migrate
   python manage.py seed_demo

5. Start the server.

   python manage.py runserver

6. Open the following address in a browser:

   http://127.0.0.1:8000/

The seed command is intended for local demonstration and requires DEBUG=True.
It can be run again to restore the supplied demo accounts and demonstration
records. Unrelated local users and orders are not deleted.


DEMO ACCOUNTS
-------------
The password for every account below is: Password

Master platform administrator
Username: platform_admin

Platform administrator employee
Username: platform_employee

Nike vendor manager
Username: nike_employee

Customer 1
Username: demo_customer

Customer 2
Username: demo_customer_2


DEMO SEED DATA
--------------
Run the following command after applying the migrations:

python manage.py seed_demo

The command loads:
- One Nike vendor.
- 13 Nike product listings, 14 variants and 12 product images.
- Five clothing style tags.
- One master platform administrator and one platform administrator employee.
- One Nike vendor manager.
- Two customers with different style profiles, product views and wishlists.
- Rental orders at confirmed, preparing, dispatched, active, overdue,
  returned, completed and cancelled stages.
- Return inspections, simulated 20/80 settlements and one customer review.

The rental dates are generated relative to the day the command is run so that
the active and overdue examples remain suitable for demonstration.


FULL DEMONSTRATION VIDEO
------------------------
YouTube link: https://youtu.be/827GMc5VVGM
