document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch('/auth/login', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(response => {
            if (response.status === "success") {
                Swal.fire({
                    icon: 'success',
                    title: '🎉 Welcome back!',
                    html: `Welcome to <strong>Foodi<span style="color:red;">Go</span></strong>!<br>
                           We're happy to see you again.<br>
                           You have successfully logged in.<br>
                           Let's get your cravings satisfied!`,
                    showConfirmButton: false,
                    timer: 2000
                }).then(() => {
                    window.location.href = response.redirect;
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: response.message || "Login failed!"
                });
            }
        })
        .catch(err => {
            Swal.fire({
                icon: 'error',
                title: 'Something went wrong',
                text: err.message
            });
        });
    });
});
