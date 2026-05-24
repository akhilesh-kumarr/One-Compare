import type { Metadata } from "next";
import { Navbar } from "@/components/navbar";
import "./globals.css";

export const metadata: Metadata = {
  title: "oneCompare | Real Time Price Comparison",
  description: "Compare electronics prices and cab fares across top platforms."
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className="antialiased">
        <div className="noise" />
        <Navbar />
        {children}
      </body>
    </html>
  );
}
