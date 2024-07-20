import gi
gi.require_version('Gst', '1.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gst, GObject
import signal

# Initialize GStreamer
Gst.init(None)

# Define the GStreamer pipeline
pipeline_str = """
    playbin uri=rtsp://admin:ntipl12345@192.168.1.108:554 flags=0x00000008 retry-max=3 retry-delay=5000 video-sink=autovideosink
"""
pipeline = Gst.parse_launch(pipeline_str)

# Set up a signal handler to handle KeyboardInterrupt
def handle_keyboard_interrupt(sig, frame):
    pipeline.set_state(Gst.State.NULL)
    print("KeyboardInterrupt: Pipeline stopped.")
    exit(0)

signal.signal(signal.SIGINT, handle_keyboard_interrupt)

# Start the pipeline
pipeline.set_state(Gst.State.PLAYING)

# Create a GObject main loop
loop = GObject.MainLoop()

# Run the main loop
try:
    loop.run()
except KeyboardInterrupt:
    pipeline.set_state(Gst.State.NULL)
    loop.quit()
