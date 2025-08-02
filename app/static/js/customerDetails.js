// <---------------------- add the user details ----------------->

const formData = document.getElementById('customerDetails')

formData.addEventListener('submit',(e) => {
    e.preventDefault()

    const form = new FormData(formData)

    const data = Object.fromEntries(form.entries())

    let id = document.getElementById('customerDetailsId').value

    if (id){
        fetch('http://127.0.0.1:5000/customerDetails/new',{

            method: "POST",
            headers:{
                'Content-Type':'application/json'
            }, 
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data =>{
            if (data.status == "success"){
                alert(data.message)
            }
            else{
                throw new Error(data.message);
            }
        })
        .catch(err =>{
            alert(err)
        }
        )
    }

})