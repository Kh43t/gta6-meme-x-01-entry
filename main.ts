// gta6-meme-x-01 entry program (Node 22, standard library only).
//
// The entry itself is the X post named in POST.json: a GTA 6 meme whose
// picture shows make.fun's ghost and whose text carries make.fun and this
// account's play code. The house reads the post from X and builds the
// dossier the judge sees, so this program does nothing clever. It hands
// POST.json over to the output directory, exactly as the gate expects,
// and fails loudly if the file is missing or malformed instead of
// writing a half-good output.
//
// Grader-style run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

const repoRoot = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

async function handOverPostFile() {
  const source = join(repoRoot, "POST.json");
  const raw = await readFile(source, "utf8");
  const parsed = JSON.parse(raw);
  if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
    throw new Error("POST.json must hold one JSON object");
  }
  if (typeof parsed.url !== "string" || parsed.url.length === 0) {
    throw new Error("POST.json must name the post in a url string");
  }
  const postAddress = /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/.+\/status\/\d+/.test(
    parsed.url,
  );
  if (!postAddress) {
    throw new Error("POST.json url is not an X post address");
  }
  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, "POST.json"), raw, "utf8");
}

handOverPostFile().catch((error) => {
  console.error(`could not hand over POST.json: ${error.message}`);
  process.exit(1);
});
