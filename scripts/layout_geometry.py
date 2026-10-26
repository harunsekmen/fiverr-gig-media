#!/usr/bin/env python3
"""Print layout coordinates and fit diagnostics; no media edits or crop guarantees."""

import argparse
import json
import math


PROFILES = {
    "gig-image": (1280, 769, 0, "official recommended image canvas; no official numeric safe zone"),
    "approved-video": (1280, 714, 104, "historical creator-approved reference; not an official video size"),
    "new-video-hd": (1280, 720, 104, "16:9 canvas with reference-derived buffers; live card unverified"),
    "new-video-fullhd": (1920, 1080, 156, "scaled HD layout; live card unverified"),
}


def geometry(profile, source_size=None, inner_margin=0, duration=None, fps=30,
             text_inset_x=None, text_inset_y=None, cover_seconds=0.3):
    width, height, side, evidence = PROFILES[profile]
    artwork_width = width - 2 * side
    if not math.isfinite(inner_margin) or inner_margin < 0:
        raise ValueError("inner margin must be finite and nonnegative")
    inset_x = inner_margin if text_inset_x is None else text_inset_x
    inset_y = inner_margin if text_inset_y is None else text_inset_y
    if not all(math.isfinite(n) and n >= 0 for n in (inset_x, inset_y)):
        raise ValueError("text insets must be finite and nonnegative")
    if inset_x * 2 >= artwork_width or inset_y * 2 >= height:
        raise ValueError("text insets must leave a nonempty text box")
    if not math.isfinite(fps) or fps <= 0:
        raise ValueError("fps must be finite and positive")
    if duration is not None and (not math.isfinite(duration) or duration <= 0):
        raise ValueError("duration must be finite and positive")
    if not math.isfinite(cover_seconds) or cover_seconds <= 0:
        raise ValueError("cover duration must be finite and positive")

    result = {
        "profile": profile,
        "evidence": evidence,
        "canvas": [width, height],
        "artwork_xywh": [side, 0, artwork_width, height],
        "outer_buffers": {"left": side, "right": side, "top": 0, "bottom": 0},
        "artwork_master_2x": [artwork_width * 2, height * 2],
        "stretch_allowed": False,
        "optional_text_guide": {
            "insets_within_artwork": {"x": inset_x, "y": inset_y},
            "xywh_in_outer_canvas": [side + inset_x, inset_y,
                                     artwork_width - 2 * inset_x, height - 2 * inset_y],
            "status": "selected design guide, not an official or measured platform crop boundary",
        },
    }
    if source_size is not None:
        if len(source_size) != 2 or not all(math.isfinite(n) and n > 0 for n in source_size):
            raise ValueError("source dimensions must be finite and positive")
        sw, sh = source_size
        cover_scale = max(artwork_width / sw, height / sh)
        contain_scale = min(artwork_width / sw, height / sh)
        result["source_fit_diagnostic"] = {
            "source_size": [sw, sh],
            "cover_uniform_scale": cover_scale,
            "cover_crop_each_side": max(0, (sw * cover_scale - artwork_width) / 2),
            "cover_crop_each_top_bottom": max(0, (sh * cover_scale - height) / 2),
            "contain_padding_each_side_inside_artwork": max(0, (artwork_width - sw * contain_scale) / 2),
            "contain_padding_each_top_bottom": max(0, (height - sh * contain_scale) / 2),
            "action": "Inspect complete text and faces; adapt background/composition rather than stretch.",
        }
    if side:
        result["buffer_background"] = {
            "suggestion": "extend the cover palette using a solid color or subtle gradient",
            "black_required": False,
            "important_content_allowed": False,
        }
        if duration is not None and duration < cover_seconds:
            raise ValueError("video duration must be at least the selected cover duration")
        frame_count = cover_seconds * fps
        timing = {
            "status": "example workflow convention; configurable, not a Fiverr requirement",
            "cover_seconds": cover_seconds,
            "fps": fps,
            "frame_count_exact": frame_count,
            "start_seconds": None if duration is None else round(duration - cover_seconds, 9),
            "end_seconds": duration,
            "placement": "replace the end of the video; preserve total duration",
            "selects_preview_automatically": False,
        }
        if abs(frame_count - round(frame_count)) > 1e-9:
            timing["frame_alignment_note"] = (
                "Cover duration is not an integer number of frames at this fps; "
                "choose a frame count explicitly."
            )
        if duration is not None:
            total_frames = duration * fps
            if (abs(frame_count - round(frame_count)) <= 1e-9
                    and abs(total_frames - round(total_frames)) <= 1e-9):
                timing["frame_range_zero_based_end_exclusive"] = [
                    round(total_frames) - round(frame_count), round(total_frames)
                ]
        result["cover_timing"] = timing
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=PROFILES, required=True)
    parser.add_argument("--source-size", nargs=2, type=int, metavar=("WIDTH", "HEIGHT"))
    parser.add_argument("--inner-margin", type=int, default=0,
                        help="Optional equal text inset inside the artwork (default: 0)")
    parser.add_argument("--text-inset-x", type=int,
                        help="Optional horizontal text inset; overrides --inner-margin on x")
    parser.add_argument("--text-inset-y", type=int,
                        help="Optional vertical text inset; overrides --inner-margin on y")
    parser.add_argument("--duration", type=float, help="Total video duration, in seconds")
    parser.add_argument("--fps", type=float, default=30)
    parser.add_argument("--cover-seconds", type=float, default=0.3,
                        help="Example end-cover duration (default: 0.3); not a Fiverr rule")
    args = parser.parse_args()
    try:
        result = geometry(args.profile, args.source_size, args.inner_margin,
                          args.duration, args.fps, args.text_inset_x,
                          args.text_inset_y, args.cover_seconds)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
