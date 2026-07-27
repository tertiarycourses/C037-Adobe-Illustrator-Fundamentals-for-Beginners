"""
SINGLE SOURCE OF TRUTH — C037 Generative AI for Concept Art (non-WSQ).

An intensive, one-day, hands-on course on using generative-AI image tools —
Midjourney, Stable Diffusion and Adobe Firefly — to create professional concept
art: characters, environments and props. Learners craft effective prompts,
generate and curate artwork, develop a consistent visual style and strong
compositions, then iterate, edit, enhance and paint over the results into
portfolio-ready pieces. Every artifact (PPT, LP, LG, LG.md) and every lab is
generated from this module + data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C037.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Concept Art (C037)"
SHORT_TITLE  = "Generative AI for Concept Art (C037)"   # used in output filenames
COURSE_CODE  = "C037"                                    # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how generative-AI image tools create concept art, compare Midjourney, Stable Diffusion and Adobe Firefly, and navigate the generate–review–refine loop.",
    "LO2: Write effective, structured prompts that control the subject, style, composition, shot, lighting and level of detail of generated concept art.",
    "LO3: Generate consistent character concepts — a hero character with costume and expression variations — from a written brief.",
    "LO4: Generate environment and key-location concepts, controlling place, time of day, mood, scale and shot.",
    "LO5: Generate props, assets and gadgets as a clean, coherent asset sheet.",
    "LO6: Develop a consistent visual style and strong compositions so a set of concept art reads as one world.",
    "LO7: Iterate and refine artwork using variations, seeds, image-to-image and style/character references.",
    "LO8: Edit and enhance concept art with inpainting, outpainting, upscaling and a hand paint-over finish.",
    "LO9: Assemble and present a concept-art portfolio, and apply commercial-use and IP considerations.",
]
LO_TITLES = [
    "Tools & the loop",
    "Prompting for art",
    "Character concepts",
    "Environment concepts",
    "Prop & asset sets",
    "Style & composition",
    "Iterate & refine",
    "Edit & enhance",
    "Portfolio & delivery",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Generative AI for Concept Art",
         subtitle="Introduction to generative AI for art · Popular AI image tools (Midjourney, Stable Diffusion, Firefly) · Writing effective prompts for concept art · Generating characters, environments and props",
         weighting="55%",
         concepts=[
            "Generative AI for art — text-to-image models turn a written description into a finished image in seconds; for concept art they let one artist explore dozens of characters, worlds and props in the time a single painting used to take.",
            "What concept art is for — concept art is exploration and communication, not final art: it sells a look, a character or a place to a team early, so generative AI's speed at producing many options fits the job perfectly.",
            "Popular AI image tools — Midjourney (a strong, painterly, art-directed look, run in Discord or the web app), Stable Diffusion (open and highly controllable, run locally or through hosted UIs such as Leonardo.Ai or DreamStudio) and Adobe Firefly (commercial-safe and built into Photoshop) are the three you meet in this course.",
            "Choosing a tool — they share the same prompt-driven idea but differ: Midjourney for fast, beautiful results, Stable Diffusion for control and reproducibility (seeds, models, ControlNet), Firefly for commercial-safe output and in-editor editing; you pick by the job.",
            "The generate–review–refine loop — you write a prompt, the tool returns a grid of variations, you review and pick the strongest, then upscale, vary or re-prompt; this loop is the heart of every generative task.",
            "Prompt-writing for concept art — a strong prompt names the subject, the style or medium, the composition and shot, the lighting and mood, and the level of detail; concrete, art-directed wording beats a vague sentence.",
            "Prompt structure and modifiers — subject + descriptors + style reference + camera/shot + lighting + quality terms, plus tool-specific parameters (aspect ratio, stylize, seed) that steer the result.",
            "Generating characters — you describe who the character is (role, age, silhouette, costume, personality) and generate front-facing character concepts, then explore variations of costume, pose and expression.",
            "Generating environments — you describe a place (location, time of day, weather, scale, key landmark) and the shot (wide establishing, aspect ratio) to generate environment and key-location concepts.",
            "Generating props — you generate individual objects, gadgets and gear, often as a clean asset sheet on a plain background so each design reads clearly for the team.",
         ]),
    dict(num=2, code="02",
         title="Creating and Refining Concept Art with AI",
         subtitle="Developing styles and compositions · Iterating and refining artwork · Editing and enhancing with AI · Building a concept art portfolio",
         weighting="45%",
         concepts=[
            "Developing a consistent style — concept art for one project must feel like one world; you lock a house style with a repeatable style phrase, reference images and (in Stable Diffusion) a chosen model or LoRA, so every piece matches.",
            "Composition and shot — strong concept art is well composed; you steer it with aspect ratio, shot type (wide establishing, close-up, low angle), rule-of-thirds and focal-point words, and you thumbnail several compositions before committing.",
            "Iterating with variations and seeds — you refine by generating variations of a chosen image, reusing a seed for reproducibility, and making small single-change prompt edits so you converge on the intended result instead of starting over.",
            "Image-to-image and references — feeding an existing image (a sketch, a photo, a previous generation) back in with image-to-image, or supplying a style or character reference, keeps the subject or look consistent while you change other things.",
            "Editing with inpainting and outpainting — inpainting regenerates a selected region (fix a hand, change a helmet) while keeping the rest; outpainting extends the canvas to widen a scene or change the crop.",
            "Enhancing and upscaling — AI upscalers raise resolution and add detail for portfolio-quality output, and generative-fill editors (Photoshop or Firefly) add or remove elements cleanly.",
            "Paint-over and finishing — the professional finish is a hand paint-over: you take the AI image into an editor, fix anatomy and perspective, adjust colour and value, and add the details that make the piece intentional and yours.",
            "Building a concept-art portfolio — you curate the strongest pieces, present them cleanly (character, environment, props, key art) with brief captions, and show the range and consistency a studio looks for.",
            "Commercial use and IP — the tools differ on commercial terms (Firefly is trained for commercial safety and indemnified, while Midjourney and Stable Diffusion vary by plan and model); you avoid prompting for trademarks, living artists' names and copyrighted characters, check licences, and disclose AI use where appropriate.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Build a complete concept-art pitch pack for Emberdrift — a hero character, a key environment, a prop set, a locked house style and a finished key-art piece — by generating with Midjourney, Stable Diffusion and Adobe Firefly, then refining with variations, image-to-image, inpainting, upscaling and a hand paint-over into a portfolio-ready, commercially-considered set",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The day totals exactly 480 scheduled minutes
# (excluding the 1-hour lunch); the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction, ground rules, and setup: signing in to your AI image generator (Midjourney, a Stable Diffusion tool such as Leonardo.Ai, or Adobe Firefly) and confirming your image editor with generative fill is ready for the labs"),
        ("9:20","10:05",45,"topic","TOPIC 01 — Getting Started with Generative AI for Concept Art: introduction to generative AI for art; popular AI image tools (Midjourney, Stable Diffusion, Firefly); writing effective prompts for concept art; generating characters, environments and props (concepts + live demo)"),
        ("10:05","10:45",40,"lab","Hands-on: "+lab_titles([1])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([2,3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"lab","Hands-on: "+lab_titles([5])),
        ("14:30","15:00",30,"topic","TOPIC 02 — Creating and Refining Concept Art with AI: developing styles and compositions; iterating and refining artwork; editing and enhancing with AI; building a concept art portfolio (concepts + live demo)"),
        ("15:00","16:15",75,"lab","Hands-on: "+lab_titles([6,7])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","17:50",80,"lab","Hands-on: "+lab_titles([8,9])),
        ("17:50","18:00",10,"recap","Course wrap-up, assembling and presenting the concept-art portfolio, commercial-use and IP considerations, and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI for Concept Art Really Is",
    concepts=[
        "From prompt to picture — you describe a character, place or object in words and the tool paints a finished image in seconds, so you explore many ideas fast.",
        "Exploration, not final art — concept art's job is to communicate a look early; generative AI's speed at producing options is exactly what that job needs.",
        "Three tools, one idea — Midjourney, Stable Diffusion and Firefly all turn prompts into images, but each trades beauty, control and commercial-safety differently.",
        "AI drafts, the artist finishes — the tool gives a strong first image; you curate, iterate, edit and paint over it to make it consistent, correct and yours.",
    ],
    framework_title="The Concept-Art Generation Pipeline",
    framework=[
        ("Prompt", "Describe the subject, style, composition, shot, lighting and detail — or supply a reference — so the tool generates the image you intend."),
        ("Generate", "Midjourney, Stable Diffusion or Firefly returns a grid of variations you preview and compare."),
        ("Curate", "Choose the strongest, most on-brief variation and discard the rest — good taste in selecting is half the craft."),
        ("Refine", "Iterate with variations, seeds, image-to-image and references, then inpaint, outpaint, upscale and paint over to finish."),
        ("Present", "Curate the pieces into a portfolio, present them cleanly, and check commercial-use and IP terms before you publish."),
    ],
    statement=dict(
        headline="Generative AI gives you a striking first image in seconds — the craft is prompting well, curating with taste, and refining it into a consistent, finished, commercially-considered concept-art set.",
        body="This course is hands-on: you take one game — Emberdrift, a fictional sky-exploration adventure — from a text prompt all the way to a concept-art pitch pack of a hero character, a key environment, a prop set, a locked house style and finished key art, generated with Midjourney, Stable Diffusion and Firefly and finished by hand.",
        kicker="THE PIPELINE RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A strong prompt system", ["A structured concept-art prompt", "A reusable prompt template", "A locked house-style phrase"]),
        ("The core concepts", ["A hero character with variations", "A key environment / location", "A clean prop asset sheet"]),
        ("Refined artwork", ["Iterations via variations & seeds", "Image-to-image & reference control", "Inpainted, outpainted, upscaled art"]),
        ("A portfolio-ready pack", ["A hand painted-over key-art piece", "A curated, captioned portfolio", "An IP-checked, delivered pack"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the technique on the shared Emberdrift game example.",
        "You build it yourself in your own tool using the supplied concept-art brief.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You refine the result — regenerate, iterate or edit by hand — until it meets the brief.",
        "You keep the finished image — it becomes the next piece of your Emberdrift concept-art pack.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Concept Art (C037) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 9 hands-on labs, in the order you "
    "will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — the Emberdrift concept-art pitch pack, for a fictional "
    "indie game about sky-salvagers exploring floating islands above a sea of clouds. You start in Lab 1 by "
    "getting oriented in the AI image tools, then in every lab you take the pack one stage further — a strong "
    "structured prompt, a hero character with variations, a key environment, a prop asset sheet, a locked house "
    "style with composition thumbnails, refined iterations, an inpainted-outpainted-upscaled-and-painted-over "
    "key-art piece, and finally a curated, presented portfolio. A concept-art brief is supplied; you may "
    "substitute your own non-confidential project wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) able to run a modern browser smoothly — a reasonably recent machine with 8 GB RAM minimum, 16 GB preferred.",
        "Access to at least one AI image generator: Midjourney (a paid plan, run in Discord or the web app), a Stable Diffusion tool (a hosted UI such as Leonardo.Ai or DreamStudio, or a local install), or Adobe Firefly (web, or built into Photoshop). The trainer will confirm which tool the class uses at the start of the day.",
        "An image editor with generative fill and layers for editing and paint-over — Adobe Photoshop (with Generative Fill) is ideal; the free Krita or the browser-based Photopea also work.",
        "An internet connection (the generative tools run in the cloud), a modern browser, and about 1 GB of free disk space for your generated images and exports.",
        "The supplied Emberdrift concept-art brief (world, characters, props and a reference-image guide in labs/reference-pack/) — or a few notes and a reference image of your own non-confidential project to use instead.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to your chosen AI image generator and run one test generation, and that your image editor opens and can create a new layered document. If anything is missing, tell the trainer.",
    verify_code="Sign in to your AI image tool (Midjourney / Stable Diffusion tool / Adobe Firefly)  ·  run one test image  ·  open your image editor (Photoshop / Krita / Photopea) and create a new document",
    conventions=[
        "Placeholders such as <YOUR PROJECT> or <YOUR REFERENCE IMAGE> are replaced with your own values.",
        "Prompts to type into the image generator are shown in the 'Text to use' blocks — adapt them to your own project and tool (Midjourney uses --ar and --seed; Stable Diffusion and Firefly have equivalent aspect-ratio and seed controls).",
        "Every lab ends with a 'Test it' step — an explicit check that the result meets the brief before you move on.",
        "Keep every image for the project in a single folder (Emberdrift) so your pack stays together and consistent.",
    ],
)
LAB_NOTE = (
    "Use only projects, images and references you are authorised to use. Do not prompt for a real company's "
    "trademark, a living artist's name or copyrighted characters, and do not upload confidential or "
    "copyrighted reference material without permission. Use the supplied Emberdrift concept-art brief rather "
    "than real client material, and check the licensing and commercial-use terms of your chosen tool and of "
    "any reference image before you publish or sell a piece."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one game — Emberdrift — through the entire concept-art pipeline in a single day, from a text prompt to a complete, portfolio-ready pitch pack generated with Midjourney, Stable Diffusion and Adobe Firefly and finished by hand.",
    sections=[
        dict(title="What you built", bullets=[
            "A strong, structured concept-art prompt and a reusable template that control subject, style, composition, shot, lighting and detail.",
            "A hero character with costume and expression variations, a key environment concept, and a clean prop asset sheet.",
            "A locked house style with composition thumbnails, so the whole pack reads as one world.",
            "Refined iterations (variations, seeds, image-to-image, references) and a finished key-art piece that you inpainted, outpainted, upscaled and painted over.",
            "A curated, captioned concept-art portfolio — a complete, commercially-considered pitch pack.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild the pack for a real, non-confidential project of your own from the same prompt template and brief structure.",
            "Extend the pack — add more characters, locations or a colour-script — reusing your saved prompts and house-style phrase.",
            "Keep your prompt sheet, style reference and export presets as reusable templates so future work follows the same clean pipeline.",
            "Always check the commercial-use terms of your tool and any reference, and disclose AI assistance where appropriate before you publish or sell.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the pack from your prompt and brief alone, then curate, iterate and finish it without the step-by-step.",
    "Apply the pipeline to a real, non-confidential project or portfolio piece of your own.",
    "Review each lab's detailed steps in this guide and re-create the pack in your own tool.",
]
LG_GLOSSARY = [
    ("Generative AI (text-to-image)", "AI models that create an image from a written description; the core technology behind every tool in this course."),
    ("Concept art", "Exploratory artwork made early in a project to communicate the look of a character, place or object to a team — the purpose of everything you make here."),
    ("Midjourney", "A generative-AI image tool known for a strong, painterly, art-directed look, run through Discord or its web app; uses parameters such as --ar and --stylize."),
    ("Stable Diffusion", "An open, highly controllable text-to-image model, run locally or via hosted UIs (Leonardo.Ai, DreamStudio); supports seeds, custom models, LoRAs and ControlNet."),
    ("Adobe Firefly", "Adobe's commercial-safe generative-AI model, available on the web and built into Photoshop as Generative Fill; trained for commercial use with IP indemnification."),
    ("Prompt", "The text instruction you give an image tool; a specific prompt naming subject, style, composition, shot, lighting and detail produces a far better result than a vague one."),
    ("Prompt modifiers / parameters", "Extra terms and tool settings — style words, quality terms, aspect ratio, stylize, seed — that steer how the image is generated."),
    ("Generate–review–refine loop", "The core generative workflow — prompt, review the grid of variations, then upscale, vary or re-prompt until the result is right."),
    ("Aspect ratio", "The width-to-height proportion of the image (for example 16:9 for a wide establishing shot, 2:3 for a character); set with --ar in Midjourney or the size control elsewhere."),
    ("Seed", "A number that fixes the random starting point of a generation, so reusing it reproduces or gently varies a specific image instead of a wholly new one."),
    ("Variations", "New images generated from a chosen result, keeping its overall idea while exploring small differences — the main way to iterate toward a final."),
    ("Image-to-image (img2img)", "Generating from an input image plus a prompt, so a sketch, photo or previous generation guides the composition or subject of the new image."),
    ("Style reference / character reference", "An image supplied to the tool so new generations adopt its look (style reference) or keep the same character (character reference), for consistency."),
    ("Character concept", "A design exploration of a character — silhouette, costume, expression — usually generated front-facing and then varied."),
    ("Environment concept", "A design exploration of a place or key location, controlled by location, time of day, weather, scale and shot."),
    ("Prop / asset sheet", "A clean layout of individual objects, gadgets or gear on a plain background, so each design reads clearly for the team."),
    ("Composition", "How elements are arranged in the frame; steered with aspect ratio, shot type, rule-of-thirds and focal-point words, and explored with thumbnails."),
    ("House style", "The consistent look locked across a project with a repeatable style phrase, reference images and a chosen model, so every piece feels like one world."),
    ("Inpainting", "Regenerating only a selected region of an image (fix a hand, change a helmet) while keeping the rest unchanged."),
    ("Outpainting", "Extending an image beyond its original edges to widen the scene or change the crop."),
    ("Upscaling", "Raising an image's resolution — often with an AI upscaler that also adds detail — for portfolio-quality output."),
    ("Generative Fill", "Photoshop's Firefly-powered feature that adds, removes or replaces content inside a selection from a prompt."),
    ("Paint-over", "A hand pass in an image editor over an AI image — fixing anatomy and perspective, adjusting colour and value, adding detail — that makes the piece intentional and yours."),
    ("Portfolio", "A curated, presented set of the strongest pieces (character, environment, props, key art) that shows a studio your range and consistency."),
    ("Commercial-safe / IP indemnification", "Terms describing whether a tool's output can be used commercially; Firefly is trained for commercial use and indemnified, while Midjourney and Stable Diffusion vary by plan and model."),
    ("Export (PNG / JPEG / PDF)", "Saving finished artwork in a delivery format — high-resolution PNG or JPEG for images, PDF for a presented portfolio."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C037 Generative AI for Concept Art courseware.", TRAINER),
]
