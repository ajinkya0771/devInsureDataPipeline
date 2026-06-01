# 🚀 Insurance Data Pipeline Project

## Table of Contents

* [Overview](#-overview)
* [Architecture Workflow](#️-architecture-workflow)
* [Features](#️-features)
* [Technologies Used](#️-technologies-used)
* [Project Structure](#-project-structure)
* [Pipeline Execution Flow](#-pipeline-execution-flow)
* [Execution Screenshots](#-execution-screenshots)
* [How To Run](#️-how-to-run)
* [Sample Outputs](#-sample-outputs)
* [Learning Outcomes](#-learning-outcomes)
* [Author](#-author)

## 📌 Overview

An end-to-end **Insurance Data Pipeline (IDP)** built using **Python** and **Pandas** to automate ingestion, validation, preprocessing, transformation, semantic reporting, and archival of insurance datasets.

This project simulates a real-world mini data engineering workflow using layered architecture and modular Python development.

---

# 🏗️ Architecture Workflow

```text
CSV Files
   ↓
Ingestion Layer
   ↓
Validation Layer
   ↓
Preprocessing Layer
   ↓
Curated Layer
   ↓
Semantic Layer
   ↓
Retention & Archive Layer
```

---

# ⚙️ Features

✅ CSV file validation using JSON control files
✅ Automated ingestion workflow
✅ Data preprocessing and cleaning
✅ Duplicate removal and column standardization
✅ Parquet file generation
✅ Curated business layer creation
✅ Semantic reporting layer
✅ Retention and archival automation
✅ Audit logging and monitoring
✅ End-to-end orchestration using `main.py`
✅ GitHub-integrated project structure

---

# 🛠️ Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python       | Core Development        |
| Pandas       | Data Processing         |
| Parquet      | Optimized Storage       |
| JSON         | Validation Rules        |
| VS Code      | Development Environment |
| Git & GitHub | Version Control         |
| PowerShell   | Execution Terminal      |

---

# 📂 Project Structure

```text
devInsureDataPipeline/
│
├── config/
│   └── control_files/
│
├── data/
│   ├── ingestion/
│   ├── preprocessed/
│   ├── curated/
│   ├── semantic/
│   └── retention/
│
├── logs/
│
├── screenshots/
│
├── src/
│   ├── ingestion_manager.py
│   ├── preprocessing_engine.py
│   ├── transformation_engine.py
│   ├── retention_manager.py
│   ├── audit_logger.py
│   ├── utils.py
│   └── main.py
│
├── requirements.txt
└── .gitignore
```

---

# 🔄 Pipeline Execution Flow

## 1️⃣ Ingestion Layer

* Reads CSV files from ingestion folder
* Reads JSON control files
* Validates schema and structure

## 2️⃣ Preprocessing Layer

* Removes duplicates
* Cleans whitespace
* Standardizes column names
* Generates parquet files

## 3️⃣ Curated Layer

* Performs business transformations
* Creates enriched curated datasets

## 4️⃣ Semantic Layer

* Generates business metrics
* Creates reporting datasets

## 5️⃣ Retention Layer

* Archives processed source files
* Maintains historical retention folders

---

# 📸 Execution Screenshots

The project includes execution screenshots for:

* Folder structure
* Virtual environment setup
* Ingestion success
* Preprocessing success
* Transformation success
* Curated layer
* Semantic layer
* Retention layer
* Final pipeline execution

---

# ▶️ How To Run

## Step 1 — Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Step 2 — Run Pipeline

```bash
python src/main.py
```

---

# 📈 Sample Outputs

Generated outputs include:

* Preprocessed parquet files
* Curated datasets
* Semantic reporting datasets
* Audit logs
* Archived ingestion files

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Modular Python development
* Data engineering workflow concepts
* File automation
* Logging and monitoring
* Layered pipeline architecture
* GitHub project deployment
* Real-world debugging and orchestration

---

# 👨‍💻 Author

**Ajinkya Dhote**

AI/ML & Data Engineering Enthusiast  
Focused on Python, AWS, Data Engineering, and Automation Projects.
