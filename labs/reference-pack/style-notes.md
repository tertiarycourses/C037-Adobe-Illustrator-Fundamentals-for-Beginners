# Style Notes — Emberdrift

*Read alongside [concept-art-brief.md](concept-art-brief.md). These notes turn the
world's feeling into concrete prompt words for your AI image tool.*

## The look in one line

> Painterly game concept art, warm amber lantern light against cool misty blues,
> golden-dusk atmosphere — hopeful, cinematic and full of wonder.

## Prompt vocabulary that works

Reuse these words to keep every generation on-style:

- **Subject words:** sky-salvager, floating island, sea of clouds, patched glider,
  lantern sky-port, rope bridge, salvage-crane, relic-tech, brass-and-leather gear.
- **Style/medium words:** painterly game concept art, digital painting,
  cinematic, illustrative, atmospheric, key-art quality.
- **Composition/shot words:** wide establishing shot, low angle, over-the-shoulder,
  close-up, rule of thirds, clear focal point, sense of scale.
- **Lighting/mood words:** warm amber lantern glow, golden-dusk, volumetric light,
  cool blue shadows, misty, atmospheric depth, hopeful, adventurous.
- **Colour words:** amber gold, ember orange, misty sky blue, deep slate, pale haze.
- **Avoid (note it, or use the negative-prompt field):** no text, no watermark,
  no logo, no modern cars, no grimdark gore, no flat lighting.

## The house-style phrase (locked in Lab 6)

Append this to every prompt so the whole pack matches:

```
painterly game concept art, warm amber lantern light against cool misty blues,
golden-dusk atmosphere, hopeful cinematic mood, cohesive Emberdrift house style
```

## Do / Don't

| Do | Don't |
|---|---|
| Keep warm light vs cool sky | Let everything go one flat colour |
| Give every scene a clear focal point | Fill the frame edge to edge |
| Set an aspect ratio for the shot | Leave framing to chance |
| Reuse the house-style phrase everywhere | Re-describe the style differently each time |
| Curate to ONE best variation | Keep every variation "just in case" |

## The structured prompt template (from Lab 2)

```
[SUBJECT] — a ...,
[STYLE/MEDIUM] — painterly game concept art, cinematic,
[COMPOSITION/SHOT] — wide establishing shot, low angle, rule of thirds,
[LIGHTING/MOOD] — warm amber lantern glow, cool misty sky, hopeful,
[DETAIL] — highly detailed painterly rendering,
[COLOUR] — amber gold and ember against misty slate blue,
[PARAMETERS] — --ar 16:9 (and a seed once you find a look you like).
```

## Reference imagery to gather (see reference-image-guide.md)

- Your own best piece from Labs 3–5 (as a **style reference** for consistency).
- Your **Wren hero concept** (as a **character reference** to keep Wren on-model).
- A plain reference photo or sketch if you want to guide a composition with
  image-to-image.
