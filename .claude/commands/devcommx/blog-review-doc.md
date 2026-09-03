---
description: Compile a DevCommX blog batch into a shareable review document.
argument-hint: "[batch name or slug list]"
---
# /devcommx:blog-review-doc

Compile a review doc for: **$ARGUMENTS**

Load `devcommx-blog-ops`.

## Steps

1. **Gather** the drafts from `devcommx/blogs/{batch}/` and their scores from
   `devcommx/validation/` (via `scripts/score_findings.py`).
2. **Build a standalone HTML doc.** One section per blog: title, slug, target keyword,
   meta title and description, word count, weighted score and verdict, the rendered
   post body, and the internal and external links used. Add a contents list at the top
   with the score table.
3. **Design system** — the review docs use navy `#213065` and coral `#D22B27` with
   theme-aware tokens. Load `artifact-design` before building the page.
4. **`.docx` via pandoc** when the user wants a Word copy:
   ```bash
   pandoc review.html -o DevCommX-{Batch}-{N}-Blogs.docx
   ```
   Earlier compilations are in the original handoff for format reference.
5. **Publish as an Artifact** if the user wants a shareable link, and hand them the URL.

## Output

The HTML and, on request, the `.docx`, plus a one-paragraph summary of the batch:
count, mean score, verdict split, and what still needs the client's input.
