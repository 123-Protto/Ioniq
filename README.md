# IONIQ Batteries — Django Website

A responsive, modern marketing and product-catalogue website based on the IONIQ Batteries brochure and the workshop/product photos supplied with the request. Includes animated sections, responsive navigation, product categories, product detail pages, enquiry form, and Django admin management.

## Features
- Modern landing page with animated gradient text, floating product cards, scroll reveals, and responsive layouts.
- Product catalogue with category filters and individual product pages.
- Enquiry/contact form stored in the database.
- Django admin for managing products and tracking enquiries.
- Seed command for starter categories/products.
- Supplied product and workshop images bundled in static assets.
- Accessibility considerations including keyboard-friendly links, form labels, and reduced-motion support.

## Requirements
- Python 3.10+
- pip

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_products
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the site and http://127.0.0.1:8000/admin/ for admin.

## Add and edit products
Sign in at `/admin/`, open **Products**, and create a product. Set a category, name, short description, optional capacity, detailed description, image, and whether it should be featured. Featured active products appear on the home page. All active products appear in the catalogue.

The site starts with demo catalogue entries. Replace or edit these with the company's verified product models and specifications before publishing.

## Enquiries
Enquiries are stored in the database and can be viewed in Django admin under **Enquiries**. The default email backend writes email output to the console; the form itself stores submissions in the database. For production email notifications, configure an SMTP provider and update `EMAIL_*` settings.

## Production checklist
1. Set `DJANGO_SECRET_KEY` to a secure secret and set `DJANGO_DEBUG=False`.
2. Set `DJANGO_ALLOWED_HOSTS` to your domain(s), comma-separated.
3. Use PostgreSQL or another production database if needed.
4. Configure SMTP, HTTPS, secure cookies and static file hosting.
5. Configure persistent media storage for uploaded product images.
6. Confirm phone number, email, address, product specifications, certification wording and all claims with the business owner.
7. Do not publish brochure claims as independently verified performance guarantees. Battery details can vary by model; use current official datasheets for technical specifications.

## Notes about brochure content
The site reflects the supplied brochure's listed categories: automotive, pasted/flat plate, solar, tubular & stationary batteries, and UPS/inverters. The brochure mentions 99.97% pure lead active material, PE envelopes and glass mat combination for vibration resistance, low internal resistance, robust container construction, and an Aqua Trap vent plug. These claims should be confirmed against current product datasheets before using them in advertising. The site avoids inventing battery prices, warranty periods, or model-specific ratings.
