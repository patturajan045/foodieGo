document.addEventListener("DOMContentLoaded", () => {
  // 🔹 Scroll setup
  const setupScroll = (sectionId, btnLeftId, btnRightId) => {
    const box = document.getElementById(sectionId);
    document.getElementById(btnLeftId)?.addEventListener("click", () =>
      box.scrollBy({ left: -200, behavior: "smooth" })
    );
    document.getElementById(btnRightId)?.addEventListener("click", () =>
      box.scrollBy({ left: 200, behavior: "smooth" })
    );
  };

  [
    ["scrollBox", "btnLeft", "btnRight"],
    ["scrollBoxJuice", "btnLeftJuice", "btnRightJuice"],
    ["scrollBoxdessert", "btnLeftdessert", "btnRightdessert"],
    ["scrollBoxsnacks", "btnLeftsnacks", "btnRightsnacks"]
  ].forEach(args => setupScroll(...args));

  // 🔹 Intersection animation
  const observer = new IntersectionObserver(entries =>
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("visible");
        observer.unobserve(e.target);
      }
    }), { threshold: 0.15 }
  );
  document.querySelectorAll(".section-animate").forEach(s => observer.observe(s));

  // 🔹 SweetAlert popup for food actions
  const showFoodPopup = ({ id, foodName, description, foodPrice, imageUrl }) => {
    Swal.fire({
      title: foodName,
      html: `
        <img src="${imageUrl}" alt="${foodName}" 
             style="width:100%;max-height:200px;object-fit:cover;border-radius:10px;margin-bottom:10px;" />
        <p>${description}</p>
        <p><strong>Price:</strong> ${foodPrice}</p>
      `,
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: '🛒 Add to Cart',
      denyButtonText: '✅ Order Now',
      cancelButtonText: '❌ Cancel',
      confirmButtonColor: '#3085d6',
      denyButtonColor: '#28a745',
      cancelButtonColor: '#d33'
    }).then(result => {
      if (result.isConfirmed) {
        // ✅ Add to Cart
        fetch("http://127.0.0.1:5000/cart/add", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ foodId: id, quantity: 1 })
        })
          .then(res => res.json())
          .then(() => Swal.fire("Added!", `${foodName} added to your cart 🛒`, "success"))
          .catch(() => Swal.fire("Error", "Failed to add item to cart ❌", "error"));
      } else if (result.isDenied) {
        // ✅ Direct redirect (no SweetAlert shown)
        window.location.href = "/orderPage";
      }
    });
  };

  // 🔹 Render cards
  const renderCards = async (url, sectionId, label) => {
    const container = document.getElementById(sectionId);
    if (!container) return;
    container.innerHTML = `<p>Loading ${label}...</p>`;

    try {
      const res = await fetch(url);
      const { status, data } = await res.json();

      if (status !== "success" || !Array.isArray(data) || !data.length) {
        container.innerHTML = `<p>No ${label} found.</p>`;
        return;
      }

      container.innerHTML = "";
      data.forEach(item => {
        const card = document.createElement("div");
        card.className = "food-card";
        card.innerHTML = `
          <img src="${item.imageUrl}" alt="${item.foodName}" class="food-img" />
          <h5>${item.foodName}</h5>
          <p>${item.description}</p>
          <p><strong>Price:</strong> ${item.foodPrice}</p>
        `;
        card.addEventListener("click", () => showFoodPopup(item));
        container.appendChild(card);
      });
    } catch (err) {
      console.error(`❌ Error loading ${label}:`, err);
      container.innerHTML = `<p>Error loading ${label}.</p>`;
    }
  };

  // 🔹 Fetch all categories
  renderCards("http://127.0.0.1:5000/foods/all", "scrollBox", "food");
  renderCards("http://127.0.0.1:5000/juice/all", "scrollBoxJuice", "juice");
  renderCards("http://127.0.0.1:5000/desserts/all", "scrollBoxdessert", "dessert");
  renderCards("http://127.0.0.1:5000/snacks/all", "scrollBoxsnacks", "snack");
});
