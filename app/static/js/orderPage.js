document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('orderDetails');
  const orderItemsContainer = document.getElementById('orderItems');
  const addItemBtn = document.getElementById('addItemBtn');
  const paymentSelect = document.getElementById('paymentMethod');
  const cardSection = document.getElementById('cardDetails');
  const cashMsg = document.getElementById('cashMessage');
  const schedulePicker = document.getElementById('schedulePicker');
  const asapRadio = document.getElementById('asap');
  const scheduleRadio = document.getElementById('schedule');

  // ===== Add / Remove order items =====
  addItemBtn.addEventListener('click', () => {
    const firstItem = orderItemsContainer.querySelector('.order-item');
    const newItem = firstItem.cloneNode(true);
    newItem.querySelector('input[name="foodName[]"]').value = '';
    newItem.querySelector('input[name="quantity[]"]').value = '1';
    orderItemsContainer.appendChild(newItem);
  });

  orderItemsContainer.addEventListener('click', (e) => {
    const target = e.target;

    if (target.classList.contains('removeItem')) {
      if (orderItemsContainer.children.length > 1) {
        target.closest('.order-item').remove();
      } else {
        Swal.fire({
          icon: 'warning',
          title: 'At least one item required',
          text: 'You must have at least one order item.',
          confirmButtonColor: '#ff6f61'
        });
      }
    }

    if (target.classList.contains('plusBtn') || target.classList.contains('minusBtn')) {
      const qtyInput = target.closest('.order-item').querySelector('input[name="quantity[]"]');
      let currentVal = parseInt(qtyInput.value, 10);
      if (target.classList.contains('plusBtn')) {
        qtyInput.value = currentVal + 1;
      } else if (target.classList.contains('minusBtn')) {
        qtyInput.value = Math.max(1, currentVal - 1);
      }
    }
  });

  // ===== Payment method toggle =====
  paymentSelect.addEventListener('change', () => {
    if (paymentSelect.value === 'credit' || paymentSelect.value === 'debit') {
      cardSection.style.display = 'block';
      cashMsg.style.display = 'none';
    } else if (paymentSelect.value === 'cash') {
      cardSection.style.display = 'none';
      cashMsg.style.display = 'block';
    } else {
      cardSection.style.display = 'none';
      cashMsg.style.display = 'none';
    }
  });

  // ===== Delivery time toggle =====
  asapRadio.addEventListener('change', () => { if (asapRadio.checked) schedulePicker.style.display = 'none'; });
  scheduleRadio.addEventListener('change', () => { if (scheduleRadio.checked) schedulePicker.style.display = 'block'; });

  // ===== Form submission =====
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const showError = (msg) => Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: msg,
      confirmButtonColor: '#ff6f61'
    });

    const restaurant = document.getElementById('restaurantSelect').value;
    if (!restaurant) return showError('Please select a restaurant.');

    const orderItemDivs = document.querySelectorAll('.order-item');
    const items = [];
    for (const div of orderItemDivs) {
      const foodName = div.querySelector('input[name="foodName[]"]').value.trim();
      const quantity = parseInt(div.querySelector('input[name="quantity[]"]').value, 10);
      if (!foodName) return showError('Please enter a food name for all items.');
      if (isNaN(quantity) || quantity < 1) return showError('Please enter a valid quantity for all items.');
      items.push({ foodName, quantity });
    }
    if (items.length === 0) return showError('Add at least one item to your order.');

    const paymentMethod = paymentSelect.value;
    if (!paymentMethod) return showError('Please select a payment method.');
    let cardDetails = {};
    if (paymentMethod === 'credit' || paymentMethod === 'debit') {
      const cardNumber = document.getElementById('cardNumber').value.trim();
      const cardName = document.getElementById('cardName').value.trim();
      const cardExpiry = document.getElementById('cardExpiry').value;
      const cardCVV = document.getElementById('cardCVV').value.trim();
      if (!cardNumber || !cardName || !cardExpiry || !cardCVV)
        return showError('Please fill in all card details.');
      cardDetails = { cardNumber, cardName, expiry: cardExpiry, cvv: cardCVV };
    }

    const deliveryTimePreference = document.querySelector('input[name="delivery_time"]:checked').value;
    const scheduledDelivery = (deliveryTimePreference === 'Schedule') ? document.getElementById('scheduled_datetime').value : null;
    const tipAmount = parseFloat(document.getElementById('tip').value) || 0;
    const couponCode = document.getElementById('couponCode').value.trim() || null;
    const specialInstructions = document.getElementById('instructions').value.trim() || null;

    const orderPayload = {
      restaurant,
      items,
      paymentMethod,
      cardDetails,
      deliveryTimePreference,
      scheduledDelivery,
      tipAmount,
      couponCode,
      specialInstructions
    };

    try {
      const res = await fetch('/orders/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(orderPayload)
      });
      const result = await res.json();
      if (res.ok) {
        Swal.fire({
          icon: 'success',
          title: 'Order Confirmed! 🛵',
          html: `
            <b>FoodieGo</b> has received your order.<br>
            Your feast is on its way 🚀<br>
            <small>Sit back & relax while we bring the yum to you 🍕🍔</small>
        `,
          showCancelButton: true,
          confirmButtonText: 'See Your Orders',
          cancelButtonText: 'Close',
          confirmButtonColor: '#28a745',
          cancelButtonColor: '#6c757d'
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = '/orderDetails'; // redirect to orders page
          }
        });

        form.reset();
        cardSection.style.display = 'none';
        cashMsg.style.display = 'none';
        schedulePicker.style.display = 'none';
      } else {
        showError(result.error || 'Something went wrong.');
      }

    } catch (err) {
      console.error(err);
      showError('Network error: ' + err.message);
    }
  });
});
