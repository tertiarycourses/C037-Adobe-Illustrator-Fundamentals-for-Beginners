# C037 — Generative AI for Concept Art

Create professional **concept art** with generative AI. This one-day, hands-on course
teaches you to use **Midjourney**, **Stable Diffusion** and **Adobe Firefly** to generate
characters, environments and props from text prompts, then develop a consistent style,
iterate, edit and paint over the results into a portfolio-ready, commercially-considered set.

## Course Information

- **Course Code:** C037
- **Course Title:** Generative AI for Concept Art
- **Duration:** 1 day / 7.5 hours
- **Level:** Beginner
- **Mode:** Instructor-led, hands-on practical labs
- **Course Registration:** [Generative AI for Concept Art](https://www.tertiarycourses.com.sg/generative-ai-for-concept-art.html)

## One Connected Concept-Art Pack

Every lab builds one **connected deliverable** — the concept-art pitch pack for a fictional
indie game, **Emberdrift**, about sky-salvagers exploring floating islands above a sea of
clouds. You start with a text prompt in Lab 1 and, with Midjourney, Stable Diffusion and
Firefly, take the world all the way to a complete pack by Lab 9: a hero character, a key
environment, a prop asset sheet, a locked house style, refined iterations and a finished,
painted-over key-art piece, presented as a portfolio. Wherever possible you use your **own**
non-confidential project, so you leave applying the skills to your own work; an Emberdrift
brief is supplied for everyone to follow along.

There is **no assessment** — this is a commercial short course. Each lab proves itself with an
explicit *Test it* verification step instead.

## What You'll Learn

| Topic | Coverage |
|---|---|
| 01 — Getting Started with Generative AI for Concept Art | Introduction to generative AI for art · popular AI image tools (Midjourney, Stable Diffusion, Firefly) · writing effective prompts for concept art · generating characters, environments & props |
| 02 — Creating and Refining Concept Art with AI | Developing styles & compositions · iterating & refining artwork · editing & enhancing with AI (inpainting, outpainting, upscaling, paint-over) · building a concept art portfolio |

## Labs

Nine connected hands-on labs (5 in Topic 1, 4 in Topic 2). See [labs/README.md](labs/README.md) for
the index, [labs/tools.md](labs/tools.md) for the accounts and tools used, and
[labs/reference-pack/](labs/reference-pack/) for the Emberdrift concept-art brief.

## Courseware

Built artifacts live in [`courseware/`](courseware/):

- Trainer slide deck — `Generative AI for Concept Art (C037)-v1.0.pptx` (+ PDF)
- Learner Guide — `LG-*.docx` (+ PDF); the Markdown mirror is at the repo root
- Lesson Plan — `LP-*.docx` (+ PDF)

## Building the Courseware

Everything is generated from a single source (`course_data.py` + `data_domainN.py`) so the deck,
Lesson Plan, Learner Guide and labs stay 100% aligned:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
python .claude/skills/non-wsq-courseware-build/build/gen_labs.py
```

## Non-WSQ

This is a **non-WSQ** commercial short course. It carries **no** WSQ, SSG/SkillsFuture, TRAQOM,
digital-attendance, funding/subsidy or assessment content — those are deliberately excluded.

---

© 2026 Tertiary Infotech Academy Pte Ltd · UEN 201200696W
