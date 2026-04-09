# 📄 Document Q&A System

## 🔍 Overview

This project is a Document Question Answering System where users can upload a PDF and ask questions based on its content.

## 🚀 Features

* Upload PDF document
* Ask questions from document
* Get relevant answers
* Works locally (no external APIs)

## 🛠️ Tech Stack

* Python
* Flask
* PDFPlumber
* Scikit-learn (TF-IDF + Cosine Similarity)

## ⚙️ How It Works

1. Extract text from PDF
2. Split text into chunks
3. Convert text into vectors using TF-IDF
4. Convert user question into vector
5. Use cosine similarity to find best match
6. Return most relevant answer
