

# BPJSChaBo

**Tanya BPJS, Dijawab Bot!**

<!-- <p align="center">
  <img src="logo-bpjschabo.png" width=350 align="center">
</p> -->
<h1 align="center">Hi Everyone 👋, We are Team 3 FTDS RMT 043 Final Project 2025</h1>
By Ach. Anwar Idam Fanani, Andro Kwok, Fadhola Asandi Mardika Putra, Gilang Pramata Wardhana, Riko Fadilah Alam

---

## Dataset & Sumber Data

Kami mengumpulkan data pertanyaan dan jawaban dari sumber-sumber resmi BPJS:

* [BPJS Kesehatan](https://www.bpjs-kesehatan.go.id/)
* [FAQ BPJS Ketenagakerjaan](https://www.bpjsketenagakerjaan.go.id/)
* [FAQ Aplikasi Mobile JKN]

Data dikumpulkan melalui proses **scraping**, **manual collection**, dan **cleaning** untuk membentuk dataset tanya-jawab yang siap dilatih dengan model NLP.

---

## Deployment Link

🌐 [Click here to access the app](https://huggingface.co/spaces/ifananwar/p2-final-project-ftds-043-rmt-group-003)

---

## App Description

BPJSChaBo is an AI-powered chatbot designed to assist users in finding answers about **BPJS Kesehatan** and **BPJS Ketenagakerjaan** in a user-friendly, real-time manner.

### Features:

* Membantu pelayanan user atau calon user dalam mendapatkan informasi seputar BPJS Kesehatan.
* Memberikan informasi sesuai dengan pertanyaan seputar BPJS sesuai inputan dari user.
* Akses mudah bagi lansia dan masyarakat awam tanpa perlu login aplikasi resmi.

---

## Background & Problem Statement

> Lembaga BPJS Kesehatan dan Ketenagakerjaan menerima jutaan klaim dan pertanyaan tiap tahun, namun proses pencarian informasi masih terhambat sistem yang kurang ramah pengguna.

Banyak masyarakat mengeluhkan akses informasi yang **tidak intuitif**, **sulit dipahami**, atau **kurang cepat**, terutama bagi pengguna lansia dan masyarakat dengan keterbatasan teknologi.

**Justifikasi:**

* [HukumOnline - Masyarakat Sulit Akses JKN](https://www.hukumonline.com/berita/a/masyarakat-kesulitan-mengakses-informasi-jkn-lt532128516421a)
* [LiputanBekasi - Transisi JKN Kurang Edukatif](https://www.liputanbekasi.com/nasional/1267764791/transisi-layanan-aplikasi-mobile-jks-dinilai-kurang-edukasi-pasien-lansia-keluhkan-sulit-akses-sendiri)

---

## Objective

Mengembangkan chatbot berbasis **Natural Language Processing (NLP)** dengan tujuan:

* Meningkatkan kemudahan akses informasi terkait layanan BPJS.
* Mengurangi beban call center dan antrian informasi.
* Menyediakan jawaban **cepat, akurat, dan real-time**.

---

## Target User

* Pengguna BPJS Kesehatan & Ketenagakerjaan
* Calon peserta BPJS
* Keluarga peserta lansia
* Masyarakat umum yang membutuhkan informasi BPJS

---

## Methodology

### Flow of Work:

```
Scraping/Manual Collection (FAQ BPJS) 
    ↓
Cleaning + Labeling + Mergering
    ↓
Dataset Finalisasi
    ↓
Database MongoDB
    ↓
EDA & Visualisasi
    ↓
Modeling NLP 
    ↓
Model Evaluation
    ↓
Deploy (Streamlit/Huggingface)
```


## Interaction Example

<p align="center">
  <img src="./readme/deploy.png" width=700>
</p>

---

## 📊 Exploratory Data Analysis (EDA)

<p align="center">
  <img src="./readme/eda1.png" width=700>
</p>
<p align="center">
  <img src="./readme/eda2.png" width=700>
</p>

Contoh visualisasi yang dilakukan untuk memahami distribusi karakter (question & answer) dan pola entitas yang sering ditanyakan berdasarkan most common words.

---

## Method & Technology Used for Modeling

- **Python, Pandas,**
- **LangChain** for RAG pipeline
- **gemini-15-flash-latest**
- **Deepseek-V3**
- **Deepseek-R1**
- **MongoDB Atlas Vector Search** as the NoSQL vector database
- **Streamlit** for UI development
- **Hugging Face** for web deployment hosting
  
---

## Model Evaluation

| Model     | Strengths                                              | Weaknesses                                                       |
|-----------|--------------------------------------------------------|------------------------------------------------------------------|
| Deepseek-V3   | Lower Cost. Lighter Model, Medium Accuracy |  Fast speed     |
| Deepseek-R1   |  Good Accuracy |  Low speed, Weight Model    |
| Gemini    | High Speed responses. Lower Cost. Lighter model.  | Slightly Lower Accuracy than Pro version.                   |



---

## 📘 Slide Presentation

<p align="center">
  <a href="https://docs.google.com/presentation/d/11rrHIzQ6qqF1QIHMiuL6ctJ3hdtoi2ARr1SD6O8K4OE/edit?slide=id.g37057aa0036_8_27#slide=id.g37057aa0036_8_27">
    <img src="https://images.fonearena.com/blog/wp-content/uploads/2018/10/Google-Slides-e1539062763406.jpg" alt="Google Slides" width="70" height="70">
  </a>
</p>

---

## 👨‍💻 Contributors
1. [Ach. Anwar Idam Fanani - Github](https://github.com/ifananwar)
2. [Andro Kwok - Github](https://github.com/Andro1406)
3. [Fadhola Asandi Mardika Putra - Github](https://github.com/Fadhola)
4. [Gilang Pramata Wardhana - GitHub](https://github.com/GilangPramata)
4. [Riko Fadilah Alam - GitHub](https://github.com/rfalam2211)

---

<h3 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Lobster&color=00ADB5&size=50&center=true&vCenter=true&width=1000&height=70&duration=5000&lines=Thanks+for+checking+out+BPJSChaBo!;+Stay+informed,+stay+healthy!" />
</h3>

---
