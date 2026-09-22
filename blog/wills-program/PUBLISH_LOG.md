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
