"""
Domain 2 — Creating and Refining Concept Art with AI. Labs 6-9.

THE CONNECTED PROJECT CONTINUES — the same Emberdrift pack, now refined and
finished.

Lab 6 develops a consistent house style and strong compositions across the pack;
Lab 7 iterates and refines a chosen piece with variations, seeds, image-to-image
and references; Lab 8 edits and enhances a key-art piece with inpainting,
outpainting, upscaling and a hand paint-over; Lab 9 curates and presents the
concept-art portfolio and applies commercial-use and IP considerations. Use your
own project instead of Emberdrift wherever you prefer.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, "
 "the connected project you assemble across all 9 labs."
)

DOMAIN2 = [
 dict(
 num=6, topic=2,
 title="Develop a Consistent Style and Strong Compositions",
 objective="Lock a repeatable house style for Emberdrift and thumbnail strong compositions, so the character, environment and props all read as one world.",
 desc="Concept art for one project must feel like one world. In this lab you develop and lock a house style. "
 "You study your Labs 3–5 pieces, distil what makes them feel like Emberdrift, and write a single repeatable "
 "'house-style phrase' (medium, palette, lighting, mood) that you append to every prompt. You gather one or "
 "two style-reference images to reinforce it. Then you work on composition: you thumbnail several framings of "
 "a scene, applying shot type, aspect ratio, rule-of-thirds and focal-point words, and pick the strongest. "
 "The result is a locked style and a set of composition thumbnails that make the whole pack consistent. " + PROJECT_NOTE,
 build="A locked Emberdrift house-style phrase plus one or two style-reference images, and a set of composition thumbnails for a scene with the strongest framing chosen — so the whole pack reads as one world.",
 services="Your image tool's prompt field, a repeatable house-style phrase, style-reference images, composition thumbnails, shot type / aspect ratio / rule-of-thirds / focal-point control",
 steps=[
 ("Lay out your Labs 3–5 pieces (Wren, the sky-port, the props). Write down what makes them feel like one world — the painterly medium, the warm-lantern-against-cool-sky palette, the golden-dusk lighting, the hopeful mood.", ""),
 ("Distil that into one repeatable 'house-style phrase' you can append to every prompt. Paste your phrase below and test it by generating a fresh small subject with it.",
  "painterly game concept art, warm amber lantern light against cool misty blues, golden-dusk atmosphere, hopeful cinematic mood, cohesive Emberdrift house style."),
 ("Gather one or two style-reference images that capture the look (your own best piece from Labs 3–5 is the safest reference). You will use these to keep future generations on-style; note how your tool accepts a reference (Midjourney --sref or image prompt; Firefly/Stable Diffusion style or reference image).", ""),
 ("Now work composition. Pick a scene (for example Wren arriving at the sky-port) and thumbnail several framings quickly — vary only the shot and aspect ratio. Paste the thumbnail prompt below and generate a few.",
  "Wren arriving at the floating lantern sky-port, thumbnail compositions: (1) wide low-angle establishing shot, (2) over-the-shoulder from behind Wren looking at the port, (3) tight close-up of Wren with the port bokeh behind; rule of thirds, clear focal point, house style appended, --ar 16:9."),
 ("Compare the thumbnails for storytelling and focal point. Pick the strongest composition and note why it works (leading lines, figure placement, contrast). Upscale/select it as your chosen framing.", ""),
 ("Re-generate your weakest earlier piece (from Labs 3–5) with the locked house-style phrase and, if your tool supports it, the style reference — and confirm it now sits consistently with the rest of the pack.", ""),
 ("Save your house-style phrase, your style-reference image(s) and the composition thumbnails into your Emberdrift folder. Note one line on the house style so you can reuse it on every future piece.", ""),
 ],
 test="You have written and tested a repeatable Emberdrift house-style phrase, gathered a style reference, thumbnailed several compositions and chosen the strongest with clear reasons, and brought your weakest earlier piece back on-style — so the whole pack now reads as one world.",
 ),
 dict(
 num=7, topic=2,
 title="Iterate and Refine Artwork",
 objective="Take one chosen piece and refine it with variations, reused seeds, image-to-image and style/character references until it matches your intent and stays consistent.",
 desc="Great concept art is converged on, not stumbled into. In this lab you take one chosen piece — the "
 "best candidate for your final key art, for example Wren at the sky-port — and refine it deliberately. You "
 "generate variations of it to explore near neighbours, reuse its seed for reproducible control, and make "
 "small single-change prompt edits so you steer rather than restart. You use image-to-image (feeding the "
 "chosen image back in) and a character/style reference to keep Wren and the look consistent while you improve "
 "composition and detail. You end with a refined, near-final image that clearly matches your intent. " + PROJECT_NOTE,
 build="A refined, near-final key-art candidate, converged on through variations, a reused seed, small prompt edits, image-to-image and a character/style reference — consistent with the rest of the pack.",
 services="Variations, seeds (reproducibility), single-change prompt edits, image-to-image (img2img), character/style references, upscale/select",
 steps=[
 ("Choose the single image you most want as your final key art (for example Wren arriving at the sky-port, from Lab 6). Note its seed if your tool shows one (Midjourney: react to get the seed; Stable Diffusion: it is displayed; Firefly: use the same reference/settings).", ""),
 ("Generate variations of that chosen image to explore near neighbours without starting over. Keep the ones that move it toward your intent, discard the rest.", ""),
 ("Reuse the seed with a small single-change prompt edit so the change is controlled, not random — for example strengthen the focal point or fix the time of day. Paste the edited prompt below.",
  "Wren arriving at the floating lantern sky-port, push the warm lantern glow on Wren as the clear focal point, deepen the dusk sky, keep composition and character, house style appended, same seed, --ar 16:9."),
 ("Use image-to-image: feed the chosen image back in as the input with a modest strength, plus your prompt, so the tool improves it while keeping the composition. Compare against a from-scratch generation to feel the difference in control.", ""),
 ("Add a character reference (your Wren hero concept from Lab 3) and/or a style reference (from Lab 6) so Wren and the look stay consistent through the iterations. Regenerate and confirm Wren still reads as the same character.", ""),
 ("Do two or three more focused iterations, changing one thing each time (composition, lighting, a detail). Stop when the image clearly matches your intent — converging beats endless re-rolling.", ""),
 ("Curate the single best refined image as your near-final key art and upscale/select it. Save it into your Emberdrift folder (for example 'keyart_refined.png') and note the seed and the final prompt so the result is reproducible.", ""),
 ],
 test="You have taken one chosen piece and refined it with variations, a reused seed, small single-change prompt edits, image-to-image and a character/style reference, kept Wren and the look consistent, and saved a refined near-final key-art candidate with its seed and prompt recorded.",
 ),
 dict(
 num=8, topic=2,
 title="Edit and Enhance with Inpainting, Outpainting and Paint-Over",
 objective="Finish your key-art piece by fixing regions with inpainting, widening the frame with outpainting, upscaling for resolution, and adding a hand paint-over in your image editor.",
 desc="AI images almost always need a human finish. In this lab you take your Lab 7 near-final key art and "
 "make it portfolio-ready. You use inpainting to regenerate any weak region (a distorted hand, an awkward "
 "lantern) while keeping the rest; outpainting to extend the canvas and improve the crop or widen the scene; "
 "and an AI upscaler to raise resolution and detail. Then you do the professional finish: a hand paint-over in "
 "your image editor — fixing anatomy and perspective, adjusting colour and value, and adding the small details "
 "that make the piece intentional and unmistakably yours. " + PROJECT_NOTE,
 build="A finished, portfolio-ready Emberdrift key-art piece — inpainted to fix weak regions, outpainted to improve the crop, upscaled for resolution, and hand painted over in your image editor.",
 services="Inpainting (regenerate a selected region), outpainting (extend the canvas), AI upscaling, Photoshop/Firefly Generative Fill, an image editor with layers for the paint-over",
 steps=[
 ("Open your Lab 7 near-final key art. Identify one or two weak regions to fix (a distorted hand, a muddy lantern, an awkward edge). These are your inpainting targets.", ""),
 ("Inpaint each weak region: select just that area and regenerate it with a short prompt so it is fixed while the rest is untouched. (Firefly/Photoshop: select and use Generative Fill; Stable Diffusion tools: use inpaint; Midjourney: use Vary Region.) Paste an example inpaint prompt below.",
  "A correctly-drawn hand gripping the rope, matching the painterly style and warm lantern lighting."),
 ("Outpaint to improve the crop: extend the canvas on one or two sides so the composition breathes — for example add more sky above or more dock below. Confirm the extension blends seamlessly with the original.", ""),
 ("Upscale the image with an AI upscaler to raise resolution and add detail for portfolio quality. Check the upscale did not introduce artefacts; re-inpaint any it created.", ""),
 ("Bring the image into your editor (Photoshop, Krita or Photopea) on its own layer and do a hand paint-over: fix any remaining anatomy or perspective, adjust colour and value for a stronger read, and deepen the focal point.", ""),
 ("Add the finishing details that make it yours: a few sharp highlights on the lanterns, atmospheric haze for depth, a subtle rim light on Wren. Keep your edits on separate layers so they stay adjustable.", ""),
 ("Flatten a copy and export the finished key art at high resolution into your Emberdrift folder (for example 'keyart_final.png'). Note one line on what you fixed by hand versus what the AI generated — the finish is the artist's job.", ""),
 ],
 test="You have finished your key-art piece by inpainting weak regions, outpainting to improve the crop, upscaling for resolution, and adding a hand paint-over in your image editor — and exported a portfolio-ready 'keyart_final' image, keeping your edit layers adjustable.",
 ),
 dict(
 num=9, topic=2,
 title="Build and Present the Concept-Art Portfolio",
 objective="Curate the Emberdrift pieces into a presented concept-art portfolio, assemble and export it, and apply commercial-use and IP considerations before delivery.",
 desc="One finished world, curated and presented responsibly. In this lab you bring the whole pack together. "
 "You curate the strongest pieces — the Wren character page, the sky-port environment, the prop asset sheet "
 "and the finished key art — and lay them out as a clean, presented portfolio with brief captions that show "
 "range and consistency. You export it in delivery formats and assemble a simple presentation (a PDF or a set "
 "of boards). Finally you apply the commercial-use and IP checks that make the work safe to share: your tool's "
 "licensing, avoiding trademarks and protected styles, and disclosing AI assistance. This completes the course "
 "pipeline end to end. " + PROJECT_NOTE,
 build="A curated, presented Emberdrift concept-art portfolio — character, environment, props and key art with captions — exported as a PDF/board set, with a completed commercial-use and IP checklist.",
 services="Curation, portfolio layout (character / environment / props / key art), captions, Export As (PNG/JPEG/PDF), a presentation editor, the commercial-use and IP checklist",
 steps=[
 ("Gather your finished pieces into the Emberdrift folder: the Wren character page (hero + variations), the sky-port environment (wide + detail), the prop asset sheet, and the finished key art from Lab 8.", ""),
 ("Curate ruthlessly: keep only the strongest, most on-style version of each. A tight portfolio of four excellent boards beats a loose pile — cut anything off-model or weak.", ""),
 ("Lay out the portfolio: create clean boards (one per category) in your editor or a slide tool, each with a short caption naming the piece and the tool/technique used. Keep the house style consistent across the boards.",
  "Emberdrift — Concept Art Pack: 01 Character — Wren, sky-salvager; 02 Environment — the floating lantern sky-port at dusk; 03 Props — Wren's salvaging gear; 04 Key Art — Wren arrives at the sky-port."),
 ("Add a short title board with the game name, a one-line pitch, and your name/role as concept artist, so the portfolio presents as a coherent pack.", ""),
 ("Export for delivery: export each board as high-resolution PNG/JPEG and assemble them into a single PDF portfolio. Keep your working files and edit layers in the folder too.", ""),
 ("Run the commercial-use and IP checklist: confirm you did not prompt for any trademark, living artist or copyrighted character; note your tool's commercial terms (Firefly is commercial-safe and indemnified; check your Midjourney/Stable Diffusion plan and model licences); check any placed reference or photo licence; and record where you will disclose AI assistance.", ""),
 ("Write a one-page read-me listing each board, its tool/technique and its format, plus the IP checklist result. Save the PDF portfolio and the read-me — this presented pack is your deliverable and the end-to-end result the course set out to build.", ""),
 ],
 test="You have curated the Emberdrift pieces into a presented concept-art portfolio (character, environment, props, key art) with captions and a title board, exported it as a PDF/board set in delivery formats, and completed a commercial-use and IP checklist — a finished, responsibly-delivered concept-art pack.",
 ),
]
