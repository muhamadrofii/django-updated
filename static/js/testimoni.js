const stars = document.querySelectorAll('.stars span');
const ratingValue = document.getElementById('rating-value');

stars.forEach((star) => {
    star.addEventListener('click', function () {
        stars.forEach((s) => s.classList.remove('selected'));
        
        this.classList.add('selected');
        let previousSibling = this.previousElementSibling;
        while (previousSibling) {
            previousSibling.classList.add('selected');
            previousSibling = previousSibling.previousElementSibling;
        }

        const value = this.getAttribute('data-value');
        ratingValue.textContent = `Rating Anda: ${value}/5`;
    });
});

const submitButton = document.querySelector('.button-footer');
const formModal = new bootstrap.Modal(document.getElementById('resultModal'));
const thankYouModal = new bootstrap.Modal(document.getElementById('terkirimModal'));

submitButton.addEventListener('click', function (e) {
    e.preventDefault();
    formModal.hide();
    thankYouModal.show();
});