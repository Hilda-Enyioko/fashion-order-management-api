# Fashion Designer Order & Client Management API – Project Plan
### *ALX BACKEND WEB DEVELOPMENT CAPSTONE PROJECT*
---

## 1. Project Overview
---
**Project Name:** Fashion Designer Order & Client Management API

**Category:** Inventory Management (Back-End)

**Description:**
This API is designed to help fashion designers and tailoring businesses efficiently manage their operations through a centralized system. It provides structured endpoints for managing inventory items, customers, orders, and order items, ensuring accurate tracking of stock levels and customer requests.

The system enables designers to:
- Maintain a well-organized inventory of fashion items and materials
- Create and manage customer orders seamlessly
- Track order progress, delivery status, and timelines
-Associate orders with specific inventory items and quantities
- Improve operational efficiency and reduce errors caused by manual record-keeping

By exposing a clean and scalable API, the platform supports integration with web or mobile applications used in day-to-day fashion business operations.

**Target Users:** Fashion designers, boutique managers, tailors handling multiple clients and custom orders.

---
## 2. Problem Statement
---
Managing inventory and orders manually within fashion businesses often leads to inefficiencies, inconsistencies, and loss of critical data. Designers and small fashion houses struggle with keeping accurate records of available items, tracking order fulfillment, and maintaining up-to-date stock levels as orders are created, updated, or canceled.

**Common challenges include:**
- Lack of real-time visibility into inventory availability
- Difficulty tracking inventory usage across multiple orders
- Errors caused by duplicate records or outdated stock information
- Inefficient order processing and fulfillment workflows

In alignment with the ALX inventory management problem statement, this project addresses these challenges by providing a structured API that enables accurate inventory tracking, controlled order creation, and consistent data management. The goal is to improve reliability, scalability, and transparency in fashion order and inventory management systems.

---
## 3. Objectives
---
- Implement full CRUD operations for inventory items
- Enable inventory tracking and association with customer orders
- Provide CRUD operations for customers and orders
- Manage customer measurements and order-specific details
- Upload and store customer style reference images
- Track order timelines, delivery dates, and order status
- Record pricing and payment status for orders
- Implement authentication, authorization, and role-based access control

---
## 4. Features
---
| Feature               | Description                                                       |
|-----------------------|-------------------------------------------------------------------|
| Inventory Management | Add, update, delete, and view inventory items, including quantity and availability |
| Customer Management   | Add, update, delete, and view customers                           |
| Order Management      | Create, update, delete, and track orders                          |
| Measurements Management | Record and update customer measurements                         |
| Style Images          | Upload and manage images of customer styles                       |
| Timeline & Delivery   | Track order progress, expected delivery, and completion           |
| Payment & Pricing     | Record payment status and order price                             |
| Authentication        | Secure access for designers and team members                      |
| User and Role Management | Manage designer accounts, roles, and permissions for access control |


---
## 5. Tech Stack
---
- **Backend:** Django + Django REST Framework
- **Database:** MySQL (or SQLite for local dev)
- **Deployment:** PythonAnywhere or Heroku
- **Authentication:** Token-based (DRF Auth)
- **Permissions:** Django permissions / DRF permissions
- **Version Control:** GitHub

---
## 6. Database Models
---
| Model       | Fields                                                                                       | Description                                                                                                   |
|-------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| InventoryItem | inventory_item_id, name, description, quantity, price, category, created_at, updated_at, created_by, updated_by | Stores available inventory items and stock levels |
| InventoryChange | change_id, inventory_item, old_quantity, new_quantity, changed_at, changed_by | Logs every inventory quantity update |
| Customer    | customer_id, name, email, phone, created_at                                                   | Stores customer information                                                                                   |
| Order       | order_id, customer, order_status, price, payment_status, delivery_date, created_at, updated_at, created_by, updated_by      | Stores each order                                                                                             |
| OrderItem | order_item_id, order, inventory_item, size, quantity, created_at | Represents items within an order |
| Measurement | measurement_id, customer, order, type, values, created_at, updated_at                                                | Stores measurements for an order                                                                              |
| Image  | image_id, order, image_file, description, uploaded_at, uploaded_by, deleted_at, deleted_by                                                       | Stores style images for an order                                                                              |
| User        | user_id, username, email, first_name, last_name, role (admin, junior_admin), is_active, date_joined                        | For authentication and role management: Lead designers have full access; junior designers have restricted access to measurements and images only |


---
## 7. API Endpoints (Preliminary)
---
| Endpoint                | Method              | Description                                                   |
|-------------------------|---------------------|---------------------------------------------------------------|
| /customers/             | GET, POST           | List or create customers                                      |
| /customers/{id}/        | GET, PUT, DELETE    | Retrieve, update, or delete a customer                        |
| /orders/                | GET, POST           | List or create orders                                         |
| /orders/{id}/           | GET, PUT, DELETE    | Retrieve, update, or delete an order                          |
| /measurements/          | GET, POST           | Add or view measurements                                      |
| /measurements/{id}/     | GET, PUT, DELETE    | Update or delete a measurement                                |
| /style-images/          | GET, POST           | Upload or view style images                                   |
| /style-images/{id}/     | GET, PUT, DELETE    | Manage individual style images                                |
| /orders/{id}/status/    | PATCH               | Update order status (pending → in progress → completed)       |
| /users/                 | GET, POST           | List or create users                                          |
| /users/{id}/            | GET, PUT, DELETE    | Retrieve, update, or delete users                             |
| /auth/login/            | POST                | Login and obtain token                                        |
| /auth/logout/           | POST                | Revoke token                                                  |


---								
## 8. Project Timeline (5 Weeks)
---
| Week    | Focus              | Deliverables                                                                 |
|---------|---------------------|------------------------------------------------------------------------------|
| Week 1  | Idea & Planning     | Project plan document, peer review                                           |
| Week 2  | Design Phase        | ERD diagram, API endpoint list, peer review                                  |
| Week 3  | Start Building      | GitHub repository, basic models & endpoints                                  |
| Week 4  | Continue Building   | Full CRUD functionality, status endpoints, image uploads, payment tracking, updated GitHub |
| Week 5  | Final Submission    | Complete GitHub repo, deployed API, 5-min demo video                         |


---
## 9. Success Metrics
---
- All CRUD operations function correctly
- Authentication protects sensitive endpoints
- Users can only perform actions allowed by their role, e.g., junior designers cannot modify order details or payment details.
- Orders and timelines can be tracked accurately
- Images upload and retrieve properly
- Payment and delivery statuses update correctly
- API deployed and accessible on hosting platform
- Positive peer and mentor feedback

---
## 10. Risks & Mitigation
---
| Risk                     | Mitigation                                              |
|--------------------------|----------------------------------------------------------|
| Deployment issues        | Use Heroku/PythonAnywhere tutorials in advance          |
| Image storage errors     | Use proper media handling in DRF & test locally         |
| Timeline mismanagement   | Strict weekly planner & progress tracking               |
| Database integrity issues| Use Django ORM & validations                            |


---
## 11. References
---
- [Django REST Framework documentation](https://www.django-rest-framework.org/)
- [PythonAnywhere deployment guides](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- [Heroku deployment guides](https://devcenter.heroku.com/categories/deployment)
- [ALX Back-End Capstone Guidelines](https://www.alxafrica.com/wp-content/uploads/2024/03/Back-End-Web-Development-Course-Overview-7.pdf)

