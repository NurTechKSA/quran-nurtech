---
project: quran
public: true
backfilled: true
type: feature
audience: users
title: 'Надёжное аудио и новые чтецы'
summary: 'Аудио берётся из надёжного источника, добавлены Ахмад Талиб бин Хумайд и Юнус ас-Сувейли, чтец по умолчанию задан с запасными вариантами.'
user_impact:
  - 'Звук не обрывается'
  - 'Можно слушать новых чтецов'
  - 'Исправлена ошибка, когда играл не тот чтец'
screenshots: []
checks: []
deploy_url: https://quran.nurtech.dev
commits: e723023..b302345
---

Notes for editor:
- What changed: CDN islamic.network, цепочка запасных источников, исправлен устаревший кэш /data.
- Where to verify: https://quran.nurtech.dev
- Risks: восстановлено по git log задним числом.
