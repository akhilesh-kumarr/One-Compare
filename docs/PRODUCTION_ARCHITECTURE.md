# oneCompare Production Architecture

## Frontend

- Next.js App Router frontend with Tailwind CSS and Framer Motion.
- Shared comparison logic lives in `lib/comparison-data.ts`.
- Search APIs are available at:
  - `GET /api/search?q=iphone&category=electronics&sort=price`
  - `GET /api/recommend?id=iphone-15`

## Backend Option A: Node + Express

Folder: `backend/`

Recommended endpoints:

- `GET /health`
- `GET /api/search?q=&category=&sort=`
- `GET /api/recommend/:id`
- `POST /api/history`
- `POST /api/favorites`
- `GET /api/users/:uid/saved-comparisons`

## Backend Option B: Flask

Folder: `flask_api/`

Use Flask for ML/recommendation experiments or scraping pipelines, while Express handles auth and persistence.

## MongoDB Atlas Schemas

### Product

```js
{
  category: "electronics | food | grocery | cabs",
  name: String,
  brand: String,
  tags: [String],
  specs: Object,
  offers: [{
    platform: String,
    price: Number,
    mrp: Number,
    discount: Number,
    rating: Number,
    deliveryMinutes: Number,
    availability: String,
    offer: String
  }],
  popularity: Number,
  updatedAt: Date
}
```

### User Activity

```js
{
  uid: String,
  searchHistory: [{ query: String, category: String, createdAt: Date }],
  favorites: [{ itemId: String, createdAt: Date }],
  savedComparisons: [{ name: String, itemIds: [String], createdAt: Date }]
}
```

## Firebase Authentication

Use Firebase Auth on the frontend, then send the Firebase ID token to Express:

```http
Authorization: Bearer <firebase_id_token>
```

The backend should verify the token with Firebase Admin SDK before saving user history, favorites, or alerts.

## Deployment

- Frontend: Vercel or Netlify.
- Express API: Render, Railway, Fly.io, or AWS Elastic Beanstalk.
- Flask recommendation API: Render, Railway, or Google Cloud Run.
- Database: MongoDB Atlas.
- Auth: Firebase Authentication.
