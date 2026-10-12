# AR-1731 — visual language and wizard shell

1. Define renderer-neutral semantic tokens for base, muted, focused, selected,
   success, warning, error, disabled, and step-complete states; require
   contrast-safe non-color distinctions for monochrome/limited terminals.
2. Create a consistent shell: title/identity header, bounded content frame,
   persistent horizontal wizard-step region, contextual footer region, and
   responsive small-terminal fallback.
3. Establish typography/spacing rules for headings, labels, wrapped prose,
   unavailable reasons, warnings, and empty states so descriptions are concise,
   scannable, and visually separated from controls.
4. Capture representative TestBackend/PTY snapshots for normal, narrow,
   monochrome, warning, and error states; update formal model, ownership, and
   help inventory for shell elements.
