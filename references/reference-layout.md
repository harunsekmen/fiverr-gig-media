# Reference layout

Measured on 2026-10-26 from a local cover frame. Its creator accepted one supplied marketplace view; other device crops were not verified. The 104 px buffers are our reference setup, not an official Fiverr rule.

## Video geometry

Coordinates start at the upper left.

| Region | x | y | Width | Height |
|---|---:|---:|---:|---:|
| Outer frame | 0 | 0 | 1280 | 714 |
| Left background buffer | 0 | 0 | 104 | 714 |
| Cover artwork | 104 | 0 | 1072 | 714 |
| Right background buffer | 1176 | 0 | 104 | 714 |

Each side occupies 8.125% of the frame width. The artwork fills the height with no outer top/bottom padding. Extend its background palette into the side buffers.

## Text guides

These insets are optional design suggestions, not measured platform crop boundaries. Preserve accepted text placements unless there is demonstrated clipping or overlap.

| Layout | Inset within artwork | Text box in outer-canvas coordinates: x, y, width, height |
|---|---|---|
| Gig image | 104 px horizontal; 48 px vertical | 104, 48, 1072, 673 |
| Reference video | 40 px | 144, 40, 992, 634 |
| HD video | 40 px | 144, 40, 992, 640 |
| Full HD video | 60 px | 216, 60, 1488, 960 |

## Exact SVG guides

Red identifies margins or background-only buffers; green identifies the suggested content area. Dashed lines mark the optional text inset. These colors are guide overlays, not colors to add to a finished cover.

Open [Gig image](../assets/gig-image-guide.svg), [reference video](../assets/reference-video-guide.svg), [HD video](../assets/new-video-hd-guide.svg), or [Full HD video](../assets/new-video-fullhd-guide.svg) in a vector editor. Hide `guide-fills` to view artwork underneath, then hide `guides` before final export.

The [comparison image](../assets/safe-zone-comparison.png) is an explanatory schematic; the SVGs encode the exact coordinates.
