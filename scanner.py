import cv2
from pyzbar.pyzbar import decode

def scan_barcode():
    cap = cv2.VideoCapture(0)

    print("Scanning...")

    while True:
        ret, frame = cap.read()
        barcodes = decode(frame)

        for barcode in barcodes:
            data = barcode.data.decode('utf-8')
            print("Scanned:", data)
            cap.release()
            cv2.destroyAllWindows()
            return data

        cv2.imshow("Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()