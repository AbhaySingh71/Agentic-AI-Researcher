# Agentic AI Researcher

**An AI‑powered research assistant that fetches, summarizes, and analyzes arXiv papers using LangGraph. Supports reading existing PDFs and exporting summaries to PDF via Tectonic.**

---

## Key Features

* **arXiv Integration** – Search and retrieve academic papers by title, author, abstract, or unique identifier (arXiv ID).
* **Smart Summaries** – Generate concise, high-quality summaries to distill key insights.
* **PDF Input Support** – Use `read_pdf.py` to ingest and process PDFs directly in the pipeline.
* **PDF Output via Tectonic** – Export polished summaries in PDF format using Tectonic for professional presentation.
* **Streamlit Interface** – (Assuming you use it based on topics) Offers an interactive UI for real-time querying and quick access to research content.

---

## Directory Structure

```
├── ai_researcher.py             # Core driver script (CLI/interactive logic)
├── ai_researcher_langgraph.py   # LangGraph orchestration logic
├── arxiv_tool.py                # API integration with arXiv
├── read_pdf.py                  # PDF parsing and ingestion utility
├── write_pdf.py                 # Summary-to-PDF exporter using Tectonic
├── frontend.py                  # Streamlit (or similar) UI frontend
├── output/                      # Directory for generated PDFs and outputs
├── tectonic.exe                 # Bundled Tectonic executable (if applicable)
├── README.md                    # This documentation
├── LICENSE                      # Apache‑2.0 open-source license
```

---

## Getting Started

### Prerequisites

* Python 3.8 or higher
* Optional: Tectonic installed or `tectonic.exe` included for PDF generation
* API access as needed (e.g., LangGraph API credentials, if applicable)

### Installation

```bash
git clone https://github.com/AbhaySingh71/Agentic-AI-Researcher.git
cd Agentic-AI-Researcher
pip install -r requirements.txt
```

For Tectonic, if not bundled, ensure:

* **macOS/Linux**: `tectonic` is installed and available in your PATH
* **Windows**: Include `tectonic.exe` in the project root or provide its path

---

## Usage Guide

### 1. Fetch & Summarize from arXiv

```bash
python ai_researcher_langgraph.py --query "transformer networks" --summarize
```

This will:

* Fetch relevant arXiv papers (using `arxiv_tool.py`)
* Summarize them via summary logic in `ai_researcher_langgraph.py`
* Display or save to console (depending on your implementation)

### 2. Read and Process Local PDFs

```bash
python read_pdf.py --file path/to/paper.pdf --summarize
```

This leverages PDF parsing followed by summary generation. Works with both arXiv and external PDFs.

### 3. Export Summary to PDF via Tectonic

```bash
python write_pdf.py --input summary.md --output summary.pdf
```

Use this to convert your **Markdown summaries** into well-formatted PDFs using Tectonic.

### 4. (Optional) Launch the Streamlit App

```bash
streamlit run frontend.py
```

Enjoy a user-friendly interface for:

* Searching arXiv
* Viewing paper abstracts and summaries
* Uploading PDFs
* Exporting summaries with a click

---

## Architecture Overview

1. **arXiv Fetching** — Querying arXiv and retrieving raw metadata or PDFs (`arxiv_tool.py`)
2. **LangGraph Orchestration** — Pipelines managing fetch → summarize → format (`ai_researcher_langgraph.py`)
3. **PDF Parsing (read\_pdf.py)** — Extracts text from PDFs to feed into summarizer
4. **PDF Rendering (write\_pdf.py + Tectonic)** — Converts Markdown outputs to PDF with high-quality typesetting
5. **Frontend (frontend.py)** — Optional interactive UI layer for end-user interaction

---

## Why It Matters

* **Speeds up literature review workflows**
* **Handles both remote (arXiv) and local sources**
* **Generates clean, professional PDFs for sharing**
* **Built with modular structure for easy extension**

---

## Future Enhancements

* **Citation Export** (e.g., BibTeX, RIS)
* **Full‑text PDF generation** (beyond summaries, for note aggregations)
* **Keyword filters and semantic search**
* **Multi‑language or domain‑adaptive summarization**
* **Collaborative workspace or team‑share deployment**

---

## License

This project is licensed under the **Apache‑2.0 License**. See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions, suggestions, and pull requests are welcome!
Please raise issues or pull requests for bugs, feature enhancements, or improvements.

---

## Contact

Created by Abhay Singh — happy to connect!
Reach out via GitHub or \[link to your contact/profile].
