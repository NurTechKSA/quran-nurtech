---
project: quran
public: true
backfilled: true
type: performance
audience: users
title: 'Бесшовное переключение аятов'
summary: 'Следующий аят подгружается заранее, паузы между аятами пропали.'
user_impact:
  - 'Непрерывное слушание'
screenshots: []
checks: []
deploy_url: https://quran.nurtech.dev
commits: 21a65a1..21a65a1
---

Notes for editor:
- What changed: Предзагрузка следующего аята.
- Where to verify: https://quran.nurtech.dev
- Risks: восстановлено по git log задним числом.
