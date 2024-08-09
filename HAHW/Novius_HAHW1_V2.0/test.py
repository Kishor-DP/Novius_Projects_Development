import cv2
import time

class TestMotionDetection:
    def __init__(self, roi, motion_threshold):
        self.roi = roi
        self.motion_threshold = motion_threshold
        self.roi_enabled = True  # Initial state of ROI
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()
        self.camera = cv2.VideoCapture(0)  # Using the default camera

    def enable_roi(self):
        self.roi_enabled = True
        print("ROI enabled.")

    def disable_roi(self):
        self.roi_enabled = False
        print("ROI disabled.")

    def capture_image(self):
        ret, frame = self.camera.read()
        if not ret:
            print("Failed to capture image.")
            return None
        return frame

    def process_image(self, frame):
        if self.roi_enabled:
            roi_frame = frame[self.roi[1]:self.roi[1]+self.roi[3], self.roi[0]:self.roi[0]+self.roi[2]]
            motion_mask = self.background_subtractor.apply(roi_frame)
            motion_value = motion_mask.sum()
            cv2.rectangle(frame, (self.roi[0], self.roi[1]), (self.roi[0]+self.roi[2], self.roi[1]+self.roi[3]), (0, 255, 0), 2)
        else:
            motion_value = 0  # No motion detected if ROI is disabled
        
        return frame, motion_value

    def run(self):
        roi_enable_duration = 20  # Seconds to enable ROI
        roi_disable_duration = 10  # Seconds to disable ROI

        start_time = time.time()

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if (elapsed_time // (roi_enable_duration + roi_disable_duration)) % 2 == 0:
                if not self.roi_enabled:
                    self.enable_roi()
            else:
                if self.roi_enabled:
                    self.disable_roi()

            frame = self.capture_image()
            if frame is None:
                continue

            frame, motion_value = self.process_image(frame)
            print(f"Motion value: {motion_value}")

            cv2.imshow('Motion Detection', frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    roi = (100, 100, 200, 200)  # x, y, width, height
    motion_threshold = 1000000  # Adjust the threshold value as needed
    motion_detection = TestMotionDetection(roi, motion_threshold)
    motion_detection.run()
