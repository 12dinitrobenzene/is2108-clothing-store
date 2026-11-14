# IS2108 PAIR PROJECT - THE RENTAL RACK

The Rental Rack is a clothing rental marketplace built with Django. Customers
rent outfits for 1 to 7 days, vendors manage their catalogue and fulfil
rentals, and the platform team moderates vendors and listings and tracks
simulated commission settlements.

## Group information

**Group number:** PP52

### Member 1 (Group Leader)

- **Full name:** FOO CHUAN KANG
- **Student number:** A0322968R
- **Email:** e1525875@u.nus.edu
- **Contact Number:** +65 9759 0865

### Member 2

- **Full name:** ER TENG SHENG ELGIN
- **Student number:** A0315640M
- **Email:** e1512591@u.nus.edu
- **Contact Number:** +65 8101 7361

## Full demonstration video

YouTube link: https://youtu.be/827GMc5VVGM

## Requirements

- Python 3.11 or newer (the pinned pandas and scikit-learn versions do not
  install on older Python versions).
- pip
- No database server is needed. The project uses SQLite, which is created
  automatically by the migrate step.

## How to run the web application

1. Open a terminal in the folder containing `manage.py`.

2. Create and activate a virtual environment.

   **macOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows:**
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the required packages.

   ```bash
   pip install -r requirements.txt
   ```

4. Create the database tables and load the demonstration data.

   ```bash
   python manage.py migrate
   python manage.py seed_demo
   ```

5. Start the server.

   ```bash
   python manage.py runserver
   ```

6. Open the following address in a browser:

   http://127.0.0.1:8000/

   All roles sign in through the same login page:

   http://127.0.0.1:8000/accounts/login/

   After signing in, each account is sent to its own portal automatically.

## Demo accounts

The password for every account below is `Password` (capital P).

| Username | Role |
| --- | --- |
| `platform_admin` | Master platform administrator |
| `platform_employee` | Platform administrator employee |
| `nike_employee` | Nike vendor manager |
| `demo_customer` | Customer 1 (Jamie Tan) |
| `demo_customer_2` | Customer 2 (Avery Lim) |

The `platform_admin` account is also a Django superuser and can open the
Django admin site at http://127.0.0.1:8000/admin/.

Running `seed_demo` again resets these five accounts and their password back
to the values above.

## Demo seed data

`python manage.py seed_demo` loads:

- One approved Nike vendor.
- 13 Nike product listings, 14 variants and 12 product images.
- Five clothing style tags used by the recommendation model.
- One master platform administrator and one platform administrator employee.
- One Nike vendor manager.
- Two customers with different style profiles, product views and wishlists.
- Ten rental orders at the confirmed, preparing, dispatched, delivered
  (active), overdue, returned, completed and cancelled stages.
- Return inspections, simulated 20/80 settlements and one customer review.

Rental dates are generated relative to the day the command is run, so the
active and overdue examples stay correct. If you test the application several
days after seeding, run `python manage.py seed_demo` again first.

The command only resets the demo accounts, their activity and the Nike
catalogue. Other local users and orders are not deleted. It requires
`DEBUG=True`, which is already set in `config/settings.py`.

## Suggested walkthrough

1. **Customer - `demo_customer`**
   - Home page: personalised "For You" recommendations based on the saved
     style profile (urban streetwear).
   - Catalogue and product pages: browse, choose a variant and rental dates,
     add to cart and check out (payment is simulated).
   - Wishlist: two saved products.
   - Orders: rentals at confirmed, dispatched, overdue and returned stages,
     plus a completed rental that already has a review.
   - Style preferences: retake the style quiz to change recommendations.

2. **Customer - `demo_customer_2`**
   - Different recommendations (minimalist clean style profile).
   - Orders: a completed "nike windrunner men pants" rental that can still be
     reviewed, and a cancelled order that was refunded.

3. **Vendor manager - `nike_employee` (Employee portal: `/employee/`)**
   - Products: add or edit products, variants and images; archive listings.
   - Rentals: move the "nike minimalist clean" order from Preparing to
     Dispatched, then to Delivered.
   - Returns: the "nike experimental style" rental has been returned and
     inspected as Ready for reuse. Complete it to create a simulated
     settlement. The "nike classic style" return is on hold for cleaning.
   - Analytics: revenue and rental performance for the vendor.
   - Team: add vendor employees at
     http://127.0.0.1:8000/accounts/team/.

4. **Master administrator - `platform_admin` (Platform portal: `/platform_admin/`)**
   - Create admin and Manage admins: create, edit, deactivate and reactivate
     ordinary platform admin accounts.
   - Vendors: approve, reject or suspend vendors.
   - Listings: moderate product listings.
   - Rentals, Settlements and Performance: platform-wide monitoring.

5. **Platform administrator - `platform_employee`**
   - Same platform portal as above, but without access to admin account
     management.

## Recommendation model

The "For You" recommendations use a trained random forest model that is
included in the project (`recommendations/ml/style_random_forest.joblib`).
No training step is needed to run the application. The training script and
data are in the same folder for reference.

## Running the tests

```bash
python manage.py test
```

## Troubleshooting

- "pip install" fails on pandas or scikit-learn: check that Python is 3.11
  or newer (`python --version`).
- "That port is already in use": run `python manage.py runserver 8001` and
  open http://127.0.0.1:8001/ instead.
- Rental statuses or dates look out of date: run `python manage.py seed_demo`
  again.
- `db.sqlite3.backup` is an old backup file and is not used by the application.
