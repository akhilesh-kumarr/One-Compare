"use client";

import { SlidersHorizontal } from "lucide-react";
import {
  RecommendationPanel,
  SmartInsights,
  type AIInsight
} from "@/components/ai-widgets";
import { ModuleHeroMockup } from "@/components/mockup-visuals";
import { PageShell } from "@/components/page-shell";
import { SectionHeading } from "@/components/section-heading";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

const insights: AIInsight[] = [
  {
    title: "Best value laptop under Rs. 60,000",
    score: 91,
    badge: "Best Value",
    summary:
      "A Ryzen 7 productivity laptop wins because it balances processor score, 16GB RAM, SSD storage, warranty, and real offer price.",
    points: [
      "Strong performance per rupee.",
      "Meets RAM and storage preferences.",
      "Offer price is stable across two stores."
    ]
  },
  {
    title: "Cheapest reliable airport ride",
    score: 87,
    badge: "Commute Pick",
    summary: "Namma Yatri Auto is cheaper than sedan options while keeping pickup ETA under six minutes.",
    points: []
  },
  {
    title: "Dinner delivery winner",
    score: 84,
    badge: "Food Pick",
    summary: "Magicpin wins after coupon savings, but Swiggy is recommended if fastest delivery matters more.",
    points: []
  }
];

export default function AIPage() {
  return (
    <PageShell>
      <section className="mx-auto max-w-7xl">
        <div className="mb-8 max-w-3xl">
          <Badge>Module 7 . AI Recommendation Engine</Badge>
          <h1 className="mt-4 text-3xl font-black text-white sm:text-5xl">Turn comparison data into decisions.</h1>
          <p className="mt-3 text-zinc-400">
            Recommendations based on budget, ratings, specs, delivery, reviews, and value for money.
          </p>
        </div>

        <div className="mb-8">
          <ModuleHeroMockup
            kind="ai"
            title="Premium AI recommendation engine"
            subtitle="Scores products and services using budget, ratings, specs, delivery, reviews, reliability, and value."
          />
        </div>

        <Card className="mb-8">
          <CardContent className="grid gap-4 pt-5 md:grid-cols-4">
            {["Budget", "Ratings", "Specs", "Delivery"].map((item) => (
              <div key={item} className="rounded-md border border-white/10 bg-white/[0.04] p-4">
                <SlidersHorizontal className="mb-3 h-4 w-4 text-emerald-300" />
                <p className="text-sm font-semibold text-white">{item}</p>
                <p className="mt-1 text-xs text-zinc-500">Weighted in AI score</p>
              </div>
            ))}
          </CardContent>
        </Card>

        <SectionHeading title="Recommendation panel" description="Premium neon AI cards with score, smart explanations, and personalized suggestions." />
        <RecommendationPanel insights={insights} />

        <section className="mt-10 grid gap-5 lg:grid-cols-[.9fr_1.1fr]">
          <Card>
            <CardContent className="pt-5">
              <h2 className="text-xl font-black text-white">Example prompt</h2>
              <p className="mt-3 rounded-md border border-white/10 bg-white/[0.04] p-4 text-sm leading-6 text-zinc-300">
                Best value laptop under Rs. 60,000 with 16GB RAM, good battery, and reliable warranty.
              </p>
              <Button className="mt-5 w-full">Run Recommendation</Button>
            </CardContent>
          </Card>
          <SmartInsights points={insights[0].points} />
        </section>
      </section>
    </PageShell>
  );
}
