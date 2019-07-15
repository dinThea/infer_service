import cv2, sys
import numpy as np

def yolo_parser (output, width, height, threshhold, names):
    
    return_list = []
    for out in output:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence >= threshhold:

                centerX, centerY, w, h = tuple(int(val*multiplier) for val, multiplier in zip(detection[0:4], [width,height,width,height]))

                x = int(centerX - (w / 2))
                y = int(centerY - (h / 2))
                return_list.append ((x,y,(x+w),(y+h),names[class_id]))
        
    return return_list

parser = {
    'yolo': yolo_parser 
}

class Infer:

    def __init__(self, cfg='/models/yolo.cfg', weights='/models/yolov3.weights', parser_type='yolo', threshold = 0.5):

        self.net = cv2.dnn.readNetFromDarknet(cfg, weights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
        self.parser = parser[parser_type]
        self.names = open('src/coco.names').read().split('\n')
        self.threshold = threshold

    def getOutputLayers(self):

        ln = self.net.getLayerNames()
        ln = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        return ln

    def detect(self, image):

        h, w = image.shape[:2]
        blob = cv2.dnn.blobFromImage(image, 1.0/255, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.getOutputLayers())
        
        return self.parser(outs, w, h, self.threshold, self.names)

    def detect_encoded(self, raw_image):
        
        image = self.decode(raw_image)
        return self.detect(image)

    def decode(self, raw_image):

        nparr = np.fromstring(raw_image, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return image

    def insert_bboxes(self, image, results):

        res = image.copy()
        font = cv2.FONT_HERSHEY_SIMPLEX
        for x0, y0, x1, y1, label in results:
            cv2.rectangle(res, (x0, y0-22), (x1, y0), (0,255,0), -1)
            cv2.putText(res, label, (x0, y0-4), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.rectangle(res, (x0,y0), (x1,y1), (0,255,0), 2)

        return res

    def encode_image(self, image):

        _, encoded = cv2.imencode('.png', image)
        return encoded.tostring()