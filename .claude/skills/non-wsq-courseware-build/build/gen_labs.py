#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md, labs/README.md and refreshes nothing else
(tools.md and the brief pack are hand-authored). Enrichment sections
(Prerequisites, Troubleshooting, Challenge, Reflection, Deliverable) live in the
ENRICH table below, keyed by lab number.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ approx minutes per lab
# Derived from the schedule lab blocks so the labs match the Lesson Plan timing.
def lab_titles(nums):
    return "; ".join("" for _ in nums)


def approx_minutes():
    sched = C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums))
    mins = {}
    for _day, (_theme, rows) in sched.items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
    return mins


MINS = approx_minutes()

# ------------------------------------------------------------------ per-lab enrichment
ENRICH = {
 1: dict(
    prereqs=[
        "A laptop with a modern browser and an internet connection — the generative tools run in the cloud.",
        "Access to at least one AI image generator (Midjourney, a Stable Diffusion tool such as Leonardo.Ai, or Adobe Firefly), signed in with generations/credits available.",
        "An image editor with layers installed (Adobe Photoshop, or the free Krita or Photopea).",
    ],
    trouble=[
        "**Your tool returns nothing or errors.** Confirm you are signed in and have credits/generations left; Midjourney runs in a Discord server or the web app, Firefly on the web, hosted Stable Diffusion tools in the browser — check you are in the right place.",
        "**Generation is slow.** The tools queue at busy times — start a generation and read ahead; if credits are exhausted, ask the trainer about the class plan.",
        "**The result looks rough or generic.** That is expected for a first quick pass — you learn to steer it with a proper prompt in Lab 2. For now, just learn the loop and the interface.",
    ],
    challenge="Run the same prompt in a second tool (say Midjourney and Firefly) and compare the look, the control and the commercial terms side by side.",
    lo=1,
    deliverable="Keep your first saved images and your notes on the interface — it is your warm-up before you build the real concept-art pack across the next labs.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (you can generate, review and select an image).",
        "The supplied Emberdrift concept-art brief open (labs/reference-pack/).",
    ],
    trouble=[
        "**The tool ignores part of the prompt.** Put the most important element first and keep each part short; regenerate rather than piling on more words.",
        "**Style overrides the subject (or vice versa).** Keep your subject description separate from your style, shot and lighting words so you can change one without losing the other.",
        "**Unwanted extras appear (text, a border, clutter).** Add a short negative/avoid note, or in Stable Diffusion tools use the negative-prompt field.",
    ],
    challenge="Write a structured prompt for a completely different subject of your own using the same seven slots, proving the template works beyond Emberdrift.",
    lo=2,
    deliverable="Keep your final Emberdrift prompt and the reusable prompt template — you adapt them in Labs 3, 4, 5 and 6.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you have a strong prompt and template).",
        "Your image tool signed in with generations available.",
    ],
    trouble=[
        "**The character changes face/costume across variations.** That is normal — describe the design tightly, and use a character reference to lock consistency properly in Lab 7.",
        "**The full body is cramped or cropped.** Use a portrait/full-body aspect ratio (2:3) and add 'full-body, head to toe, neutral background'.",
        "**No single variation is fully right.** Curate the closest, then fix it by hand (inpaint and paint-over) in Lab 8 — you do not have to get it perfect from the prompt alone.",
    ],
    challenge="Generate a second, contrasting character for the world (an older sky-port harbourmaster) in the same style, proving your character pipeline can grow the cast consistently.",
    lo=3,
    deliverable="Keep the Wren hero concept and two variations — the character page and the reference you use to keep Wren consistent later.",
 ),
 4: dict(
    prereqs=[
        "Completed Lab 3 (you have on-brief artwork and a clear style forming).",
        "Your prompt template and the world brief to hand.",
    ],
    trouble=[
        "**The environment has no sense of scale.** Add a small human silhouette or a familiar object, and use a low-angle wide shot to make the space feel vast.",
        "**The composition is cluttered.** Name one clear focal point (the salvage-crane landmark) and add 'atmospheric depth, clear focal point, uncluttered foreground'.",
        "**Dusk looks flat.** Push warm-versus-cool: 'warm amber lantern glow against cool blue shadows, volumetric light'.",
    ],
    challenge="Generate the same sky-port at a different time or weather (dawn, or a storm rolling in) to build a small colour-script for the location.",
    lo=4,
    deliverable="Keep the wide establishing shot and the detail view — the environment page and the mood the whole pack shares.",
 ),
 5: dict(
    prereqs=[
        "Completed Labs 3–4 (you have a character and environment, and a forming style).",
        "Your image editor ready to assemble the sheet.",
    ],
    trouble=[
        "**Props don't read clearly.** Use a plain studio background, a single object per generation, and a three-quarter view; regenerate anything busy or ambiguous.",
        "**The three props don't look like a set.** Reuse the exact same style, background and lighting words for all three and change only the object.",
        "**The assembled sheet looks uneven.** Align the props on a grid with even spacing and consistent scale in your editor, and keep the background plain.",
    ],
    challenge="Generate a fourth prop (a patched glider, or a salvaged relic) in the same style and add it to the sheet, proving your asset system can grow.",
    lo=5,
    deliverable="Keep the three props and the assembled asset sheet — the prop page of your pack.",
 ),
 6: dict(
    prereqs=[
        "Completed Labs 3–5 (you have character, environment and props to unify).",
        "Your best piece so far, to use as a style reference.",
    ],
    trouble=[
        "**Pieces still feel inconsistent.** Tighten the house-style phrase (name the medium, palette, lighting and mood explicitly) and append it to every prompt; add a style reference where your tool supports it.",
        "**The style reference has little effect.** Use a cleaner, stronger reference and raise its influence (Midjourney --sref weight; the reference/style strength slider elsewhere).",
        "**Thumbnails all look the same.** Change only the shot and aspect ratio between them, and push more extreme framings (very wide vs very tight) to see real options.",
    ],
    challenge="Write a second, contrasting house style for the same world (a grittier, stormier take) and generate one piece in it, so you can compare art directions.",
    lo=6,
    deliverable="Keep the locked house-style phrase, the style reference and the composition thumbnails — the consistency layer the rest of the pack relies on.",
 ),
 7: dict(
    prereqs=[
        "Completed Lab 6 (you have a locked style and a chosen composition).",
        "Your character/style references ready to supply to the tool.",
    ],
    trouble=[
        "**Iterations drift away from the original.** Lower the change per step, reuse the seed, and use image-to-image at a modest strength so the tool improves rather than reinvents.",
        "**Wren looks like a different person each time.** Supply the Wren hero concept as a character reference and keep the description identical between iterations.",
        "**You keep re-rolling forever.** Change one thing per iteration and stop when it matches your intent — converging beats endless new generations.",
    ],
    challenge="Reproduce your chosen image exactly from the recorded seed and prompt on a fresh session, proving your result is reproducible.",
    lo=7,
    deliverable="Keep the refined near-final key-art candidate plus its recorded seed and prompt — the piece you finish in Lab 8.",
 ),
 8: dict(
    prereqs=[
        "Completed Lab 7 (you have a refined near-final key-art image).",
        "An image editor with layers (Photoshop with Generative Fill is ideal; Krita or Photopea also work).",
    ],
    trouble=[
        "**Inpainting doesn't match the surroundings.** Keep the selection tight and mention the lighting/style in the inpaint prompt so the fix blends; feather the selection edge.",
        "**Outpainting shows a visible seam.** Extend in smaller steps and let the tool sample the existing edge; paint over any remaining join by hand.",
        "**Upscaling adds artefacts.** Use a lower upscale strength, then inpaint or paint over the artefacts; export at the resolution you actually need.",
    ],
    challenge="Produce a second, alternative crop of the same key art (a square social format and a wide banner) using outpainting, so the piece works across formats.",
    lo=8,
    deliverable="Keep the finished, portfolio-ready 'keyart_final' image and your adjustable edit layers — the centrepiece of your pack.",
 ),
 9: dict(
    prereqs=[
        "Completed Lab 8 (you have a finished key-art piece and the full set).",
        "A slide or layout tool for the portfolio boards, and export access.",
    ],
    trouble=[
        "**The portfolio feels loose.** Curate harder — four excellent boards beat a pile; cut anything off-model or weak.",
        "**Boards look inconsistent.** Use one layout template, consistent captions and the same house style across all boards.",
        "**Unsure whether the work is commercial-safe.** Re-run the IP checklist: no trademarks, no living-artist styles, check your tool's plan/model licence, and disclose AI use where required.",
    ],
    challenge="Add one more touchpoint — a title/key-art cover and a one-line pitch — and present the pack as if pitching Emberdrift to a publisher.",
    lo=9,
    deliverable="Keep the complete, curated Emberdrift concept-art portfolio — character, environment, props and key art, exported as a PDF with a read-me and a completed IP checklist. This is the end-to-end deliverable the course set out to build.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Text to use (type into your AI image tool's prompt field):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 40)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day 1**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[e["lo"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{e['lo']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        rows.append(
            f"| 1 | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 9 labs build one connected **Emberdrift concept-art pitch pack**, which you begin in Lab 1 and "
        "finish in Lab 9 — from a text prompt, through prompting, character, environment and prop generation "
        "with Midjourney, Stable Diffusion and Adobe Firefly, into a locked house style, refined iterations, "
        "inpainting, outpainting, upscaling and a hand paint-over, and out as a curated, presented portfolio. "
        "An Emberdrift concept-art brief is supplied in `reference-pack/`; use your own non-confidential "
        "project wherever you prefer. There is **no assessment** — each lab verifies itself with a 'Test it' "
        "step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the Emberdrift concept-art brief.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    # remove stale lab-*.md so renamed labs don't linger
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()
