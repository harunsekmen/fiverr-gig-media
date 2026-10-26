# Comparison graphic

## Caption

Two working layouts, with optional text guides. Schematic; these are not official Fiverr safe-zone rules. The historical video reference was checked in one supplied marketplace view. For exact geometry, use the accompanying SVG guides.

## Alt text

Side-by-side comparison of a 1280 by 769 standalone Gig image and a historical 1280 by 714 video cover frame. The image fills its canvas and has optional 104 pixel horizontal and 48 pixel vertical text insets. The video reference has 104 pixel background-only buffers on both sides around 1072 by 714 central artwork, no outer top or bottom padding, and an optional 40 pixel inner text inset. A footer recommends a 16:9 canvas for new videos and verification of the live card.

## Production and accuracy

Created using the built-in image_gen tool, not the CLI fallback. The illustration is AI-generated; the numbers were supplied from the documented sources and reference measurements. Its drawn proportions are schematic. It is not a screenshot, a Fiverr interface mockup, or a pixel-accurate upload template. Exact SVG templates are generated from explicit coordinates separately.

Official source links and verification date are in [official-specs.md](../references/official-specs.md). Reference evidence limits are in [reference-layout.md](../references/reference-layout.md).

## Final generation prompt

```text
Use case: infographic-diagram.
Asset type: English educational graphic for a public GitHub README and a Fiverr community forum post.
Primary request: Explain why a standalone Fiverr Gig image and a video thumbnail need separate compositions and separate working safe-area guides.
Make a polished flat technical infographic, landscape approximately 1800 x 1200 or similar. White/off-white background, dark navy typography, teal and amber accents, clean precise dimension lines. Large legible text, no photographs, no people, no Fiverr logo or fake marketplace UI.
Title exactly: "Fiverr Gig covers: two layouts"
Subtitle exactly: "Standalone image vs. a frame selected from your video"
Two equally prominent panels side by side. The layouts are geometrical diagrams, not literal upload templates.
LEFT PANEL heading "Standalone Gig image". Badge "Official recommended canvas". Diagram a 1280 x 769 landscape rectangle, filled pale teal all the way to its edges. Caption "1280 × 769 px". Inside show a dashed dark teal text guide inset from all four edges. Label it "Optional text guide". Dimension labels for this optional text inset: "104 px sides" and "48 px top / bottom". Under this panel print "Background fills the canvas." and "These text margins are optional."
RIGHT PANEL heading "Video cover frame". Badge "Our measured reference". Diagram a 1280 x 714 landscape rectangle: exact proportions, the left and right sides each 8.125 percent wide, pale amber background-only buffers. Central teal area 83.75 percent wide filling the full height. Clearly label the outer rectangle "1280 × 714 px", the left strip "104 px", the central area "1072 × 714 px", the right strip "104 px". Place the 104px strip labels outside if needed so they fit. In the central area show an additional dashed rectangle slightly inset on all four sides, labeled "Optional text inset: 40 px". The central artwork area fills the height; NO top or bottom outer buffers. Under this panel print "Side buffers: background only." and "No top or bottom outer padding."
Below both panels, a short band with exactly "Our solution: recompose the artwork. Keep text and faces proportional."
Footer in readable text on two lines: "Working guides, not official Fiverr safe-zone rules. Reference checked in one marketplace view." and "For new videos, use a 16:9 canvas (for example, 1280 × 720) and verify the live card."
Precision constraints: 1280 x 714 is a historical measured reference, never label it an official Fiverr video size or a universal safe zone. The 104 /48 static text insets and the extra 40 video text inset are optional suggestions, not measured platform crop boundaries. Do not draw crop marks that imply Fiverr's actual crop is known. Keep artwork zone separate from text guide. All spelling and arithmetic must be correct. No extra claims about clicks, rankings, conversion or universal device compatibility. No watermark.
```
