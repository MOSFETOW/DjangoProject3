document.addEventListener('DOMContentLoaded', function() {
    const mailForm = document.querySelector('form[action*="mailing_list"]');
    if (mailForm) {
        mailForm.addEventListener('submit', function(e) {

            const emailInput = this.querySelector('input[name="e"]');

            if (emailInput.value.includes('@')) {

                const toastEl = document.getElementById('mailToast');
                const toast = new bootstrap.Toast(toastEl);
                toast.show();


            }
        });
    }
});