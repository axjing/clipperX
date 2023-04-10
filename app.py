import os
import cv2
import json
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

from common.utils import base64_to_pil,np_to_base64,str_to_bool,gen_web
from common.camera import CameraParams,Camera
# Declare a flask app
app = Flask(__name__,static_folder="./web/static",template_folder="./web/templates",)

IMAGE_SUFFIX = ['jpg','jpeg','png']
VIDEO_SUFFIX = ['mp4','avi']

@app.route('/')
def upload_file():
   return render_template('index1.html')

# @app.route('/')
# def upload_index():
#    return render_template('index0.html')

# API that returns image with detections on it
@app.route('/images', methods= ['POST'])
def get_image():
    image = request.files["images"]
    image_name = image.filename

    with open('./caches/result.txt', 'r') as f:
        im_na = f.read()
    try:
        os.remove(im_na)
    except:
        pass

    if image_name.split('.')[-1] in VIDEO_SUFFIX:
        with open('./caches/result.txt', 'w') as f:
            f.write(image_name)

    image.save(os.path.join(os.getcwd(), image_name))

    if image_name.split(".")[-1] in IMAGE_SUFFIX:
        img = cv2.imread(image_name)
        h,w,_ = img.shape
        if h > 2000 or w > 2000:
            h = h // 2
            w = w // 2
            img = cv2.resize(img,(int(w),int(h)))

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # bbox, cls_conf, cls_ids = yolo(img)
        # from vizer.draw import draw_boxes as db
        # if bbox is not None:
        #     img = db(img, bbox, cls_ids, cls_conf, class_name_map=class_names)
        img = img[:, :, (2, 1, 0)]
        _, img_encoded = cv2.imencode('.jpg', img)
        response = img_encoded.tobytes()
        os.remove(image_name)
        try:
            return Response(response=response, status=200, mimetype='image/jpg')
        except:
            return render_template('index1.html')
            # return render_template('index0.html')
    else:
        return render_template('video1.html')
        # return render_template('video0.html')


@app.route('/cameraParams', methods=['GET', 'POST'])
def cameraParams():
    if request.method == 'GET':
        data = {
            'gray': CameraParams.gray,
            'gaussian': CameraParams.gaussian,
            'sobel': CameraParams.sobel,
            'canny': CameraParams.canny,
        }
        return app.response_class(response=json.dumps(data),
                                    status=200,
                                    mimetype='application/json')
    elif request.method == 'POST':
        try:
            data = request.form.to_dict()
            CameraParams.gray = str_to_bool(data['gray'])
            CameraParams.gaussian = str_to_bool(data['gaussian'])
            CameraParams.sobel = str_to_bool(data['sobel'])
            CameraParams.canny = str_to_bool(data['canny'])
            message = {'message': 'Success'}
            response = app.response_class(response=json.dumps(message),
                                    status=200,
                                    mimetype='application/json')
            return response
        except Exception as e:
            print(e)
            response = app.response_class(response=json.dumps(e),
                                    status=400,
                                    mimetype='application/json')
            return response
    else:
        data = { "error": "Method not allowed. Please GET or POST request!" }
        return app.response_class(response=json.dumps(data),
                                    status=400,
                                    mimetype='application/json')
@app.route('/realtime')
def realtime():
    # return render_template('video0.html')
    return render_template('video1.html')
    

########get  path
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_web(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/cutter', methods=['GET', 'POST'])
def web_cutter():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        # img.save("./uploads/image.png")

        # Make prediction
        preds = model_predict(img, model)

        # Process your result for human
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        result = str(pred_class[0][0][1])               # Convert to string
        result = result.replace('_', ' ').capitalize()
        
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)

    return None

@app.route('/upload_video', methods=['GET'])
def upload_video():
    return render_template('video.html')
    
def web_transcriber():
    return

def web_daemoner():
    return
if __name__=="__main__":
    #   Run locally
    app.run(debug=True,port=5002,threaded=False)
    #   Run on the server
    # app.run(debug=True, host = '0.0.0.0', port=5000)
