# Uploading rendered posts to Webflow (Wills Flooring)

`render.py` writes `out/<slug>.json`, a ready `fieldData` object for the Blog Posts collection
(`66cecfc7e7f88d2528ab474e`, site `66cc1f4542ee0c42e43d0303`).

Create (new scheduled posts), always as drafts:

```
data_cms_tool → create_collection_items
  collection_id: 66cecfc7e7f88d2528ab474e
  request: { isDraft: true, fieldData: [ <contents of out/<slug>.json> ] }
```

Update (legacy posts; manifest contains "id"):

```
data_cms_tool → update_collection_items
  collection_id: 66cecfc7e7f88d2528ab474e
  request: { items: [ { id: <id>, fieldData: { description-small, description-big, time-to-read } } ] }   # omit isDraft to keep live status
```

Rules
- One item per call is safest (bodies are 40–60 KB). Never set isDraft false on new posts; the daily Routine does that.
- After each create, list the item by slug and confirm `description-big` length equals the local file length.
- Slugs must be unique; if a create fails with a slug conflict, check whether the item already exists before retrying.
- Image Main is left empty on purpose: the owner adds hero photos in the Webflow Editor.
