//
///** @odoo-module **/
//
//import { patch } from 'web.utils';
//import { FormController } from "@web/views/form/form_controller";
//
//patch(FormController.prototype, 'web_widget_image_cam.CustomFormController', {
//    async saveRecord() {
//        const result = await this._super(...arguments); // Correctly call super method
//        if (this.modelName === 'medical.endoscopes' && this.mode === 'edit' && this.initialState.isNew) {
//            // Check if it's a new record being saved
//            this.trigger_up('history_back'); // Correct action for refreshing the form or redirecting
//        }
//        return result;
//    },
//});