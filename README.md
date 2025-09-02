# MusicScape - Big Data & ML Analysis

MusicScape leverages Big Data and Machine Learning techniques to analyze the Million Song Dataset (MSD), a comprehensive collection of contemporary music tracks' metadata and audio features. This project utilizes scalable data processing tools such as PySpark and MongoDB to perform unsupervised clustering, dimensionality reduction, and recommendation system development.

## 📂 Project Structure

```
/MusicScape-Big-Data-ML-Analysis/
│── data/                           # Contains processed datasets (not uploaded)
│── notebooks/                      # Jupyter notebooks for each stage of the pipeline
│   ├── 01-dataprep-pyspark-msd.ipynb   # Data Preprocessing using PySpark
│   ├── 02-dimreduce.ipynb              # Dimensionality Reduction using PCA and UMAP
│   ├── 03-kmeans-clustering.ipynb      # K-Means Clustering
│   ├── 04-cluster-analysis-visualization.ipynb   # Cluster Analysis & Visualization
│   └── 05-recommendation-function.ipynb          # Recommendation System Implementation
│── README.md                       # Project Overview
│── .gitignore                      # Excludes data and sensitive files
```

## 🚀 Project Overview

MusicScape employs Big Data processing to uncover patterns within the Million Song Dataset, using audio features and metadata to generate song clusters and recommendations. This project is structured in five primary notebooks, each focusing on a specific stage of the analysis pipeline:

1. **Data Preprocessing:** Extract and aggregate time-series data from HDF5 files, convert to fixed-length vectors, and export to Parquet and MongoDB.
2. **Dimensionality Reduction:** Reduce dataset dimensionality using PCA and UMAP to facilitate clustering and visualization.
3. **Clustering Analysis:** Apply K-Means clustering to identify song groupings based on audio features (e.g., timbre, pitch).
4. **Visualization & Analysis:** Visualize cluster distributions using Plotly, comparing PCA and UMAP-based clusters.
5. **Recommendation System:** Implement a basic recommendation function that suggests similar songs within the same cluster using Euclidean distance.

## 📊 Dataset

* **Source:** Million Song Dataset (MSD)
* **Subset Size:** 10,000 songs
* **Data Format:** HDF5 files containing audio features, metadata, and time-series data

## 🛠️ Tools & Technologies

* **Data Processing:** PySpark, Pandas, NumPy
* **Clustering Analysis:** K-Means Clustering (PySpark MLlib)
* **Dimensionality Reduction:** PCA, UMAP
* **Database:** MongoDB Atlas
* **Visualization:** Plotly
* **Environment:** Kaggle Notebooks, Local Development

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/MusicScape-Big-Data-ML-Analysis.git
   cd MusicScape-Big-Data-ML-Analysis
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Configure MongoDB connection in each notebook before running.

## ✅ Key Insights

* PCA and UMAP effectively reduced dataset dimensionality while retaining key audio features.
* K-Means clustering revealed natural groupings of songs based on timbre and pitch statistics.
* The recommendation system provides similar songs based on proximity in the feature space, serving as a proof-of-concept for potential music recommendation systems.

## 🎯 Future Work

* Expand clustering analysis using DBSCAN and hierarchical clustering.
* Integrate advanced audio features (MFCC, spectral contrast) to refine clusters.
* Develop real-time recommendation system using vector databases (e.g., Qdrant).

## 📜 References

* Million Song Dataset: [Link](http://millionsongdataset.com)
