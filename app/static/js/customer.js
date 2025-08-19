document.addEventListener("DOMContentLoaded", () => {
    const customerForm = document.getElementById("customerForm");
    const customerList = document.getElementById("customerList");

    // -------------------
    // Load Customers
    // -------------------
    async function loadCustomers() {
        try {
            const res = await fetch("/customer/all");
            const { status, data, message } = await res.json();

            if (status !== "success") {
                customerList.innerHTML = `<div class="text-center text-danger">${message}</div>`;
                return;
            }

            if (!data.length) {
                customerList.innerHTML = `<div class="text-center text-muted">No customers found</div>`;
                return;
            }

            // Render table
            customerList.innerHTML = `
                <div class="table-responsive">
                    <table class="table table-striped table-bordered align-middle text-center">
                        <thead class="table-dark">
                            <tr>
                                <th>#</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Phone</th>
                                <th>Address</th>
                                <th>City</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${data.map((cust, index) => `
                                <tr>
                                    <td>${index + 1}</td>
                                    <td>${cust.customerName}</td>
                                    <td>${cust.email}</td>
                                    <td>${cust.phone}</td>
                                    <td>${cust.address}</td>
                                    <td><span class="badge bg-success">${cust.city}</span></td>
                                    <td>
                                        <button class="btn btn-outline-danger btn-sm" data-id="${cust._id}">
                                            <i class="bi bi-trash-fill"></i> Delete
                                        </button>
                                    </td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            `;
        } catch (err) {
            console.error(err);
            customerList.innerHTML = `<div class="text-center text-danger">Error loading customers</div>`;
        }
    }

    // -------------------
    // Add Customer
    // -------------------
    if (customerForm) {
        customerForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = Object.fromEntries(new FormData(customerForm).entries());

            try {
                const res = await fetch("/customer/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(formData)
                });
                const result = await res.json();

                if (result.status === "success") {
                    Swal.fire({
                        icon: "success",
                        title: "Customer Added",
                        text: "The customer was added successfully!",
                        timer: 2000,
                        showConfirmButton: false
                    }).then(() => {
                        const modal = bootstrap.Modal.getInstance(document.getElementById("customerModal"));
                        if (modal) modal.hide();
                    });
                    customerForm.reset();
                    loadCustomers();
                } else {
                    Swal.fire({ icon: "error", title: "Error", text: result.message });
                }
            } catch (err) {
                console.error(err);
                Swal.fire({ icon: "error", title: "Error", text: "Error adding customer" });
            }
        });
    }

    // -------------------
    // Delete Customer
    // -------------------
    customerList.addEventListener("click", async (e) => {
        if (e.target.tagName === "BUTTON" && e.target.dataset.id) {
            const id = e.target.dataset.id;

            Swal.fire({
                title: "Are you sure?",
                text: "This will permanently delete the customer.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                confirmButtonText: "Yes, delete it!"
            }).then(async (result) => {
                if (result.isConfirmed) {
                    try {
                        const res = await fetch(`/customer/${id}`, { method: "DELETE" });
                        const resultData = await res.json();

                        if (resultData.status === "success") {
                            Swal.fire({
                                icon: "success",
                                title: "Deleted!",
                                text: "Customer has been deleted.",
                                timer: 2000,
                                showConfirmButton: false
                            });
                            loadCustomers();
                        } else {
                            Swal.fire({ icon: "error", title: "Error", text: resultData.message });
                        }
                    } catch (err) {
                        console.error(err);
                        Swal.fire({ icon: "error", title: "Error", text: "Error deleting customer" });
                    }
                }
            });
        }
    });

    // Initial load
    loadCustomers();
});
