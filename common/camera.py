import time
import cv2

from common.base_camera import BaseCamera


# class_names = [c.strip() for c in open(classes_path).readlines()]
print('classes loaded')



class Camera(BaseCamera):
    @staticmethod
    def frames():
        go = 1
        while True:
            if go == 1:
                with open('./caches/result.txt', 'r') as f:
                    image_name = f.read()
                fi_name = image_name
                cam = cv2.VideoCapture(image_name)
                g = 0
                y = 0
                s = 0
                c = 0
                sum = 0
                a = time.time()
                go = 0
                de_sum = []
                de_sum.append(-1)
                fps = int(cam.get(cv2.CAP_PROP_FPS)) // 15 + 1
            else:

                with open('./caches/result.txt', 'r') as f:
                    image_name = f.read()
                if image_name != fi_name:
                    go = 1
                    continue
                b = time.time() - a
                if b > 150:
                    break
                ret,img = cam.read()
                if ret:
                    h, w, _ = img.shape
                    if h > 2000 or w > 2000:
                        h = h // 2
                        w = w // 2
                        img = cv2.resize(img, (int(w), int(h)))
                    if CameraParams.gray:
                        if g == 0:
                            cam = cv2.VideoCapture(image_name)
                            g = 1
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        while (h > 512 and w > 512):
                            h = h / 1.2
                            w = w / 1.2
                        h = int(h)
                        w = int(w)
                        img = cv2.resize(img, (w, h))
                        yield cv2.imencode('.jpg', img)[1].tobytes()
                    elif CameraParams.gaussian:
                        sum = sum + 1
                        if sum & fps == 0:
                            if y == 0:
                                cam = cv2.VideoCapture(image_name)
                                y = 1

                            im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            # bbox_xywh, cls_conf, cls_ids = detector(im)

                            # mask = cls_ids == 0
                            # new_bbox_xywh = bbox_xywh[mask]
                            # new_bbox_xywh[:, 3:] *= 1.2

                            # new_cls_conf = cls_conf[mask]
                            # outputs = deepsort.update(new_bbox_xywh, new_cls_conf, im)
                            # if len(outputs) > 0:
                            #     bbox_xyxy = outputs[:, :4]
                            #     identities = outputs[:, -1]
                            #     if -1 in de_sum:
                            #         de_sum = []
                            #     else:
                            #         for id in identities:
                            #             if id not in de_sum:
                            #                 de_sum.append(id)

                            #     img = draw_boxes(img, bbox_xyxy, identities)

                            text = "people "
                            if -1 in de_sum:
                                de_sum = []
                            if (len(de_sum) > 0):
                                text = text + str(len(de_sum))
                            else:
                                text = text + str(0)
                            cv2.putText(img, text, (50, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (250, 250, 0), 8)
                            while (h > 512 and w > 512):
                                h = h / 1.2
                                w = w / 1.2
                            h = int(h)
                            w = int(w)
                            img = cv2.resize(img, (w, h))
                            yield cv2.imencode('.jpg', img)[1].tobytes()

                    elif CameraParams.sobel:
                        if s == 0:
                            cam = cv2.VideoCapture(image_name)
                            s = 1
                        img = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
                        img = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
                        while (h > 512 and w > 512):
                            h = h / 1.2
                            w = w / 1.2
                        h = int(h)
                        w = int(w)
                        img = cv2.resize(img, (w, h))
                        yield cv2.imencode('.jpg', img)[1].tobytes()
                    elif CameraParams.canny:
                        if c == 0:
                            cam = cv2.VideoCapture(image_name)
                            c = 1
                        img = cv2.Canny(img, 100, 200, 3, L2gradient=True)
                        while (h > 512 and w > 512):
                            h = h / 1.2
                            w = w / 1.2
                        h = int(h)
                        w = int(w)
                        img = cv2.resize(img, (w, h))
                        yield cv2.imencode('.jpg', img)[1].tobytes()
                    else:
                        while (h > 512 and w > 512):
                            h = h / 1.2
                            w = w / 1.2
                        h = int(h)
                        w = int(w)
                        img = cv2.resize(img, (w, h))
                        yield cv2.imencode('.jpg', img)[1].tobytes()
                else:
                    cam = cv2.VideoCapture(image_name)
        
class CameraParams():
    
    gray = False
    gaussian = False
    sobel = False
    canny = False
    def __init__(self, gray, gaussian, sobel, canny, yolo):
        self.gray = gray
        self.gaussian = gaussian
        self.sobel = sobel
        self.canny = canny
        self.yolo=yolo