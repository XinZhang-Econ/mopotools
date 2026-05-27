export default function Home() {
  return (
    <main className="max-w-xl mx-auto pt-16 px-4 text-center">
      <h1 className="text-2xl font-bold mb-4">MoPoTools</h1>
      <p className="text-gray-500 mb-8 text-sm">
        Monetary Policy Tools — collaborative wiki for central bank research.
      </p>
      <div className="flex gap-4 justify-center">
        <a
          href="/upload"
          className="px-5 py-2.5 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700"
        >
          Upload a paper
        </a>
        <a
          href="/review"
          className="px-5 py-2.5 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200"
        >
          Review queue
        </a>
      </div>
    </main>
  );
}
