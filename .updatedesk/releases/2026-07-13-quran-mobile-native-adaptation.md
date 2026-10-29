---
project: quran
public: true
backfilled: true
type: design
audience: users
title: 'Адаптация под телефон и Safari'
summary: 'Интерфейс использует весь экран с учётом вырезов, вибрацией, панели ведут себя как нижние листы, мусхаф работает в Safari.'
user_impact:
  - 'Удобно на iPhone и Android'
screenshots: []
checks: []
deploy_url: https://quran.nurtech.dev
commits: b27b053..689af1c
---

Notes for editor:
- What changed: Safe-area, хаптик, fallback для Safari.
- Where to verify: https://quran.nurtech.dev
- Risks: восстановлено по git log задним числом.
