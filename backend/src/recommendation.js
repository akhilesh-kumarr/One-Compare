export function recommend(item) {
  const offers = item.offers.filter((offer) => offer.availability !== "Unavailable");
  const cheapest = [...offers].sort((a, b) => a.price - b.price)[0];
  const fastest = [...offers].sort((a, b) => a.deliveryMinutes - b.deliveryMinutes)[0];
  const rated = [...offers].sort((a, b) => b.rating - a.rating)[0];

  const best = offers
    .map((offer) => {
      const priceScore = cheapest.price / offer.price;
      const ratingScore = offer.rating / 5;
      const speedScore = fastest.deliveryMinutes / offer.deliveryMinutes;
      const score = Math.round(priceScore * 42 + ratingScore * 28 + speedScore * 20 + 10);
      return { ...offer, score };
    })
    .sort((a, b) => b.score - a.score)[0];

  return { best, cheapest, fastest, rated };
}
