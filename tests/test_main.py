import pytest
from utils.llm_helpers import safe_api_call
from utils.tokenizer_helpers import tokenize_and_compare
from utils.advanced_features import analyze_sentiment, text_statistics

def test_summarization():
    text = "This is a simple example text."
    summary = safe_api_call(text)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_tokenizer():
    text = "This is a test."
    tokens = tokenize_and_compare(text)
    assert "BERT" in tokens and "GPT" in tokens

def test_sentiment():
    text = "I love programming!"
    sentiment = analyze_sentiment(text)
    assert "label" in sentiment

def test_statistics():
    text = "This is a test sentence. Another sentence here."
    stats = text_statistics(text)
    assert "word_count" in stats and stats["word_count"] > 0
