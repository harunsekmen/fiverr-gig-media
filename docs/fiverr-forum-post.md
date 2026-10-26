# Gig image vs. video thumbnail: why I use two layouts

A standalone Gig image uses Fiverr's recommended [1280 × 769 px canvas](https://help.fiverr.com/hc/en-us/articles/15863342952977-Creating-Gig-images-and-tagging-your-Gig-gallery). With a video, the selected video frame takes priority as the cover, so I prepare a separate composition. [Fiverr's guide](https://help.fiverr.com/hc/en-us/articles/360010451397-Creating-a-Gig).

My solution: keep the normal image's background edge to edge, with text inset. In my tested **1280 × 714 video reference**, I reserved **104 px on each side** for background, leaving **1072 × 714** for the artwork, with no top/bottom padding. I adapted the composition without stretching text or faces.

These use different working safe-area guides. **104 px is my measured setup, not an official Fiverr rule or a guarantee across devices.** For new videos, use 16:9 and check the live card. After approval, choose the cover through **Gallery → Video → Edit → Set as preview**. [Instructions](https://help.fiverr.com/hc/en-us/articles/360010451657-Adding-and-managing-your-Gig-video).

I packaged the workflow, editable guides, and calculator as a reusable English Codex skill. [Get it on my GitHub](https://github.com/harunsekmen/fiverr-gig-media).
