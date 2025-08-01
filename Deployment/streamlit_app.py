import streamlit as st
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import re
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


# --- Set Page Config First ---
st.set_page_config(
    page_title="Asisten Virtual BPJS",
    layout="centered",
    initial_sidebar_state="expanded"
)


load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEEPSEEK_API_NEW=os.getenv("DEEPSEEK_API_NEW")


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", # Ini adalah model embedding yang direkomendasikan
    google_api_key=GOOGLE_API_KEY,
)


@st.cache_resource
def init_mongodb():
    try:
        client = MongoClient(MONGODB_URI)
        client.server_info()
        return client['finalproject_db']['faq_tb']
    except Exception as e:
        st.error(f"⚠️ Gagal terhubung ke database: {str(e)}")
        st.stop()

collection = init_mongodb()


# Vector Store Configuration
vector_store = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name='vector_index',
)


# Prompt Template
PROFESSIONAL_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Anda adalah Asisten Virtual Resmi BPJS Indonesia.

    Peran Anda:
    Anda bertindak sebagai Customer Service (Layanan Pelanggan) untuk membantu masyarakat dalam memahami layanan dan prosedur dari:
    - Website BPJS Kesehatan
    - FAQ BPJS Ketenagakerjaan
    - FAQ Aplikasi JKN Mobile

    Tugas & Tanggung Jawab:
    1. Memberikan jawaban akurat, terpercaya, dan relevan sesuai dengan data dari sumber resmi (FAQ).
    2. Menjelaskan prosedur atau solusi dengan cara yang mudah dimengerti, terstruktur, dan menggunakan Bahasa Indonesia baku.
    3. Menjadi perantara informasi yang ramah, efisien, dan profesional dalam menangani keluhan atau pertanyaan pengguna.
    4. Jawablah dengan ringkas, jangan menjawab hal yang tidak ditanyakan

    Aturan yang Wajib Dipatuhi:
    1. Jawab hanya berdasarkan informasi yang tersedia dalam dokumen FAQ resmi.
    2. Jangan mengarang jawaban atau memberikan informasi tambahan yang tidak tercantum dalam sumber resmi.
    3. Jika pertanyaan tidak relevan atau tidak tersedia dalam data, sampaikan secara sopan bahwa Anda tidak memiliki informasi tersebut.
    4. Dilarang mencantumkan** tautan eksternal, nomor telepon, alamat, atau informasi pribadi lain yang tidak ada dalam dokumen FAQ.
    5. Gunakan:
    - Penomoran (1., 2., 3., dst)** untuk menjelaskan langkah atau prosedur berurutan.
    - Simbol bullet (•) untuk daftar yang tidak berurutan.

    Konteks resmi:
    {context}

    Pertanyaan: {question}

    Jawaban profesional:
    """
)

# Config model deepseek
llm_deepseek = ChatOpenAI(
    model="deepseek-chat",  # sesuaikan dengan model yang tersedia
    openai_api_key=DEEPSEEK_API_NEW,  # dari DeepSeek langsung
    base_url="https://api.deepseek.com/v1",  # ganti sesuai endpoint resmi dari DeepSeek
    temperature=0,
    max_tokens=500
)

qa = RetrievalQA.from_chain_type(
    llm=llm_deepseek,
    chain_type="stuff",
    retriever=vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3,
            "score_threshold": 0.80
        }
    ),
    chain_type_kwargs={"prompt": PROFESSIONAL_PROMPT},
)

def clean_answer(text):
    """Hilangkan tanda bold/italic Markdown"""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    cleaned_text = re.sub(r'\n{3,}', '\n\n', text)
    return cleaned_text.strip()

# Judul
st.title('👩‍✈️ Virtual Asisten BPJS Indonesia')
# Sub header
st.subheader("Halo Selamat Datang di Asisten Virtual BPJS Indonesia, Aplikasi ini dibuat dengan tujuan memberikan informasi seputar BPJS Indonesia")

# Input Chat
prompt = st.chat_input("Tulis pertanyaan anda disini....")

if prompt:
    # Proses jawaban
    with st.spinner("🔎 Loading pencarian informasi..."):
        try:
            result = qa.invoke({"query": prompt})
            answer = result['result'].strip()
            st.write("🕵️ Pertanyaan Anda:")
            st.write(prompt)
            st.write("🤖 Jawaban")
            st.write(clean_answer(result['result']))

        except Exception as e:
            answer = f"⚠️ Mohon Maaf Terdapat Gangguan {str(e)}\nSilahkan coba lagi atau hubungi 165"
            st.write(answer)

with st.sidebar:
    st.markdown("# **BPJSChaBo**")
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
                BPJSChaBo adalah aplikasi/chatbot BPJS berbasis AI yang berfungsi untuk membantu pelayanan user atau calon user dalam mendapatkan informasi seputar BPJS Kesehatan  seperti layanan informasi pembuatan ID atau keanggotaan, hingga layanan informasi pembayara dan informasi lainnya.
                BPJSChaBo memberikan informasi sesuai dengan pertanyaan seputar BPJS sesuai inputan dari user
    </div>""", unsafe_allow_html=True)


    st.markdown("### Kontak Kami :")
    st.markdown("""
    Jika anda tertarik dengan projek kami, anda bisa temukan kami di kontak berikut:
    
    • [Ach. Anwar Idam Fanani](mailto:ifananwar001@gmail.com) 💌
    
    • [Andro Kwok](mailto:kwokandro@gmail.com) 💌
    
    • [Fadhola Asandi Mardika Putra](mailto:fadholasandi@gmail.com) 💌
    
    • [Gilang Pramata Wardhana](mailto:gilangpramata@gmail.com) 💌
    
    • [Riko Fadilah Alam](mailto:rikofalam.work@gmail.com) 💌
    
    Mari berkolaborasi bersama untuk perkembangan Teknologi Indonesia 🇮🇩
    """)