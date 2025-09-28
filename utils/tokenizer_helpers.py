from transformers import BertTokenizer, GPT2TokenizerFast
from config import BERT_MODEL_NAME
from config import GPT_MODEL_NAME
import statistics

# Load pretrained tokenizers: 
bert_tokenizer = BertTokenizer.from_pretrained(BERT_MODEL_NAME)
gpt_tokenizer = GPT2TokenizerFast.from_pretrained(GPT_MODEL_NAME)

def tokenize_and_compare(text):
    """
    Tokenizes the given text using BERT and GPT tokenizers,
    then returns statistics comparing both.
    """
    # Tokenize with BERT:
    bert_tokens = bert_tokenizer.tokenize(text)
    # Tokenize with GPT:
    gpt_tokens = gpt_tokenizer.tokenize(text)

    # Calculate statistics:
    bert_token_count = len(bert_tokens)
    gpt_token_count = len(gpt_tokens)

    comparison_stats = {
        "BERT": {
            "token_count": bert_token_count,
            "avg_token_length": statistics.mean([len(t) for t in bert_tokens]) if bert_tokens else 0,
            "tokens": bert_tokens
        },
        "GPT": {
            "token_count": gpt_token_count,
            "avg_token_length": statistics.mean([len(t) for t in gpt_tokens]) if gpt_tokens else 0,
            "tokens": gpt_tokens
        }
    }

    return comparison_stats

# Example usage when run directly:
if __name__ == "__main__":
    user_text = input("Enter text to tokenize and compare: ")
    stats = tokenize_and_compare(user_text)

    print("\n--- Tokenization Comparison ---")
    print(f"BERT Token Count: {stats['BERT']['token_count']}")
    print(f"GPT Token Count: {stats['GPT']['token_count']}")
    print(f"Average BERT Token Length: {stats['BERT']['avg_token_length']:.2f}")
    print(f"Average GPT Token Length: {stats['GPT']['avg_token_length']:.2f}")
