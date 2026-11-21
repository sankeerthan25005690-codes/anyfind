
# ==========================================
# YOUTUBE SUBTITLE EXTRACTION USING NLP
# ==========================================

# STEP 1: Import libraries

from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from nltk.tokenize import sent_tokenize


# STEP 2: Download NLP resources

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)


# STEP 3: YouTube Video ID

video_id = "dQw4w9WgXcQ"

print("======================================")
print("     YOUTUBE NLP SUBTITLE EXTRACTOR")
print("======================================")

print("Selected Video ID:", video_id)
print("Fetching subtitles...")


try:

    # STEP 4: Retrieve subtitles

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)


    # STEP 5: Extract subtitle text

    full_text = " ".join(
        snippet.text for snippet in transcript
    )


    # STEP 6: Apply NLP sentence tokenization

    sentences = sent_tokenize(full_text)


    # STEP 7: Display subtitles

    print("\n========== YOUTUBE SUBTITLES ==========\n")

    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")


    # STEP 8: NLP analysis

    words = full_text.split()

    print("\n========== NLP ANALYSIS ==========")

    print("Total Sentences:", len(sentences))
    print("Total Words:", len(words))


    # STEP 9: Display complete transcript

    print("\n========== COMPLETE TRANSCRIPT ==========\n")

    print(full_text)


except Exception as e:

    print("\nUnable to retrieve subtitles.")
    print("Error:", e)

    print("Check whether subtitles are available.")


# ==========================================
# END OF PROJECT
# ==========================================
