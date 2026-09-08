# Pradeep's Golu 2026, deploy to GitHub Pages

Live URL (once deployed): https://gmuthukannan.github.io/pradeep-golu/

## What's in here
- `index.html` is the portal page (4 write-up links + embedded YouTube video)
- `writeup1.html` .. `writeup4.html` are placeholder write-up pages, edit the text
- `assets/qr_code.png` is the reliable fallback QR, already encodes the real URL above
- `assets/ganesha_badge.png` is the placeholder center-logo icon for the fallback QR
- `assets/make_logo.py`, `assets/make_qr.py` are the scripts that generated those
- `assets/style_reference.png` is the look we want for the AI-art QR (if saved)

## 1. Create the repo
On github.com: New repository, name it `pradeep-golu`, Public, Create.
Do not add a README or .gitignore on the GitHub side, this folder already has them.

## 2. Push these files
From this folder, run:

```
git remote add origin https://github.com/gmuthukannan/pradeep-golu.git
git branch -M main
git push -u origin main
```

(The initial commit is already made locally.)

## 3. Turn on Pages
Repo, Settings, Pages, Source: "Deploy from a branch", Branch: `main`, folder `/ (root)`, Save.
The site goes live at https://gmuthukannan.github.io/pradeep-golu/ about 1 to 2 minutes later.

## 4. Replace placeholder content
- Edit the title and body text in `writeup1.html` .. `writeup4.html`
- In `index.html`, update the 4 card labels and descriptions to match
- In `index.html`, replace the YouTube video ID in `src="https://www.youtube.com/embed/VIDEO_ID"`
- Commit and push again

## 5. If the URL ever changes
Regenerate the fallback QR:

```
python assets/make_qr.py "https://gmuthukannan.github.io/pradeep-golu/"
```

Then commit and push the updated `assets/qr_code.png`.

## The AI-art QR code (the real goal)

`assets/qr_code.png` right now is the safe fallback: a standard QR with a small
icon in the center. It always scans. The goal is the full painted-deity QR where
the whole image looks like a black-and-white Ganesha with a mandala background
and the three corner finder squares are still visible.

That needs a ControlNet "QR Code Monster" pass, which is not available in this
environment. Do it yourself for free with the Hugging Face Space
`monster-labs/QR_code_monster`.

### Steps
1. Make sure `assets/qr_code.png` already encodes the correct final URL (step 5 above).
2. Open the Space. Upload `assets/qr_code.png` as the **control image**. This is the
   part that makes the output scannable. A prompt alone produces art with no QR in it.
3. Settings:
   - ControlNet conditioning scale: 1.3 to 1.5 (lower looks better but risks not scanning)
   - Controlnet start: 0, Controlnet end: 0.9 to 1.0
   - Guidance scale: 7 to 9
   - Steps: 30 to 40
   - Generate 4 at a time, change the seed each batch
4. Prompt:
   ```
   black and white ink illustration of Lord Ganesha, seated, intricate
   mandala background, ornate linework, high contrast, symmetrical,
   temple art, detailed patterns, white background
   ```
   Negative prompt:
   ```
   color, blurry, low contrast, grey, washed out, photo, text, watermark
   ```
5. Pick a result where you can clearly see the three corner squares and a faint
   blocky grid running through the art.

### Verify before printing (do not skip)
1. Scan it on screen with 2 or more phones.
2. Print a test at the exact final size and scan that under normal room light.
3. If it fails: raise the ControlNet scale by 0.1 and regenerate, or pick a
   busier, higher-contrast result. AI-art QR codes fail to scan when the art is
   pushed too hard.
4. Save the winning image into the project (replace `assets/qr_code.png` or add a
   new file) and commit it.
