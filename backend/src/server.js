import cors from "cors";
import dotenv from "dotenv";
import express from "express";
import { comparisonItems } from "./data.js";
import { recommend } from "./recommendation.js";

dotenv.config();

const app = express();
const port = process.env.PORT ?? 5000;

app.use(cors({ origin: process.env.CLIENT_ORIGIN ?? "http://localhost:3000" }));
app.use(express.json());

app.get("/health", (_request, response) => {
  response.json({ status: "ok", service: "oneCompare API" });
});

app.get("/api/search", (request, response) => {
  const query = String(request.query.q ?? "").toLowerCase();
  const category = String(request.query.category ?? "all");
  const sort = String(request.query.sort ?? "best");

  let results = comparisonItems.filter((item) => {
    const text = `${item.name} ${item.tags.join(" ")}`.toLowerCase();
    return (category === "all" || item.category === category) && (!query || text.includes(query));
  });

  results = results.sort((a, b) => {
    const aRec = recommend(a);
    const bRec = recommend(b);
    if (sort === "price") return aRec.cheapest.price - bRec.cheapest.price;
    if (sort === "rating") return bRec.rated.rating - aRec.rated.rating;
    if (sort === "fastest") return aRec.fastest.deliveryMinutes - bRec.fastest.deliveryMinutes;
    return bRec.best.score - aRec.best.score;
  });

  response.json({ results });
});

app.get("/api/recommend/:id", (request, response) => {
  const item = comparisonItems.find((entry) => entry.id === request.params.id);
  if (!item) {
    response.status(404).json({ error: "Comparison item not found" });
    return;
  }

  response.json({ item, recommendation: recommend(item) });
});

app.listen(port, () => {
  console.log(`oneCompare API running on http://localhost:${port}`);
});
