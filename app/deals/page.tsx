"use client";

import {
  PriceAlerts,
  SavedComparisons,
  TrendingDeals,
  Wishlist
} from "@/components/deals-widgets";
import { ModuleHeroMockup } from "@/components/mockup-visuals";
import { PageShell } from "@/components/page-shell";
import { SectionHeading } from "@/components/section-heading";
import { Badge } from "@/components/ui/badge";

export default function DealsPage() {
  return (
    <PageShell>
      <section className="mx-auto max-w-7xl">
        <div className="mb-8 max-w-3xl">
          <Badge>Module 8 . Deals, Trends & Personalization</Badge>
          <h1 className="mt-4 text-3xl font-black text-white sm:text-5xl">Keep users engaged after comparison.</h1>
          <p className="mt-3 text-zinc-400">
            Trending products, flash deals, price drop alerts, wishlists, saved comparisons, and user preferences.
          </p>
        </div>

        <div className="mb-8">
          <ModuleHeroMockup
            kind="deals"
            title="Deals, alerts, and saved comparisons"
            subtitle="A personalized layer for flash deals, wishlists, saved comparisons, price drop notifications, and user preferences."
          />
        </div>

        <SectionHeading
          title="Trending deals"
          description="Horizontal-slider inspired deal cards presented as a responsive dashboard grid."
        />
        <TrendingDeals />

        <section className="mt-10 grid gap-5 lg:grid-cols-[1fr_1fr_1fr]">
          <Wishlist />
          <SavedComparisons />
          <PriceAlerts />
        </section>
      </section>
    </PageShell>
  );
}
