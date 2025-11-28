# Prometheus Autonomous Logistics Rover - Websocket and REST Bridge

## 🛠 Kurulum ve Çalıştırma
```
pip install -r requirements.txt
python3 rest.py
```





## 📡 API Reference

Robotun durumu ve görev takibi için aşağıdaki endpoint kullanılır.

### Get Robot Status

```http
GET /api/status
```

Bu endpoint, aktif görevin durumunu (`status`), ilerlemesini ve robotun anlık konumunu döndürür.

**Örnek Yanıt (200 OK):**

```json
{
  "task_id": "task_12345",
  "status": "IN_PROGRESS",
  "pos": {
    "x": 1.5,
    "y": 2.3,
    "theta": 0.52
  },
  "type": "delivery"
}
```

**Alan Açıklamaları:**

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| `task_id` | `string\|null` | Mevcut görevin ID'si. Görev yoksa `null` döner. |
| `status` | `string` | Görev durumu: `PENDING`, `IN_PROGRESS`, `SUCCESSFUL`, `FAILED`, `TIMEOUT`. |
| `progress` | `int` | Görev ilerleme yüzdesi (`0-100`). |
| `type` | `string` | İşlem türü (örn: `cleaning`, `delivery`). |
| `pos` | `object` | Robotun anlık koordinat verisi. |
| `pos.x` | `float` | X ekseni konumu (metre). |
| `pos.y` | `float` | Y ekseni konumu (metre). |
| `pos.theta` | `float` | Robotun açısı/yönü (radyan). |

