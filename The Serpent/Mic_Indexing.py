import pyaudio, os, wave, numpy as np   # type: ignore

p = pyaudio.PyAudio()

def is_working_microphone(device_index, rate=44100, seconds=1):
    try:
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=rate,
                        input=True,
                        frames_per_buffer=1024,
                        input_device_index=device_index)
        frames = []
        for _ in range(int(rate / 1024 * seconds)):
            data = stream.read(1024, exception_on_overflow=False)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        # Convert bytes to numpy array & check for non-silence
        audio_data = b''.join(frames)
        arr = np.frombuffer(audio_data, dtype=np.int16)
        return np.any(arr != 0)  # Returns True if there is non-zero audio
    except Exception as e:
        return False

def list_real_microphones():
    working = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        name = info.get('name', '').lower()
        # Heuristics: skip certain names
        skip_names = ['mapper', 'primary', 'stereo mix']
        if info.get('maxInputChannels', 0) > 0 and not any(skip in name for skip in skip_names):
            if is_working_microphone(i):
                print(f"Working microphone: {info.get('name')} , Device Index: {i}")
                working.append((i, info.get('name')))
            else:
                print(f"Non-working microphone: {info.get('name')} , Device Index: {i}")
    return working

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), "")

    try:
        real_mics = list_real_microphones()
        if not real_mics:
            print("No working microphones found!")
            exit(1)
        print("\nSelect a microphone:")
        for dev_index, name in real_mics:
            print(f"Microphone: {name} (Device Index: {dev_index})")
        choice = int(input("Enter the Device Index of the microphone to use: "))
        # Validate input: check if it's in real_mics
        if not any(dev_index == choice for dev_index, _ in real_mics):
            print("Invalid device index!")
            exit(1)

        def record_from_device(device_index, seconds, filename, rate=44100):
            stream = p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=rate,
                            input=True,
                            frames_per_buffer=1024,
                            input_device_index=device_index)
            print(f"Recording from device index {device_index}...")
            frames = []
            import math
            for _ in range(math.ceil(rate / 1024 * seconds)):
                data = stream.read(1024)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            wf = wave.open(filename, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            print(f"Saved {filename}")

        # Example usage:
        record_from_device(choice, 3, os.path.join(path, "output.wav"))
    finally:
        p.terminate()
