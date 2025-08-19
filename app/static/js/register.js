document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch('/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(response => {
            if (response.status === "success") {
                Swal.fire({
                    icon: 'success',
                    title: '🎉 Account Created!',
                    html: `Welcome to FoodieGo!<br>
                           Your account has been successfully created.<br>
                           Log in now to start ordering your favorite meals.`,
                    showConfirmButton: false,
                    timer: 2500
                }).then(() => {
                    window.location.href = "/index";
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Registration Failed',
                    text: response.message || "Please try again."
                });
            }
        })
        .catch(err => {
            Swal.fire({
                icon: 'error',
                title: 'Something went wrong',
                text: err.toString()
            });
        });
    });
});
