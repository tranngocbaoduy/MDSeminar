import flask
import os
from flask import Flask
# from flask_dropzone import Dropzone
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import urllib.parse 
from JPAppServer.config import Config 
from flask_mongoengine import *


db = MongoEngine() 

def create_app(class_config=Config):
    app = Flask(__name__) 
    app.config.from_object(Config) 
    # app.config['SECRET_KEY'] = config.SECRET_KEY
    # dropzone = Dropzone(app)
    # Dropzone settings
    # app.config['DROPZONE_UPLOAD_MULTIPLE'] = config.DROPZONE_UPLOAD_MULTIPLE
    # app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = config.DROPZONE_ALLOWED_FILE_CUSTOM
    # app.config['DROPZONE_ALLOWED_FILE_TYPE'] = config.DROPZONE_ALLOWED_FILE_TYPE
    # # app.config['DROPZONE_REDIRECT_VIEW'] = os.getcwd() + '/output'
    # # Uploads settings
    # app.config['DROPZONE_MAX_FILE_SIZE'] = config.DROPZONE_MAX_FILE_SIZE
    # app.config['UPLOADED_PHOTOS_DEST'] = config.UPLOADED_PHOTOS_DEST
    # photos = UploadSet('photos', IMAGES)
    # configure_uploads(app, photos)
    # patch_request_class(app)  # set maximum file size, default is 16MB
    # DS = str(os.path.sep)
    # ROOT = DS.join(app.instance_path.split(DS)[:-1]) + DS
    # config = {
    #     "path": {
    #         "root": ROOT
    #         , "input" : ROOT + "input" + DS
    #         , "output" : ROOT + "output" + DS
    #     }
    # }
    # app.custom = config
    db.init_app(app)

    from JPAppServer.Vocabulary.routes import vocab

    app.register_blueprint(vocab)   
 
    return app
