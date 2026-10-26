---
name: fiverr-gig-media
description: "Prepare or review Fiverr Gig images and video thumbnail frames. Use for cover sizing, safe-area guides, proportional artwork adaptation, and preview-frame timing; distinguish official specifications from reference measurements and optional design margins."
---

# Fiverr Gig images and video covers

Prepare separate compositions for standalone Gig images and video preview frames. Read [official specifications](references/official-specs.md) for upload requirements and [reference layout](references/reference-layout.md) when reproducing the measured example. This skill prepares media; it does not authorize uploading or publishing it.

## Keep the evidence separate

- **Official:** Fiverr's published image dimensions and video instructions. Last checked: 2026-10-26. Recheck the linked sources for new uploads or current-requirements questions. Report conflicting limits rather than inventing one definitive rule.
- **Measured reference:** A creator accepted one marketplace screenshot using the video layout below. The 104 px side buffers were measured in the local video frame. They are not an official Fiverr safe zone or proof of every desktop/mobile crop.
- **Optional design guides:** Standalone-image text insets of 104 px horizontally and 48 px vertically, and an additional 40 px text inset within the video artwork, are starting suggestions. Do not treat them as requirements or shrink an accepted design to enforce them.

## Choose the appropriate canvas

| Use | Outer canvas | Artwork area | Evidence |
|---|---:|---|---|
| Standalone Gig image | 1280 × 769 | Entire canvas | Official recommended image size |
| Reproduce the measured video reference | 1280 × 714 | x=104, y=0; 1072 × 714 | Historical creator-approved example |
| New HD video | 1280 × 720 | x=104, y=0; 1072 × 720 | 16:9 canvas with reference-derived side buffers; live card unverified |
| New Full HD video | 1920 × 1080 | x=156, y=0; 1608 × 1080 | Scaled version of the HD layout; live card unverified |

- For a new video, use a 16:9 canvas unless the user's current upload requirements establish otherwise. For an existing accepted reference project, preserve its 1280 × 714 geometry. Never present that historical size as Fiverr's official video minimum.
- For the reference-derived video profiles, reserve 8.125% of the outer width on each side for background only. The central artwork fills the height: no outer top/bottom padding.
- Extend the artwork palette into those side buffers with a solid color or subtle gradient. The historical reference used black; black is not required. Fiverr's video troubleshooting advice recommends a 16:9 export without black bars.
- For a standalone image, extend the background to all four edges. Do not automatically add the video's side buffers. Text insets are a separate design decision.

## Adapt the composition without distortion

- The standalone canvas is approximately 5:3; the measured video artwork area is approximately 3:2. Recompose the artwork for each area instead of stretching the same flattened image into both.
- Preserve letter, face, and circle proportions. Do not use unequal x/y scaling or `object-fit: fill`.
- Crop only nonessential background, extend the background where needed, or reposition elements proportionally. Keep complete words, badges, and essential face details.
- After adapting to the target ratio, a centered, uniformly scaled `cover` fit is appropriate. Inspect the crop. Unwanted top/bottom bands from `contain` are not a finished adaptation.
- Use the available image-editing workflow for raster changes and preserve the original. No image-generation tool is required to use the calculator or SVG guides.

## Separate artwork buffers from text guides

The side buffers protect the composition by keeping important content away from the outer frame edges. They do not automatically make all text inside the artwork safe. Keep text inset from the artwork's own edges, check it at card size, and account for visible interface overlays.

The optional image guide is x=104, y=48, w=1072, h=673. The optional 40 px text guide inside the measured video artwork is x=144, y=40, w=992, h=634. Both are design suggestions, not measured Fiverr crop boundaries. Preserve an accepted closer text placement when there is no demonstrated clipping or overlap.

Use [the comparison graphic](assets/safe-zone-comparison.png) for explanation and [the SVG guide files](references/reference-layout.md#exact-svg-guides) for exact coordinates. The generated comparison is schematic, not a pixel-accurate template.

## Cover timing and preview selection

The original workflow replaced the final 0.3 seconds with the cover: 9 frames at 30 fps, without extending the video. This is an example convention, not a Fiverr requirement or a global user preference. Use it when reproducing that workflow; follow the current user's timing instructions otherwise.

Embedding a cover does not select it automatically. After approval, Fiverr documents: **Gig Edit → Gallery → Video → Edit → play/pause on the desired frame → Set as preview → Close**. See [the official video guide](references/official-specs.md#video-and-thumbnail-selection).

If working in an existing video project, use its established editing/rendering workflow. A cover change does not justify unrelated audio or scene changes.

## Verify and report scope

Check canvas dimensions, artwork bounds, side buffers, top/bottom coverage, complete text, proportions, and cover timing. Inspect the first and last cover frames when editing a video. A local preview around 260 × 144 px is useful for readability; it does not reproduce Fiverr's rendering.

Separate local checks from actual marketplace checks. The original screenshot supports acceptance of that one view only. Report new HD/Full HD variants as unverified on the live card until checked; do not claim universal clipping protection.

Calculate coordinates with Python 3, without third-party dependencies:

```bash
python3 scripts/layout_geometry.py --profile approved-video --source-size 1536 1024 --duration 44 --fps 30
python3 scripts/layout_geometry.py --profile gig-image --text-inset-x 104 --text-inset-y 48
python3 scripts/layout_geometry.py --profile new-video-hd --inner-margin 40
```

Profiles: `gig-image`, `approved-video`, `new-video-hd`, `new-video-fullhd`. Insets default to zero. `--inner-margin` applies the same optional inset on both axes; explicit axis insets override it. `--cover-seconds` changes the example 0.3-second convention. The calculator prints JSON; it does not edit or upload media.
