# Where to Get Your Data

Almost every app you use will give you a copy of your own data for free. This page lists where to click for the common ones, what you get, and where to put it in your vault.

Back to the [README](../README.md) · Previous: [Getting Started](GETTING-STARTED.md) · Next: [Prompts to copy](PROMPTS.md)

> **Menus move.** Apps rename their settings pages often. If a path below is out of date, open the linked help page or search *"<app> download my data"*. The idea is always the same: **Settings > Privacy (or Data) > Download / Export**.

---

## How every export works

1. **Request it.** Click export in the app's settings.
2. **Wait.** Some are instant, most email you a link within minutes to a few days. Download links often **expire in 24 hours to a few days**, so grab it when the email lands.
3. **Unzip it.** You'll usually get a `.zip` holding `.json`, `.csv` or `.html` files. Don't worry if they look unreadable; Claude reads them fine.
4. **File it.** Put the unzipped folder in `raw/`, named with the app and date, for example `raw/07 Chats/chatgpt-export-2026-10-25/`.
5. **Ingest it.** Tell Claude what it is (prompts in [PROMPTS.md](PROMPTS.md)). For big exports, ask for a **plan first**, then let it run.

## Start with these five

If you only do a few, do these. They give the most "who am I" for the least effort.

| # | Export | Why it's great |
|---|---|---|
| 1 | **ChatGPT / Claude / Gemini chats** | Years of questions you've asked. It's basically a diary of what you were thinking about |
| 2 | **Your resume + LinkedIn** | Career timeline, jobs, schools, skills and your network in one go |
| 3 | **Google Takeout** (Calendar, Keep, YouTube history) | Dates for your life timeline, plus old notes |
| 4 | **Spotify extended history** | A fun music timeline: what you played, when, for how long |
| 5 | **Old notes apps** (Apple Notes, Notion, Evernote, Keep) | Everything you already wrote down, brought into one place |

---

## AI chats

