import { NextResponse } from "next/server";
import { comparisonItems, getRecommendation } from "@/lib/comparison-data";

export function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const id = searchParams.get("id");
  const item = comparisonItems.find((entry) => entry.id === id) ?? comparisonItems[0];

  return NextResponse.json({
    item,
    recommendation: getRecommendation(item)
  });
}
