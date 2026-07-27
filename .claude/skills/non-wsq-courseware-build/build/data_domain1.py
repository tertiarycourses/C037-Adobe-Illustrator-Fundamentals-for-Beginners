"""
Domain 1 — Getting Started with Generative AI for Concept Art. Labs 1-5.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — the Emberdrift
concept-art pitch pack, for a fictional indie game about sky-salvagers exploring
floating islands above a sea of clouds — one stage further. Lab 1 gets you
oriented in the AI image tools and the generate–review–refine loop; Lab 2 builds
a strong, reusable concept-art prompt from the brief; Lab 3 generates the hero
character with variations; Lab 4 generates a key environment; Lab 5 generates a
prop asset sheet. A concept-art brief is supplied; use your own non-confidential
project instead wherever you prefer.
"""

SCENARIO = (
 "Emberdrift is a fictional indie adventure game from the (fictional) studio Northlight Studios. It is set on a "
 "world of floating islands drifting above an endless sea of clouds, where young sky-salvagers ride patched "
 "gliders between lantern-lit sky-ports, scavenging relic-tech from ruins that rise through the cloud sea. The "
 "look is painterly and cinematic: warm ember and amber lantern light against cool sky-blues and misty greys, "
 "hopeful and adventurous. Northlight needs a concept-art pitch pack to sell the game's world: a hero "
 "character (Wren, a young sky-salvager), a key environment (a floating lantern sky-port at dusk), a prop set "
 "(Wren's salvaging gear), a locked house style, and a finished key-art piece. You are the concept artist, and "
 "across this course you take Emberdrift from a text prompt all the way to a portfolio-ready pack. Use this "
 "scenario only if you cannot use a real, non-confidential project of your own; your own project is always "
 "welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Emberdrift concept-art pack, "
 "the connected project you assemble across all 9 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Get Started with Generative AI Image Tools",
 objective="Sign in to your AI image generator, run your first generations, compare Midjourney, Stable Diffusion and Firefly, and learn the generate–review–refine loop that every later lab uses.",
 desc="This lab gets you comfortable with the tools before any real concept-art work begins. You sign in to "
 "your chosen AI image generator (Midjourney, a Stable Diffusion tool such as Leonardo.Ai, or Adobe Firefly), "
 "confirm your image editor is ready, and run a simple generation. You learn to read the grid of variations "
 "the tool returns, upscale or select the strongest, and re-prompt or vary it. You try the same idea in a "
 "second tool if you have access, and note how Midjourney, Stable Diffusion and Firefly differ in look, "
 "control and commercial terms. By the end you understand the describe -> generate -> review -> refine loop "
 "that is the heart of generative concept art. " + PROJECT_NOTE,
 build="A project folder with your first AI-generated images, produced from more than one prompt, with the strongest variation selected/upscaled — plus a clear understanding of your tool's interface and the generate–review–refine loop.",
 services="Midjourney / Stable Diffusion tool (e.g. Leonardo.Ai) / Adobe Firefly, sign-in and credits, prompt field, the grid of variations, upscale/select, aspect-ratio and basic parameters, an image editor",
 steps=[
 ("Create a project folder on your machine called 'Emberdrift' so every image you make today stays together. Sign in to your chosen AI image generator (Midjourney in Discord or the web app, a Stable Diffusion tool such as Leonardo.Ai, or Adobe Firefly) and confirm you have credits/generations available.", ""),
 ("Run a simple first generation so you can see how the tool works. Type the prompt below and generate. (In Midjourney use /imagine; in a Stable Diffusion tool or Firefly, type it into the prompt box.)",
  "A young explorer standing on a floating island above a sea of clouds, warm lantern light, painterly concept art, cinematic."),
 ("Wait for the tool to return a grid of variations. Review them and pick the strongest. Upscale or select it (Midjourney U1–U4; other tools have an upscale/download button). Notice this is one full turn of the loop.", ""),
 ("Make a small change and regenerate to feel how prompts steer the result — for example add a time of day or a mood word — and compare. Paste the changed prompt below.",
  "A young explorer standing on a floating island above a sea of clouds at dusk, warm amber lantern light, misty blue sky, painterly concept art, cinematic, hopeful mood."),
 ("Set an aspect ratio to change the framing: try a wide establishing shot. (Midjourney: add --ar 16:9; other tools: choose a 16:9 or landscape size.) Regenerate and see how the composition changes with the frame.", ""),
 ("If you have access to a second tool, run the same prompt in it and compare — note how Midjourney, Stable Diffusion and Firefly differ in look, how much control each gives, and their commercial terms. If you only have one tool, note its strengths for concept art.", ""),
 ("Save two or three of your best images into your Emberdrift folder. Write one line, in your own words, describing what the generate–review–refine loop is and where your tool's prompt field, variation grid and upscale/aspect-ratio controls live — you rely on all of them in every later lab.", ""),
 ],
 test="You have run more than one generation in your AI image tool, reviewed the grid of variations, selected/upscaled the strongest, changed the prompt and the aspect ratio to see how each steers the result, and saved your best images in your Emberdrift folder — with a clear understanding of the generate–review–refine loop.",
 ),
 dict(
 num=2, topic=1,
 title="Write Effective Prompts for Concept Art",
 objective="Turn the supplied Emberdrift brief into a strong, structured prompt that controls subject, style, composition, shot, lighting and detail, and save it as a reusable template.",
 desc="A good concept-art image starts with a good prompt, not a lucky one. In this lab you read the supplied "
 "Emberdrift brief and shape it into a structured prompt with clear parts: the subject, the style/medium "
 "(painterly concept art, digital painting), the composition and shot (wide establishing, close-up, low "
 "angle), the lighting and mood (warm amber lantern light, cool misty sky), the level of detail, and words to "
 "steer colour. You run small, single-change edits to see how each part moves the result, then save your best "
 "version as a reusable template with clearly marked slots you will reuse for the rest of the project. " + PROJECT_NOTE,
 build="A structured Emberdrift prompt (subject, style, composition/shot, lighting/mood, detail, colour) plus a reusable prompt template with marked slots, saved in your project folder.",
 services="Your image tool's prompt field, the supplied Emberdrift brief, a structured prompt template, style/composition/lighting keywords, aspect-ratio and stylize parameters",
 steps=[
 ("Open the supplied brief (labs/reference-pack/): the world brief, the style notes and the reference-image guide. Skim all three so you know the look you are describing — painterly, warm ember lantern light against cool misty blues, hopeful and cinematic.", ""),
 ("Write a first structured prompt that names the subject and its style/medium, and generate. Paste the prompt below.",
  "A lone sky-salvager on a drifting island, painterly digital concept art, cinematic, in the style of a game key art illustration."),
 ("Add composition and shot guidance and regenerate. Notice how the framing tightens while the subject stays. This shows composition words steer the shot independently of the subject.",
  "Same lone sky-salvager, wide establishing shot, low angle looking up, rule of thirds, the figure small against a vast cloud sea, --ar 16:9."),
 ("Add lighting, mood and a level-of-detail instruction, then regenerate.",
  "Warm amber lantern light rimming the figure, cool misty blue sky, golden-hour glow, atmospheric depth, highly detailed painterly rendering, hopeful and adventurous mood."),
 ("Run two or three more small, single-change edits to feel how each part matters — for example change 'wide establishing shot' to 'close-up portrait', or 'golden-hour' to 'stormy overcast' — and note which direction you prefer for Emberdrift.", ""),
 ("Combine your best choices into one clean prompt. Then ask yourself the prompting rule: does it name the subject, the style, the composition/shot, the lighting/mood, the detail level and the colour, and does it set an aspect ratio? Fill any gap.", ""),
 ("Save two things in your Emberdrift folder: your final Emberdrift prompt, and a reusable template version with clearly marked slots — [SUBJECT], [STYLE/MEDIUM], [COMPOSITION/SHOT], [LIGHTING/MOOD], [DETAIL], [COLOUR], [PARAMETERS] — that you can reuse for any future piece.", ""),
 ],
 test="You have a structured Emberdrift prompt that explicitly controls subject, style, composition/shot, lighting/mood, level of detail and colour (with an aspect ratio set), and you have saved a reusable prompt template with clearly marked slots in your project folder.",
 ),
 dict(
 num=3, topic=1,
 title="Generate Character Concepts",
 objective="Use your prompt to generate the Emberdrift hero character (Wren) with a consistent design, then explore costume, pose and expression variations and curate the strongest.",
 desc="With a strong prompt in hand you can generate the first real piece of the pack: the hero character. In "
 "this lab you adapt your Lab 2 prompt to describe Wren — a young sky-salvager — with a clear role, silhouette, "
 "costume and personality, and generate front-facing character concepts. You then explore variations: "
 "different costumes, poses and expressions, keeping the character recognisable across them. You curate the "
 "single strongest, most on-brief design as Wren's hero concept, and keep a couple of variations that show the "
 "character's range. These become the character page of your pack. " + PROJECT_NOTE,
 build="A curated Emberdrift hero-character concept (Wren) plus a few costume/expression variations that keep the character recognisable, saved as the character page of your pack.",
 services="Your image tool's prompt field, character-description prompting (role, silhouette, costume, expression), variations, aspect ratio for a character shot, upscale/select, curating the best",
 steps=[
 ("In your image tool, adapt your Lab 2 template to describe Wren clearly: role, age, silhouette, costume and personality. Set a character-friendly aspect ratio (a portrait/full-body ratio such as 2:3). Paste the prompt below and generate.",
  "Full-body character concept of Wren, a determined teenage sky-salvager, wiry and agile, wearing a patched leather flight coat, goggles pushed up on the forehead, a coil of rope and salvage tools at the belt, worn boots; painterly game concept art, neutral studio background, front view, warm key light, --ar 2:3."),
 ("Review the grid and pick the strongest, clearest design. Upscale/select it. This is your candidate hero concept for Wren — a single, readable character silhouette.", ""),
 ("Explore costume and gear variations, changing only wardrobe words so the character stays recognisable. Generate a couple. Paste the variation prompt below.",
  "Same character Wren, same face and build, alternative outfit: a lighter summer flight vest and rolled sleeves; then a heavier storm cloak with a hood; keep the goggles and salvage tools, painterly game concept art, front view, --ar 2:3."),
 ("Explore expression and pose variations — for example a confident grin, a wary glance, a mid-action leap — so the character sheet shows personality and range. Generate one or two.",
  "Same character Wren, three expressions: a confident grin, a wary sideways glance, and a determined shout mid-leap; consistent design and costume, painterly game concept art, --ar 3:2."),
 ("Curate: choose the single strongest, most on-brief design as Wren's hero concept, and keep two variations that best show the character's range. Discard the rest so your folder stays clean.", ""),
 ("Check consistency across the kept images: same face, build, costume language and feel. If one variation drifts off-model, note what changed (the tool re-invented the face or costume) — you fix consistency properly with references in Lab 7.", ""),
 ("Save the hero concept and the two variations into your Emberdrift folder as the character page (for example 'wren_hero.png' plus 'wren_var1.png', 'wren_var2.png'). Note one line on what makes Wren's silhouette read as one character.", ""),
 ],
 test="You have generated a hero-character concept for Wren from a structured prompt, explored costume/pose/expression variations that keep the character recognisable, curated the single strongest design plus two range-showing variations, and saved them as the character page of your Emberdrift pack.",
 ),
 dict(
 num=4, topic=1,
 title="Generate Environment Concepts",
 objective="Generate the Emberdrift key environment — a floating lantern sky-port at dusk — controlling place, time of day, mood, scale and shot, and curate the strongest establishing image.",
 desc="Every game world needs a place that sells it. In this lab you generate Emberdrift's key location: a "
 "floating lantern sky-port at dusk, where salvagers dock their gliders. You adapt your prompt to describe an "
 "environment, not a character — naming the location, the time of day, the weather, the scale and a key "
 "landmark — and set a wide establishing aspect ratio. You generate several compositions, push the mood with "
 "lighting words, and curate the single strongest establishing shot. You also generate one closer 'detail' "
 "view of the same place so the location reads at two scales. These become the environment page of your pack. " + PROJECT_NOTE,
 build="A curated Emberdrift environment concept — a wide establishing shot of the floating lantern sky-port at dusk — plus one closer detail view of the same location, saved as the environment page of your pack.",
 services="Your image tool's prompt field, environment prompting (location, time of day, weather, scale, landmark), wide aspect ratios, atmospheric lighting words, variations and curating",
 steps=[
 ("Adapt your prompt template to describe a place rather than a person. Name the location, time of day, weather, scale and a key landmark, and set a wide establishing aspect ratio. Paste the prompt below and generate.",
  "Wide establishing shot of a floating lantern sky-port at dusk, wooden docks and rope bridges strung between drifting islands above a sea of clouds, patched gliders moored, hundreds of warm lanterns glowing, a tall salvage-crane landmark, painterly game concept art, atmospheric depth, cinematic, --ar 16:9."),
 ("Review the grid and pick the composition with the clearest focal point and the strongest sense of place and scale. Upscale/select it as your candidate establishing shot.", ""),
 ("Push the mood: regenerate with stronger lighting and atmosphere words to make dusk feel warm and inviting against the cool sky. Compare with your first pick.",
  "Same floating lantern sky-port, deeper dusk, warm amber lantern glow reflecting off mist, cool blue shadows, volumetric light, drifting fog between the islands, hopeful and adventurous, --ar 16:9."),
 ("Generate a closer 'detail' view of the same place so the location reads at two scales — for example one dock with a moored glider and a salvager silhouette. Keep the same style and palette.",
  "Closer view of one dock at the Emberdrift sky-port, a moored patched glider and a small salvager silhouette beside a glowing lantern, ropes and crates, warm amber light, cool misty background, painterly game concept art, --ar 3:2."),
 ("Curate: keep the single strongest wide establishing shot and the best detail view, and discard the rest. Check both clearly belong to the same place and the same time of day.", ""),
 ("Check consistency with Wren's character page from Lab 3: same painterly medium, same warm-lantern-against-cool-sky palette, same mood. Note any drift to fix when you lock the house style in Lab 6.", ""),
 ("Save the establishing shot and the detail view into your Emberdrift folder as the environment page (for example 'skyport_wide.png' and 'skyport_detail.png'). Note one line on what gives the location its sense of scale.", ""),
 ],
 test="You have generated a wide establishing environment concept of the floating lantern sky-port at dusk and a closer detail view of the same location, controlled place, time of day, mood, scale and shot, curated the strongest of each, and saved them as the environment page of your Emberdrift pack.",
 ),
 dict(
 num=5, topic=1,
 title="Generate a Prop and Asset Sheet",
 objective="Generate Wren's salvaging gear as individual props on clean backgrounds and assemble them into a coherent asset sheet that matches the pack's style.",
 desc="A game world is made of objects, and props must read clearly on their own. In this lab you generate "
 "Wren's salvaging gear — a grappling lantern-hook, a brass wind-compass, and goggles — as individual props, "
 "each on a plain, uncluttered background so the design reads for the team. You use consistent style and "
 "lighting words across all three so they look like one set, generate variations of each, curate the "
 "strongest, and assemble them into a single clean asset sheet. This completes the Topic 1 hands-on and gives "
 "your pack its prop page. " + PROJECT_NOTE,
 build="A coherent Emberdrift prop asset sheet — a grappling lantern-hook, a brass wind-compass and goggles, each generated on a clean background in a consistent style and assembled into one sheet.",
 services="Your image tool's prompt field, prop/asset prompting (single object, plain background), consistent style/lighting words, variations, curating, an image editor to assemble the sheet",
 steps=[
 ("Generate the first prop on a plain background so the design reads clearly. Name a single object, the material, and a neutral studio setup. Paste the prompt below and generate.",
  "Concept art of a single prop: a salvager's grappling lantern-hook — a brass hook with a small glowing lantern housing and a coiled rope — worn and functional, three-quarter view, plain light-grey studio background, soft even lighting, painterly game concept art, --ar 1:1."),
 ("Generate the other two props the same way, reusing the exact same style, background and lighting words so the set looks consistent — change only the object.",
  "Same style and plain studio background: a brass wind-compass with a spinning vane and a small pressure dial; then a pair of leather-and-brass flight goggles with amber-tinted lenses; worn and functional, painterly game concept art, --ar 1:1."),
 ("For each prop, review the grid, generate a variation or two if the shape is unclear, and curate the single clearest, most on-brief version. Aim for props that would read on a plain sheet at a glance.", ""),
 ("Check the three props read as one set: same painterly style, same soft studio lighting, same worn brass-and-leather material language, same warm palette as the rest of the pack. Regenerate any outlier.", ""),
 ("Assemble the asset sheet: open your image editor, place the three curated props on one clean canvas with even spacing and a simple label under each (Lantern-Hook, Wind-Compass, Goggles). Keep the background plain.", ""),
 ("Do a consistency pass across Labs 3–5: character, environment and props should share the same medium, palette and mood. Note any drift for the house-style lock in Lab 6.", ""),
 ("Save the individual props and the assembled sheet into your Emberdrift folder as the prop page (for example 'prop_lanternhook.png', 'prop_compass.png', 'prop_goggles.png' and 'prop_sheet.png'). Note one line on what keeps the three props reading as one set.", ""),
 ],
 test="You have generated three of Wren's props — a grappling lantern-hook, a wind-compass and goggles — each on a clean background in a consistent style, curated the strongest of each, and assembled them into one coherent asset sheet saved as the prop page of your Emberdrift pack.",
 ),
]
