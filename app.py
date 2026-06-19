import streamlit as st
import numpy as np
import json
import os
from PIL import Image

st.set_page_config(page_title="🦋 Butterfly Classifier", page_icon="🦋", layout="centered")

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.main{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.hero{
    text-align:center;
    padding:2rem 1rem;
}

.hero-title{
    font-size:3.2rem;
    font-weight:700;
    background:linear-gradient(90deg,#4ade80,#22d3ee);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    color:#cbd5e1;
    font-size:1.05rem;
}

.result-card{
    background:rgba(255,255,255,0.06);
    backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:24px;
    padding:25px;
    text-align:center;
    margin-top:15px;
}

.species{
    font-size:2.2rem;
    font-weight:700;
    color:#4ade80;
}

.conf-label{
    color:white;
    font-size:1.1rem;
    margin-top:10px;
}

.top5-row{
    display:flex;
    align-items:center;
    gap:10px;
    margin:10px 0;
}

.rank{
    color:#94a3b8;
    width:30px;
}

.bar-wrap{
    flex:1;
    height:8px;
    background:#334155;
    border-radius:999px;
    overflow:hidden;
}

.bar-fill{
    height:100%;
    background:linear-gradient(90deg,#22c55e,#06b6d4);
}

.pct{
    width:60px;
    text-align:right;
    color:white;
}

.stButton>button{
    width:100%;
    border-radius:15px;
    height:50px;
    font-size:16px;
    font-weight:600;
}

[data-testid="stImage"] img{
    border-radius:20px;
    border:2px solid rgba(255,255,255,0.15);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">🦋 Butterfly Vision AI</div>
    <p class="hero-sub">
        Upload a butterfly image and let AI identify the species instantly
    </p>
</div>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner="Loading model…")
def load_model():

    import onnxruntime as ort

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(BASE_DIR, "butterfly_model.onnx")
    names_path = os.path.join(BASE_DIR, "class_names.json")

    if not os.path.exists(model_path):
        return None, None, None, f"❌ Model not found: {model_path}"

    if not os.path.exists(names_path):
        return None, None, None, f"❌ Class file not found: {names_path}"

    try:
        session = ort.InferenceSession(model_path)

        input_name = session.get_inputs()[0].name

        with open(names_path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        class_names = {
            str(k): v for k, v in raw.items()
        }

        return session, input_name, class_names, None

    except Exception as e:
        return None, None, None, f"❌ Error: {e}"


session, input_name, class_names, load_error = load_model()

if load_error:
    st.error(load_error)
    st.info("📂 Make sure `butterfly_model.onnx` and `class_names.json` are in the root of your GitHub repo.")
    st.stop()

st.success(
    f"AI Model Loaded Successfully • {len(class_names)} Species Available"
)

st.divider()

st.markdown("### 📤 Upload Butterfly Image")

uploaded = st.file_uploader("Upload a butterfly image", type=["jpg", "jpeg", "png", "webp"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    fmt = img.format or uploaded.name.rsplit(".", 1)[-1].upper()

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.image(img, use_container_width=True, caption=f"{uploaded.name} · {img.size[0]}×{img.size[1]} · {fmt}")

    with col2:
        if st.button("🔍 Identify Species", use_container_width=True, type="primary"):
            with st.spinner("Analysing…"):
                img_resized = img.resize((150, 150))
                arr = np.array(img_resized, dtype=np.float32) / 255.0
                arr = np.expand_dims(arr, axis=0)

                preds = session.run(None, {input_name: arr})[0][0]
                top5  = np.argsort(preds)[::-1][:5]
                best_label = class_names.get(str(top5[0]), f"Class {top5[0]}")
                best_conf  = round(float(preds[top5[0]]) * 100, 1)

            st.markdown(f"""
            <div class="result-card">
                <div class="species">{best_label.title()}</div>
                <div class="conf-label">Confidence: {best_conf}%</div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(best_conf / 100)

            st.markdown("#### Top 5 Predictions")
            rows_html = ""
            for idx in top5:
                label = class_names.get(str(idx), f"Class {idx}").title()
                conf  = round(float(preds[idx]) * 100, 1)
                rows_html += f"""
                <div class="top5-row">
                    <span class="rank">#{top5.tolist().index(idx)+1}</span>
                    <span style="flex:2">{label}</span>
                    <div class="bar-wrap"><div class="bar-fill" style="width:{conf}%"></div></div>
                    <span class="pct">{conf}%</span>
                </div>"""
            st.markdown(rows_html, unsafe_allow_html=True)
        else:
            st.info("👆 Click **Identify Species** to classify")

st.divider()
st.markdown("""
<hr>
<div style='text-align:center;color:#94a3b8'>
🦋 Butterfly Vision AI <br>
Powered by CNN + ONNX Runtime
</div>
""", unsafe_allow_html=True)