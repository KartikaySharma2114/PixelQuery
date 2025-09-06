# PixelQuery
<<<<<<< HEAD

A powerful image search system that combines visual embeddings with OCR text extraction for comprehensive image retrieval. Built with SigLIP-2 for visual understanding and PaddleOCR for text extraction.

## Tech Stack

- **Backend**: FastAPI, Python 3.8+
- **ML Models**: SigLIP-2 (Google), PaddleOCR
- **Vector Database**: Qdrant
- **Text Database**: SQLite with FTS4
- **Deep Learning**: PyTorch, Transformers
- **Deployment**: Docker, Docker Compose
- **Testing**: Pytest
- **Monitoring**: File system watching with Watchdog

## Features

- **Visual Search**: Find images based on visual similarity using SigLIP-2 embeddings
- **Text Search**: Search through OCR-extracted text from images
- **Hybrid Search**: Combine visual and text search with configurable weights
- **Real-time Processing**: Monitor folders for new images and process automatically
- **FastAPI Backend**: RESTful API for easy integration
- **Vector Database**: Efficient similarity search using Qdrant

## Setup

You'll need Python 3.8+ and conda installed. GPU is recommended but not required.

```bash
# Clone and navigate
git clone <your-repo-url>
cd PixelQuery

# Create conda environment
conda create -n pixelquery python=3.9
conda activate pixelquery

# Install dependencies
pip install -r requirements.txt

# Create data directories
mkdir -p data/vector_db data/logs
```

## Configuration

Edit `src/config/config.yaml` to customize:

- **Model settings**: Change SigLIP model, batch size, device
- **OCR settings**: Languages, confidence threshold, GPU usage
- **Database paths**: Vector and text database locations
- **Performance**: Memory limits, worker threads
- **Search weights**: Balance between visual and text search

## Running

```bash
# Activate environment
conda activate pixelquery

# Start the server
uvicorn src.api.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`. Main endpoints:
- `POST /search` - Search images
- `POST /upload` - Add new images  
- `GET /health` - Status check

## Project Structure

```
PixelQuery/
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py          # Configuration management
│   │   └── config.yaml          # Default configuration
│   ├── models/
│   │   ├── __init__.py
│   │   ├── embedding_generator.py  # SigLIP-2 integration
│   │   └── ocr_engine.py          # PaddleOCR wrapper
│   ├── database/
│   │   ├── __init__.py
│   │   ├── vector_db.py          # Qdrant integration
│   │   └── text_db.py            # SQLite for OCR text
│   ├── search/
│   │   ├── __init__.py
│   │   └── search_manager.py     # Hybrid search logic
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── image_processor.py    # Main processing pipeline
│   │   └── file_monitor.py       # File system monitoring
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── search.py        # Search endpoints
│   │       └── management.py    # Admin endpoints
│   └── utils/
│       ├── __init__.py
│       ├── error_handler.py     # Error handling
│       └── performance.py       # Performance monitoring
├── static/                      # Frontend files
│   ├── index.html
│   ├── style.css
│   └── script.js
├── tests/
│   ├── __init__.py
│   ├── test_embedding.py
│   ├── test_ocr.py
│   ├── test_search.py
│   └── test_api.py
├── data/                        # Local data storage
│   ├── vector_db/              # Qdrant data
│   ├── text.db                 # SQLite database
│   └── logs/                   # Application logs
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Development

Run tests with `pytest tests/`

Common issues:
- CUDA out of memory → reduce batch size in config.yaml
- Slow processing → enable GPU for OCR
- Import errors → check all dependencies installed
=======
>>>>>>> 6a8aff78d09050a35384aeb04607d9d532ce8ccb