| App | Where to click | You get | Wait | Put it in |
|---|---|---|---|---|
| **ChatGPT** | Profile > **Settings > Data controls > Export data** > Confirm ([help](https://help.openai.com/en/articles/7260999-exporting-your-chatgpt-history-and-data)) | `conversations.json` + `chat.html` | Email, minutes to hours | `raw/07 Chats/` |
| **Claude** | **Settings > Privacy > Export data**, on the web or desktop app, not mobile ([help](https://support.claude.com/en/articles/9450526-export-your-claude-data)) | JSON of chats, projects and memory | Email link (expires in about a day) | `raw/07 Chats/` |
| **Gemini** | [Google Takeout](https://takeout.google.com), select **My Activity**, then filter to **Gemini Apps** | HTML/JSON activity | Email, hours | `raw/07 Chats/` |
| **Perplexity, Copilot, others** | Settings > look for Export or Download data, or copy useful threads by hand | Varies | Varies | `raw/07 Chats/` |

**Tip:** you don't need every chat. Ask Claude to **file only chats that taught you something or recorded a decision**, and to skip "fix this typo" chats.

## Google (one export for everything)

[**Google Takeout**](https://takeout.google.com) exports almost all Google products at once. Click **Deselect all**, then pick only what you want:

| Product | Useful for | Put it in |
|---|---|---|
| **Calendar** (`.ics`) | Dates for your life timeline: trips, birthdays, big events | `raw/01 Timeline/` |
| **Keep** | Old notes and lists (the Obsidian Importer below also handles Keep) | `raw/00 Inbox/` |
| **YouTube and YouTube Music** (watch history) | What you were learning or into, by month | `raw/05 Journals & Trackers/` |
| **Chrome** (bookmarks) | Links worth keeping | `raw/06 Library/` |
| **Drive** | Documents you wrote | Matching folder |
| **Fit / Fitbit** | Health and workout history (keep private) | `raw/05 Journals & Trackers/Health/` |

**Google Maps Timeline** (where you've been) is now stored on your phone, not in Takeout. In the Google Maps app look under your profile > **Your Timeline** / **Location settings** for an export or backup option. It's great for a travel history, but it's **very private**.

## Career and social

| App | Where to click | You get | Put it in |
|---|---|---|---|
| **LinkedIn** | **Me > Settings & Privacy > Data privacy > Get a copy of your data** ([direct link](https://www.linkedin.com/mypreferences/d/download-my-data)). Pick "the works" for everything | CSVs: positions, education, skills, connections, messages | `raw/02 Me/Career/` |
| **Instagram / Facebook / Threads** | **Accounts Center > Your information and permissions > Download your information** ([direct link](https://accountscenter.facebook.com/info_and_permissions)). Choose **JSON** | Posts, comments, messages, likes | `raw/02 Me/` |
| **X (Twitter)** | **Settings > Your account > Download an archive of your data** ([direct link](https://x.com/settings/download_your_data)) | Your posts and DMs | `raw/02 Me/` |
| **Reddit** | [reddit.com/settings/data-request](https://www.reddit.com/settings/data-request) | CSVs of posts, comments, saved | `raw/06 Library/` |
| **Discord** | **User Settings > Data & Privacy > Request all of my data** | Messages by channel | `raw/07 Chats/` |
| **Snapchat** | [accounts.snapchat.com](https://accounts.snapchat.com) > **My Data** | Memories, chat history | `raw/02 Me/` |
| **TikTok** | **Profile > Settings and privacy > Account > Download your data** | Watch history, likes | `raw/05 Journals & Trackers/` |
| **WhatsApp** | Open one chat > **More / contact name > Export chat** (one chat at a time) | `.txt` of that chat | `raw/07 Chats/` |
| **Your resume** | Just the PDF or Word file you already have | Your career in one page | `raw/02 Me/Career/` |

## Music, reading and watching

| App | Where to click | You get | Put it in |
|---|---|---|---|
| **Spotify** | [Account > Privacy](https://www.spotify.com/account/privacy/) > **Download your data**. Tick **Extended streaming history** for your whole life on Spotify, not just one year ([what's included](https://support.spotify.com/us/article/understanding-your-data/)) | JSON: every play with date and length | `raw/05 Journals & Trackers/` |
| **Kindle highlights** | [read.amazon.com/notebook](https://read.amazon.com/notebook): every book's highlights on one page (copy or save the page) | Your highlights per book | `raw/06 Library/Books/` |
| **Goodreads** | [My Books > Import and export](https://www.goodreads.com/review/import) > **Export Library** | CSV of books, ratings, dates read | `raw/06 Library/Books/` |
| **Netflix** | [Account > Profile > Viewing activity](https://www.netflix.com/viewingactivity) > **Download all** | CSV of everything you watched | `raw/05 Journals & Trackers/` |
| **Letterboxd** | **Settings > Data > Export your data** | CSV of films and reviews | `raw/05 Journals & Trackers/` |

## Notes apps you already use

Obsidian has an official, free **Importer** plugin that converts other notes apps straight into notes ([help page](https://help.obsidian.md/import)). It handles **Apple Notes, Evernote, Notion, Microsoft OneNote, Google Keep, Bear, Roam** and HTML files.

1. In Obsidian: **Settings > Community plugins > Browse**, search **Importer**, install and enable it.
2. Run it from the command palette (`Cmd/Ctrl + P` > "Importer: Open importer").
3. **Import into `wiki/00 Inbox/`**, then ask Claude to sort the notes into the right folders.

For **Notion** you can also export directly: **Settings > Workspace > General > Export all workspace content**, format **Markdown & CSV**.

## Money (keep these private)

| Source | Where to click | You get | Put it in |
|---|---|---|---|
| **Bank and credit cards** | Account > Transactions or Statements > **Download / Export** (pick CSV) | Transactions by date | `raw/03 Knowledge/Finance/` |
| **Brokerage** (Robinhood, Fidelity, Schwab...) | Account > Statements & documents / History > download CSV or PDF | Trades, dividends, statements | `raw/03 Knowledge/Finance/` |
| **Venmo / PayPal / Cash App** | Settings / Activity > **Statements** > download CSV | Payments to and from friends | `raw/03 Knowledge/Finance/` |
| **Amazon orders** | [Request your data](https://www.amazon.com/hz/privacy-central/data-requests/preview.html) > **Your Orders** | CSV of everything you bought | `raw/05 Journals & Trackers/` |
| **Pay stubs, tax forms** | Your employer's HR site, or your tax software | PDFs | `raw/03 Knowledge/Finance/` |

## Health and fitness (keep these private)

| Source | Where to click | You get | Put it in |
|---|---|---|---|
| **Apple Health** | iPhone **Health** app > your picture (top right) > **Export All Health Data** | Big ZIP with `export.xml` (steps, sleep, workouts, heart rate) | `raw/05 Journals & Trackers/Health/` |
| **Strava** | **Settings > My Account > Download or Delete Your Account > Request your archive** | Every activity, GPX files | `raw/05 Journals & Trackers/Health/` |
| **Garmin** | [Garmin account > Data management > Export your data](https://www.garmin.com/account/datamanagement/) | Activities, sleep, stats | `raw/05 Journals & Trackers/Health/` |
| **Fitbit** | Through [Google Takeout](https://takeout.google.com) > **Fitbit** | Activity, sleep, heart rate | `raw/05 Journals & Trackers/Health/` |

## Everything Apple

[privacy.apple.com](https://privacy.apple.com) > **Request a copy of your data**: iCloud contacts, calendars, App Store purchases, Apple Music history and more. Takes up to a week.

## Web pages and articles

Install the free [**Obsidian Web Clipper**](https://obsidian.md/clipper) browser extension. One click saves any article as a clean note. Point it at `wiki/00 Inbox/` and let Claude file it later.

## Photos and screenshots

Drop images into `raw/` and ask Claude to describe them (receipts, whiteboards, handwritten notes, screenshots of texts). It reads text in images. Big photo libraries are better left in your photos app; just bring in the ones that matter.

---

## Privacy rules for exports

- **Use a private copy.** If your vault is on GitHub, the repo must be **Private**. Exports contain messages, contacts, locations and money.
- **Most private** (never share, never paste into public tools): health, money, location history, messages, contacts.
- **Big raw exports don't need to be in git.** The template's `.gitignore` already skips `.zip` files and anything in `raw/private/`. Put the heaviest or most sensitive exports in `raw/private/` and only the notes Claude writes get backed up.
- **Delete what you don't need.** Once something is ingested, you can delete the original ZIP from your Downloads folder.

**Next:** [Prompts to copy](PROMPTS.md) for ingesting each of these.
