---
project: quran
public: true
backfilled: true
type: fix
audience: users
title: 'Исправления первого дня: клики, телефон, арабский текст'
summary: 'Клик по странице суры больше не уводил на другую страницу, на телефоне не ломалась вёрстка, в арабском тексте пропал «чёрный кружок».'
user_impact:
  - 'Читать удобнее и без сбоев'
screenshots: []
checks: []
deploy_url: https://quran.nurtech.dev
commits: 1585060..b738372
---

Notes for editor:
- What changed: Исправлены навигация, горизонтальный оверфлоу панели и неверный символ.
- Where to verify: https://quran.nurtech.dev
- Risks: восстановлено по git log задним числом.
