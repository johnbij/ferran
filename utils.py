import streamlit as st


def render_proximamente(codigo):
    st.markdown(f"""
    <style>
    @keyframes pulse {{
        0%   {{ transform: scale(1);   opacity: 1; }}
        50%  {{ transform: scale(1.05); opacity: 0.8; }}
        100% {{ transform: scale(1);   opacity: 1; }}
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    .prox-card {{
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
        border-radius: 20px;
        padding: 50px 30px;
        text-align: center;
        color: white;
        animation: fadeIn 0.6s ease-out;
        margin: 20px 0;
    }}
    .prox-icon {{
        font-size: 70px;
        animation: pulse 2s infinite;
        display: block;
        margin-bottom: 15px;
    }}
    .prox-codigo {{
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 3px;
        color: #f0c040;
        margin-bottom: 10px;
    }}
    .prox-titulo {{
        font-size: 18px;
        opacity: 0.85;
        margin-bottom: 25px;
    }}
    .prox-badge {{
        display: inline-block;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 30px;
        padding: 8px 22px;
        font-size: 14px;
        letter-spacing: 1px;
    }}
    </style>

    <div class="prox-card">
        <span class="prox-icon">🚧</span>
        <div class="prox-codigo">{codigo}</div>
        <div class="prox-titulo">Esta clase está siendo preparada con cariño.</div>
        <div class="prox-badge">✨ Próximamente disponible</div>
    </div>
    """, unsafe_allow_html=True)


def render_multiple_choice_quiz(questions, key_prefix):
    for i, question in enumerate(questions, start=1):
        st.markdown(f"**{i}. {question['question']}**")
        option_keys = list(question["options"].keys())
        option_texts = question["options"]
        selected = st.radio(
            "Selecciona una alternativa:",
            options=["__none__"] + option_keys,
            format_func=lambda option, option_texts=option_texts: "— Elegir alternativa —" if option == "__none__" else f"{option}) {option_texts[option]}",
            key=f"{key_prefix}_q{i}",
        )

        if selected != "__none__":
            if selected == question["answer"]:
                st.success("✅ ¡Correcta!")
            else:
                st.error(f"❌ Incorrecta. La correcta es **{question['answer']}**.")
            st.caption(f"🛠️ Mini-corrección: {question['explanation']}")

        if i < len(questions):
            st.markdown("---")
