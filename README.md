# Fiverr Gig Media

An English Codex skill for preparing Fiverr Gig images and video cover frames without stretching artwork.

![Fiverr image and video cover guides with red margins, green content areas, and dimension arrows](assets/safe-zone-comparison.png)

Red marks areas to keep important content out of; green marks the suggested content area. These are working guides, not official Fiverr crop boundaries. The image's text margins and the video's extra 40 px text inset are optional.

## Use

Copy this folder to your skills directory, such as `~/.codex/skills/fiverr-gig-media/`, then ask:

```text
Use $fiverr-gig-media to prepare a Gig image and a separate video cover.
Preserve text and face proportions and explain which layout profile you use.
```

## Layouts

| Profile | Canvas | Artwork area | Status |
|---|---|---|---|
| Gig image | 1280 × 769 | Full canvas | Official recommended image size |
| Reference video | 1280 × 714 | 1072 × 714; 104 px side buffers | Our accepted reference, not an official video size |
| New HD video | 1280 × 720 | 1072 × 720; 104 px side buffers | 16:9 with reference-derived buffers; verify the live card |
| New Full HD video | 1920 × 1080 | 1608 × 1080; 156 px side buffers | Scaled HD guide; verify the live card |

Normal images keep the background edge to edge. The reference video uses background-only side buffers and no outer top/bottom padding. Adapt the composition for each layout rather than stretching one image into both.

Editable guides: [Gig image](assets/gig-image-guide.svg) · [Reference video](assets/reference-video-guide.svg) · [HD video](assets/new-video-hd-guide.svg) · [Full HD video](assets/new-video-fullhd-guide.svg). Hide `guide-fills` while placing artwork underneath, and hide `guides` before final export.

## Calculator

Python 3, no extra dependencies. Prints coordinates without editing files:

```bash
python3 scripts/layout_geometry.py --profile new-video-hd --inner-margin 40
```

See [SKILL.md](SKILL.md) for the workflow, [official sources](references/official-specs.md) for upload requirements, and [layout measurements](references/reference-layout.md) for guide coordinates.

By [Harun Sekmen](https://github.com/harunsekmen) · [MIT License](LICENSE)
