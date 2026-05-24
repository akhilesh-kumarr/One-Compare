import { NextResponse } from "next/server";
import { searchComparisons, type Category, type SortKey } from "@/lib/comparison-data";

export function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get("q") ?? "";
  const category = (searchParams.get("category") ?? "all") as Category | "all";
  const sort = (searchParams.get("sort") ?? "best") as SortKey;
  const maxPriceParam = searchParams.get("maxPrice");
  const maxPrice = maxPriceParam ? Number(maxPriceParam) : undefined;

  try {
    return NextResponse.json({
      query,
      category,
      sort,
      results: searchComparisons({ query, category, sort, maxPrice })
    });
  } catch {
    return NextResponse.json({ error: "Unable to search comparisons" }, { status: 500 });
  }
}
