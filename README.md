# vault-overflow

**Blog content source** for the homepage. The site pulls `index.json` and raw Markdown from here.

See the blog: **https://zzhang.tech/blog/**

---

**What’s here**

| Item | Description |
|------|-------------|
| `*.md` | Posts (YAML frontmatter + Markdown). Any folder. |
| `index.json` | Generated post list. Written by the script. |
| `scripts/build_index.py` | Scans `.md` → writes `index.json`. Skips `publish: false`. |

**New post**

1. Add a `.md` file with frontmatter: `title`, `date`, `tags`, `description`, `publish` (optional).
2. Run `python scripts/build_index.py` (needs PyYAML), or push to `main` and let the [workflow](.github/workflows/build-index.yml) update the index.
3. Push. Homepage picks up the new `index.json`.

**Comments** — [Utterances](https://github.com/apps/utterances) uses this repo; authorize **study-overflow/vault-overflow** for comments to work.
