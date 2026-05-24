from typing import Any


def get_best_electronics_deal(platforms: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Pick the best electronics offer using simple mock-friendly logic.

    The logic is intentionally readable:
    - Prefer lower price.
    - Slightly reward better ratings.
    - Return a reason that can later be replaced or enhanced by Gemini.
    """

    if not platforms:
        return None

    best_platform = min(
        platforms,
        key=lambda item: (
            item["price"],
            -item.get("rating", 0),
        ),
    )
    savings = max(best_platform["originalPrice"] - best_platform["price"], 0)

    return {
        "label": "Best Deal",
        "platform": best_platform["platform"],
        "price": best_platform["price"],
        "savings": savings,
        "reason": (
            f"{best_platform['platform']} has the lowest current price"
            f" with a {best_platform.get('rating', 0):.1f}/5 rating."
        ),
    }


def get_best_cab_deal(estimates: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Pick the best cab option using fare first, then ETA as tie-breaker."""

    available_estimates = [
        estimate
        for estimate in estimates
        if estimate.get("availability", "").lower() == "available"
    ]

    if not available_estimates:
        return None

    best_estimate = min(
        available_estimates,
        key=lambda item: (
            item["fare"],
            item["etaMinutes"],
            -item.get("rating", 0),
        ),
    )

    return {
        "label": "Best Deal",
        "provider": best_estimate["provider"],
        "cabType": best_estimate["cabType"],
        "fare": best_estimate["fare"],
        "reason": (
            f"{best_estimate['provider']} {best_estimate['cabType']} is the cheapest"
            f" available ride and should arrive in about {best_estimate['etaMinutes']} minutes."
        ),
    }
