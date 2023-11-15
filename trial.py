import assemblyai as aai

aai.settings.api_key = f"Need a KEY"

def getValues(transcript: aai.RealtimeTranscript):
    prompt = "Which of the following directions is in the script (Straight/Left/Right)?"
    result1 = transcript.lemur.task(prompt)
    
    if result1 != "Straight" | "Left" | "Right":
        result1 == "Stop"
    
    prompt2 = "How many units is mentioned in the script? Mention the number only. In case of no number, output 0" 
    result2 = transcript.lemur.task(prompt2)

def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id)


def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(transcript.text, end="\r\n")
    else:
        print(transcript.text, end="\r")
        getValues(transcript)


def on_error(error: aai.RealtimeError):
    print("An error occured:", error)


def on_close():
    print("Closing Session")


transcriber = aai.RealtimeTranscriber(
    sample_rate=16_000,
    on_data=on_data,
    on_error=on_error,
    on_open=on_open,
    on_close=on_close,
)

transcriber.connect()

microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_000)
transcriber.stream(microphone_stream)

transcriber.close()
