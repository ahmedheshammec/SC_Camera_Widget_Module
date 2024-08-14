/** @odoo-module **/
import { Dialog } from "@web/core/dialog/dialog";
import { useService } from "@web/core/utils/hooks";
import { ImageField } from "@web/views/fields/image/image_field";
import { patch } from "@web/core/utils/patch";

const { Component, onMounted, useRef, onWillDestroy } = owl;
    const PartnerDetailsEdit = require('point_of_sale.PartnerDetailsEdit');
    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');
    var rpc = require("web.rpc");
    class PosImageCaptureDialog extends Component {
    setup() {
        super.setup();
        this.live_cam_img = useRef("live_cam_img");
        this.webcam_img = useRef("webcam_img");
        this.img_data = "";
        onMounted(() => {
            Webcam.set({
                width: 320,
                height: 240,
                dest_width: 320,
                dest_height: 240,
                image_format: "jpeg",
                jpeg_quality: 90,
                force_flash: false,
                fps: 45,
            });

            Webcam.attach(".live_cam_img");
            $(".save_close_btn").attr("disabled", "disabled");
            $(this.webcam_img.el).html(
                '<img src="/web/static/img/placeholder.png"/>'
            );
        });

        onWillDestroy(() => {
            Webcam.reset();
        });
    }

    _captureImage() {
        var self = this;
        Webcam.snap(function (data) {
            self.img_data = data;
            $(self.webcam_img.el).html(`<img src="${data}"/>`);
        });
        if (Webcam.live) {
            $(".save_close_btn").removeAttr("disabled");
        }
    }

    displayImage() {
            self = this;
            var img_data_base64 = self.img_data.split(",")[1];
            var ImgData = "data:image/jpeg;base64," + img_data_base64
            const loadedImage = this.props.Rec._loadImage(ImgData);
            if (loadedImage) {
                    this.props.Rec.changes.image_1920 = ImgData
                    this.props.Rec.render(true);
                }
    }
    _saveClose() {
        this.displayImage();
        this.props.close();
    }
}
    PosImageCaptureDialog.components = { Dialog };
    PosImageCaptureDialog.template = "web_widget_image_cam.PopCameraDialog";


    const PopupPartnerDetailsEdit = (PartnerDetailsEdit) => {
        class PopupPartnerDetailsEdit extends PartnerDetailsEdit {
            setup() {
                super.setup();
                this.dialog = useService("dialog");
            }

            async onOpenCam() {
                    self=this;
                    this.dialog.add(PosImageCaptureDialog, {
                    rec_to_update: this,
                    Rec: self,
        });
            }
        }
        return PopupPartnerDetailsEdit;
    };
    Registries.Component.extend(PartnerDetailsEdit, PopupPartnerDetailsEdit);

    return PartnerDetailsEdit;
