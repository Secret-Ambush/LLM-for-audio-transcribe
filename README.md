# Transcribe Streaming Audio from a Microphone in Python

Learn how to transcribe streaming audio using Real-Time Transcription in Python.

## Overview

By the end of this tutorial, you'll be able to transcribe audio from your microphone in Python.

### Before You Begin

To complete this tutorial, you need:

- Python installed.
- An AssemblyAI account with a credit card set up.

Here's the full sample code of what you'll build in this tutorial:

```python
# Insert the provided Python code here
```

## Step 1: Install Dependencies

### 1. PortAudio Installation

- macOS: `brew install portaudio`
- Linux: apt install portaudio19-dev

### 2. Install Python Package

Install the package via pip. Extras enable additional features, such as streaming audio from a microphone.

```bash
pip install "assemblyai[extras]"
```

## Step 2: Configure the API Key

In this step, you'll create an SDK client and configure it to use your API key.

1. Browse to your AssemblyAI Account and copy your API token.
2. Configure the SDK to use your API key by replacing `YOUR_API_KEY` with your copied API key in the Python code.

```python
# Python code snippet for configuring the API key
```

## Step 3: Create a Transcriber

In this step, set up a real-time transcriber object and callback functions to handle different events.

1. Create functions to handle events from the real-time transcriber.
2. Create a function to handle transcripts (RealtimeFinalTranscript and RealtimePartialTranscript).
3. Create a new `RealtimeTranscriber` using the functions created.

```python
# Python code snippet for creating the transcriber and defining callback functions
```

### Sample Rate Recommendations

The `sample_rate` is crucial for audio quality and network data. Recommended sample rates:
- Minimum quality: 8_000 (8 kHz)
- Medium quality: 16_000 (16 kHz)
- Maximum quality: 48_000 (48 kHz)

## Step 4: Connect the Transcriber

Real-Time Transcription uses WebSockets to stream audio to AssemblyAI. Connect to the API.

```python
# Python code snippet to connect the transcriber
```

## Step 5: Record Audio from Microphone

Configure your Python app to record audio from the microphone using the provided helper class.

```python
# Python code snippet to open a microphone stream and start sending data
```

## Step 6: Close the Connection

Finally, close the connection to disconnect the transcriber.

```python
# Python code snippet to close the connection
```

---

