# Структура и создание проекта

Наше приложение будет состоять из бекенд и фронтенд части.<br>
Весь код в папке [app](../app)<br>
Схема в проде будет такая.<br>

```mermaid
graph TB;
  I("Пользователь")-->N("Nginx как балансировщик статики и апи");
  N-->I;
  N-->V("Vue");
  N-->B("Backend");
  B-->N;
```

---

## Запуск локально

1. Фронт в [app/frontend](../app/frontend) 
   1. `npm install`
   2. `npm run dev`
2. Бэк в [app/backend](../app/backend)



[След](./docker.md)