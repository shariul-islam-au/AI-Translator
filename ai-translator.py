from mcp.server.fastmcp import FastMCP
import os
import csv

# Create an MCP server
mcp = FastMCP("AI Translator")

bangla_sms_file = os.path.join(os.path.dirname(__file__), "bangla_sms.csv")

english_sms_file = os.path.join(os.path.dirname(__file__), "english_sms.csv")
banglish_sms_file = os.path.join(os.path.dirname(__file__), "banglish_sms.csv")
code_mix_sms_file = os.path.join(os.path.dirname(__file__), "code_mixed_sms.csv")
sinhala_sms_file = os.path.join(os.path.dirname(__file__), "sinhala_sms.csv")
mandarin_sms_file = os.path.join(os.path.dirname(__file__), "mandarin_sms.csv")

def ensure_files():
    if not os.path.exists(english_sms_file):
        with open(english_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(banglish_sms_file):
        with open(banglish_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(code_mix_sms_file):
        with open(code_mix_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(sinhala_sms_file):
        with open(sinhala_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(mandarin_sms_file):
        with open(mandarin_sms_file, "w", encoding="utf-8") as f:
            f.write("")

ensure_files()

def read_sms_range(start: int, end: int) -> str:
    """Reads Bangla SMS dataset and returns only the specified range as CSV."""
    with open(bangla_sms_file, "r", encoding="utf-8", newline='') as f:
        reader = list(csv.reader(f))    
    data_rows = reader[:]    
    selected_rows = data_rows[start+1:end+1]    
    # Convert back to CSV string
    from io import StringIO
    output = StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    
    writer.writerows(selected_rows)
    
    return output.getvalue().strip()

@mcp.tool()
def bangla_2_english_range(start: int, end: int) -> str:
    """
    Reads Bangla SMS dataset (bangla_sms.txt) and prepares a translation prompt
    for only the given row range.
    """
    csv_data = read_sms_range(start, end)

    prompt = f"""
            You are a CSV translator.
            Here is a CSV of Bangla SMS messages.
            Translate ONLY the message text (last column) into English.
            Keep:
            - same index (first column)
            - same label (second column)
            - translated text in double quotes
            - replace Bangladeshi Taka sign (৳) with "TK"

            CSV:
            {csv_data}
            """
    return prompt.strip()

@mcp.tool()
def save_english_sms(translated_sms: str) -> str:
    """
    Saves translated SMS data to a text file.
    """
    with open(english_sms_file, "a", encoding="utf-8") as f:
        f.write(translated_sms + "\n")
    return "SMS saved!"


@mcp.tool()
def bangla_2_banglish_range(start: int, end: int) -> str:    
    """
    Reads Bangla SMS dataset (bangla_sms.txt) and prepares a translation prompt
    for only the given row range.
    """
    csv_data = read_sms_range(start, end)

    prompt = f"""
            You are a CSV translator.
            Here is a CSV of Bangla SMS messages.
            Translate ONLY the message text (last column) into Banglish.
            Keep:
            - same index (first column)
            - same label (second column)
            - translated text in double quotes
            - replace Bangladeshi Taka sign (৳) with "TK"

            CSV:
            {csv_data}
            """
    return prompt.strip()

@mcp.tool()
def save_banglish_sms(translated_sms: str) -> str:
    """
    Saves translated SMS data to a text file.
    """
    with open(banglish_sms_file, "a", encoding="utf-8") as f:
        f.write(translated_sms + "\n")
    return "SMS saved!"


@mcp.tool()
def bangla_2_code_mixed_range(start: int, end: int) -> str:   
    """
    Reads Bangla SMS dataset (bangla_sms.txt) and prepares a translation prompt
    for only the given row range.
    """
    csv_data = read_sms_range(start, end)
    
    prompt = f"""
            You are a CSV translator.
            Here is a CSV of Bangla SMS messages.
            Translate ONLY the message text (last column) into Bangla and English Code mixed.
            Ensure the translation is a mix of Bangla and English words.
            The translation should be a mix of Bangla and English words, maintaining the context and meaning
            of the original message. The goal is to create a code-mixed version that is natural
            and easy to understand for speakers of both languages.
            Keep:
            - same index (first column)
            - same label (second column)
            - translated text in double quotes (third column)
            - try to maintain Bangla and English words in equal proportion

            Examples:
            Input → Output
            0,smish,সোনালী ব্যাংক অ্যাকাউন্টে সমস্যা হয়েছে। কল করুন: +8801818788890 → 0,smish,"সোনালী Bank account-এ problem হয়েছে। Call করুন: +8801818788890"
            1,smish,ক্রিপ্টো বিনিয়োগে লাভবান হন! আজই শুরু করুন: http://bit.ly/CryptoInvest → 1,smish,"Crypto investment-এ লাভবান হন! আজই শুরু করুন: http://bit.ly/CryptoInvest"
            2,promo,"স্পেশাল ডিল শেষ দিন,৩০জিবি @৩০০৳,৩০দিন! আজই নাও- cutt.ly/jwkuSC76" → 2,promo,"Special deal শেষ দিন, 30GB @300৳, 30দিন! আজই নাও- cutt.ly/jwkuSC76"
            3,promo,ফার্নিচারে মেগা সেল! সব পণ্যে ১৫-৩০% ছাড়। আজই ভিজিট করুন। → 3,promo,"Furniture-এ Mega sale! সব পণ্যে 15-30% discount। আজই visit করুন।"
            4,smish,আপনার ব্যাংক কার্ডটি অবিলম্বে আপডেট করুন। এখানে ক্লিক করুন: [verifybankcard.com/UpdateBD] → 4,smish,"আপনার Bank cardটি অবিলম্বে update করুন। এখানে click করুন: [verifybankcard.com/UpdateBD]"


            Now Translate the Following:
                        CSV:
                        {csv_data}
                        """
    return prompt.strip()

@mcp.tool()
def save_code_mixed_sms(translated_sms: str) -> str:
    """
    Saves translated SMS data to a text file.
    """
    with open(code_mix_sms_file, "a", encoding="utf-8") as f:
        f.write(translated_sms + "\n")
    return "SMS saved!"


@mcp.tool()
def bangla_2_sinhala_range(start: int, end: int) -> str:   
    """
    Reads Bangla SMS dataset (bangla_sms.txt) and prepares a translation prompt
    for only the given row range.
    """
    csv_data = read_sms_range(start, end)
    
    prompt = f"""
            You are a CSV translator.
            Here is a CSV of Bangla SMS messages.
            Translate ONLY the message text (last column) into Sinhala.
            Keep:
            - same index (first column)
            - same label (second column)
            - translated text in double quotes
            - replace Bangladeshi Taka sign (৳) with "LKR"

            CSV:
            {csv_data}
            """
    return prompt.strip()

@mcp.tool()
def save_sinhala_sms(translated_sms: str) -> str:
    """
    Saves translated SMS data to a text file.
    """
    with open(sinhala_sms_file, "a", encoding="utf-8") as f:
        f.write(translated_sms + "\n")
    return "SMS saved!"

@mcp.tool()
def bangla_2_mandarin_range(start: int, end: int) -> str:
    """
    Reads Bangla SMS dataset (bangla_sms.txt) and prepares a translation prompt
    for only the given row range.
    """
    csv_data = read_sms_range(start, end)

    prompt = f"""
            You are a CSV translator.
            Here is a CSV of Bangla SMS messages.
            Translate ONLY the message text (last column) into Mandarin Chinese.
            Keep:
            - same index (first column)
            - same label (second column)
            - translated text in double quotes
            - replace Bangladeshi Taka sign (৳) with "CNY"

            CSV:
            {csv_data}
            """
    return prompt.strip()

@mcp.tool()
def save_mandarin_sms(translated_sms: str) -> str:
    """
    Saves translated SMS data to a text file.
    """
    with open(mandarin_sms_file, "a", encoding="utf-8") as f:
        f.write(translated_sms + "\n")
    return "SMS saved!"