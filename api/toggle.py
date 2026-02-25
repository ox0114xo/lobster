export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

  const { status } = req.body;
  const GITHUB_TOKEN = process.env.GITHUB_TOKEN; // 記得在 Vercel 設定環境變數
  const GIST_ID = "94acdb8bea0ceb153a79fce5422f9a21";

  const response = await fetch(`https://api.github.com/gists/${GIST_ID}`, {
    method: 'PATCH',
    headers: {
      Authorization: `token ${GITHUB_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      files: { 'signal.txt': { content: status } }
    }),
  });

  if (response.ok) {
    res.status(200).json({ success: true });
  } else {
    res.status(500).json({ success: false });
  }
}
