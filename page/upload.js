const url = 'https://iagoeli.pagekite.me/infer/yolo'
const form = document.querySelector('form')

form.addEventListener('submit', e => {
  e.preventDefault()

  const files = document.querySelector('[type=file]').files
  const formData = new FormData()

  formData.append('files[]', files[0])

  fetch(url, {
    method: 'POST',
    headers: {'Content-Type':'image/png'},
    body: files[0]
  })
  .then((response) => response.blob())
  .then(images => {
    outside = URL.createObjectURL(images)
    document.getElementById("result").src = outside;

    console.log(outside)
  })
})
