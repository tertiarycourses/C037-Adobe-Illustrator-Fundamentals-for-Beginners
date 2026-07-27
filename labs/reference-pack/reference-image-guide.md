# Reference-Image Guide — Emberdrift

*How to gather and use the reference images the labs rely on. You may use your own
generated pieces, or any image you are **authorised** to use.*

## Why references matter

Several labs use a reference image rather than a prompt alone:

- **Lab 6 — Style reference.** A style reference tells the tool the *look* to
  adopt, so every new piece matches the pack.
- **Lab 7 — Character & style reference.** A character reference keeps **Wren**
  the same person across iterations; a style reference keeps the look consistent.
- **Lab 7 — Image-to-image.** An input image (a sketch, a previous generation)
  guides the composition while you change other things.
- **Lab 8 — Editing.** Your own near-final image is the surface you inpaint,
  outpaint, upscale and paint over.

## What to gather

### 1. A style reference (Lab 6)
- One clean piece of **painterly concept art** in the Emberdrift look.
- **Best option:** use your own strongest piece from Labs 3–5 — it guarantees the
  new work matches your pack exactly.
- How to supply it: Midjourney `--sref <image url>`; Leonardo/DreamStudio an
  image/style reference slot; Firefly a reference image.

### 2. A character reference (Lab 7)
- Your **Wren hero concept** from Lab 3, on a clean background, face and costume
  clearly visible.
- How to supply it: Midjourney character reference (`--cref`); other tools an
  image prompt or reference slot. This is what keeps Wren on-model.

### 3. An input image for image-to-image (Lab 7, optional)
- A rough **sketch** of the composition you want, or a previous generation to
  improve.
- Feed it in at a **modest strength** so the tool refines rather than reinvents.

## Rules for any reference you use

- Use only images you **own or are licensed/authorised** to use.
- Do **not** upload confidential client material or a competitor's artwork.
- Do **not** use a reference to copy a **living artist's** style or a **trademark**.
- When in doubt, generate a fresh reference with a prompt instead.

## Preparing an image for best results

1. Crop to the single subject or the clear composition.
2. Put it on a plain, uncluttered background where it helps.
3. Make sure the whole subject is visible and evenly lit.
4. Keep the file reasonably sized (a clean input beats a huge messy one).
