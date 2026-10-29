---
project: quran
public: true
backfilled: true
type: feature
audience: users
title: 'Прогресс чтения и скрытие пояснений в скобках'
summary: 'Показывается процент прочитанного, пояснения в скобках можно скрыть, добавлено простое «поделиться».'
user_impact:
  - 'Видно, сколько осталось до хатма'
  - 'Чище текст перевода'
screenshots: []
checks: []
deploy_url: https://quran.nurtech.dev
commits: 232b823..89f49bc
---

Notes for editor:
- What changed: Прогресс, идемпотентное скрытие скобок.
- Where to verify: https://quran.nurtech.dev
- Risks: восстановлено по git log задним числом.
