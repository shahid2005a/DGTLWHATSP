import webbrowser
import urllib.request
import json

# --- DGTL CYBER Bio Data ---
bio = """
🔥 SHAHID AFRIDI (ARYAN AFRIDI) 🔥
🛡️ Aspiring Cybersecurity Engineer | Ethical Hacking
🎯 DGTL CYBER Family

💡 Skills: Penetration Testing, Vulnerability Assessment,
   Web/Network/Cloud Security, OSINT, Malware Analysis

🔗 Instagram: @dgtlcyberblog
🔗 GitHub: shahid2005a
🔗 Telegram: GsmhackerBot, encrypt_code_decode_Bot
"""

links = [
    "https://www.instagram.com/dgtlcyberblog",
    "https://t.me/GsmhackerBot",
    "https://t.me/encrypt_code_decode_Bot",
    "https://looduking.kesug.com",
    "https://firebasehack.wuaze.com",
    "https://dgtlstore.xo.je",
    "https://github.com/shahid2005a",
]

def github_bio():
    """GitHub se live bio fetch karo"""
    try:
        url = "https://api.github.com/users/shahid2005a"
        with urllib.request.urlopen(url) as r:
            data = json.load(r)
        return f"👤 {data.get('name')}\n📝 {data.get('bio')}\n🔗 {data.get('html_url')}"
    except Exception as e:
        return f"GitHub fetch fail: {e}"

def show_bio():
    print("=" * 45)
    print("        DGTL CYBER — BIO DATA")
    print("=" * 45)
    print(bio)
    print("\n--- GitHub Live Data ---")
    print(github_bio())
    print("=" * 45)

def open_all():
    print("\n🚀 Saare links browser me open ho rahe hain...\n")
    for link in links:
        print(f"  → {link}")
        webbrowser.open_new_tab(link)

if __name__ == "__main__":
    show_bio()
    open_all()
    print("\n✅ Done bhai! Browser me sab khul gaya.")