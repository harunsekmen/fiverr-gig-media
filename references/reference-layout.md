# Measured reference and optional design guides

Recorded: **2026-10-26**. This is an English, public summary of a creator-approved example. Original screenshots and artwork remain outside the public package. This repository therefore provides documented measurements, not an independently reproducible live Fiverr rendering test.

## What was observed

The creator accepted a supplied 1229 × 492 marketplace screenshot. The relevant card's image rectangle was approximately 260 × 144 px. Its main headings and labels appeared without losing the outer words; a play button appeared at lower left and a heart button at upper right. That is acceptance evidence for the visible view only. It does not establish every small label's readability, platform CSS, or all device crops.

The 104 px buffers were measured in the **local 1280 × 714 cover frame**, not calculated from that miniature card screenshot. There is no supplied paired, controlled marketplace test proving different numeric crop boundaries for standalone images and video thumbnails.

## Exact frame geometry

Coordinates start at the upper left; right and bottom bounds are exclusive.

| Region | x | y | Width | Height |
|---|---:|---:|---:|---:|
| Outer video frame | 0 | 0 | 1280 | 714 |
| Left background buffer | 0 | 0 | 104 | 714 |
| Central cover artwork | 104 | 0 | 1072 | 714 |
| Right background buffer | 1176 | 0 | 104 | 714 |

Each side is **8.125%** of the outer width; the center is **83.75%**. Outer top/bottom padding is zero. The original frame used black sides; palette-matched background extensions preserve the geometry without making black a requirement.

A 1536 × 1024 adapted source fitted uniformly into 1072 × 714 has approximately 0.333 px of technical crop at both the top and bottom. Its exact 2× design master is 2144 × 1428.

The original source artwork was 2080 × 1248, exactly 5:3. At 1280 px wide, it becomes 1280 × 768; reaching Fiverr's recommended image height requires 1 px of background adaptation, not text distortion. This does not itself establish a safe area.

## Optional text guides

The old standalone-image suggestion was 104 px horizontal and 48 px vertical text insets. A separate video suggestion was 40 px inside the artwork area. Neither was an official rule or a measured platform crop boundary. Approximate text measurements in the accepted video artwork included about 19–23 px of inner space; a mandatory 40 px rule would incorrectly reject that accepted placement.

With the optional guides selected:

- Standalone image: x=104, y=48, width=1072, height=673.
- Measured video reference: x=144, y=40, width=992, height=634.
- New HD variant: x=144, y=40, width=992, height=640.
- New Full HD variant, scaling the optional inset to 60 px: x=216, y=60, width=1488, height=960.

The background still fills the outer canvas. The video side buffers contain no essential artwork. The smaller dashed text box is an optional additional inset; it is not the same region as the central artwork.

## Exact SVG guides

The SVGs encode the coordinates above at their native dimensions. Hide `guide-fills` when placing artwork underneath, then hide the entire `guides` group before exporting a final cover. Dashed borders indicate optional text guides. Tinted video side bands indicate background-only buffers, not a required band color.

- [Gig image](../assets/gig-image-guide.svg): official canvas; optional text guide.
- [Reference video](../assets/reference-video-guide.svg): measured historical geometry; optional text guide.
- [New HD video](../assets/new-video-hd-guide.svg): 16:9 with reference-derived buffers; live marketplace view unverified.
- [New Full HD video](../assets/new-video-fullhd-guide.svg): 1.5× HD geometry; live marketplace view unverified.

The [AI-generated comparison](../assets/safe-zone-comparison.png) is an explanatory schematic. Its drawn proportions are not an exact guide for cropping or uploading.

## Timing example

The original project was 44 seconds at 30 fps: 1320 frames. Its cover replaced **[43.7, 44.0)**, zero-based frames **1311–1319**. Frame 1310 was still the preceding scene. That convention kept total duration unchanged. It does not automatically select Fiverr's preview frame and should not be imposed on unrelated projects.
