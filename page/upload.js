const form = document.querySelector('form')

form.addEventListener('submit', e => {
    e.preventDefault()

    const files = document.querySelector('[type=file]').files
    const url = `http://${document.querySelector('[type=text]').value ? document.querySelector('[type=text]').value : '129.213.59.242:5000'}/infer/yolo`
    const formData = new FormData()

    formData.append('files[]', files[0])
    console.log(files[0])
    axios.post(url, files[0],
        {
            headers: {                  
                "Origin": "129.213.59.242",
                "Content-Type": "image/png;charset=UTF-8"                   
            }
        }
    )
    .then(response => {

        key = response.data
        console.log(response, response.data)
        document.getElementById("result").src = `http://${document.querySelector('[type=text]').value ? document.querySelector('[type=text]').value : '129.213.59.242:5000'}/file/${key}`;

        console.log(outside)
    })
})