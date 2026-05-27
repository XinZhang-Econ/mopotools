import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MoPoTools",
  description: "Monetary Policy Tools — paper upload and wiki review",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-gray-900 min-h-screen">
        <header className="border-b px-6 py-3 flex items-center gap-6">
          <span className="font-bold text-sm">MoPoTools</span>
          <nav className="flex gap-4 text-sm text-gray-500">
            <a href="/upload" className="hover:text-gray-900">Upload</a>
            <a href="/review" className="hover:text-gray-900">Review queue</a>
          </nav>
        </header>
        <div className="pb-16">{children}</div>
      </body>
    </html>
  );
}
