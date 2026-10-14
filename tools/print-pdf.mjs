// Print a reading view to PDF the way WP7 and WP9 were printed: Chromium, A4,
// print media (the stylesheet re-inverts to the light palette in @media print).
// Usage: node tools/print-pdf.mjs <path-under-site> <out.pdf>
//   e.g. node tools/print-pdf.mjs wp9/ wp9/working-paper.pdf
// Serves the repository root itself on a free port bound to the container's
// address (Chromium in the cloud container routes loopback through the proxy).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { spawn, execSync } from 'node:child_process';
import { resolve } from 'node:path';

const [, , page, out] = process.argv;
if (!page || !out) { console.error('usage: node tools/print-pdf.mjs <path/> <out.pdf>'); process.exit(2); }
const ip = execSync('hostname -I').toString().trim().split(' ')[0];
const port = 8700 + Math.floor(Math.random() * 200);
const root = resolve(import.meta.dirname, '..');
const srv = spawn('python3', ['-m', 'http.server', String(port), '--bind', ip], { cwd: root, stdio: 'ignore' });
await new Promise(r => setTimeout(r, 1200));
try {
  const b = await chromium.launch({ args: ['--no-proxy-server'] });
  const c = await b.newContext({ colorScheme: 'light' });
  const pg = await c.newPage();
  await pg.goto(`http://${ip}:${port}/${page.replace(/^\//, '')}`, { waitUntil: 'networkidle' });
  await pg.emulateMedia({ media: 'print' });
  await pg.evaluate(() => document.fonts.ready);
  await pg.waitForTimeout(800);
  await pg.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
  console.log('printed', out);
} finally { srv.kill(); }
