# Wills blog publish log

One line per Routine run. Format: `YYYY-MM-DD | slug | published or held`.
2026-09-16 | (none) | nothing due; first post 2026-09-17

## 2026-09-22 15:37 UTC — first run after the rebase

Nothing due, nothing published. The only item dated on or before today is
`best-carpet-for-stairs-with-dogs-everett`, already live since 2026-09-17. Queue starts
2026-09-23. Correct no-op.

**Step 3 of the Routine prompt was withdrawn, not performed.** It asked for the live stairs
post's body to be re-pushed to correct `datePublished: 2027-02-15` (a future date on a live
page). Two reasons not to do it from this session:

1. A `description-big` push means reproducing 45,012 characters verbatim inside a tool call.
   That is not a file copy from here, it is a transcription, and a subtle error is possible.
2. `update_collection_items` **stages** rather than publishes (`lastPublished` stayed at
   2026-09-17T01:46:59Z through two updates today). A bad staged body would sit there
   invisibly and go live on Oleg's next *site* publish, which is imminent. A failed push
   would therefore plant a landmine rather than fail safely.

For drafts neither risk applies: a garbled draft is caught by the hash check before publish,
and a site publish does not publish drafts. So the daily body refresh stays for drafts and is
removed for the live post. Fixing the stairs post needs Oleg's call.

Reference for whoever does fix it: local body is 45,012 chars,
sha1 `825692402ab94e3af15e5e68cefe01e1dda1b15b`, schema dates `2026-09-17` / `2027-12-31`.

## 2026-09-22 16:2x UTC — stairs post schema date fixed (Oleg approved, foreground)

`best-carpet-for-stairs-with-dogs-everett` (6aaafc2d8f4d1f2643a0869a) advertised
`datePublished` / `dateModified` of `2027-02-15`, a future date, because it was published
early on 2026-09-17 out of its 2027 slot. Both now read `2026-09-17`.

Sequence, with the verification gate that made this safe:

1. Pushed the corrected `description-big` with `update_collection_items`, no `isDraft`.
   `lastPublished` stayed at 2026-09-17T01:46:59Z, confirming the push only staged.
2. Read the item back and hashed the stored body in Bash, not by eye:
   stored 45,012 chars sha1 `825692402ab94e3af15e5e68cefe01e1dda1b15b`, local identical. MATCH.
   Image, slug, name, category and hero all preserved; `isDraft` still false.
3. Only then `publish_collection_items` on that one item. `publishedItemIds` returned it,
   `errors` empty.

Nothing else was touched and the site itself was not published.

## 2026-09-23 — post 1 of 200 published

**Published:** `how-much-does-it-cost-to-refinish-hardwood-floors-in-seattle` (6aa9e4214e18075875156202)
"How Much Does It Cost to Refinish Hardwood Floors in Seattle? (2026 Real Prices)"

Held: none. Failed: none. One due draft, hero image present.

The stored body still carried the pre-rebase `datePublished: 2026-09-17`; re-rendered and pushed
so it reads `2026-09-23`. Verified before publishing: stored 44,085 chars
sha1 `75f2d15aeb96c8b88cbe026276fc52658fb262c9`, identical to `out/`. Published with
`errors: []`.

Oleg published the Webflow site on 2026-09-22T19:30:17Z (both custom domains), so this post
went live on the updated template, not the old one. That blocker is cleared.

Oleg also gave standing permission on this date to publish on schedule without checking in first.

## 2026-09-24 — post 2 of 200 published (late)

**Published:** `how-much-does-hardwood-floor-installation-cost-in-lynnwood` (6aa9e531b196331d6d3afa59)
"How Much Does Hardwood Floor Installation Cost in Lynnwood? 2026 Labor and Material Prices"

The 15:40 UTC Routine run was interrupted by a Claude Code permission prompt before it reached
the publish call, so the post went out later in the day when Oleg came back to the session.
Published as-is, hero present, `errors: []`. Held: none.

Root cause: the project allow-list did not cover every tool the Routine uses (Bash git/python
calls, `data_sites_tool`), so the harness asked Oleg to approve them. Widening the allow-list from
inside the session is blocked as self-modification; Oleg has to add the rules himself. Exact
block is in UPLOAD.md under "Making the Routine prompt-free".

## 2026-09-24 — permission check

Oleg committed the widened allow-list (`defaultMode: bypassPermissions` + Webflow tools).
Pulled as 0eb3e0c. Exercising git/python/Webflow directly and firing the Routine manually to
confirm no prompt appears anywhere in a run.

## 2026-09-25 — post 3 of 200 published

**Published:** `how-much-does-vinyl-plank-flooring-installation-cost-in-edmonds` (6aa9e611a765e6616e45f9d5)
"How Much Does Vinyl Plank Flooring Installation Cost in Edmonds? 2026 Prices"

Scheduled 15:40 UTC run, published as-is, hero present, `errors: []`. Held: none.
First run under the widened allow-list: no permission prompt at any step.

2026-09-25 17:15 UTC — manual run on Oleg's revised prompt: nothing due (posts 1–3 already live). No-op. Revised prompt installed on the Routine.
