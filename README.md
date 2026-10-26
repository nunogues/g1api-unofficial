<div align="center">

# 📰 G1 API

**An unofficial REST API that turns G1 headlines into clean, structured JSON.**


![Live API](https://img.shields.io/badge/Live%20API-online-22c55e?style=flat-square&logo=render&logoColor=white)


![Docs](https://img.shields.io/badge/Swagger-docs-0ea5e9?style=flat-square&logo=swagger&logoColor=white)



![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)




![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)




![License](https://img.shields.io/badge/status-unofficial-lightgrey?style=flat-square)



[Live API](https://g1api-unofficial.onrender.com/) · [Documentation](https://g1api-unofficial.onrender.com/docs) · [Try it](https://g1api-unofficial.onrender.com/news?limit=5)

</div>

---

## ✨ Features

- 📰 Fetch the latest news from the G1 homepage
- 🔎 Search by title and summary
- 🖼️ Metadata included: publication dates and image URLs (when available)
- ⚡ In-memory cache with a 60-second TTL
- 📖 Interactive docs powered by FastAPI
- ✅ Query parameter validation

## 🚀 Quick Start

```bash
curl "https://g1api-unofficial.onrender.com/news?limit=5"
```

```bash
curl "https://g1api-unofficial.onrender.com/news/search?q=tecnologia"
```

## 📡 Endpoints

| Method | Endpoint       | Description                     |
| ------ | -------------- | ------------------------------- |
| `GET`  | `/`            | API information                 |
| `GET`  | `/health`      | Health check                    |
| `GET`  | `/news`        | Retrieve news                   |
| `GET`  | `/news/search` | Search news by title or summary |
| `GET`  | `/docs`        | Interactive API documentation   |

### `GET /news`

Retrieve news collected from the G1 homepage.

| Parameter | Type    | Default | Constraints |
| --------- | ------- | ------- | ----------- |
| `limit`   | integer | `10`    | 1–20        |

[▶ Try this endpoint](https://g1api-unofficial.onrender.com/news?limit=5)

### `GET /news/search`

Search collected news by title or summary.

| Parameter | Type    | Description                                          |
| --------- | ------- | ---------------------------------------------------- |
| `q`       | string  | Search term                                          |
| `limit`   | integer | Maximum number of results (default: 10, range: 1–20) |

[▶ Try this endpoint](https://g1api-unofficial.onrender.com/news/search?q=tecnologia)

> [!NOTE]
> Search runs only on the news currently in the API's cache. It does not search the entire G1 archive.

<details>
<summary><b>📦 Example response</b></summary>

```json
[
  {
    "title": "Example news headline",
    "url": "https://g1.globo.com/example",
    "image_url": "https://example.com/image.jpg",
    "summary": "A short description of the news article.",
    "published_at": "2026-10-26T10:00:00",
    "updated_at": "2026-10-26T11:00:00"
  }
]
```

The response above is illustrative. Actual values depend on the metadata available on G1.

</details>

## 🛠️ Tech Stack

| Tool                                                | Purpose             |
| --------------------------------------------------- | ------------------- |
| [Python](https://www.python.org/)                   | Core language       |
| [FastAPI](https://fastapi.tiangolo.com/)            | REST API framework  |
| [Requests](https://requests.readthedocs.io/)        | HTTP requests       |
| [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) | HTML parsing |
| [Pydantic](https://docs.pydantic.dev/)              | Data validation     |

## 💻 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/nunogues/g1api-unofficial.git
cd g1api-unofficial

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the development server
uvicorn app.main:app --reload
```

Then open:

- **API:** http://127.0.0.1:8000
- **Docs:** http://127.0.0.1:8000/docs

## 🧠 Caching

The API keeps an in-memory cache with a **60-second TTL**, reusing news data during that window to reduce repeated requests to the source website.

The cache resets when the application restarts and is not shared between separate server processes.

## ⚠️ Limitations

- Collection depends on G1's website structure and publicly accessible metadata.
- The API may return fewer articles than requested, depending on successful extraction.
- Full article text is not provided.
- Availability depends on the hosting service and the source website.

## 📄 Disclaimer

> [!IMPORTANT]
> This is an independent, unofficial project and is not affiliated with, endorsed by, or sponsored by G1 or Grupo Globo.

News content and trademarks belong to their respective owners. This project provides links and extracted metadata for informational and educational purposes.

## 👤 Author

**nunogues** · [GitHub](https://github.com/nunogues)

---

<div align="center">
<sub>Built to explore web scraping, REST API development, caching, and deployment.</sub>
</div>
