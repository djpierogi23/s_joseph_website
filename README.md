# S Joseph Law LLC — Website

Working draft of the S Joseph Law LLC website. Built and maintained by Full Signal Technologies.

**Live preview:** https://djpierogi23.github.io/s_joseph_website/
*(available once GitHub Pages is enabled — see below)*

---

## Enabling the live preview

One-time setup, takes about a minute:

1. Go to the repo on GitHub → **Settings** → **Pages**
2. Under **Build and deployment → Source**, choose **Deploy from a branch**
3. Branch: **`main`**, folder: **`/ (root)`** → **Save**

The site is live at the URL above within a minute or two. Every push to `main` republishes automatically, so the client sees changes as soon as they land.

## Viewing it locally

It is a single self-contained file — no build step, no dependencies.

```bash
# simplest: open the file directly
open index.html

# or serve it, which matches how Pages will behave
python3 -m http.server 8000
# then visit http://localhost:8000
```

---

## How it is built

Everything is in `index.html`: markup, styles, and behavior. No frameworks, no build tooling, no external requests. That is deliberate at this stage — it keeps review friction near zero and means the file can be dropped onto any host later.

**Routing** is hash-based (`#/practice`, `#/schedule`), which works on GitHub Pages with no server configuration. When this moves to a real host, these become clean paths (`/practice`) with per-page HTML — the metadata for that is already defined in the `ROUTES` object at the bottom of the file.

### Pages

| Route | Page |
|---|---|
| `#/` | Home |
| `#/path` | The Development Path — interactive lifecycle timeline |
| `#/practice` | Practice Areas |
| `#/condominium-conversion` | Condominium Conversion — the SEO page |
| `#/team` | Team |
| `#/schedule` | Schedule a Call — three-step booking flow |
| `#/message` | Send a Message — short contact form |
| `#/contact` | Contact — offices, hours, both contact paths |

### Design tokens

Defined once in `:root` at the top of the file. Change them there and they propagate everywhere.

| Token | Value | Use |
|---|---|---|
| `--forest` | `#1f3a2e` | Primary. Nav, buttons, dark sections |
| `--forest2` | `#172c22` | Footer, deepest surface |
| `--brass` | `#b28a4c` | Accent rules, borders, highlights |
| `--brasstx` | `#7d5e2d` | Accent **text** — darkened from `#8f6d38` to pass WCAG AA on cream |
| `--cream` | `#f7f6ef` | Alternating section background |
| `--ink` | `#22302a` | Headings |
| `--body` | `#4f554d` | Body copy |
| `--mut` | `#6a6e64` | Muted text — darkened from `#767a70` for contrast |

Typography: Cormorant Garamond / Garamond / Georgia serif for display, system sans for UI and body.

---

## Status: what is real and what is not

**Placeholders are visible on purpose.** Anything unverified renders in a bracketed tan box (`.tbd`). There are currently **28** of them. Nothing can ship by accident — search the file for `class="tbd"` to find them all.

### Needed from the client before launch

- **Firm roster.** The Team page has two `[Name] — Of Counsel` cards. If the firm is one attorney, delete them. Firm composition is a material representation under the advertising rules in both NJ and NY.
- **Real contact details.** Phone, email, and the New York address are all placeholders. The Hoboken address is in.
- **Stats bar figures** — years advising developers, units entitled, project value. These need a "past results do not guarantee future outcomes" footnote once populated.
- **Representative matters.** The four project cards are empty. Recommendation: replace with a dated recent-approvals list (`07/22/26 — Hudson County — 84-unit multifamily — site plan + use variance approved`) rather than named buildings.
- **Attorney bio and headshots.**
- **NJ vs NY condominium process** section on the condo page — this is the section that does the SEO work and needs to be genuinely specific.
- **Billing approach** and **NJ entitlement timelines** FAQ answers.

### Not yet wired

- **Booking flow** shows illustrative availability generated client-side. Needs real calendar availability, a hold on the selected slot, a confirmation email, and matter-record creation. **Microsoft Bookings** is the recommended backend — included in M365 Business Standard and above, publishes real availability from Outlook, no extra cost.
- **Both forms** submit to nothing. They need a handler that routes to intake and creates the matter record.
- **Analytics** and **Google Business Profile** are not set up.

### Open questions

- **Tagline conflict.** The business card reads *Land Development · Commercial Real Estate · Financing · Condominiums*. The site reads *Land Use, Zoning & Development · ...*. The site version is in use here because land use and zoning is the stated core expertise. One answer needed — the cards are printed.
- **Business card office.** The card shows a New York Park Avenue address and a (212) number; the site is Hoboken-primary with a (201) number. The card likely needs a reprint.
- **The brick mark** from the app-icon sheet is unused. The masthead uses the SJ monogram, matching the letterhead and cards. Is the brick an app icon only, or is it competing for primary?

---

## Accessibility and SEO

Already handled:

- Real anchor links and routing with `aria-current` on the active nav item
- Timeline and FAQ toggles are real buttons with `aria-expanded` — fully keyboard operable
- Skip link and visible focus rings throughout
- Two color tokens darkened to pass WCAG AA contrast on cream
- Nothing renders below 11px
- `prefers-reduced-motion` respected
- Per-route `<title>` and meta description
- `LegalService` JSON-LD with the Hoboken address and practice areas

Outstanding: real Open Graph tags and a social share image, sitemap and robots.txt (both need the final domain), and Google Business Profile.

---

## Conventions

Commit messages: short imperative subject, e.g. `Add condominium conversion FAQ`, `Fix contrast on footer disclaimer`. Keep each commit to one reviewable change so the client can follow the history.
