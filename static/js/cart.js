// --- ВАШ СТАРИЙ КОД ---
document.addEventListener('input', function(e) {
    if (e.target.classList.contains('item-quantity') || e.target.classList.contains('item-checkbox')) {
        calculateCart();
    }
});

function calculateCart() {
    let total = 0;
    document.querySelectorAll('.cart-row').forEach(row => {
        const price = parseFloat(row.dataset.price.replace(',', '.'));
        const qty = parseInt(row.querySelector('.item-quantity').value) || 0;
        const isSelected = row.querySelector('.item-checkbox').checked;

        const sum = price * qty;
        row.querySelector('.item-total-price').textContent = sum.toFixed(2) + ' грн';

        if (isSelected) total += sum;
    });

    const display = document.getElementById('final-total');
    if (display) display.textContent = total.toFixed(2);
}

calculateCart();

// --- НОВИЙ КОД ДЛЯ ОФОРМЛЕННЯ ЗАМОВЛЕННЯ ---

function showPaymentStep() {
    const selectedRows = document.querySelectorAll('.cart-row');
    const listBody = document.getElementById('items-list-body');
    listBody.innerHTML = '';

    let total = 0;
    let hasItems = false;

    selectedRows.forEach(row => {
        const checkbox = row.querySelector('.item-checkbox');
        if (checkbox && checkbox.checked) {
            hasItems = true;
            const name = row.dataset.name;
            const price = parseFloat(row.dataset.price.replace(',', '.'));
            const qty = row.querySelector('.item-quantity').value;
            const sum = (price * qty).toFixed(2);
            const imgUrl = row.dataset.image;
            total += parseFloat(sum);

            // Формуємо тег картинки, якщо вона є
            const imgTag = imgUrl ? `<img src="${imgUrl}" style="width: 40px; height: 40px; object-fit: cover; border-radius: 6px;" class="me-3 shadow-sm">` : '';

            // Додаємо рядок з картинкою
            listBody.innerHTML += `
                <tr class="align-middle border-bottom">
                    <td class="py-2 d-flex align-items-center">
                        ${imgTag}
                        <span class="small fw-medium">${name}</span>
                    </td>
                    <td class="text-center small py-2">${qty} шт.</td>
                    <td class="text-end small fw-bold py-2">${sum} грн</td>
                </tr>
            `;
        }
    });

    if (!hasItems) {
        alert("Виберіть хоча б один товар!");
        return;
    }

    document.getElementById('payment-total').textContent = total.toFixed(2);
    document.getElementById('cart-main-section').classList.add('d-none');
    document.getElementById('payment-section').classList.remove('d-none');
    window.scrollTo(0,0);
}

function handleFinalBuy() {
    // Зчитуємо нові поля
    const contact = document.getElementById('user-contact').value;
    const delivery = document.getElementById('delivery-method').value;
    const branch = document.getElementById('branch-number').value;

    if (contact.trim() === '' || branch.trim() === '') {
        alert("Будь ласка, заповніть контактні дані та номер відділення!");
        return;
    }

    // Додаємо зчитані дані як приховані поля у головну форму
    const form = document.getElementById('cart-form');
    form.insertAdjacentHTML('beforeend', `<input type="hidden" name="contact_info" value="${contact}">`);
    form.insertAdjacentHTML('beforeend', `<input type="hidden" name="delivery_method" value="${delivery}">`);
    form.insertAdjacentHTML('beforeend', `<input type="hidden" name="branch_number" value="${branch}">`);

    // Показуємо Тост
    const toastEl = document.getElementById('buyToast');
    const toast = new bootstrap.Toast(toastEl);
    toast.show();

    // Відправляємо форму
    setTimeout(() => {
        form.submit();
    }, 2000);
}