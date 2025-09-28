import streamlit as st
from utils.llm_helpers import safe_api_call        # Summarization
from utils.tokenizer_helpers import tokenize_and_compare  # BERT & GPT tokenization
from utils.advanced_features import analyze_sentiment, text_statistics  # Sentiment & stats

# --- Streamlit Page Config ---
st.set_page_config(page_title="Text Analysis Tool", page_icon="📝", layout="wide")

# --- App Title ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📝 Text Analysis Tool</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Analyze your text with summarization, tokenization comparison, sentiment analysis, and readability statistics.</p>", unsafe_allow_html=True)

# --- Input Section ---
user_text = st.text_area("**Enter your text below:**", height=200, placeholder="Type or paste your text here...")

if st.button("🚀 Analyze"):
    if not user_text.strip():
        st.warning("⚠️ Please enter some text before analyzing.")
    else:
        # --- Summarization ---
        with st.spinner("⏳ Summarizing your text..."):
            summary = safe_api_call(user_text)

        # --- Tokenization ---
        with st.spinner("⏳ Tokenizing using BERT and GPT..."):
            token_stats = tokenize_and_compare(summary)

        # --- Sentiment ---
        with st.spinner("⏳ Analyzing sentiment..."):
            sentiment_result = analyze_sentiment(user_text)

        # --- Text Statistics ---
        with st.spinner("⏳ Calculating text statistics..."):
            stats_result = text_statistics(user_text)

        # --- Display Results ---
        st.markdown("---")
        st.markdown("### 🔹 **Summarized Text**")
        st.success(summary)

        # --- Tokenization ---
        st.markdown("### 🔹 **Tokenization Comparison**")
        st.write(f"**BERT Token Count:** {token_stats['BERT']['token_count']} | **GPT Token Count:** {token_stats['GPT']['token_count']}")

        bert_tokens_preview = token_stats['BERT']['tokens'][:20]
        gpt_tokens_preview = token_stats['GPT']['tokens'][:20]

        col3, col4 = st.columns(2)
        with col3:
            st.markdown("**BERT Tokens Preview (first 20):**")
            st.code(", ".join(bert_tokens_preview))
        with col4:
            st.markdown("**GPT Tokens Preview (first 20):**")
            st.code(", ".join(gpt_tokens_preview))

        # --- Sentiment ---
        st.markdown("### 🔹 **Sentiment Analysis**")
        st.info(f"**Label:** {sentiment_result['label']} | **Confidence Score:** {sentiment_result['score']:.2f}")

        # --- Text Statistics (below sentiment, not side by side) ---
        st.markdown("### 🔹 **Text Statistics**")
        st.write(f"**Word Count:** {stats_result['word_count']}")
        st.write(f"**Sentence Count:** {stats_result['sentence_count']}")
        st.write(f"**Average Sentence Length:** {stats_result['avg_sentence_length']:.2f} words")
        st.write(f"**Flesch Reading Ease:** {stats_result['flesch_reading_ease']:.2f}")

        # Display top words in a nice compact format
        st.markdown("**Top 10 Words:**")
        st.markdown(
            "<div style='display: flex; flex-wrap: wrap; gap: 10px;'>"
            + "".join([f"<span style='background:#f0f0f0; padding:5px 10px; border-radius:5px;'>{word}: {count}</span>" for word, count in stats_result['top_words']])
            + "</div>",
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.success("✅ **Analysis Complete!**")
