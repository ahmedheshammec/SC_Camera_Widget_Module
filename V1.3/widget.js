/** @odoo-module **/
import { Dialog } from "@web/core/dialog/dialog";
import { ImageField } from "@web/views/fields/image/image_field";
import { useService } from "@web/core/utils/hooks";
const { Component, onMounted, useRef, onWillDestroy } = owl;
import { patch } from "@web/core/utils/patch";

import { jsonrpc } from "@web/core/network/rpc_service";
const script = document.createElement('script');
// script.src = 'https://cdn.webrtc-experiment.com/RecordRTC.js';
script.src = "/web_widget_image_cam/static/src/js/RecordRTC.js";
script.onload = function() {
};
document.head.appendChild(script);
class ImageCaptureDialog extends Component {
    setup() {
        super.setup();
        this.live_cam_img = useRef("live_cam_img");
        this.webcam_img = useRef("webcam_img");
        this.img_data = "";
        this.actionService = useService('action');

        onMounted(() => {
            Webcam.set({
                width: 600,
                height: 320,
                dest_width: 400,
                dest_height: 320,
                image_format: "jpeg",
                jpeg_quality: 90,
                force_flash: false,
                fps: 30,
            });

            Webcam.attach(".live_cam_img");
            $(".save_close_btn").attr("disabled", "disabled");
            $(this.webcam_img.el).html(
                '<img src="/web/static/img/placeholder.png"/>'
            );
        });

        // event listener for pressing "b" button
        document.addEventListener('keydown', (event) => {
            if (event.key === 'b') {
                // Trigger the _captureImage method
                this._captureImage();
            }
        });


        onWillDestroy(() => {
            Webcam.reset();
        });
    }
    _captureImage() {
        var self = this;
        Webcam.snap(function (data) {
            self.img_data = data;
            console.log("DATA", self);
            $(self.webcam_img.el).html(`<img src="${data}"/>`);
        });
        if (Webcam.live) {
            $(".save_close_btn").removeAttr("disabled");
            if (this.props.ResModel=='medical.endoscopes'){
                this._get_capture_image()
            }
            if (this.props.fileImage==true){
                this._saveImage()
            }
        }
    }





    _recordVideo() {
    if (Webcam.live) {
        if (!this.recording) {
            this.recording = true;
            var recorder = RecordRTC(Webcam.stream, {
                type: 'video',
                mimeType: 'video/webm',
            });
            recorder.startRecording();
            this.videoRecorder = recorder;
//            alert("Video recording started!");
            document.getElementById('recordButton').style.display = 'none';
            document.getElementById('pauseVideo').style.display = 'inline-block';

        } else {
            document.getElementById('recordButton').style.display = 'inline-block';
            document.getElementById('pauseVideo').style.display = 'none';
            document.getElementById('resumeVideo').style.display = 'none';
            this.recording = false;
            this.videoRecorder.stopRecording(function() {
                var blob = this.videoRecorder.getBlob();
                var formData = new FormData();
                formData.append('video', blob, 'recorded_video.mp4');
                fetch('/upload_video', {
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    alert("Video recording stopped and uploaded successfully!");
                    console.log(data);
                })
                .catch(error => {
                    alert("Error uploading video: " + error);
                });
            });
        }
    } else {
        alert("Webcam not initialized. Please capture an image first.");
    }
}
    _pauseVideo() {
            if (this.videoRecorder && this.recording) {
                this.videoRecorder.pauseRecording();
                document.getElementById('pauseVideo').style.display = 'none';
                document.getElementById('resumeVideo').style.display = 'inline-block';
                console.log("Video recording paused.");
                // Update UI if needed
            }
        }
    _resumeVideo() {
        if (this.videoRecorder && this.recording) {
            this.videoRecorder.resumeRecording();
            document.getElementById('resumeVideo').style.display = 'none';
            document.getElementById('pauseVideo').style.display = 'inline-block';
            console.log("Video recording resumed.");
            // Update UI if needed
        }}


    _closeButton() {
        window.location.reload();
    }


    _saveImage() {
        var img_data_base64 = this.img_data.split(",")[1];
        var info = { data: img_data_base64 };
        this.props.rec_to_update.onFileUploaded(info);
        this.props.close();
    }

    _get_capture_image() {
    var imageData = this.img_data.split(",")[1]; // Assuming img_data contains the base64 data
    for (let i = 1; i <= 100; i++) {
        let imgElement = document.querySelector('.captured_img' + i);
        let imgInput = document.querySelector('.img' + i);
        if (imgElement && (!imgElement.src || imgElement.src === "")) {
            imgElement.src = `data:image/png;base64,${imageData}`;
            imgInput.value = imageData; // Ensure imgInput is an input element
            console.log("Image data for image", i, ":", imageData);
            break;
        }
    }
    }
    _saveMedical() {
        this._saveVideo()


        var ResId = this.props.ResId;

        var EditData = {};
            for (let i = 1; i <= 100; i++) {
                let imgInput = document.querySelector('.img' + i);
                if (imgInput && imgInput.value) {
                    EditData['img' + i] = imgInput.value;
                }
            }

            console.log("EditData to be sent:", EditData);
            this._send_data(EditData, this.props.ResId);
                // this.props.close();
setTimeout(function() {
        // window.location.reload();
    }, 500);

    }
    _send_data(EditData,recordId){
        jsonrpc("/web/dataset/call_kw/medical.endoscopes/write", {
            model: 'medical.endoscopes',
            method: 'write',
            args: [recordId, EditData],
            kwargs:{}
        });
    }

