# AI-Translator: MCP-Based Multilingual SMS Translation Pipeline

A Model Context Protocol (MCP) server for translating Bengali SMS messages into multiple linguistic varieties using Claude (Anthropic). Developed as part of the **SmishDetect-LLM** research framework for multilingual SMS phishing (smishing) detection.

## Overview

This tool automates the translation of a Bengali SMS dataset into three additional linguistic formats to support multilingual smishing detection research:

| Target Language | Description | Tool Function |
|----------------|-------------|---------------|
| **English** | Full semantic translation | `bangla_2_english_range()` |
| **Banglish** | Romanized Bengali (Latin script) | `bangla_2_banglish_range()` |
| **Code-Mixed** | Bengali-English code-switched text | `bangla_2_code_mixed_range()` |

## Architecture

The translation pipeline is built on the **Model Context Protocol (MCP)** framework, which enables structured, reproducible prompt engineering for each linguistic variety. Each translation type is handled by a dedicated MCP tool with domain-specific instructions and, in the case of code-mixed translation, few-shot examples to guide authentic code-switching generation.

```
bangla_sms.csv → MCP Server (ai-translator.py) → Claude (Anthropic)
                                                      ↓
                                          english_sms.csv
                                          banglish_sms.csv
                                          code_mixed_sms.csv
```

## Files

| File | Description |
|------|-------------|
| `ai-translator.py` | MCP server with translation tool definitions and prompt templates |
| `csv_reader.py` | Utility for reading SMS dataset in batch ranges |
| `bangla_sms.csv` | Source Bengali SMS dataset |
| `english_sms.csv` | Translated English output |
| `banglish_sms.csv` | Translated Banglish output |
| `code_mixed_sms.csv` | Translated Code-Mixed output |

## Requirements

- Python 3.10+
- `mcp` library (`pip install mcp`)
- Claude Desktop or Claude Code with MCP support

## Usage

1. Ensure `bangla_sms.csv` is in the same directory as `ai-translator.py`
2. Configure the MCP server in your Claude client
3. Use the translation tools with batch ranges:
   - `bangla_2_english_range(start=0, end=50)` → Translates rows 0–50 to English
   - `bangla_2_banglish_range(start=0, end=50)` → Translates rows 0–50 to Banglish
   - `bangla_2_code_mixed_range(start=0, end=50)` → Translates rows 0–50 to Code-Mixed
4. Save results using corresponding `save_*_sms()` functions

## Prompt Design

Each translation tool constructs a structured prompt that instructs Claude to:
- Preserve the CSV structure (row index, class label)
- Translate only the message text column
- Handle currency symbols appropriately (৳ → TK)
- Maintain class-specific characteristics (smishing urgency markers, promotional patterns)

The code-mixed prompt additionally includes **few-shot examples** demonstrating authentic Bengali-English code-switching conventions.

## Citation

If you use this tool in your research, please cite:

```
@mastersthesis{shariul2025smishdetect,
  title={SmishDetect-LLM: Multilingual SMS Security Framework},
  author={Shariul Islam},
  year={2025},
  school={Murdoch University}
}
```

## Related

- **SmishDetect-LLM Repository:** [github.com/shariul-islam-au/SmishDetect-LLM](https://github.com/shariul-islam-au/SmishDetect-LLM)
- **Bengali SMS Smishing Dataset:** [HuggingFace](https://huggingface.co/datasets/shariul-islam-au/bengali-sms-smishing-dataset)

## License

This project is part of academic research. Please contact the author for usage permissions.
