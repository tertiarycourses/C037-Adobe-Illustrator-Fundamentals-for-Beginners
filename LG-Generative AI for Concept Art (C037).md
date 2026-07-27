# Generative AI for Concept Art (C037) — Learner Guide

**Course Code:** C037  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 27 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Generative AI for Concept Art  (55%)](#topic-01--getting-started-with-generative-ai-for-concept-art--55)
  - [Lab 1 — Get Started with Generative AI Image Tools](#lab-1--get-started-with-generative-ai-image-tools)
  - [Lab 2 — Write Effective Prompts for Concept Art](#lab-2--write-effective-prompts-for-concept-art)
  - [Lab 3 — Generate Character Concepts](#lab-3--generate-character-concepts)
  - [Lab 4 — Generate Environment Concepts](#lab-4--generate-environment-concepts)
  - [Lab 5 — Generate a Prop and Asset Sheet](#lab-5--generate-a-prop-and-asset-sheet)
- [Topic 02 — Creating and Refining Concept Art with AI  (45%)](#topic-02--creating-and-refining-concept-art-with-ai--45)
  - [Lab 6 — Develop a Consistent Style and Strong Compositions](#lab-6--develop-a-consistent-style-and-strong-compositions)
  - [Lab 7 — Iterate and Refine Artwork](#lab-7--iterate-and-refine-artwork)
  - [Lab 8 — Edit and Enhance with Inpainting, Outpainting and Paint-Over](#lab-8--edit-and-enhance-with-inpainting-outpainting-and-paint-over)
  - [Lab 9 — Build and Present the Concept-Art Portfolio](#lab-9--build-and-present-the-concept-art-portfolio)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Generative AI for Concept Art (C037) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 9 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build a single, connected deliverable — the Emberdrift concept-art pitch pack, for a fictional indie game about sky-salvagers exploring floating islands above a sea of clouds. You start in Lab 1 by getting oriented in the AI image tools, then in every lab you take the pack one stage further — a strong structured prompt, a hero character with variations, a key environment, a prop asset sheet, a locked house style with composition thumbnails, refined iterations, an inpainted-outpainted-upscaled-and-painted-over key-art piece, and finally a curated, presented portfolio. A concept-art brief is supplied; you may substitute your own non-confidential project wherever you prefer.


## Course Learning Outcomes

- LO1: Explain how generative-AI image tools create concept art, compare Midjourney, Stable Diffusion and Adobe Firefly, and navigate the generate–review–refine loop.
- LO2: Write effective, structured prompts that control the subject, style, composition, shot, lighting and level of detail of generated concept art.
- LO3: Generate consistent character concepts — a hero character with costume and expression variations — from a written brief.
- LO4: Generate environment and key-location concepts, controlling place, time of day, mood, scale and shot.
- LO5: Generate props, assets and gadgets as a clean, coherent asset sheet.
- LO6: Develop a consistent visual style and strong compositions so a set of concept art reads as one world.
- LO7: Iterate and refine artwork using variations, seeds, image-to-image and style/character references.
- LO8: Edit and enhance concept art with inpainting, outpainting, upscaling and a hand paint-over finish.
- LO9: Assemble and present a concept-art portfolio, and apply commercial-use and IP considerations.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) able to run a modern browser smoothly — a reasonably recent machine with 8 GB RAM minimum, 16 GB preferred.
- Access to at least one AI image generator: Midjourney (a paid plan, run in Discord or the web app), a Stable Diffusion tool (a hosted UI such as Leonardo.Ai or DreamStudio, or a local install), or Adobe Firefly (web, or built into Photoshop). The trainer will confirm which tool the class uses at the start of the day.
- An image editor with generative fill and layers for editing and paint-over — Adobe Photoshop (with Generative Fill) is ideal; the free Krita or the browser-based Photopea also work.
- An internet connection (the generative tools run in the cloud), a modern browser, and about 1 GB of free disk space for your generated images and exports.
- The supplied Emberdrift concept-art brief (world, characters, props and a reference-image guide in labs/reference-pack/) — or a few notes and a reference image of your own non-confidential project to use instead.

**Verify your setup**

Before Lab 1, confirm you can sign in to your chosen AI image generator and run one test generation, and that your image editor opens and can create a new layered document. If anything is missing, tell the trainer.

```bash
Sign in to your AI image tool (Midjourney / Stable Diffusion tool / Adobe Firefly)  ·  run one test image  ·  open your image editor (Photoshop / Krita / Photopea) and create a new document
```

**Conventions used in every lab**

- Placeholders such as <YOUR PROJECT> or <YOUR REFERENCE IMAGE> are replaced with your own values.
- Prompts to type into the image generator are shown in the 'Text to use' blocks — adapt them to your own project and tool (Midjourney uses --ar and --seed; Stable Diffusion and Firefly have equivalent aspect-ratio and seed controls).
- Every lab ends with a 'Test it' step — an explicit check that the result meets the brief before you move on.
- Keep every image for the project in a single folder (Emberdrift) so your pack stays together and consistent.


## Topic 01 — Getting Started with Generative AI for Concept Art  (55%)

Introduction to generative AI for art · Popular AI image tools (Midjourney, Stable Diffusion, Firefly) · Writing effective prompts for concept art · Generating characters, environments and props

**Key concepts**

- Generative AI for art — text-to-image models turn a written description into a finished image in seconds; for concept art they let one artist explore dozens of characters, worlds and props in the time a single painting used to take.
- What concept art is for — concept art is exploration and communication, not final art: it sells a look, a character or a place to a team early, so generative AI's speed at producing many options fits the job perfectly.
- Popular AI image tools — Midjourney (a strong, painterly, art-directed look, run in Discord or the web app), Stable Diffusion (open and highly controllable, run locally or through hosted UIs such as Leonardo.Ai or DreamStudio) and Adobe Firefly (commercial-safe and built into Photoshop) are the three you meet in this course.
- Choosing a tool — they share the same prompt-driven idea but differ: Midjourney for fast, beautiful results, Stable Diffusion for control and reproducibility (seeds, models, ControlNet), Firefly for commercial-safe output and in-editor editing; you pick by the job.
- The generate–review–refine loop — you write a prompt, the tool returns a grid of variations, you review and pick the strongest, then upscale, vary or re-prompt; this loop is the heart of every generative task.
- Prompt-writing for concept art — a strong prompt names the subject, the style or medium, the composition and shot, the lighting and mood, and the level of detail; concrete, art-directed wording beats a vague sentence.
- Prompt structure and modifiers — subject + descriptors + style reference + camera/shot + lighting + quality terms, plus tool-specific parameters (aspect ratio, stylize, seed) that steer the result.
- Generating characters — you describe who the character is (role, age, silhouette, costume, personality) and generate front-facing character concepts, then explore variations of costume, pose and expression.
- Generating environments — you describe a place (location, time of day, weather, scale, key landmark) and the shot (wide establishing, aspect ratio) to generate environment and key-location concepts.
- Generating props — you generate individual objects, gadgets and gear, often as a clean asset sheet on a plain background so each design reads clearly for the team.


### Lab 1 — Get Started with Generative AI Image Tools

Learning outcome: Sign in to your AI image generator, run your first generations, compare Midjourney, Stable Diffusion and Firefly, and learn the generate–review–refine loop that every later lab uses..

Goal: This lab gets you comfortable with the tools before any real concept-art work begins. You sign in to your chosen AI image generator (Midjourney, a Stable Diffusion tool such as Leonardo.Ai, or Adobe Firefly), confirm your image editor is ready, and run a simple generation. You learn to read the grid of variations the tool returns, upscale or select the strongest, and re-prompt or vary it. You try the same idea in a second tool if you have access, and note how Midjourney, Stable Diffusion and Firefly differ in look, control and commercial terms. By the end you understand the describe -> generate -> review -> refine loop that is the heart of generative concept art. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A project folder with your first AI-generated images, produced from more than one prompt, with the strongest variation selected/upscaled — plus a clear understanding of your tool's interface and the generate–review–refine loop.   (Tools: Midjourney / Stable Diffusion tool (e.g. Leonardo.Ai) / Adobe Firefly, sign-in and credits, prompt field, the grid of variations, upscale/select, aspect-ratio and basic parameters, an image editor.)

**Step-by-step**

1. Create a project folder on your machine called 'Emberdrift' so every image you make today stays together. Sign in to your chosen AI image generator (Midjourney in Discord or the web app, a Stable Diffusion tool such as Leonardo.Ai, or Adobe Firefly) and confirm you have credits/generations available.
2. Run a simple first generation so you can see how the tool works. Type the prompt below and generate. (In Midjourney use /imagine; in a Stable Diffusion tool or Firefly, type it into the prompt box.)

   ```bash
   A young explorer standing on a floating island above a sea of clouds, warm lantern light, painterly concept art, cinematic.
   ```

3. Wait for the tool to return a grid of variations. Review them and pick the strongest. Upscale or select it (Midjourney U1–U4; other tools have an upscale/download button). Notice this is one full turn of the loop.
4. Make a small change and regenerate to feel how prompts steer the result — for example add a time of day or a mood word — and compare. Paste the changed prompt below.

   ```bash
   A young explorer standing on a floating island above a sea of clouds at dusk, warm amber lantern light, misty blue sky, painterly concept art, cinematic, hopeful mood.
   ```

5. Set an aspect ratio to change the framing: try a wide establishing shot. (Midjourney: add --ar 16:9; other tools: choose a 16:9 or landscape size.) Regenerate and see how the composition changes with the frame.
6. If you have access to a second tool, run the same prompt in it and compare — note how Midjourney, Stable Diffusion and Firefly differ in look, how much control each gives, and their commercial terms. If you only have one tool, note its strengths for concept art.
7. Save two or three of your best images into your Emberdrift folder. Write one line, in your own words, describing what the generate–review–refine loop is and where your tool's prompt field, variation grid and upscale/aspect-ratio controls live — you rely on all of them in every later lab.

**Test it**

You have run more than one generation in your AI image tool, reviewed the grid of variations, selected/upscaled the strongest, changed the prompt and the aspect ratio to see how each steers the result, and saved your best images in your Emberdrift folder — with a clear understanding of the generate–review–refine loop.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 2 — Write Effective Prompts for Concept Art

Learning outcome: Turn the supplied Emberdrift brief into a strong, structured prompt that controls subject, style, composition, shot, lighting and detail, and save it as a reusable template..

Goal: A good concept-art image starts with a good prompt, not a lucky one. In this lab you read the supplied Emberdrift brief and shape it into a structured prompt with clear parts: the subject, the style/medium (painterly concept art, digital painting), the composition and shot (wide establishing, close-up, low angle), the lighting and mood (warm amber lantern light, cool misty sky), the level of detail, and words to steer colour. You run small, single-change edits to see how each part moves the result, then save your best version as a reusable template with clearly marked slots you will reuse for the rest of the project. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A structured Emberdrift prompt (subject, style, composition/shot, lighting/mood, detail, colour) plus a reusable prompt template with marked slots, saved in your project folder.   (Tools: Your image tool's prompt field, the supplied Emberdrift brief, a structured prompt template, style/composition/lighting keywords, aspect-ratio and stylize parameters.)

**Step-by-step**

1. Open the supplied brief (labs/reference-pack/): the world brief, the style notes and the reference-image guide. Skim all three so you know the look you are describing — painterly, warm ember lantern light against cool misty blues, hopeful and cinematic.
2. Write a first structured prompt that names the subject and its style/medium, and generate. Paste the prompt below.

   ```bash
   A lone sky-salvager on a drifting island, painterly digital concept art, cinematic, in the style of a game key art illustration.
   ```

3. Add composition and shot guidance and regenerate. Notice how the framing tightens while the subject stays. This shows composition words steer the shot independently of the subject.

   ```bash
   Same lone sky-salvager, wide establishing shot, low angle looking up, rule of thirds, the figure small against a vast cloud sea, --ar 16:9.
   ```

4. Add lighting, mood and a level-of-detail instruction, then regenerate.

   ```bash
   Warm amber lantern light rimming the figure, cool misty blue sky, golden-hour glow, atmospheric depth, highly detailed painterly rendering, hopeful and adventurous mood.
   ```

5. Run two or three more small, single-change edits to feel how each part matters — for example change 'wide establishing shot' to 'close-up portrait', or 'golden-hour' to 'stormy overcast' — and note which direction you prefer for Emberdrift.
6. Combine your best choices into one clean prompt. Then ask yourself the prompting rule: does it name the subject, the style, the composition/shot, the lighting/mood, the detail level and the colour, and does it set an aspect ratio? Fill any gap.
7. Save two things in your Emberdrift folder: your final Emberdrift prompt, and a reusable template version with clearly marked slots — [SUBJECT], [STYLE/MEDIUM], [COMPOSITION/SHOT], [LIGHTING/MOOD], [DETAIL], [COLOUR], [PARAMETERS] — that you can reuse for any future piece.

**Test it**

You have a structured Emberdrift prompt that explicitly controls subject, style, composition/shot, lighting/mood, level of detail and colour (with an aspect ratio set), and you have saved a reusable prompt template with clearly marked slots in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 3 — Generate Character Concepts

Learning outcome: Use your prompt to generate the Emberdrift hero character (Wren) with a consistent design, then explore costume, pose and expression variations and curate the strongest..

Goal: With a strong prompt in hand you can generate the first real piece of the pack: the hero character. In this lab you adapt your Lab 2 prompt to describe Wren — a young sky-salvager — with a clear role, silhouette, costume and personality, and generate front-facing character concepts. You then explore variations: different costumes, poses and expressions, keeping the character recognisable across them. You curate the single strongest, most on-brief design as Wren's hero concept, and keep a couple of variations that show the character's range. These become the character page of your pack. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A curated Emberdrift hero-character concept (Wren) plus a few costume/expression variations that keep the character recognisable, saved as the character page of your pack.   (Tools: Your image tool's prompt field, character-description prompting (role, silhouette, costume, expression), variations, aspect ratio for a character shot, upscale/select, curating the best.)

**Step-by-step**

1. In your image tool, adapt your Lab 2 template to describe Wren clearly: role, age, silhouette, costume and personality. Set a character-friendly aspect ratio (a portrait/full-body ratio such as 2:3). Paste the prompt below and generate.

   ```bash
   Full-body character concept of Wren, a determined teenage sky-salvager, wiry and agile, wearing a patched leather flight coat, goggles pushed up on the forehead, a coil of rope and salvage tools at the belt, worn boots; painterly game concept art, neutral studio background, front view, warm key light, --ar 2:3.
   ```

2. Review the grid and pick the strongest, clearest design. Upscale/select it. This is your candidate hero concept for Wren — a single, readable character silhouette.
3. Explore costume and gear variations, changing only wardrobe words so the character stays recognisable. Generate a couple. Paste the variation prompt below.

   ```bash
   Same character Wren, same face and build, alternative outfit: a lighter summer flight vest and rolled sleeves; then a heavier storm cloak with a hood; keep the goggles and salvage tools, painterly game concept art, front view, --ar 2:3.
   ```

4. Explore expression and pose variations — for example a confident grin, a wary glance, a mid-action leap — so the character sheet shows personality and range. Generate one or two.

   ```bash
   Same character Wren, three expressions: a confident grin, a wary sideways glance, and a determined shout mid-leap; consistent design and costume, painterly game concept art, --ar 3:2.
   ```

5. Curate: choose the single strongest, most on-brief design as Wren's hero concept, and keep two variations that best show the character's range. Discard the rest so your folder stays clean.
6. Check consistency across the kept images: same face, build, costume language and feel. If one variation drifts off-model, note what changed (the tool re-invented the face or costume) — you fix consistency properly with references in Lab 7.
7. Save the hero concept and the two variations into your Emberdrift folder as the character page (for example 'wren_hero.png' plus 'wren_var1.png', 'wren_var2.png'). Note one line on what makes Wren's silhouette read as one character.

**Test it**

You have generated a hero-character concept for Wren from a structured prompt, explored costume/pose/expression variations that keep the character recognisable, curated the single strongest design plus two range-showing variations, and saved them as the character page of your Emberdrift pack.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 4 — Generate Environment Concepts

Learning outcome: Generate the Emberdrift key environment — a floating lantern sky-port at dusk — controlling place, time of day, mood, scale and shot, and curate the strongest establishing image..

Goal: Every game world needs a place that sells it. In this lab you generate Emberdrift's key location: a floating lantern sky-port at dusk, where salvagers dock their gliders. You adapt your prompt to describe an environment, not a character — naming the location, the time of day, the weather, the scale and a key landmark — and set a wide establishing aspect ratio. You generate several compositions, push the mood with lighting words, and curate the single strongest establishing shot. You also generate one closer 'detail' view of the same place so the location reads at two scales. These become the environment page of your pack. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A curated Emberdrift environment concept — a wide establishing shot of the floating lantern sky-port at dusk — plus one closer detail view of the same location, saved as the environment page of your pack.   (Tools: Your image tool's prompt field, environment prompting (location, time of day, weather, scale, landmark), wide aspect ratios, atmospheric lighting words, variations and curating.)

**Step-by-step**

1. Adapt your prompt template to describe a place rather than a person. Name the location, time of day, weather, scale and a key landmark, and set a wide establishing aspect ratio. Paste the prompt below and generate.

   ```bash
   Wide establishing shot of a floating lantern sky-port at dusk, wooden docks and rope bridges strung between drifting islands above a sea of clouds, patched gliders moored, hundreds of warm lanterns glowing, a tall salvage-crane landmark, painterly game concept art, atmospheric depth, cinematic, --ar 16:9.
   ```

2. Review the grid and pick the composition with the clearest focal point and the strongest sense of place and scale. Upscale/select it as your candidate establishing shot.
3. Push the mood: regenerate with stronger lighting and atmosphere words to make dusk feel warm and inviting against the cool sky. Compare with your first pick.

   ```bash
   Same floating lantern sky-port, deeper dusk, warm amber lantern glow reflecting off mist, cool blue shadows, volumetric light, drifting fog between the islands, hopeful and adventurous, --ar 16:9.
   ```

4. Generate a closer 'detail' view of the same place so the location reads at two scales — for example one dock with a moored glider and a salvager silhouette. Keep the same style and palette.

   ```bash
   Closer view of one dock at the Emberdrift sky-port, a moored patched glider and a small salvager silhouette beside a glowing lantern, ropes and crates, warm amber light, cool misty background, painterly game concept art, --ar 3:2.
   ```

5. Curate: keep the single strongest wide establishing shot and the best detail view, and discard the rest. Check both clearly belong to the same place and the same time of day.
6. Check consistency with Wren's character page from Lab 3: same painterly medium, same warm-lantern-against-cool-sky palette, same mood. Note any drift to fix when you lock the house style in Lab 6.
7. Save the establishing shot and the detail view into your Emberdrift folder as the environment page (for example 'skyport_wide.png' and 'skyport_detail.png'). Note one line on what gives the location its sense of scale.

**Test it**

You have generated a wide establishing environment concept of the floating lantern sky-port at dusk and a closer detail view of the same location, controlled place, time of day, mood, scale and shot, curated the strongest of each, and saved them as the environment page of your Emberdrift pack.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 5 — Generate a Prop and Asset Sheet

Learning outcome: Generate Wren's salvaging gear as individual props on clean backgrounds and assemble them into a coherent asset sheet that matches the pack's style..

Goal: A game world is made of objects, and props must read clearly on their own. In this lab you generate Wren's salvaging gear — a grappling lantern-hook, a brass wind-compass, and goggles — as individual props, each on a plain, uncluttered background so the design reads for the team. You use consistent style and lighting words across all three so they look like one set, generate variations of each, curate the strongest, and assemble them into a single clean asset sheet. This completes the Topic 1 hands-on and gives your pack its prop page. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A coherent Emberdrift prop asset sheet — a grappling lantern-hook, a brass wind-compass and goggles, each generated on a clean background in a consistent style and assembled into one sheet.   (Tools: Your image tool's prompt field, prop/asset prompting (single object, plain background), consistent style/lighting words, variations, curating, an image editor to assemble the sheet.)

**Step-by-step**

1. Generate the first prop on a plain background so the design reads clearly. Name a single object, the material, and a neutral studio setup. Paste the prompt below and generate.

   ```bash
   Concept art of a single prop: a salvager's grappling lantern-hook — a brass hook with a small glowing lantern housing and a coiled rope — worn and functional, three-quarter view, plain light-grey studio background, soft even lighting, painterly game concept art, --ar 1:1.
   ```

2. Generate the other two props the same way, reusing the exact same style, background and lighting words so the set looks consistent — change only the object.

   ```bash
   Same style and plain studio background: a brass wind-compass with a spinning vane and a small pressure dial; then a pair of leather-and-brass flight goggles with amber-tinted lenses; worn and functional, painterly game concept art, --ar 1:1.
   ```

3. For each prop, review the grid, generate a variation or two if the shape is unclear, and curate the single clearest, most on-brief version. Aim for props that would read on a plain sheet at a glance.
4. Check the three props read as one set: same painterly style, same soft studio lighting, same worn brass-and-leather material language, same warm palette as the rest of the pack. Regenerate any outlier.
5. Assemble the asset sheet: open your image editor, place the three curated props on one clean canvas with even spacing and a simple label under each (Lantern-Hook, Wind-Compass, Goggles). Keep the background plain.
6. Do a consistency pass across Labs 3–5: character, environment and props should share the same medium, palette and mood. Note any drift for the house-style lock in Lab 6.
7. Save the individual props and the assembled sheet into your Emberdrift folder as the prop page (for example 'prop_lanternhook.png', 'prop_compass.png', 'prop_goggles.png' and 'prop_sheet.png'). Note one line on what keeps the three props reading as one set.

**Test it**

You have generated three of Wren's props — a grappling lantern-hook, a wind-compass and goggles — each on a clean background in a consistent style, curated the strongest of each, and assembled them into one coherent asset sheet saved as the prop page of your Emberdrift pack.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


## Topic 02 — Creating and Refining Concept Art with AI  (45%)

Developing styles and compositions · Iterating and refining artwork · Editing and enhancing with AI · Building a concept art portfolio

**Key concepts**

- Developing a consistent style — concept art for one project must feel like one world; you lock a house style with a repeatable style phrase, reference images and (in Stable Diffusion) a chosen model or LoRA, so every piece matches.
- Composition and shot — strong concept art is well composed; you steer it with aspect ratio, shot type (wide establishing, close-up, low angle), rule-of-thirds and focal-point words, and you thumbnail several compositions before committing.
- Iterating with variations and seeds — you refine by generating variations of a chosen image, reusing a seed for reproducibility, and making small single-change prompt edits so you converge on the intended result instead of starting over.
- Image-to-image and references — feeding an existing image (a sketch, a photo, a previous generation) back in with image-to-image, or supplying a style or character reference, keeps the subject or look consistent while you change other things.
- Editing with inpainting and outpainting — inpainting regenerates a selected region (fix a hand, change a helmet) while keeping the rest; outpainting extends the canvas to widen a scene or change the crop.
- Enhancing and upscaling — AI upscalers raise resolution and add detail for portfolio-quality output, and generative-fill editors (Photoshop or Firefly) add or remove elements cleanly.
- Paint-over and finishing — the professional finish is a hand paint-over: you take the AI image into an editor, fix anatomy and perspective, adjust colour and value, and add the details that make the piece intentional and yours.
- Building a concept-art portfolio — you curate the strongest pieces, present them cleanly (character, environment, props, key art) with brief captions, and show the range and consistency a studio looks for.
- Commercial use and IP — the tools differ on commercial terms (Firefly is trained for commercial safety and indemnified, while Midjourney and Stable Diffusion vary by plan and model); you avoid prompting for trademarks, living artists' names and copyrighted characters, check licences, and disclose AI use where appropriate.


### Lab 6 — Develop a Consistent Style and Strong Compositions

Learning outcome: Lock a repeatable house style for Emberdrift and thumbnail strong compositions, so the character, environment and props all read as one world..

Goal: Concept art for one project must feel like one world. In this lab you develop and lock a house style. You study your Labs 3–5 pieces, distil what makes them feel like Emberdrift, and write a single repeatable 'house-style phrase' (medium, palette, lighting, mood) that you append to every prompt. You gather one or two style-reference images to reinforce it. Then you work on composition: you thumbnail several framings of a scene, applying shot type, aspect ratio, rule-of-thirds and focal-point words, and pick the strongest. The result is a locked style and a set of composition thumbnails that make the whole pack consistent. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A locked Emberdrift house-style phrase plus one or two style-reference images, and a set of composition thumbnails for a scene with the strongest framing chosen — so the whole pack reads as one world.   (Tools: Your image tool's prompt field, a repeatable house-style phrase, style-reference images, composition thumbnails, shot type / aspect ratio / rule-of-thirds / focal-point control.)

**Step-by-step**

1. Lay out your Labs 3–5 pieces (Wren, the sky-port, the props). Write down what makes them feel like one world — the painterly medium, the warm-lantern-against-cool-sky palette, the golden-dusk lighting, the hopeful mood.
2. Distil that into one repeatable 'house-style phrase' you can append to every prompt. Paste your phrase below and test it by generating a fresh small subject with it.

   ```bash
   painterly game concept art, warm amber lantern light against cool misty blues, golden-dusk atmosphere, hopeful cinematic mood, cohesive Emberdrift house style.
   ```

3. Gather one or two style-reference images that capture the look (your own best piece from Labs 3–5 is the safest reference). You will use these to keep future generations on-style; note how your tool accepts a reference (Midjourney --sref or image prompt; Firefly/Stable Diffusion style or reference image).
4. Now work composition. Pick a scene (for example Wren arriving at the sky-port) and thumbnail several framings quickly — vary only the shot and aspect ratio. Paste the thumbnail prompt below and generate a few.

   ```bash
   Wren arriving at the floating lantern sky-port, thumbnail compositions: (1) wide low-angle establishing shot, (2) over-the-shoulder from behind Wren looking at the port, (3) tight close-up of Wren with the port bokeh behind; rule of thirds, clear focal point, house style appended, --ar 16:9.
   ```

5. Compare the thumbnails for storytelling and focal point. Pick the strongest composition and note why it works (leading lines, figure placement, contrast). Upscale/select it as your chosen framing.
6. Re-generate your weakest earlier piece (from Labs 3–5) with the locked house-style phrase and, if your tool supports it, the style reference — and confirm it now sits consistently with the rest of the pack.
7. Save your house-style phrase, your style-reference image(s) and the composition thumbnails into your Emberdrift folder. Note one line on the house style so you can reuse it on every future piece.

**Test it**

You have written and tested a repeatable Emberdrift house-style phrase, gathered a style reference, thumbnailed several compositions and chosen the strongest with clear reasons, and brought your weakest earlier piece back on-style — so the whole pack now reads as one world.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 7 — Iterate and Refine Artwork

Learning outcome: Take one chosen piece and refine it with variations, reused seeds, image-to-image and style/character references until it matches your intent and stays consistent..

Goal: Great concept art is converged on, not stumbled into. In this lab you take one chosen piece — the best candidate for your final key art, for example Wren at the sky-port — and refine it deliberately. You generate variations of it to explore near neighbours, reuse its seed for reproducible control, and make small single-change prompt edits so you steer rather than restart. You use image-to-image (feeding the chosen image back in) and a character/style reference to keep Wren and the look consistent while you improve composition and detail. You end with a refined, near-final image that clearly matches your intent. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A refined, near-final key-art candidate, converged on through variations, a reused seed, small prompt edits, image-to-image and a character/style reference — consistent with the rest of the pack.   (Tools: Variations, seeds (reproducibility), single-change prompt edits, image-to-image (img2img), character/style references, upscale/select.)

**Step-by-step**

1. Choose the single image you most want as your final key art (for example Wren arriving at the sky-port, from Lab 6). Note its seed if your tool shows one (Midjourney: react to get the seed; Stable Diffusion: it is displayed; Firefly: use the same reference/settings).
2. Generate variations of that chosen image to explore near neighbours without starting over. Keep the ones that move it toward your intent, discard the rest.
3. Reuse the seed with a small single-change prompt edit so the change is controlled, not random — for example strengthen the focal point or fix the time of day. Paste the edited prompt below.

   ```bash
   Wren arriving at the floating lantern sky-port, push the warm lantern glow on Wren as the clear focal point, deepen the dusk sky, keep composition and character, house style appended, same seed, --ar 16:9.
   ```

4. Use image-to-image: feed the chosen image back in as the input with a modest strength, plus your prompt, so the tool improves it while keeping the composition. Compare against a from-scratch generation to feel the difference in control.
5. Add a character reference (your Wren hero concept from Lab 3) and/or a style reference (from Lab 6) so Wren and the look stay consistent through the iterations. Regenerate and confirm Wren still reads as the same character.
6. Do two or three more focused iterations, changing one thing each time (composition, lighting, a detail). Stop when the image clearly matches your intent — converging beats endless re-rolling.
7. Curate the single best refined image as your near-final key art and upscale/select it. Save it into your Emberdrift folder (for example 'keyart_refined.png') and note the seed and the final prompt so the result is reproducible.

**Test it**

You have taken one chosen piece and refined it with variations, a reused seed, small single-change prompt edits, image-to-image and a character/style reference, kept Wren and the look consistent, and saved a refined near-final key-art candidate with its seed and prompt recorded.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 8 — Edit and Enhance with Inpainting, Outpainting and Paint-Over

Learning outcome: Finish your key-art piece by fixing regions with inpainting, widening the frame with outpainting, upscaling for resolution, and adding a hand paint-over in your image editor..

Goal: AI images almost always need a human finish. In this lab you take your Lab 7 near-final key art and make it portfolio-ready. You use inpainting to regenerate any weak region (a distorted hand, an awkward lantern) while keeping the rest; outpainting to extend the canvas and improve the crop or widen the scene; and an AI upscaler to raise resolution and detail. Then you do the professional finish: a hand paint-over in your image editor — fixing anatomy and perspective, adjusting colour and value, and adding the small details that make the piece intentional and unmistakably yours. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A finished, portfolio-ready Emberdrift key-art piece — inpainted to fix weak regions, outpainted to improve the crop, upscaled for resolution, and hand painted over in your image editor.   (Tools: Inpainting (regenerate a selected region), outpainting (extend the canvas), AI upscaling, Photoshop/Firefly Generative Fill, an image editor with layers for the paint-over.)

**Step-by-step**

1. Open your Lab 7 near-final key art. Identify one or two weak regions to fix (a distorted hand, a muddy lantern, an awkward edge). These are your inpainting targets.
2. Inpaint each weak region: select just that area and regenerate it with a short prompt so it is fixed while the rest is untouched. (Firefly/Photoshop: select and use Generative Fill; Stable Diffusion tools: use inpaint; Midjourney: use Vary Region.) Paste an example inpaint prompt below.

   ```bash
   A correctly-drawn hand gripping the rope, matching the painterly style and warm lantern lighting.
   ```

3. Outpaint to improve the crop: extend the canvas on one or two sides so the composition breathes — for example add more sky above or more dock below. Confirm the extension blends seamlessly with the original.
4. Upscale the image with an AI upscaler to raise resolution and add detail for portfolio quality. Check the upscale did not introduce artefacts; re-inpaint any it created.
5. Bring the image into your editor (Photoshop, Krita or Photopea) on its own layer and do a hand paint-over: fix any remaining anatomy or perspective, adjust colour and value for a stronger read, and deepen the focal point.
6. Add the finishing details that make it yours: a few sharp highlights on the lanterns, atmospheric haze for depth, a subtle rim light on Wren. Keep your edits on separate layers so they stay adjustable.
7. Flatten a copy and export the finished key art at high resolution into your Emberdrift folder (for example 'keyart_final.png'). Note one line on what you fixed by hand versus what the AI generated — the finish is the artist's job.

**Test it**

You have finished your key-art piece by inpainting weak regions, outpainting to improve the crop, upscaling for resolution, and adding a hand paint-over in your image editor — and exported a portfolio-ready 'keyart_final' image, keeping your edit layers adjustable.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


### Lab 9 — Build and Present the Concept-Art Portfolio

Learning outcome: Curate the Emberdrift pieces into a presented concept-art portfolio, assemble and export it, and apply commercial-use and IP considerations before delivery..

Goal: One finished world, curated and presented responsibly. In this lab you bring the whole pack together. You curate the strongest pieces — the Wren character page, the sky-port environment, the prop asset sheet and the finished key art — and lay them out as a clean, presented portfolio with brief captions that show range and consistency. You export it in delivery formats and assemble a simple presentation (a PDF or a set of boards). Finally you apply the commercial-use and IP checks that make the work safe to share: your tool's licensing, avoiding trademarks and protected styles, and disclosing AI assistance. This completes the course pipeline end to end. BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, the connected project you assemble across all 9 labs.

**What you'll build**

A curated, presented Emberdrift concept-art portfolio — character, environment, props and key art with captions — exported as a PDF/board set, with a completed commercial-use and IP checklist.   (Tools: Curation, portfolio layout (character / environment / props / key art), captions, Export As (PNG/JPEG/PDF), a presentation editor, the commercial-use and IP checklist.)

**Step-by-step**

1. Gather your finished pieces into the Emberdrift folder: the Wren character page (hero + variations), the sky-port environment (wide + detail), the prop asset sheet, and the finished key art from Lab 8.
2. Curate ruthlessly: keep only the strongest, most on-style version of each. A tight portfolio of four excellent boards beats a loose pile — cut anything off-model or weak.
3. Lay out the portfolio: create clean boards (one per category) in your editor or a slide tool, each with a short caption naming the piece and the tool/technique used. Keep the house style consistent across the boards.

   ```bash
   Emberdrift — Concept Art Pack: 01 Character — Wren, sky-salvager; 02 Environment — the floating lantern sky-port at dusk; 03 Props — Wren's salvaging gear; 04 Key Art — Wren arrives at the sky-port.
   ```

4. Add a short title board with the game name, a one-line pitch, and your name/role as concept artist, so the portfolio presents as a coherent pack.
5. Export for delivery: export each board as high-resolution PNG/JPEG and assemble them into a single PDF portfolio. Keep your working files and edit layers in the folder too.
6. Run the commercial-use and IP checklist: confirm you did not prompt for any trademark, living artist or copyrighted character; note your tool's commercial terms (Firefly is commercial-safe and indemnified; check your Midjourney/Stable Diffusion plan and model licences); check any placed reference or photo licence; and record where you will disclose AI assistance.
7. Write a one-page read-me listing each board, its tool/technique and its format, plus the IP checklist result. Save the PDF portfolio and the read-me — this presented pack is your deliverable and the end-to-end result the course set out to build.

**Test it**

You have curated the Emberdrift pieces into a presented concept-art portfolio (character, environment, props, key art) with captions and a title board, exported it as a PDF/board set in delivery formats, and completed a commercial-use and IP checklist — a finished, responsibly-delivered concept-art pack.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only projects, images and references you are authorised to use. Do not prompt for a real company's trademark, a living artist's name or copyrighted characters, and do not upload confidential or copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather than real client material, and check the licensing and commercial-use terms of your chosen tool and of any reference image before you publish or sell a piece.

---


## Wrap-Up

You have taken one game — Emberdrift — through the entire concept-art pipeline in a single day, from a text prompt to a complete, portfolio-ready pitch pack generated with Midjourney, Stable Diffusion and Adobe Firefly and finished by hand.

**What you built**

- A strong, structured concept-art prompt and a reusable template that control subject, style, composition, shot, lighting and detail.
- A hero character with costume and expression variations, a key environment concept, and a clean prop asset sheet.
- A locked house style with composition thumbnails, so the whole pack reads as one world.
- Refined iterations (variations, seeds, image-to-image, references) and a finished key-art piece that you inpainted, outpainted, upscaled and painted over.
- A curated, captioned concept-art portfolio — a complete, commercially-considered pitch pack.

**What to do next**

- Rebuild the pack for a real, non-confidential project of your own from the same prompt template and brief structure.
- Extend the pack — add more characters, locations or a colour-script — reusing your saved prompts and house-style phrase.
- Keep your prompt sheet, style reference and export presets as reusable templates so future work follows the same clean pipeline.
- Always check the commercial-use terms of your tool and any reference, and disclose AI assistance where appropriate before you publish or sell.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild the pack from your prompt and brief alone, then curate, iterate and finish it without the step-by-step.
- Apply the pipeline to a real, non-confidential project or portfolio piece of your own.
- Review each lab's detailed steps in this guide and re-create the pack in your own tool.


## Glossary

- **Generative AI (text-to-image)** — AI models that create an image from a written description; the core technology behind every tool in this course.
- **Concept art** — Exploratory artwork made early in a project to communicate the look of a character, place or object to a team — the purpose of everything you make here.
- **Midjourney** — A generative-AI image tool known for a strong, painterly, art-directed look, run through Discord or its web app; uses parameters such as --ar and --stylize.
- **Stable Diffusion** — An open, highly controllable text-to-image model, run locally or via hosted UIs (Leonardo.Ai, DreamStudio); supports seeds, custom models, LoRAs and ControlNet.
- **Adobe Firefly** — Adobe's commercial-safe generative-AI model, available on the web and built into Photoshop as Generative Fill; trained for commercial use with IP indemnification.
- **Prompt** — The text instruction you give an image tool; a specific prompt naming subject, style, composition, shot, lighting and detail produces a far better result than a vague one.
- **Prompt modifiers / parameters** — Extra terms and tool settings — style words, quality terms, aspect ratio, stylize, seed — that steer how the image is generated.
- **Generate–review–refine loop** — The core generative workflow — prompt, review the grid of variations, then upscale, vary or re-prompt until the result is right.
- **Aspect ratio** — The width-to-height proportion of the image (for example 16:9 for a wide establishing shot, 2:3 for a character); set with --ar in Midjourney or the size control elsewhere.
- **Seed** — A number that fixes the random starting point of a generation, so reusing it reproduces or gently varies a specific image instead of a wholly new one.
- **Variations** — New images generated from a chosen result, keeping its overall idea while exploring small differences — the main way to iterate toward a final.
- **Image-to-image (img2img)** — Generating from an input image plus a prompt, so a sketch, photo or previous generation guides the composition or subject of the new image.
- **Style reference / character reference** — An image supplied to the tool so new generations adopt its look (style reference) or keep the same character (character reference), for consistency.
- **Character concept** — A design exploration of a character — silhouette, costume, expression — usually generated front-facing and then varied.
- **Environment concept** — A design exploration of a place or key location, controlled by location, time of day, weather, scale and shot.
- **Prop / asset sheet** — A clean layout of individual objects, gadgets or gear on a plain background, so each design reads clearly for the team.
- **Composition** — How elements are arranged in the frame; steered with aspect ratio, shot type, rule-of-thirds and focal-point words, and explored with thumbnails.
- **House style** — The consistent look locked across a project with a repeatable style phrase, reference images and a chosen model, so every piece feels like one world.
- **Inpainting** — Regenerating only a selected region of an image (fix a hand, change a helmet) while keeping the rest unchanged.
- **Outpainting** — Extending an image beyond its original edges to widen the scene or change the crop.
- **Upscaling** — Raising an image's resolution — often with an AI upscaler that also adds detail — for portfolio-quality output.
- **Generative Fill** — Photoshop's Firefly-powered feature that adds, removes or replaces content inside a selection from a prompt.
- **Paint-over** — A hand pass in an image editor over an AI image — fixing anatomy and perspective, adjusting colour and value, adding detail — that makes the piece intentional and yours.
- **Portfolio** — A curated, presented set of the strongest pieces (character, environment, props, key art) that shows a studio your range and consistency.
- **Commercial-safe / IP indemnification** — Terms describing whether a tool's output can be used commercially; Firefly is trained for commercial use and indemnified, while Midjourney and Stable Diffusion vary by plan and model.
- **Export (PNG / JPEG / PDF)** — Saving finished artwork in a delivery format — high-resolution PNG or JPEG for images, PDF for a presented portfolio.