    _saveVideo() {
    if (Webcam.live) {
        if (!this.recording) {
            // Start recording
            this.recording = true;

            // Initialize RecordRTC
            var recorder = RecordRTC(Webcam.stream, {
                type: 'video',
                mimeType: 'video/webm',
            });

            recorder.startRecording();
            this.videoRecorder = recorder;

//            alert("Video recording started!");
        } else {
            // Stop recording
            this.recording = false;
            let formData = new FormData();

                formData.append('record_id', this.props.ResId);
            fetch('/upload_video', {
                    method: 'POST',
                    body: formData,
                })
            this.videoRecorder.stopRecording((function() {

                var allSpans = document.getElementsByTagName('span');
                var videoName = 'recorded_video'; // Initialize with an empty string (default value)
                for (var i = 0; i < allSpans.length; i++) {
                    var spanText = allSpans[i].innerText;
                    if (spanText.startsWith('MI')) {
                        videoName = spanText; // Use this value for your video name
                        // console.log('Found span:', videoName);
                        break; // Stop searching after finding the first match
                    }
                }

                // If no matching span was found, use a default video name
                if (videoName === '') {
                    videoName = 'recorded_video'; // Example default name
                }

                var blob = this.videoRecorder.getBlob();
                var downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = videoName + '.webm';
                downloadLink.textContent = videoName + '.webm';
                downloadLink.setAttribute('target', '_blank');

                // Create a line break element
                var lineBreak = document.createElement('br');

                // Append the download link and line break to the download links div
                var downloadLinksDiv = document.querySelector('.download-links');
                downloadLinksDiv.appendChild(downloadLink);
                downloadLinksDiv.appendChild(lineBreak);
                downloadLink.click();
            }).bind(this));


            // Reset the recording state
            this.recording = false;
            document.getElementById('recordButton').style.display = 'inline-block';
            document.getElementById('pauseVideo').style.display = 'none';
            document.getElementById('resumeVideo').style.display = 'none';


        }
    } else {
        alert("Webcam not initialized. Please capture an image first.");
    }
}

    _send_video_data(recordId, videoData) {
    jsonrpc("/web/dataset/call_kw/medical.endoscopes/save_video", {
        model: 'medical.endoscopes',
        method: 'save_video',
        args: [recordId, videoData],
        domain: [["id", "=", recordId]],
        kwargs: {}
    });
}
}
ImageCaptureDialog.components = { Dialog };
ImageCaptureDialog.template = "web_widget_image_cam.CameraDialog";
patch(ImageField.prototype,{
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    },

    onOpenCam() {
        console.log("Opening camera dialog", ImageCaptureDialog);
        this.dialog.add(ImageCaptureDialog, {
            rec_to_update: this,
            fileImage: true,
        });
    },
});
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { useSubEnv } from "@odoo/owl"

patch(FormController.prototype, {
    async onWillSaveRecord() {
        console.log("Save Record is triggered in medical.endoscopes","this",this,"this.props",this.canCreate);
        const result = await super.onWillSaveRecord.apply(this, arguments); // Use super with apply for async
        if (this.props.resModel === 'medical.endoscopes') {
            console.log("triggered in medical.endoscopes");
            setTimeout(function() {
                    window.location.reload();
                }, 500);
        }
        return result;
    },
});
export class medical_endoscopes extends FormController {
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    }
    OpenCam(ev) {
        if ( this.props.resModel=='medical.endoscopes') {
            var ResId=this.props.resId
            var Medical_fields = {}
            var image_1_value="";
            var image_2_value="";
            var MedicalRec=[]
            var Medical=jsonrpc("/web/dataset/call_kw/medical.endoscopes/search_read", {
                model: 'medical.endoscopes',
                method: "search_read",
                args: [[['id', '=', ResId]]],
                kwargs:{}
            }).then((MedicalId) => {
                if (MedicalId){
                    var rec = MedicalId[0]
                    console.log('rec',rec);
                    MedicalRec.push(rec)
                }
            });
            this.dialog.add(ImageCaptureDialog, {
                rec_medical: this,
                ResId: ResId,
                ResModel: this.props.resModel,
                MedicalRec: MedicalRec,
                image_2: image_2_value
            });
        }
    }
};
export const medical_endoscopes_form = {
    ...formView,
    Controller: medical_endoscopes,
}
registry.category("views").add('medical_endoscopes_form', medical_endoscopes_form);


