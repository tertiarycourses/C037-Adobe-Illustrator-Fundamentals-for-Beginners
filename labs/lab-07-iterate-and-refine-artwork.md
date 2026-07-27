# Lab 7 — Iterate and Refine Artwork

**Topic 02:** Creating and Refining Concept Art with AI  |  **Day 1**  |  **Approx. 38 min**  |  **Course:** Generative AI for Concept Art (C037)

## Scenario

Emberdrift is a fictional indie adventure game from the (fictional) studio Northlight Studios. It is set on a world of floating islands drifting above an endless sea of clouds, where young sky-salvagers ride patched gliders between lantern-lit sky-ports, scavenging relic-tech from ruins that rise through the cloud sea. The look is painterly and cinematic: warm ember and amber lantern light against cool sky-blues and misty greys, hopeful and adventurous. Northlight needs a concept-art pitch pack to sell the game's world: a hero character (Wren, a young sky-salvager), a key environment (a floating lantern sky-port at dusk), a prop set (Wren's salvaging gear), a locked house style, and a finished key-art piece. You are the concept artist, and across this course you take Emberdrift from a text prompt all the way to a portfolio-ready pack. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project is always welcome.

## Goal

Take one chosen piece and refine it with variations, reused seeds, image-to-image and style/character references until it matches your intent and stays consistent.

## What you'll build

A refined, near-final key-art candidate, converged on through variations, a reused seed, small prompt edits, image-to-image and a character/style reference — consistent with the rest of the pack.

**Tools and techniques:** Variations, seeds (reproducibility), single-change prompt edits, image-to-image (img2img), character/style references, upscale/select

## Prerequisites

- Completed Lab 6 (you have a locked style and a chosen composition).
- Your character/style references ready to supply to the tool.

## Steps

### Step 1

Choose the single image you most want as your final key art (for example Wren arriving at the sky-port, from Lab 6). Note its seed if your tool shows one (Midjourney: react to get the seed; Stable Diffusion: it is displayed; Firefly: use the same reference/settings).

### Step 2

Generate variations of that chosen image to explore near neighbours without starting over. Keep the ones that move it toward your intent, discard the rest.

### Step 3

Reuse the seed with a small single-change prompt edit so the change is controlled, not random — for example strengthen the focal point or fix the time of day. Paste the edited prompt below.

Text to use (type into your AI image tool's prompt field):

```text
Wren arriving at the floating lantern sky-port, push the warm lantern glow on Wren as the clear focal point, deepen the dusk sky, keep composition and character, house style appended, same seed, --ar 16:9.
```

### Step 4

Use image-to-image: feed the chosen image back in as the input with a modest strength, plus your prompt, so the tool improves it while keeping the composition. Compare against a from-scratch generation to feel the difference in control.

### Step 5

Add a character reference (your Wren hero concept from Lab 3) and/or a style reference (from Lab 6) so Wren and the look stay consistent through the iterations. Regenerate and confirm Wren still reads as the same character.

### Step 6

Do two or three more focused iterations, changing one thing each time (composition, lighting, a detail). Stop when the image clearly matches your intent — converging beats endless re-rolling.

### Step 7

Curate the single best refined image as your near-final key art and upscale/select it. Save it into your Emberdrift folder (for example 'keyart_refined.png') and note the seed and the final prompt so the result is reproducible.

## Test it

You have taken one chosen piece and refined it with variations, a reused seed, small single-change prompt edits, image-to-image and a character/style reference, kept Wren and the look consistent, and saved a refined near-final key-art candidate with its seed and prompt recorded.

## Troubleshooting

- **Iterations drift away from the original.** Lower the change per step, reuse the seed, and use image-to-image at a modest strength so the tool improves rather than reinvents.
- **Wren looks like a different person each time.** Supply the Wren hero concept as a character reference and keep the description identical between iterations.
- **You keep re-rolling forever.** Change one thing per iteration and stop when it matches your intent — converging beats endless new generations.

## Challenge

Reproduce your chosen image exactly from the recorded seed and prompt on a fresh session, proving your result is reproducible.

## Reflection

LO7 — In your own words: Iterate and refine artwork using variations, seeds, image-to-image and style/character references?

## Deliverable

Keep the refined near-final key-art candidate plus its recorded seed and prompt — the piece you finish in Lab 8.

---

*Generative AI for Concept Art (C037) · C037 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
