

```markdown
# 🎮 Digital Goods Marketplace API

> **Status:** Active Development (Pet Project).  
> This is a backend REST API developed for a digital gaming marketplace (selling accounts, boosts, and in-game items). Designed with a focus on security, data integrity, and seamless frontend SPA integration.

## 🚀 Project Overview

The Marketplace API provides a robust backend infrastructure for trading digital gaming assets. It handles custom user authentication, secure offer creation, and dynamic filtering based on game-specific categories (e.g., Dota 2 -> Boost, CS-2 -> Skins).

### ✨ Key Features (Currently Implemented)

* **Advanced Serialization (Read Nested, Write Flat):** Optimized API responses where `GET` requests return deeply nested and detailed objects (including seller avatars and full game info), while `POST` requests accept flat IDs for maximum client-side simplicity.
* **Bulletproof Security & Authentication:** Utilizes Token-based authentication. The API prevents "Seller ID Spoofing" by completely ignoring client-provided seller IDs during offer creation, automatically assigning the entity to the authenticated user via their token.
* **Custom Relational Validation:** Strict backend validation ensures data integrity (e.g., a user cannot create an offer assigning a "Dota 2" category to a "Counter-Strike 2" game).
* **Dynamic Media Handling:** Automatically generates and serves absolute URLs for user-uploaded media (avatars, game logos), eliminating frontend routing issues.
* **Chained Dropdowns Support:** Database architecture supports chained/dependent dropdowns for seamless Game -> Category selection.

---

## 🗺️ Roadmap (Upcoming Features)

The project is continuously evolving. The following features are currently in the pipeline:

* 💳 **Payment Integration:** Secure checkout and transaction processing using the **Stripe API**.
* 💬 **Real-time Chat:** WebSocket-based communication system allowing buyers and sellers to discuss order details instantly.
* ⭐ **Review & Rating System:** Post-transaction feedback system to build seller reputation and ensure marketplace trust.
* 📊 **Internal CRM (Planned):** A comprehensive dashboard for sellers to manage orders, track revenue analytics, and communicate with clients effectively.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Django
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Authentication:** Token Authentication

---

## 📦 Database Models Hierarchy

1. **CustomUser:** Extends `AbstractUser` with roles (Admin/User), balances, and avatar support.
2. **Game:** Base model for gaming titles (e.g., Dota 2, CS-2) utilizing URL-friendly slugs.
3. **Category:** Child model linked to specific games (e.g., Boost, Accounts).
4. **Offer:** The core model connecting a User (Seller), Game, and Category, containing pricing, stock, and secure/secret data delivery fields.

---

## 🔗 Main API Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/games/` | List all available games | ❌ |
| `GET` | `/api/offers/` | List all active offers | ❌ |
| `POST` | `/api/offers/` | Create a new offer (auto-assigns seller) | ✅ (Token) |
| `GET` | `/api/offers/<slug:game_slug>/` | Get all offers for a specific game | ❌ |
| `GET` | `/api/offers/<slug:game_slug>/<slug:category_slug>/`| Get offers filtered by game AND category | ❌ |
| `GET` | `/api/offers/<uuid:uuid>/` | Retrieve detailed info about a specific offer | ❌ |

*(Note: `secret_data` field in Offers is strictly `write_only` and never exposed via GET requests).*

---

## 💻 Local Setup & Installation


**1. Clone the repository:**
```bash
git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
cd your-repo-name
